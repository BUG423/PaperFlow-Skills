#!/usr/bin/env python3
"""litsearch.py — 并发文献检索 + CCF-A 路由

为 paper-ideation 阶段服务：给定领域 / 关键词 / 时间窗，
并发查 arXiv + Semantic Scholar + OpenAlex，按被引/年份去重排序，
专为"生成 10 个 idea"的快速场景设计。

特性:
- 多进程并发 (ProcessPoolExecutor)，3 源同时查
- 内置 CCF-A 会议路由表，按领域 (cv/nlp/ml/sys/...) 自动加入 venue 过滤
- 标准库实现，免 pip install (urllib + xml + json + concurrent.futures)
- 优雅降级：任一源限流不影响其他源
- 结构化输出 (JSON-friendly)，便于 idea 生成阶段消费

用法:
    # 按领域 + 关键词检索
    python3 litsearch.py --field cv --term "diffusion" --term "molecular" --years 2

    # 不指定领域，纯 arXiv + S2 + OpenAlex
    python3 litsearch.py --term "in-context learning" --years 2

    # 列出支持的领域
    python3 litsearch.py --list-fields

    # JSON 输出 (便于程序消费)
    python3 litsearch.py --field nlp --term "RLHF" --json --limit 20

参数:
    --field FIELD     领域路由 (见 --list-fields)。加上后会用 venue 过滤
                      只保留 CCF-A 会议的工作 (S2 source)
    --term PHRASE     必须命中的概念簇 (可重复)。多个 --term AND
    --query Q         宽口径 query (与 --term 二选一)
    --years Y         只保留 >= (今年-Y) 年。默认 2 (近两年)
    --limit N         最终展示条数 (默认 15)
    --source S        arxiv | s2 | openalex | all (默认 all)
    --json            JSON 输出
    --list-fields     列出支持的领域

环境变量:
    S2_API_KEY        Semantic Scholar API key (强烈推荐，否则容易 429)
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Any

ARXIV_API = "http://export.arxiv.org/api/query"
S2_SEARCH = "https://api.semanticscholar.org/graph/v1/paper/search"
S2_FIELDS = "title,year,abstract,citationCount,venue,authors,externalIds,url"
OPENALEX_API = "https://api.openalex.org/works"
UA = "PaperFlow-litsearch/2.0 (academic literature search)"


# ============================================================================
# CCF-A 会议路由表 (含部分学界公认 A 类但 CCF 列表里不是 A 的)
# ============================================================================

CCF_A_VENUES: dict[str, list[str]] = {
    "cv": [
        # CCF-A
        "CVPR", "ICCV",
        # 学界公认 A 类 / CCF-B 但实操按 A 投
        "ECCV",
        # 期刊
        "IJCV", "TPAMI",
    ],
    "nlp": [
        # CCF-A
        "ACL",
        # 学界公认主流
        "EMNLP", "NAACL",
        # 期刊
        "TACL", "CL",
    ],
    "ml": [
        # CCF-A
        "ICML", "NeurIPS", "NIPS",
        # 学界公认 (CCF 没列)
        "ICLR",
        # 期刊
        "JMLR", "TMLR",
    ],
    "ai": [
        # CCF-A
        "AAAI", "IJCAI",
        # 期刊
        "AIJ", "JAIR",
    ],
    "sys": [
        # CCF-A 系统类
        "OSDI", "SOSP", "ASPLOS", "ISCA", "MICRO", "HPCA",
        "NSDI", "SIGCOMM",
        # ML 系统
        "MLSys",
        # 期刊
        "TOCS",
    ],
    "data": [
        # CCF-A
        "SIGMOD", "VLDB", "ICDE",
        # 期刊
        "TODS", "TKDE",
    ],
    "ir": [
        # CCF-A
        "SIGIR", "WWW",
        # 学界主流
        "KDD",
        # 期刊
        "TOIS",
    ],
    "kdd": [
        # CCF-A
        "KDD", "SIGIR",
        # 学界主流
        "WWW", "WSDM", "RecSys", "CIKM",
        # 期刊
        "TKDE",
    ],
    "graphics": [
        "SIGGRAPH", "SIGGRAPH Asia",
        "TOG",
    ],
    "robotics": [
        # 学界主流
        "ICRA", "IROS", "RSS", "CoRL",
        # 期刊
        "TRO", "IJRR",
    ],
    "security": [
        # CCF-A
        "CCS", "S&P", "USENIX Security", "NDSS",
    ],
    "hci": [
        # CCF-A
        "CHI", "UIST",
    ],
    "theory": [
        # CCF-A
        "STOC", "FOCS",
        # 学习理论
        "COLT", "AISTATS",
    ],
    "speech": [
        "ICASSP", "Interspeech", "TASLP",
    ],
    "multimedia": [
        # CCF-A
        "ACM MM",
        # 学界主流
        "ICME", "ICMR",
    ],
}


def list_fields() -> str:
    lines = ["支持的领域 (--field 取值):"]
    for k, vs in CCF_A_VENUES.items():
        lines.append(f"  {k:12s} → {', '.join(vs[:6])}{' ...' if len(vs) > 6 else ''}")
    lines.append("")
    lines.append("不指定 --field 时不做 venue 过滤,只按 --term/--query 检索。")
    return "\n".join(lines)


# ============================================================================
# HTTP
# ============================================================================

def _get(url: str, timeout: int = 30, retries: int = 3, headers: dict | None = None) -> bytes:
    last: Exception | None = None
    hdrs = {"User-Agent": UA}
    if headers:
        hdrs.update(headers)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            last = e
            if e.code != 429 and e.code < 500:
                break
            time.sleep(2 ** attempt)
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
            time.sleep(2 ** attempt)
    raise last if last else RuntimeError("request failed")


def _norm_title(t: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


# ============================================================================
# Source: arXiv
# ============================================================================

def search_arxiv(search_query: str, limit: int) -> list[dict]:
    params = {
        "search_query": search_query,
        "start": 0,
        "max_results": limit,
        "sortBy": "relevance",
        "sortOrder": "descending",
    }
    url = ARXIV_API + "?" + urllib.parse.urlencode(params)
    raw = _get(url)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(raw)
    out: list[dict] = []
    for e in root.findall("a:entry", ns):
        title = (e.findtext("a:title", default="", namespaces=ns) or "").strip()
        summary = (e.findtext("a:summary", default="", namespaces=ns) or "").strip()
        published = e.findtext("a:published", default="", namespaces=ns) or ""
        year = int(published[:4]) if len(published) >= 4 and published[:4].isdigit() else None
        authors = [
            (a.findtext("a:name", default="", namespaces=ns) or "").strip()
            for a in e.findall("a:author", ns)
        ]
        url_id = (e.findtext("a:id", default="", namespaces=ns) or "").strip()
        arxiv_id = url_id.rsplit("/", 1)[-1] if url_id else None
        out.append({
            "title": title,
            "year": year,
            "authors": authors,
            "citations": None,  # arXiv 无被引
            "venue": "arXiv",
            "url": url_id,
            "arxiv_id": arxiv_id,
            "abstract": summary,
            "source": "arxiv",
        })
    return out


def _arxiv_query_from_terms(terms: list[str], query: str | None) -> str:
    if query:
        return f"all:{query}"
    parts = [f'all:"{t}"' for t in terms]
    return " AND ".join(parts)


# ============================================================================
# Source: Semantic Scholar
# ============================================================================

def search_s2(query: str, limit: int, venues: list[str] | None = None) -> list[dict]:
    params: dict[str, Any] = {
        "query": query,
        "limit": min(limit, 100),
        "fields": S2_FIELDS,
    }
    if venues:
        params["venue"] = ",".join(venues)
    url = S2_SEARCH + "?" + urllib.parse.urlencode(params)
    headers = {}
    if os.environ.get("S2_API_KEY"):
        headers["x-api-key"] = os.environ["S2_API_KEY"]
    raw = _get(url, headers=headers)
    data = json.loads(raw)
    out: list[dict] = []
    for p in data.get("data", []):
        ext = p.get("externalIds") or {}
        out.append({
            "title": (p.get("title") or "").strip(),
            "year": p.get("year"),
            "authors": [a.get("name", "") for a in (p.get("authors") or [])],
            "citations": p.get("citationCount"),
            "venue": p.get("venue") or "",
            "url": p.get("url") or "",
            "arxiv_id": ext.get("ArXiv"),
            "doi": ext.get("DOI"),
            "abstract": (p.get("abstract") or "").strip(),
            "source": "s2",
        })
    return out


# ============================================================================
# Source: OpenAlex
# ============================================================================

def search_openalex(query: str, limit: int, years: int | None = None) -> list[dict]:
    from_year = (datetime.datetime.now().year - years) if years else None
    filt_parts = []
    if from_year:
        filt_parts.append(f"from_publication_date:{from_year}-01-01")
    params: dict[str, Any] = {
        "search": query,
        "per-page": min(limit, 50),
        "sort": "cited_by_count:desc",
    }
    if filt_parts:
        params["filter"] = ",".join(filt_parts)
    url = OPENALEX_API + "?" + urllib.parse.urlencode(params)
    raw = _get(url)
    data = json.loads(raw)
    out: list[dict] = []
    for w in data.get("results", []):
        title = (w.get("title") or "").strip()
        venue_obj = (w.get("primary_location") or {}).get("source") or {}
        venue = venue_obj.get("display_name", "") or ""
        out.append({
            "title": title,
            "year": w.get("publication_year"),
            "authors": [
                (a.get("author") or {}).get("display_name", "")
                for a in (w.get("authorships") or [])
            ],
            "citations": w.get("cited_by_count"),
            "venue": venue,
            "url": w.get("id") or "",
            "arxiv_id": None,
            "doi": (w.get("doi") or "").replace("https://doi.org/", "") or None,
            "abstract": "",  # OpenAlex 摘要要拼 inverted index,这里省略
            "source": "openalex",
        })
    return out


# ============================================================================
# 并发调度
# ============================================================================

def _worker_arxiv(query: str, limit: int) -> tuple[str, list[dict] | str]:
    try:
        return ("arxiv", search_arxiv(query, limit))
    except Exception as e:
        return ("arxiv", f"ERROR: {type(e).__name__}: {e}")


def _worker_s2(query: str, limit: int, venues: list[str] | None) -> tuple[str, list[dict] | str]:
    try:
        return ("s2", search_s2(query, limit, venues))
    except Exception as e:
        return ("s2", f"ERROR: {type(e).__name__}: {e}")


def _worker_openalex(query: str, limit: int, years: int | None) -> tuple[str, list[dict] | str]:
    try:
        return ("openalex", search_openalex(query, limit, years))
    except Exception as e:
        return ("openalex", f"ERROR: {type(e).__name__}: {e}")


def parallel_search(
    arxiv_query: str,
    s2_query: str,
    openalex_query: str,
    per_source_limit: int,
    venues: list[str] | None,
    years: int | None,
    sources: set[str],
) -> tuple[list[dict], dict[str, str]]:
    """并发跑 3 个源。返回 (合并的论文列表, {源: 错误字符串或 OK})。"""
    results: list[dict] = []
    errors: dict[str, str] = {}

    tasks = []
    with ProcessPoolExecutor(max_workers=3) as ex:
        if "arxiv" in sources:
            tasks.append(ex.submit(_worker_arxiv, arxiv_query, per_source_limit))
        if "s2" in sources:
            tasks.append(ex.submit(_worker_s2, s2_query, per_source_limit, venues))
        if "openalex" in sources:
            tasks.append(ex.submit(_worker_openalex, openalex_query, per_source_limit, years))

        for fut in as_completed(tasks):
            src, payload = fut.result()
            if isinstance(payload, str):
                errors[src] = payload
            else:
                errors[src] = f"OK ({len(payload)} hits)"
                results.extend(payload)

    return results, errors


# ============================================================================
# 后处理: 概念簇过滤、去重、年份过滤、venue 过滤、排序
# ============================================================================

def _hits_concept(text: str, phrase: str) -> bool:
    """判断 text 是否命中 phrase 的任意 token。phrase 内空格分词,只要命中一个 token 就算命中。"""
    t = re.sub(r"[^a-z0-9 ]+", " ", text.lower())
    tokens = [tok for tok in re.split(r"\s+", phrase.lower()) if len(tok) >= 3]
    if not tokens:
        return True
    return any(tok in t for tok in tokens)


def filter_by_terms(papers: list[dict], terms: list[str]) -> list[dict]:
    """每条 paper 必须命中所有 terms (AND)。命中 = 某 term 的至少一个 token 出现在 title 或 abstract。"""
    if not terms:
        return papers
    out = []
    for p in papers:
        haystack = f"{p.get('title','')} {p.get('abstract','')}"
        if all(_hits_concept(haystack, t) for t in terms):
            out.append(p)
    return out


def filter_by_years(papers: list[dict], years: int | None) -> list[dict]:
    if not years:
        return papers
    cutoff = datetime.datetime.now().year - years
    return [p for p in papers if (p.get("year") or 0) >= cutoff]


def filter_by_venues(papers: list[dict], venues: list[str] | None, strict: bool = False) -> list[dict]:
    """venue 过滤。strict=False 时,允许 arXiv (因为多数 CCF-A 论文也挂 arXiv)。"""
    if not venues:
        return papers
    out = []
    targets = [v.lower() for v in venues]
    for p in papers:
        v = (p.get("venue") or "").lower()
        if any(t in v for t in targets):
            out.append(p)
        elif (not strict) and v.startswith("arxiv"):
            out.append(p)
    return out


def dedupe(papers: list[dict]) -> list[dict]:
    seen_t: dict[str, dict] = {}
    seen_a: dict[str, dict] = {}
    seen_d: dict[str, dict] = {}
    out_order: list[dict] = []

    def _take(key_t, key_a, key_d, p):
        existing = seen_t.get(key_t) or seen_a.get(key_a) or seen_d.get(key_d)
        if existing:
            # 合并: 取被引高/有摘要/venue 更具体的
            if (p.get("citations") or 0) > (existing.get("citations") or 0):
                existing["citations"] = p["citations"]
            if not existing.get("abstract") and p.get("abstract"):
                existing["abstract"] = p["abstract"]
            if (not existing.get("venue") or existing["venue"].startswith("arXiv")) and p.get("venue") and not p["venue"].startswith("arXiv"):
                existing["venue"] = p["venue"]
            existing["sources"] = sorted(set(existing.get("sources", [existing.get("source", "?")])) | {p.get("source", "?")})
            return False
        p2 = dict(p)
        p2["sources"] = [p.get("source", "?")]
        seen_t[key_t] = p2
        if key_a:
            seen_a[key_a] = p2
        if key_d:
            seen_d[key_d] = p2
        out_order.append(p2)
        return True

    for p in papers:
        kt = _norm_title(p.get("title"))
        ka = (p.get("arxiv_id") or "").strip().lower()
        kd = (p.get("doi") or "").strip().lower()
        _take(kt, ka, kd, p)

    return out_order


def rank(papers: list[dict]) -> list[dict]:
    """按 (citations desc, year desc) 排序。None citations 视为 -1。"""
    return sorted(
        papers,
        key=lambda p: (-(p.get("citations") if p.get("citations") is not None else -1), -(p.get("year") or 0)),
    )


# ============================================================================
# 渲染
# ============================================================================

def render_human(papers: list[dict], errors: dict[str, str], venues_used: list[str] | None, terms: list[str], query: str | None) -> str:
    lines = []
    lines.append("=" * 80)
    lines.append("litsearch v2 (并发版) — 检索摘要")
    lines.append("=" * 80)
    if query:
        lines.append(f"宽口径 query: {query!r}")
    if terms:
        lines.append(f"概念簇 (AND): {terms}")
    if venues_used:
        lines.append(f"venue 过滤: {', '.join(venues_used[:10])}{' ...' if len(venues_used)>10 else ''}")
    lines.append("")
    lines.append("源状态:")
    for src, msg in errors.items():
        lines.append(f"  [{src:8s}] {msg}")
    lines.append("")
    lines.append(f"共 {len(papers)} 篇 (按 citations desc, year desc):")
    lines.append("-" * 80)
    for i, p in enumerate(papers, 1):
        c = p.get("citations")
        cs = f"{c} cites" if c is not None else "?"
        v = p.get("venue") or "?"
        y = p.get("year") or "?"
        srcs = "+".join(p.get("sources") or [p.get("source", "?")])
        lines.append(f"[{i:2d}] {p.get('title','(no title)')}")
        lines.append(f"     {y} | {v} | {cs} | sources={srcs}")
        au = p.get("authors") or []
        if au:
            au_show = ", ".join(au[:4]) + (" et al." if len(au) > 4 else "")
            lines.append(f"     {au_show}")
        if p.get("arxiv_id"):
            lines.append(f"     arxiv: {p['arxiv_id']}")
        if p.get("url"):
            lines.append(f"     url:   {p['url']}")
        abs_ = (p.get("abstract") or "").replace("\n", " ").strip()
        if abs_:
            snippet = abs_[:240] + ("..." if len(abs_) > 240 else "")
            lines.append(f"     | {snippet}")
        lines.append("")
    return "\n".join(lines)


# ============================================================================
# CLI
# ============================================================================

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="litsearch v2 - 并发文献检索 + CCF-A 路由",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--query", type=str, default=None, help="宽口径 query (与 --term 二选一)")
    ap.add_argument("--term", action="append", default=[], help="必须命中的概念簇 (可重复,AND)")
    ap.add_argument("--field", type=str, default=None, help=f"领域路由 (见 --list-fields)")
    ap.add_argument("--years", type=int, default=2, help="只保留 >=(今年-Y) 年,默认 2")
    ap.add_argument("--limit", type=int, default=15, help="最终展示条数 (默认 15)")
    ap.add_argument("--source", type=str, default="all", choices=["all", "arxiv", "s2", "openalex"],
                    help="单源 / all (默认 all,3 源并发)")
    ap.add_argument("--json", action="store_true", help="JSON 输出 (便于程序消费)")
    ap.add_argument("--list-fields", action="store_true", help="列出支持的领域并退出")
    ap.add_argument("--strict-venue", action="store_true", help="严格 venue 过滤 (不允许 arXiv)")
    args = ap.parse_args(argv)

    if args.list_fields:
        print(list_fields())
        return 0

    if not args.term and not args.query:
        ap.print_help()
        print("\n错误: 至少需要一个 --term 或一个 --query", file=sys.stderr)
        return 2

    # 解析 field → venues
    venues: list[str] | None = None
    if args.field:
        if args.field not in CCF_A_VENUES:
            print(f"错误: 未知 field {args.field!r}。可选: {', '.join(CCF_A_VENUES.keys())}", file=sys.stderr)
            return 2
        venues = CCF_A_VENUES[args.field]

    # 构造各源 query
    arxiv_query = _arxiv_query_from_terms(args.term, args.query)
    flat = (args.query or " ".join(args.term)).strip()
    s2_query = flat
    openalex_query = flat

    per_source_limit = max(args.limit * 3, 30)  # 过量抓取,过滤后还能凑够
    sources = {args.source} if args.source != "all" else {"arxiv", "s2", "openalex"}

    t0 = time.time()
    all_papers, errors = parallel_search(
        arxiv_query=arxiv_query,
        s2_query=s2_query,
        openalex_query=openalex_query,
        per_source_limit=per_source_limit,
        venues=venues,
        years=args.years,
        sources=sources,
    )
    elapsed = time.time() - t0

    # 后处理流水线
    filtered = filter_by_terms(all_papers, args.term)
    filtered = filter_by_years(filtered, args.years)
    if venues:
        filtered = filter_by_venues(filtered, venues, strict=args.strict_venue)
    deduped = dedupe(filtered)
    ranked = rank(deduped)
    final = ranked[: args.limit]

    if args.json:
        print(json.dumps({
            "meta": {
                "field": args.field,
                "venues_filter": venues,
                "terms": args.term,
                "query": args.query,
                "years": args.years,
                "elapsed_sec": round(elapsed, 2),
                "sources": errors,
                "total_after_filter": len(deduped),
                "shown": len(final),
            },
            "papers": final,
        }, ensure_ascii=False, indent=2))
    else:
        print(render_human(final, errors, venues, args.term, args.query))
        print(f"(并发用时 {elapsed:.2f}s,过滤后总数 {len(deduped)},展示 {len(final)})")

    # 失败码: 全部源都炸了
    if all(msg.startswith("ERROR") for msg in errors.values()):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
