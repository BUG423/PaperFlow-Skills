<div align="center">

# CCFA Skills

### 一個面向 CCF-A 研究選題、論文建構、審稿模擬與作者回應的研究輔助 skill 家族。

<p>
  <a href="README.md">English</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <strong>繁體中文</strong>
</p>

</div>

---

<p align="center">
  <img src="assets/ccfaskills.png" alt="CCFA Skills overview" width="100%">
</p>

## 專案定位

CCFA Skills 是一組面向 CCF-A 學術研究流程的 agent-readable research skills。它關注的是從非正式 idea 到可辯護投稿之間的關鍵階段：澄清問題、形成方法、校準新穎性、設計證據、組織論文、預判審稿，以及在審稿後進行回應。

這個倉庫不希望被綁定到某一個模型或互動介面。文件採用基於 `SKILL.md` 的組織方式，可用於支援本地 skill 模組的 agent 環境。倉庫中保留了一些便於 Codex-style 環境識別的 metadata，但核心內容是可遷移的研究流程：Markdown workflow、rubric、checklist、venue adapter、模板和參考說明。

## 研究前提

許多研究專案的問題並不是在寫作階段才出現的。真正不穩定的，往往是更早的研究鏈條：

```text
問題 -> 缺口 -> 挑戰 -> 洞察 -> 方法 -> 證據 -> 主張
```

當其中某一環薄弱時，後續潤色常常只是把問題隱藏起來，而不是解決它。模糊的 gap 會變成模糊的引言；缺少機制的方法會變成元件列表；不能檢驗中心主張的實驗會變成難以防守的表格。

CCFA Skills 的組織方式正好相反：儘早暴露薄弱環節，精確命名它，並把它轉化為下一步研究行動。它的學術立場是克制的：有根據的新穎性優先於裝飾性敘述，機制優先於術語，證據優先於強調，有邊界的主張優先於流暢卻越界的表達。

## 系統架構

這個家族按照研究流程分層組織。

| 層級 | 目的 | Skills |
| --- | --- | --- |
| **Idea Layer** | 在寫作前塑形並評估研究方向。 | `ccf-idea-optimizer`, `ccf-idea-reviewer` |
| **Manuscript Layer** | 將可行方向發展為連貫的 CCF-A 論文。 | `ccf-writing-skills` |
| **Review Layer** | 在投稿前模擬 reviewer 和 AC 壓力。 | `ccf-conference-paper-reviewer` |
| **Response Layer** | 將審稿意見轉化為清晰回應和修改承諾。 | `ccf-conference-paper-rebuttal` |
| **Maintenance Layer** | 建立、改進和校驗 skill 模組。 | `forge-skills` |

推薦的使用方式不是一條機械直線，而是帶有兩個門控點的研究閉環：

```text
raw idea
  -> ccf-idea-optimizer             ：首輪問題 / 方法 / 證據成形
  -> ccf-idea-reviewer              ：問題-方法門控
       如果薄弱但可修復          ：回到 ccf-idea-optimizer 做定向修復
       如果根本不匹配            ：pivot 或停止投入
       如果已經可發展            ：交給 ccf-writing-skills
  -> ccf-writing-skills             ：建構論文論證和章節
  -> ccf-conference-paper-reviewer  ：投稿前審稿壓力測試
       如果扣分點可修復          ：回到 ccf-writing-skills 修改論文
       如果真實審稿意見到來      ：使用 ccf-conference-paper-rebuttal
```

因此，第二次出現 `ccf-idea-optimizer` 不是重複。第一次 optimizer 負責把粗糙方向整理到「可以被判斷」的狀態；第二次只在 reviewer 發現可修復弱點時觸發，用來定向修補問題、收窄主張或重新選擇方法路線。`ccf-conference-paper-rebuttal` 也不是投稿前 reviewer 的替代品，它屬於真實審稿意見到來之後的回應階段。

<p align="center">
  <img src="assets/ccfa-skills-architecture.svg" alt="CCFA Skills workflow gates" width="100%">
</p>

這個結構重要，是因為 CCF-A 審稿並不是一個單一分數，而是新穎性、重要性、可靠性、證據、清晰度、可復現性和 venue fit 之間的綜合判斷。CCFA Skills 將這些維度拆開處理，同時保留它們之間的依賴關係。

## Skill 家族

### `ccf-idea-optimizer`

將早期研究方向轉化為結構化 idea card：任務、gap、根本挑戰、核心洞察、方法機制、貢獻類型、證據計畫和風險登記表。

它適合處理「有潛力但尚未成形」的想法。這個 skill 會追問：專案真正想證明什麼，方法依賴什麼假設，什麼證據能讓主張可信，以及哪個學術共同體會認為這項工作有意義。

### `ccf-idea-reviewer`

在論文尚未形成之前，只評價問題和方法。它使用多個專家視角，包括領域、方法、實驗、venue 和 skeptical prior-art 視角。

它的目標不是獎勵自信表達，而是區分低新穎性與未知新穎性，區分可行性風險與 framing 風險，也區分可修復設計問題與需要 pivot 的根本原因。這個階段給 idea 做的是研究層面的診斷。

### `ccf-writing-skills`

將成熟 idea 發展為論文級論證。它處理故事線、章節規劃、段落角色、claim-evidence map、venue adaptation、樣例啟發式寫作策略和 score-lifting 修改。

它最重視一致性：摘要、引言、方法、實驗、侷限性和結論應該以不同解析度講述同一個研究故事。

### `ccf-conference-paper-reviewer`

模擬嚴格但公平的 conference review。它以 program committee 的判斷距離閱讀論文，識別可能扣分點，校準分數，並將弱點轉化為修改行動。

