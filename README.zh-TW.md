<div align="center">

# CCFA Skills

### 一個面向 CCF-A 研究選題、寫作、審稿與回應的 Codex Skill 家族。

<p>
  <a href="README.md">English</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <strong>繁體中文</strong>
</p>

<p>
  <img alt="Codex Skills" src="https://img.shields.io/badge/Codex-Skills-111827?style=for-the-badge">
  <img alt="CCF A" src="https://img.shields.io/badge/Target-CCF--A-2563eb?style=for-the-badge">
  <img alt="Idea to Rebuttal" src="https://img.shields.io/badge/Workflow-Idea%20to%20Rebuttal-16a34a?style=for-the-badge">
</p>

<img src="assets/ccfa-skills-architecture.svg" alt="CCFA Skills architecture" width="920">

</div>

---

## 為什麼會有這個專案

論文通常以文字的形式進入評審系統，但它的命運往往在更早的階段就已經被決定。摘要尚未潤色之前，一系列更安靜的研究決策已經發生：什麼問題值得被提出，什麼 gap 不是修辭性的，什麼機制能讓方法不只是熟悉模組的組合，什麼證據能夠承載主張，以及哪一類審稿人會覺得這項工作是可理解、可信、可討論的。

**CCFA Skills** 試圖把這些早期決策顯性化。它把 CCF-A 投稿看作一條研究軌跡，而不是單純的寫作任務：idea 被塑形，被評估，被修改，被寫成論文，被審稿式壓力測試，最後被回應。它的目標不是把薄弱工作說得更強，而是幫助研究者看見真正缺少強度的地方，並把這種診斷轉化為下一步行動。

這套 skill 家族在學術氣質上是克制的：它更重視有根據的新穎性，而不是裝飾性的新穎性敘述；更重視機制，而不是術語；更重視證據，而不是強調；更重視有邊界的 claim，而不是流暢卻越界的主張。

## 安裝

請複製完整 skill 目錄，而不只是複製 `SKILL.md`。多個 skill 依賴 `references/`、`assets/` 和 agent metadata。

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Copy-Item -Recurse .\CCFA-Skills\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse .\CCFA-Skills\forge-skills "$HOME\.codex\skills\"
```

安裝後建議開啟一個新的 Codex 會話，以便系統發現新增 skills。

## Skill 索引

| Skill | 階段 | 用途 | 常見觸發方式 |
| --- | --- | --- | --- |
| `ccf-idea-optimizer` | 選題成形 | 把粗糙方向整理為問題、方法和證據方案。 | “Improve this idea”; “shape this for CVPR/ICLR/ACL” |
| `ccf-idea-reviewer` | 選題評估 | 用多專家 CCF-A rubric 評價問題和方法。 | “Score these ideas”; “which direction is stronger?” |
| `ccf-writing-skills` | 論文建構 | 建立故事線、章節、claim-evidence 對齊和提分修改。 | “revise this section”; “make this CCF-A ready” |
| `ccf-conference-paper-reviewer` | 投稿前審查 | 模擬 reviewer 和 AC 壓力，並輸出修改行動。 | “simulate reviewers”; “estimate score”; “review this paper” |
| `ccf-conference-paper-rebuttal` | 審後回應 | 組織 author response / rebuttal。 | “answer reviews”; “write rebuttal”; “respond to AC” |
| `forge-skills` | Skill 工程 | 建立、校驗和維護 Codex skills。 | “create a skill”; “validate SKILL.md”; “refactor this skill” |

## 工作流

```text
raw idea
  -> ccf-idea-optimizer
  -> ccf-idea-reviewer
  -> ccf-idea-optimizer
  -> ccf-writing-skills
  -> ccf-conference-paper-reviewer
  -> ccf-conference-paper-rebuttal
