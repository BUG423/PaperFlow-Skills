<div align="center">

# CCFA Skills

### 一個面向 CCF-A 研究的 Codex Skill 家族：從 idea 到 rebuttal 的閉環工作流。

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

## 一個小故事

很多研究者找 AI 助手時，往往會先給出一句看起來像論文想法的話：

> 「我想改進 X 方法，解決 Y 任務，然後投 CVPR / NeurIPS / ACL。」

最直接的回答當然是幫他寫摘要、潤色引言、補實驗建議。但這通常已經太晚了。很多論文在動筆之前就已經帶著結構性風險：問題定義不夠銳利，方法只是熟悉模組的組合，創新點沒有和最近工作拉開距離，實驗計畫也沒有真正回答審稿人最關心的問題。

**CCFA Skills** 的設計出發點正是這個更早的階段：一篇強的 CCF-A 投稿首先不是一份寫得漂亮的文本，而是一串研究決策。idea 要被壓縮成一個清晰問題；問題要推出方法機制；方法機制要支撐誠實的貢獻；貢獻要能被實驗證據檢驗；最終論文要降低審稿人的不確定性，而不是只讓語言聽起來更自信。

這個倉庫把這種思路包裝成一整個 Codex skill 家族。

## 設計主張

CCFA Skills 的核心判斷是：CCF-A 投稿準備應該被看作一個**閉環研究系統**，而不是一組互相獨立的 prompt。

頂會審稿通常是多目標判斷。審稿人會問：問題是否重要？idea 是否新？方法是否有技術含量？證據是否真的支撐主張？工作是否適合目標會議？作者是否理解侷限？所以，一個真正有用的研究助手也應該沿著這些軸線工作，而不是只停留在文字潤色層面。

因此，CCFA Skills 把流程拆成幾個專業但互相連接的角色：

```text
粗糙 idea
  -> idea 優化
  -> 多專家 idea 評審
  -> idea 修改或 pivot
  -> 論文寫作
  -> 模擬審稿
  -> rebuttal / author response
```

這套 skill 家族是有明確立場的：它更願意在早期指出弱 framing，更願意標記 novelty uncertainty，更重視 claim-evidence 紀律，也更強調 reviewer-facing risk register。它不是為了把每個 idea 都包裝成「看似能中」的樣子，而是為了發現一個 idea 到底怎樣才會真正更接近可投、可審、可信。

## Skill 家族

| Skill | 研究角色 | 主要輸出 |
| --- | --- | --- |
| `ccf-idea-optimizer` | 把粗糙想法轉化為面向 venue 的研究方案。 | 問題定義、方法藍圖、創新點、實驗矩陣、風險登記表。 |
| `ccf-idea-reviewer` | 在論文寫作前，只評價問題和方法。 | 多專家評分、fatal risks、信心度、revise / pivot / abandon 建議。 |
| `ccf-writing-skills` | 將成熟 idea 寫成 CCF-A 論文。 | 故事線、章節計畫、claim-evidence map、score-lifting action。 |
| `ccf-conference-paper-reviewer` | 模擬審稿人和 AC/meta-review 壓力。 | 校準審稿意見、分數阻塞點、修改隊列、預期提分。 |
| `ccf-conference-paper-rebuttal` | 處理審後溝通。 | 問題表、回應策略、TeX rebuttal 模板、承諾修改項。 |
| `forge-skills` | 維護和擴展 skill 生態。 | 新 skill 結構、校驗規則、reference/resource 組織。 |

## 它為什麼有用

### 1. 它從寫作之前開始介入

很多時候，最有價值的幫助不是把句子改得更順，而是發現問題應該重新定義、方法需要機制解釋、benchmark claim 太寬、核心實驗缺失。`ccf-idea-optimizer` 和 `ccf-idea-reviewer` 專門服務於這個 pre-writing 階段。

### 2. 它區分 idea 品質和論文品質

漂亮的段落救不了一個弱 idea；但一個好 idea 也可能因為論文沒有暴露清楚貢獻而被拒。這個家族把兩層分開：idea-stage review 關注問題和方法，paper-stage review 關注證據、表達、結構和 venue fit。

### 3. 它引入多專家壓力測試

`ccf-idea-reviewer` 會從領域專家、方法專家、實驗專家、AC/venue 專家、skeptical prior-art 專家等角度評估 idea。這種設計是為了模擬真實 PC discussion 中不同 reviewer 可能提出的分歧和質疑。

### 4. 它是 venue-aware 的

同一個 idea 不應該用同一種方式投 CVPR、ACL、SIGMOD、CCS、CHI 或 NeurIPS。不同 venue 對問題價值、方法機制、實驗包、侷限性和責任研究的期待不同。CCFA Skills 內建了 CCF-A venue-family adapter，讓 idea 和論文都能面向目標社群調整。

### 5. 它把批評轉化成行動隊列

這套系統強調 action queue：哪裡要重寫、哪裡要補實驗、哪裡要弱化 claim、哪裡需要新結果、哪裡應該承認為 limitation。目標不是泛泛建議，而是能影響下一輪研究決策的具體行動。

## 推薦流程

```text
1. 使用 ccf-idea-optimizer
   把粗糙想法標準化為 problem, gap, challenge, insight, method, evidence, limitation。

2. 使用 ccf-idea-reviewer
   用多專家評分體系評估問題和方法，識別 fatal risks。

3. 回到 ccf-idea-optimizer
   根據 reviewer action queue 修改、收窄、增強或 pivot。

4. 使用 ccf-writing-skills
   建構論文故事線、章節結構、claim-evidence map 和 score-lifting plan。

5. 使用 ccf-conference-paper-reviewer
   模擬審稿人，提前把潛在扣分點轉成修改計畫。

6. 使用 ccf-conference-paper-rebuttal
   收到 reviews 後，用冷靜、具體、有證據的方式組織回應。
```

## 安裝

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Copy-Item -Recurse .\CCFA-Skills\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse .\CCFA-Skills\forge-skills "$HOME\.codex\skills\"
```

## 範例用法

```text
Use $ccf-idea-optimizer to improve this rough CVPR idea.
Use $ccf-idea-reviewer to compare these three NeurIPS project directions.
Use $ccf-writing-skills to build the storyline for my ICLR submission.
Use $ccf-conference-paper-reviewer to simulate reviewer scores before submission.
Use $ccf-conference-paper-rebuttal to draft an author response from these reviews.
```

## 它不做什麼

CCFA Skills 不承諾必中，不編造實驗結果，不偽造 related work，也不會把沒有證據支撐的 claim 包裝成自信語言。它更克制一點：儘早暴露薄弱環節，幫助研究者判斷取捨，並讓研究 pipeline 的每一步都更有審稿意識。

## 一句話介紹

**CCFA Skills 是一套面向 Codex 的研究輔助 skill 家族，幫助研究者把粗糙的 CCF-A idea 逐步轉化為更銳利的問題、更強的方法、更可信的實驗、更有審稿意識的論文和更專業的 rebuttal。**