它使投稿前審查更可執行：哪些問題可以通過寫作修復，哪些需要分析，哪些需要新結果，哪些應被界定為侷限，哪些說明 venue 不匹配。

### `ccf-conference-paper-rebuttal`

支援審稿後的作者回應。它將審稿意見整理為 issue table，合併 common concerns，選擇回應策略，起草簡潔回覆，並可配合 TeX response templates。

它的原則是 evidence-grounded communication：回答關切，澄清誤解，承認有效邊界，避免不可兌現的承諾。

### `forge-skills`

提供構建和維護 skills 的工程層。它覆蓋命名、結構、資源組織、校驗和觸發設計。

它讓這個家族保持可擴展：新的領域 skill 可以被加入，而不需要把整個倉庫變成一個巨大的 prompt 文件。

## 這個家族優化什麼

| 目標 | 含義 |
| --- | --- |
| **問題精度** | 論文應命名真實瓶頸，而不只是說明現有方法不足。 |
| **機制清晰度** | 方法應解釋為什麼有效，而不只是列出元件。 |
| **新穎性校準** | 原創性主張應與相近工作對照；未檢索時應標記不確定性。 |
| **證據對齊** | 實驗、證明、使用者研究或系統評估應檢驗中心主張。 |
| **Venue fit** | 論證方式應能被目標學術共同體理解和評價。 |
| **修改連續性** | 批評應轉化為 action queue，而不是零散建議。 |

## 安裝

請複製完整 skill 目錄，而不只是複製 `SKILL.md`。多個模組依賴 `references/`、`assets/`、模板以及跨 skill 的相對路徑引用。可安裝的目錄包括：

```text
ccf-idea-optimizer
ccf-idea-reviewer
ccf-writing-skills
ccf-conference-paper-reviewer
ccf-conference-paper-rebuttal
forge-skills
```

### 1. Codex

Codex-style 本地 skill 環境通常從 `~/.codex/skills/` 讀取 skills。如果你使用自訂 `$CODEX_HOME`，請把這些目錄放到 `$CODEX_HOME/skills/` 下面。

macOS / Linux：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
cd CCFA-Skills
mkdir -p ~/.codex/skills
cp -R ccf-* forge-skills ~/.codex/skills/
```

Windows PowerShell：

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Set-Location .\CCFA-Skills
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
Copy-Item -Recurse -Force .\ccf-* "$HOME\.codex\skills\"
Copy-Item -Recurse -Force .\forge-skills "$HOME\.codex\skills\"
```

複製完成後建議重新開啟一個會話。可以用這句話快速測試：`Use ccf-idea-optimizer to refine this rough research idea...`

### 2. Claude Code

Claude Code 可以從使用者級 skills 目錄或專案級 skills 目錄載入 skills。希望所有專案都能使用時，推薦使用者級安裝；如果某個論文專案希望自帶固定研究流程，則使用專案級安裝。

使用者級安裝：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
cd CCFA-Skills
mkdir -p ~/.claude/skills
cp -R ccf-* forge-skills ~/.claude/skills/
```

專案級安裝：

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
mkdir -p your-paper-repo/.claude/skills
cp -R CCFA-Skills/ccf-* CCFA-Skills/forge-skills your-paper-repo/.claude/skills/
```

Windows PowerShell：

```powershell
git clone https://github.com/mikubaka88/CCFA-Skills.git
Set-Location .\CCFA-Skills
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse -Force .\ccf-* "$HOME\.claude\skills\"
Copy-Item -Recurse -Force .\forge-skills "$HOME\.claude\skills\"
```

安裝後可以直接按名稱呼叫，例如 `/ccf-idea-reviewer`，也可以用自然語言要求 Claude Code 使用對應的 CCFA skill。如果新加入的 skill 目錄沒有被識別，重啟 Claude Code 即可。

如果你希望使用更強的 subagent 隔離，也可以建立 Claude Code subagent wrapper 指向這些已安裝 skill 目錄，但 `SKILL.md` 和對應的 `references/` 應保持為唯一的知識源。

### 3. Other agents or manual use

對於其他 agent 框架，請將同樣的目錄複製到該框架的 skill、tool、memory 或 instruction 目錄，並保持相對路徑不變。每個模組都應以對應目錄下的 `SKILL.md` 作為入口文件。

如果框架沒有原生 skill 系統，也可以手動使用：

```text
1. 根據任務選擇對應目錄。
2. 先閱讀該目錄下的 SKILL.md。
3. 當 SKILL.md 提到 references/... 或 assets/... 時，在同一個 skill 目錄內解析路徑。
4. 當它提到 ../ccf-writing-skills/... 或其他同級 skill 時，保持倉庫原有目錄結構。
5. 只載入當前任務真正需要的引用文件。
```

後續更新時，在本地 clone 目錄中執行 `git pull`，然後重新複製這些 skill 目錄即可。

## 範例請求

```text
Use ccf-idea-optimizer to refine this rough CVPR idea into a problem-method-evidence plan.
Use ccf-idea-reviewer to rank these NeurIPS directions and identify fatal risks.
Use ccf-writing-skills to rebuild my introduction around the actual contribution.
Use ccf-conference-paper-reviewer to simulate CCF-A reviewers before submission.
Use ccf-conference-paper-rebuttal to draft a concise response from these reviews.
```

## 邊界

CCFA Skills 不保證錄用，不替代真實實驗，不偽造證據，也不能代替領域專家判斷。它更像一個結構化研究伴侶：幫助研究者暴露薄弱假設，組織決策，校準主張，並讓工作持續對目標學術共同體的標準負責。

## 交流

更多更新、範例和研究札記會整理到小紅書號：`8994074380`。