```

這個 loop 是關鍵。一個有潛力的 idea 可能在評審後變得更窄、更誠實，也可能需要更換 baseline、收緊 claim，甚至換一個更適合的 venue。一篇看起來完整的 draft 也可能在模擬審稿後暴露出缺失 ablation、證據位置不對、貢獻表達不清的問題。這套 skills 的價值在於讓這些修改保持連續，而不是每一步都重新變成一個孤立 prompt。

## 共同設計原則

1. **研究先於修辭**：首先判斷問題、方法和證據是否構成可辯護的貢獻。
2. **面向 venue 的判斷**：CVPR、SIGMOD、CCS、CHI、ACL、NeurIPS 不應被同一種泛化品味評估。
3. **claim-evidence 紀律**：核心 claim 必須被支撐、收窄、刪除，或標記為需要新證據。
4. **層次分離**：idea 品質、論文品質、審稿風險和 rebuttal 策略相互關聯，但不能混為一談。
5. **漸進式上下文**：`SKILL.md` 保持緊湊，詳細 rubric、checklist 和 venue adapter 放入 `references/`。

## Skill 剖面

### `ccf-idea-optimizer`

**做什麼** — 將早期研究方向轉化為更嚴整的 CCF-A idea card：任務、gap、根本挑戰、核心 insight、方法機制、貢獻類型、實驗方案和 reviewer-risk register。

**基礎思想** — 結合 proposal 式研究推理、CCF-A venue 適配、Heilmeier 式問題意識，以及一個實際判斷：很多論文在潤色文本之前，更需要修復概念結構。

**關鍵規則**

| 維度 | 規則 |
| --- | --- |
| 問題 | 命名一個真實瓶頸，而不只是描述性能不足。 |
| 方法 | 解釋機制，不用新術語遮蓋熟悉方法。 |
| 創新 | 選擇最強且誠實的貢獻類型，而不是聲稱什麼都有。 |
| 證據 | 設計能檢驗中心 claim 的實驗，而不是單純增加實驗數量。 |
| 風險 | 在寫作前標出 novelty、feasibility、venue fit 和 evidence gaps。 |

### `ccf-idea-reviewer`

**做什麼** — 在論文寫作之前，只評價問題和方法。它輸出多專家評分、信心度、fatal risks、可修復性，以及 develop / revise / pivot / abandon / 先查文獻 的建議。

**基礎思想** — 融合 reviewer-style evaluation、AC 式 venue fit 判斷、skeptical prior-art 檢查和多軸 CCF-A scoring。

**關鍵規則**

| 維度 | 規則 |
| --- | --- |
| 範圍 | 評估對象仍是 idea 時，不把文字表現作為評分對象。 |
| 專家視角 | 分離領域、方法、實驗、venue 和 prior-art 風險。 |
| 新穎性 | 區分「新穎性低」和「新穎性未知」。 |
| 公平性 | 如果深度和證據匹配 venue，不因方向小眾而降低判斷。 |
| 決策 | 優先使用 fatal-risk-adjusted judgment，而不是簡單平均分。 |

### `ccf-writing-skills`

**做什麼** — 把已經相對成熟的 idea 轉化為連貫的論文方案或修改方案。它以 section 為單位工作，同時保留全局鏈條：task -> gap -> challenge -> insight -> method -> evidence -> limitation。

**基礎思想** — CCF-A venue adapters、強論文樣例分析、claim-evidence audit、score-lifting loop 和 reviewer-facing revision practice。

**關鍵規則**

| 維度 | 規則 |
| --- | --- |
| 故事線 | 讓貢獻在一次認真閱讀後可以被恢復出來。 |
| 章節 | 讓每一節和每一段都有明確修辭角色。 |
| Claim | 只強化證據能夠支撐的內容。 |
| 證據 | 將決定性證據放入正文，或清楚指向 appendix。 |
| Readiness | 只有當主要審稿風險被處理或誠實標記後，才稱為 ready。 |

### `ccf-conference-paper-reviewer`

**做什麼** — 模擬嚴格但公平的 conference reviewer 和 AC/meta-review。它把弱點轉化為具體修改行動，而不是停留在「需要更多實驗」的泛泛建議。

**基礎思想** — 通用 CS review rubric、venue-specific review styles、score calibration 和 revision-action taxonomy。

**關鍵規則**

| 維度 | 規則 |
| --- | --- |
| 審稿立場 | 保持 program-committee member 的判斷距離，而不是過度代入作者立場。 |
| 證據 | 將扣分點綁定到 claim、baseline、ablation、proof、study 或 reproducibility gap。 |
| 嚴重性 | 先處理 fatal risks，再處理局部表達問題。 |
| 修改 | 把每個 fix 分類為 writing、analysis、citation、figure、new result、limitation 或 venue mismatch。 |
| 分數 | 只有在有具體修改支撐時，才報告預期分數變化。 |

### `ccf-conference-paper-rebuttal`

**做什麼** — 從審稿意見構建 author response。它整理問題、選擇回應策略、寫出簡潔回覆，並支援 TeX rebuttal 模板。

**基礎思想** — Evidence-grounded rebuttal practice、reviewer-intent analysis、issue table、common-concern grouping 和 response-letter structure。

**關鍵規則**

| 維度 | 規則 |
| --- | --- |
| 語氣 | 冷靜、具體、感謝、非防禦。 |
| 結構 | 先回答 concern，再解釋背景和證據。 |
| 證據 | 優先使用資料、位置、圖表或已完成分析，而不是尚未兌現的承諾。 |
| 邊界 | 不承諾不可獲得的實驗，也不掩蓋有效侷限。 |
| 策略 | 回應深層關切，而不僅是字面句子。 |

### `forge-skills`

**做什麼** — 為建立和維護 skills 提供工程紀律：命名、結構、資源佈局、校驗和觸發品質。

**基礎思想** — Codex skill authoring conventions 和本地 validation workflow。

**關鍵規則**

| 維度 | 規則 |
| --- | --- |
| 結構 | 保持 `SKILL.md` 緊湊，把詳細材料移入 references。 |
| 命名 | 使用 lowercase hyphen-case，並保持目錄名等於 frontmatter name。 |
| 資源 | 只有當 `references/`、`scripts/` 或 `assets/` 服務於重複工作時才添加。 |
| 校驗 | 運行 validator，並檢查 trigger、連結和 placeholder。 |

## 範例用法

```text
Use $ccf-idea-optimizer to refine this rough CVPR idea into a problem-method-evidence plan.
Use $ccf-idea-reviewer to rank these three NeurIPS directions and identify fatal risks.
Use $ccf-writing-skills to rebuild my introduction around the actual contribution.
Use $ccf-conference-paper-reviewer to simulate CCF-A reviewers before submission.
Use $ccf-conference-paper-rebuttal to draft a concise author response from these reviews.
```

## 範圍與學術誠信

CCFA Skills 不是錄用保證，也不能替代真實實驗、仔細讀文獻和領域判斷。它更像一個結構化思考工具：幫助研究者暴露薄弱假設、組織證據、校準 claim，並讓研究工作的每一步都對目標學術共同體的標準負責。

## 一句話介紹

**CCFA Skills 是一套面向 Codex 的 skill 家族，幫助研究者從早期 CCF-A idea 出發，逐步形成更清晰的問題、更有機制的方法、更可信的證據、更具審稿意識的論文，以及更克制而有效的 author response。**
