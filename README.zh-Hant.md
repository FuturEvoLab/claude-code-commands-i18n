# Claude Code 指令大全

[English](README.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-Hant.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md)

![Unofficial](https://img.shields.io/badge/Anthropic-unofficial-lightgrey) [![check](https://github.com/FuturEvoLab/claude-code-commands-i18n/actions/workflows/check.yml/badge.svg)](https://github.com/FuturEvoLab/claude-code-commands-i18n/actions/workflows/check.yml) [![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-blue)](LICENSE-CONTENT) [![Code: MIT](https://img.shields.io/badge/code-MIT-green)](LICENSE) ![Commands](https://img.shields.io/badge/commands-115-teal)

> 非官方、用淺顯文字介紹 Claude Code 所有斜線指令的參考手冊，提供 **7 種語言：英文、日文、簡體中文、繁體中文、韓文、俄文、西班牙文**。專為讀英文官方文件感到吃力的人而寫：每個指令都有簡短說明，以及一個實際的使用時機範例。

## 線上預覽

一個可以直接開啟試用的靜態頁面：搜尋、切換語言和主題、複製指令，不需要安裝。

### [可搜尋的網頁版 →](https://futurevolab.github.io/claude-code-commands-i18n/zh-hant/)

| 預設主題 | 駭客任務主題 |
|---|---|
| [![預設主題](docs/assets/preview-en.png)](https://futurevolab.github.io/claude-code-commands-i18n/?theme=terminal) | [![駭客任務主題](docs/assets/preview-matrix.png)](https://futurevolab.github.io/claude-code-commands-i18n/?theme=matrix) |

<p><img src="docs/assets/preview-search.png" alt="search" width="68%"> <img src="docs/assets/preview-mobile.png" alt="mobile" width="28%"></p>

## 如何看懂語法

- 在輸入框輸入 `/` 會開啟指令選單；繼續輸入可以篩選。
- `[ ]` = 可省略，`< >` = 必填，`|` = 擇一。參數可以直接用中文寫。
- **技能** = 一組預先寫好、交給 Claude 的提示。**工作流程** = 在背景執行多個代理。
- 許多指令取決於版本、方案、平台或是否啟用某項功能。以你看到的選單為準；用 `/status` 查看你的版本。

## ★ 新手推薦

編者為使用 Claude Code 第一週挑選的指令。

- `/clear` · 開始全新對話（舊對話之後仍可接續）
- `/compact` · 把很長的對話整理成摘要，騰出空間
- `/context` · 查看是什麼佔滿了上下文
- `/plan` · 先看計畫；經你核准後才會修改
- `/resume` · 回到之前的對話
- `/rewind` · 復原：把程式碼和對話退回去
- `/model` · 切換模型
- `/init` · 建立專案的 CLAUDE.md
- `/code-review` · 提交前檢查 bug，也可以順便修正
- `/loop` · 依固定間隔重複執行提示
- `/mcp` · 管理外部工具的連線
- `/permissions` · 決定 Claude 不必詢問就能做哪些事
- `/usage` · 查看費用和方案上限
- `/doctor` · 出問題時做一次健檢
- `/help` · 顯示說明和所有指令
- `/powerup` · 用互動課程學習功能

## 依你想做的事找指令

選擇你的情境；指令會依建議嘗試的順序列出。

- **Claude 把東西改壞了，我想復原** → `/rewind` · `/diff`
- **從頭開始一件不相關的工作** → `/clear` · `/resume`
- **對話太長，Claude 變慢或開始忘東忘西** → `/context` · `/compact` · `/autocompact`
- **繼續昨天沒做完的工作** → `/resume` · `/rename` · `/recap`
- **大幅修改前，先看計畫** → `/plan` · `/effort` · `/model`
- **讓 Claude 一律用中文回答** → `/init` · `/memory`
- **省錢、省用量** → `/usage` · `/model` · `/effort` · `/context`
- **提交或上線前先檢查** → `/diff` · `/code-review` · `/security-review` · `/verify`
- **同時做好幾件事，或放到背景執行** → `/fork` · `/subtask` · `/background` · `/tasks` · `/batch`
- **重複執行或依排程執行工作** → `/loop` · `/schedule` · `/goal`
- **權限確認提示太多** → `/permissions` · `/fewer-permission-prompts`
- **連接工具或增加新能力** → `/mcp` · `/plugin` · `/skills`
- **製作投影片、設計或圖表** → `/slides` · `/design` · `/dataviz` · `/artifacts`
- **離開電腦，用手機繼續** → `/remote-control` · `/mobile` · `/desktop`
- **Claude Code 本身運作異常** → `/doctor` · `/status` · `/debug` · `/bug`
- **有系統地學會使用 Claude Code** → `/powerup` · `/help` · `/insights`

## 安全標記

標有這些記號的指令需要特別小心。

- **¥ 可能產生費用**: 可能消耗付費用量或產生額外費用。請先查看 `/usage` 和官方價格說明。
- **↗ 會傳送到外部**: 會把對話、程式碼或留言傳送到其他服務（Anthropic、GitHub、雲端工作階段、你瀏覽器中的網站），或推送到遠端。請先確認什麼內容會送到哪裡。
- **⚿ 可能洩漏機密**: 輸出內容（檔案、剪貼簿、報告）可能含有對話文字、金鑰、密碼或個人資料。分享前請檢查並刪除敏感內容。
- **⇄ 大範圍修改檔案**: 可能一次修改或還原很多檔案。請先提交或備份，之後用 `/diff` 檢查。
- **⚑ 會變更安全設定**: 會改變 Claude 不必詢問就能做的事，或其他安全設定。只允許你了解且信任的操作。

## 目錄

- [對話與上下文](#對話與上下文) (15)
- [模型與推理](#模型與推理) (5)
- [專案與檔案](#專案與檔案) (7)
- [審查與驗證](#審查與驗證) (7)
- [平行與背景工作](#平行與背景工作) (10)
- [自動化與排程](#自動化與排程) (4)
- [網頁、投影片與設計](#網頁投影片與設計) (9)
- [外掛、技能與整合](#外掛技能與整合) (13)
- [權限與安全](#權限與安全) (7)
- [設定與介面](#設定與介面) (10)
- [帳號與用量](#帳號與用量) (8)
- [雲端、遠端與其他裝置](#雲端遠端與其他裝置) (8)
- [診斷與意見回饋](#診斷與意見回饋) (10)
- [其他](#其他) (2)
- [已移除](#已移除) (3)

## 對話與上下文

開新對話、壓縮、倒帶、恢復對話；管理上下文視窗

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/clear`<br>`[name]`<br>★ | clear<br>清除、清空 | 開始一個上下文為空的新對話，專案記憶仍然有效。舊對話會保留，可以用 `/resume` 重新開啟；加上名稱可以在清單中幫舊對話加標籤。<br>別名: `/reset`, `/new` | 做完一個功能、要開始無關的新工作時：`/clear 登入功能`。舊內容不再干擾，用量也會減少。 |
| `/compact`<br>`[instructions]`<br>★ | compact<br>壓縮 | 把目前為止的對話整理成摘要，騰出上下文空間，並在同一個對話中繼續。可以附上指示，決定摘要要保留哪些內容。 | 長時間對話之後：`/compact 保留資料庫結構和尚未修正的 bug 清單`。 |
| `/context`<br>`[all]`<br>★ | context<br>上下文（Claude 目前能「記住」的內容） | 用彩色方格圖顯示上下文的使用量，並提供最佳化建議和容量警告。`all` 會展開每一項的明細。 | 覺得 Claude 變健忘或用量增加很快時，執行 `/context`，看看是不是大型檔案或工具輸出佔滿了視窗。 |
| `/plan`<br>`[description]`<br>★ | plan<br>計畫 | 進入計畫模式：Claude 會先調查並提出計畫，再進行編輯。附上描述的話，會立刻開始處理那項工作。 | 大幅修改之前：`/plan 修正登入驗證的 bug`，看過計畫後再核准。 |
| `/resume`<br>`[session]`<br>★ | resume<br>繼續、恢復 | 用 ID 或名稱恢復之前的對話，或開啟工作階段清單。背景工作階段會標示為 `bg`。<br>別名: `/continue` | 昨天做到一半就闔上筆電：執行 `/resume`，選擇昨天的對話。 |
| `/rewind`<br>★ · ⇄ 大範圍修改檔案 | rewind<br>倒帶 | 把對話和（或）程式碼退回到之前的檢查點，或從選取的訊息開始做摘要。<br>別名: `/checkpoint`, `/undo` | Claude 把好幾個檔案改壞了：執行 `/rewind`，選擇修改之前的那則訊息，把程式碼和對話一起還原。 |
| `/autocompact`<br>`[auto\|<tokens>]`<br>需要 v2.1.221+ | auto compact<br>自動壓縮 | 設定上下文視窗用到多滿時自動壓縮，例如 `500k`；`auto` 會恢復成依模型調整的預設值。會儲存到使用者設定並立即生效。 | 長時間工作一直被壓縮打斷：`/autocompact 500k`。 |
| `/branch`<br>`[name]` | branch<br>分支 | 在目前位置為對話建立一個分支並切換過去；原本的對話會保留，可以用 `/resume` 回去。（這是對話分支，不是 Git 分支。） | 兩種做法拿不定主意：`/branch 試試方案B`；如果不行，就回去繼續方案 A。 |
| `/btw`<br>`[question]` | by the way<br>順便問一下 | 針對目前的工作階段問一個旁支問題，不會加入對話紀錄。不加問題則顯示你最近一次的旁支問題。 | 工作進行中想弄懂一個錯誤：`/btw 這個 404 是什麼意思`，不會打亂主要工作。 |
| `/copy`<br>`[N]` | copy<br>複製 | 把最後一則回答複製到剪貼簿；`/copy 2` 複製倒數第二則。有程式碼區塊時，會出現選擇器讓你只複製其中一塊；按 `w` 改為寫入檔案（透過 SSH 連線時很有用）。 | Claude 寫好一段程式碼或指令：`/copy`，再貼到你需要的地方。 |
| `/export`<br>`[filename]`<br>⚿ 可能洩漏機密 | export<br>匯出 | 把對話匯出為純文字。有給檔名就直接存成檔案，否則會開啟「複製或儲存」對話框。 | 把一次很有價值的除錯過程存檔：`/export 除錯筆記.txt`。 |
| `/goal`<br>`[condition\|clear]` | goal<br>目標 | 設定目標：Claude 會跨多輪持續工作，直到條件達成或目標被清除。不加參數會顯示目前的目標；`clear`（或 `stop`、`off` 等）會移除目標。 | `/goal 所有測試都通過`，然後讓它反覆修改，直到測試全部通過。 |
| `/memory` | memory<br>記憶 | 編輯 `CLAUDE.md` 記憶檔案、開關自動記憶，並顯示自動記憶的項目。 | 希望每次都用中文回答：開啟 `/memory`，加上一行「請一律用繁體中文回答」。 |
| `/recap` | recap<br>回顧、摘要 | 隨時為目前的工作階段產生一句話的摘要。 | 開完會回來，忘了做到哪裡：`/recap`。 |
| `/rename`<br>`[name]` | rename<br>重新命名 | 替工作階段改名，並把名稱顯示在輸入列上；不給名稱則根據對話內容自動產生。 | 同時開著很多工作階段時：`/rename 回測`，在 `/resume` 裡一眼就能找到。 |

## 模型與推理

切換模型、調整思考力度和速度

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/model`<br>`[model]`<br>★ | model<br>模型 | 切換模型，並儲存為新工作階段的預設值。不加參數會開啟選擇器；支援的模型可以用左右鍵調整思考力度；在某一列按 `s` 則只在這次工作階段切換。 | 小修改用比較快的模型；遇到難纏的 bug 時用 `/model opus` 切換。 |
| `/advisor`<br>`[model\|off]` | advisor<br>顧問 | 開啟或關閉顧問工具，在關鍵時刻詢問第二個模型的意見。可以填 `fable`、`opus`、`sonnet` 或完整的模型 ID（`fable` 需要存取權限）。不加參數會開啟選擇器。 | 平常用較快的模型工作，但在關鍵決策時取得更強模型的第二意見：`/advisor opus`。 |
| `/effort`<br>`[level\|auto\|status\|ultracode [on\|off]]` | effort<br>努力程度（思考力度） | 設定思考力度：`low` 到 `xhigh`、`max` 或 `auto`；`status` 會顯示目前的值。`max` 只在這次工作階段有效。`ultracode on\|off` 可開關 ultracode。 | 追查時好時壞的 bug：`/effort high`；只是改錯字：`/effort low`。 |
| `/fast`<br>`[on\|off]` | fast<br>快速 | 開關快速模式（同一個模型，輸出更快）。可以在回答途中切換，但正在進行的這一輪仍以原本的速度完成。價格請參考官方 fast mode 說明。 | 趕時間時：`/fast on`；其他時候：`/fast off`。 |
| `/output-style`<br>`[style]`<br>需要 v2.1.269+ | output style<br>輸出風格 | 列出輸出風格或切換到其中一種，例如 `/output-style concise`。 | 先不加參數執行 `/output-style`，看看有哪些風格，再選一個（例如比較簡潔的風格）。 |

## 專案與檔案

設定專案記憶、新增資料夾、檢視修改

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/init`<br>★ | initialize<br>初始化 | 為專案建立一份 `CLAUDE.md` 說明，之後每個新工作階段都會先讀它。如果發現 Codex 或 Gemini CLI 的設定，會建議使用 `/import`。 | 在新的儲存庫中第一件事：`/init`，然後用 `/memory` 補充調整。 |
| `/add-dir`<br>`<path>` | add directory<br>新增資料夾 | 在這次工作階段中額外允許存取另一個工作資料夾，目前位置不會改變。輸入部分路徑後可以按 `Tab` 自動完成。新增的資料夾裡大部分的 `.claude/` 設定不會被讀取，而且大多數網路路徑無法新增。 | 前端和後端放在相鄰的資料夾：`/add-dir ../backend`。 |
| `/cd`<br>`<path>` | change directory<br>切換資料夾 | 把工作階段移到新的工作資料夾，對話會保留。和 `/add-dir` 不同，`/cd` 會改變工作階段所在的位置。 | 在錯誤的資料夾開始了：`/cd ~/projects/website`，不用從頭來過。 |
| `/diff` | difference<br>差異、修改比對 | 檢視工作目錄中的修改，包括 Claude 到目前為止做的編輯。 | 提交之前，用 `/diff` 確認到底改了什麼。 |
| `/import`<br>`[codex\|gemini\|cursor] [--dry-run] [--yes]`<br>⇄ 大範圍修改檔案 | import<br>匯入 | 從 OpenAI Codex、Gemini CLI 或 Cursor 匯入說明檔、MCP 伺服器、指令、子代理和技能。`--dry-run` 只預覽。部分雲端供應商無法使用；從 Cursor 匯入需要 v2.1.265+。 | 從 Cursor 轉過來：先執行 `/import cursor --dry-run`，再正式匯入。 |
| `/insights` | insights<br>洞察、分析 | 為你在這台電腦上最近的工作階段產生一份 HTML 報告：專案、使用習慣、容易出問題的地方、值得嘗試的功能。雲端工作階段中無法使用。 | 用了幾週之後，執行 `/insights`，發現你從沒用過的功能。 |
| `/team-onboarding`<br>⚿ 可能洩漏機密 | team onboarding<br>團隊新成員入門 | 分析你過去 30 天的工作階段、指令和 MCP 使用情況，寫出一份 Markdown 指南，讓同事可以貼上當作第一則訊息。 | 有新同事加入：執行 `/team-onboarding`，把指南傳給對方。 |

## 審查與驗證

找出 bug 和漏洞、整理程式碼、實際執行應用程式來驗證

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/code-review`<br>`[low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [--max-findings n\|all\|default] [pr#\|branch\|path]`<br>★ · 技能 · ¥ 可能產生費用 · ↗ 會傳送到外部 · ⇄ 大範圍修改檔案 | code review<br>程式碼審查 | 檢查目前的修改（或指定的 PR、分支、路徑）有沒有正確性方面的 bug。`--fix` 會套用修正，`--comment` 會發布到 GitHub PR 或 GitLab MR，`ultra` 會在雲端進行深度審查。<br>別名: `/review` | 提交之前：`/code-review high --fix`。審查 PR：`/code-review high 1234`。 |
| `/run`<br>技能 | run<br>執行 | 啟動並操作你專案的應用程式，看看修改實際運作的樣子。 | `/run`，啟動網站並截圖新的首頁。 |
| `/run-skill-generator`<br>技能 | skill generator<br>技能產生器 | 為這個專案寫一個專屬技能，教 `/run` 和 `/verify` 如何從乾淨的環境建置、啟動和操作你的應用程式。 | 啟動需要好幾個步驟（例如要先開資料庫）：執行一次這個指令，之後 `/run` 就能直接運作。 |
| `/security-review` | security review<br>安全性審查 | 比對你的分支與 origin 預設分支之間的差異，找出漏洞，例如注入、驗證問題和資料外洩。需要名為 `origin` 的遠端。 | 任何涉及登入驗證、付款或使用者資料的修改，上線前都跑一次。 |
| `/simplify`<br>`[target]`<br>技能 · ⇄ 大範圍修改檔案 | simplify<br>簡化 | 4 個代理平行檢查修改過的程式碼：能否重複利用、能否更簡單、效率、抽象層級，然後直接套用修正。它不會找正確性的 bug；那要用 `/code-review`。 | 功能已經能正常運作，想讓程式碼更乾淨：`/simplify`。 |
| `/ultrareview`<br>`[PR or branch]`<br>¥ 可能產生費用 | ultra review<br>超深度審查 | 在雲端沙箱中用多個代理深度審查。建議的寫法是 `/code-review ultra`；`/ultrareview` 是別名。Pro、Max 和 Ultra 包含 3 次免費執行，之後需要用量額度。 | 重大版本發布前：`/code-review ultra`。 |
| `/verify`<br>技能 | verify<br>驗證 | 實際建置、執行並觀察你的應用程式，確認修改有效，而不是只依賴測試或型別檢查。只有在你呼叫時才會執行。 | 改了按鈕的行為：`/verify`，讓它真的去點一下。 |

## 平行與背景工作

同時執行多個代理，或把工作移到背景

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/agents` | agents<br>代理（智慧代理） | 顯示一則提醒：請直接要求 Claude 建立或管理子代理，或直接編輯 `.claude/agents/`。在 v2.1.197 及更早的版本中，會開啟互動式管理介面。 | 直接說：「建立一個只負責寫測試的子代理。」 |
| `/background`<br>`[prompt]` | background<br>背景 | 把工作階段轉為背景代理繼續執行，並釋放終端機。可以先再傳一條指示。用 `claude agents` 查看狀態。<br>別名: `/bg` | 需要 30 分鐘的工作：`/bg 完成後把結果寫進 report.md`。 |
| `/batch`<br>`<instruction>`<br>技能 · ⇄ 大範圍修改檔案 | batch<br>批次 | 平行處理大規模修改：先研究程式碼，把工作拆成 5～30 個獨立單元並提出計畫；經你核准後，每個單元由一個背景子代理在自己的 worktree 中實作並測試。需要 git 儲存庫或 WorktreeCreate hook。 | `/batch 把 src/ 從 JavaScript 遷移到 TypeScript`。 |
| `/fork`<br>`[prompt]` | fork<br>分岔（複製一份） | 把對話複製成一個新的背景工作階段，你可以繼續在這裡工作。附上指示的話，副本會立刻開始；通常會先讓它建立自己的 worktree。 | 正在做功能 A，想同時修一個小問題：`/fork 修正頁尾對齊`。 |
| `/list-agents`<br>需要 v2.1.224+ | list agents<br>列出代理 | 列出 Claude 可以傳訊息的子代理、團隊成員和其他工作階段，以及各自要用的名稱。只在啟用跨工作階段訊息時可用。<br>別名: `/peers` | 協調多個工作階段時：確認每個工作階段的名稱。 |
| `/stop` | stop<br>停止 | 停止你目前連接的背景工作階段；紀錄和 worktree 會保留。只想中斷連接而不停止，請用 `/exit` 或按 `←`。 | 背景工作偏離方向：`/stop`。 |
| `/subtask`<br>`<task>` | subtask<br>子任務 | 派出一個分岔的子代理，它會繼承對話內容，並把結果回報到這裡。與 `/fork` 的差別：`/subtask` 會把結果回報到這裡，`/fork` 則會另開一個獨立的工作階段。 | `/subtask 替這些 API 端點寫文件`，你這邊繼續寫程式。 |
| `/tasks` | tasks<br>工作、任務 | 檢視並管理這次工作階段中的背景工作，包括已完成的子代理。<br>別名: `/bashes` | 用 `/tasks` 查看背景測試或子代理的進度。 |
| `/workflow-authoring`<br>技能 | workflow authoring<br>撰寫工作流程 | 載入撰寫動態工作流程腳本的參考資料。Claude 通常會自己載入；手動編輯已儲存的腳本前可以先執行。只在啟用動態工作流程時可用。 | 手動編輯已儲存的工作流程腳本之前。 |
| `/workflows` | workflows<br>工作流程 | 開啟工作流程進度畫面，可以查看、暫停、繼續或儲存正在執行和已完成的工作流程。 | 隨時留意一個執行很久的工作流程。 |

## 自動化與排程

依間隔重複、依排程執行、自動修正 pull request

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/loop`<br>`[interval] [prompt]`<br>★ · 技能 | loop<br>迴圈 | 在工作階段開著的期間反覆執行一個提示。不寫間隔則由 Claude 自己決定節奏；不寫提示則執行內建的維護提示或你的 `loop.md`。<br>別名: `/proactive` | `/loop 5m 檢查部署是否完成`。如果要在電腦關機時也繼續執行，請用 `/schedule`。 |
| `/autofix-pr`<br>`[prompt]`<br>↗ 會傳送到外部 | auto-fix PR<br>自動修正 PR | 開啟一個雲端工作階段，盯著目前分支的 PR，在 CI 失敗或有審查意見時推送修正。需要 `gh` CLI 和雲端工作階段。 | `/autofix-pr 只修 lint 和型別錯誤`。 |
| `/deep-research`<br>`<question>`<br>工作流程 | deep research<br>深度研究 | 內建的工作流程：大量搜尋網路、抓取並交叉比對來源，然後寫出附有引用的報告。在背景執行。 | `/deep-research 比較主流 AI 影片工具的價格和品質`。 |
| `/schedule`<br>`[description]` | schedule<br>排程 | 透過引導式對話，建立、更新、列出或執行雲端排程工作（以前叫 routines）。使用 Console API 金鑰時無法使用。<br>別名: `/routines` | `/schedule 每個工作日早上 9 點，整理儲存庫中新的 issue`。 |

## 網頁、投影片與設計

製作可以分享的網頁、簡報、設計和圖表

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/artifact-capabilities`<br>技能 | artifact capabilities<br>成品頁面的進階功能 | 載入 artifact 執行時功能的參考資料，例如呼叫連接器或提供下載，以及你的帳號有哪些功能。Claude 通常會自己載入。 | 要做一個很多人填寫的頁面之前。 |
| `/artifact-diagramming`<br>技能 · 需要 v2.1.221+ | artifact diagramming<br>成品頁面中的繪圖 | 載入在 artifact 中繪製圖表的指引：什麼時候圖有幫助、要畫什麼，以及如何寫出在淺色和深色主題下都清楚的 SVG。 | 需要一張清楚的架構圖時。 |
| `/artifacts` | artifacts<br>成品（發布的網頁） | 列出你擁有或別人分享給你的 artifact，然後可以接入其中一個、開啟它，或複製連結。只在支援 artifact 的環境中可用。 | 找到上週做的儀表板，繼續編輯。 |
| `/dataviz`<br>`[request]`<br>技能 | data visualization<br>資料視覺化 | 圖表設計指引：選擇圖表形式、依角色分配顏色，並用內建的腳本檢查配色是否色盲友善、對比是否足夠。 | `/dataviz 把這份每月銷售表做成趨勢圖`。 |
| `/design`<br>`[brief]`<br>技能 · 需要 v2.1.265+ | design<br>設計 | 在同一張畫布上以多個畫板草擬 UI 設計稿、操作流程、到達頁或海報（Claude Design artifact）；可在桌面瀏覽器中編輯，並匯出 PNG 或 PDF。Bedrock、Vertex 及其他第三方平台無法使用。 | `/design 行動網銀 App 的設定畫面`。 |
| `/design consent` | consent / revoke<br>同意 / 撤銷 | 授予或撤回 Claude 對 Claude Design 的存取權。當 Claude 要求你執行 `/design consent` 時，請自己輸入。<br>別名: `/design revoke` | 出現提示時，自己輸入 `/design consent`。 |
| `/design-login` | design login<br>設計登入 | 當 `/design-sync` 或 `/design consent` 要求時，用你的 claude.ai 帳號為 `/design-sync` 授權設計系統存取。 | `/design-sync` 要求你登入時執行。 |
| `/design-sync`<br>`[hint]`<br>技能 · ↗ 會傳送到外部 | design sync<br>設計同步 | 把你儲存庫中的 React 設計系統轉換並上傳到 Claude Design，讓設計使用你真正的元件。大型儲存庫第一次同步可能要好幾個小時。上傳目標是獨立的 claude.ai/design 網站，該網站將在 2026 年 12 月 14 日前關閉。 | `/design-sync Acme DS`（請注意上面提到的關閉日期）。 |
| `/slides`<br>`[brief]`<br>技能 · 需要 v2.1.265+ | slides<br>投影片 | 根據你的說明製作一份 Claude Slides artifact。需要支援 artifact 的工作階段，以及可以使用 Slides 範本的帳號。 | `/slides 給主管看的季度回顧，8 張投影片`。 |

## 外掛、技能與整合

用外掛、技能、MCP 伺服器、瀏覽器和 IDE 整合擴充 Claude

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/mcp`<br>`[reconnect (<server>\|all)\|enable\|disable [<server>\|all]]`<br>★ | MCP (Model Context Protocol)<br>MCP（Model Context Protocol，模型上下文協定） | 管理 MCP 伺服器連線和 OAuth。不加參數會開啟清單；`reconnect`、`enable` 或 `disable` 加上伺服器名稱或 `all` 可直接操作。 | 連接器失敗或需要驗證：`/mcp reconnect all`。 |
| `/chrome` | Chrome<br>Chrome 瀏覽器 | 設定 Claude in Chrome。 | 第一次連接 Chrome 擴充功能時。 |
| `/claude-api`<br>`[subcommand]`<br>技能 | Claude API<br>Claude API（Claude 程式介面） | 載入適合你專案程式語言的 Claude API 和 Managed Agents 參考資料；程式碼匯入 `anthropic` 時會自動啟用。子指令包括 `migrate`、`upgrade`、`api-version`、`cost-optimize`、`latency-optimize`、`build-eval`、`prompt-audit`。 | 降低你的應用程式的 API 花費：`/claude-api cost-optimize`。 |
| `/claude-in-chrome`<br>`[task]`<br>技能 · ↗ 會傳送到外部 | Claude in Chrome<br>Claude in Chrome（在 Chrome 瀏覽器中使用 Claude） | 透過 Claude in Chrome 讓 Claude 在你的瀏覽器中執行工作，例如測試網頁或讀取主控台紀錄。需要啟用 Chrome 整合（例如 `claude --chrome`）。 | `/claude-in-chrome 測試我本機網站的註冊流程並回報錯誤`。 |
| `/ide` | IDE (integrated development environment)<br>IDE（整合開發環境，程式碼編輯器） | 管理 IDE 整合並顯示狀態。 | 編輯器裡看不到修改時，檢查連線狀態。 |
| `/install-github-app`<br>↗ 會傳送到外部 · ⚑ 會變更安全設定 | install GitHub app<br>安裝 GitHub 應用程式 | 為儲存庫安裝 Claude GitHub App，也可以順便設定 GitHub Actions 工作流程和機密（secrets）。只適用於 github.com。 | 想在 issue 和 PR 中提及 Claude，讓它在那裡工作。 |
| `/install-slack-app` | install Slack app<br>安裝 Slack 應用程式 | 透過瀏覽器的 OAuth 流程安裝 Claude Slack 應用程式。 | 團隊想在 Slack 裡使用 Claude。 |
| `/plugin`<br>`[subcommand]` | plugin<br>外掛 | 管理外掛。不加參數會開啟選單；`list`、`install`、`enable`、`disable` 可直接操作。如果安裝摘要有提示，請執行 `/reload-plugins`。 | 用 `/plugin` 瀏覽，安裝一個適合你工作的外掛。 |
| `/plugin-authoring`<br>技能 · 需要 v2.1.287+ | plugin authoring<br>撰寫擴充（mod） | 載入撰寫 mod 的參考資料。這是內建外掛提供的技能，可以在 `/plugin` 中關閉。 | 想做一個固定在對話旁邊的小側邊面板時。 |
| `/reload-plugins`<br>`[--force]` | reload plugins<br>重新載入外掛 | 不必重新啟動就重新載入啟用中的外掛，並回報載入錯誤。如果重新載入會改變已載入的 MCP 工具、讓提示快取失效，它會發出警告並略過，除非你加上 `--force`。 | 剛裝好一個要求重新載入的外掛之後。 |
| `/reload-skills` | reload skills<br>重新載入技能 | 重新掃描技能和指令資料夾，讓工作階段中新增或修改的技能不必重新啟動就能使用。 | 剛寫好一個自訂技能，想馬上使用。 |
| `/skill-doctor`<br>需要 v2.1.252+ | skill doctor<br>技能健檢 | 顯示每個技能佔用的上下文和使用情況，幫你找出可以關閉的技能。 | 定期執行，清理沒在用的技能。 |
| `/skills` | skills<br>技能 | 列出技能並可篩選。`t` 依 token 數排序，`Space`/`Enter` 切換技能對 Claude 和 `/` 選單是否可見，`Esc` 儲存並關閉。 | 技能太多：`/skills`，按 `t`，把佔空間又用不到的技能隱藏起來。 |

## 權限與安全

控制 Claude 可以做什麼、哪些事需要你核准

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/permissions`<br>★ · ⚑ 會變更安全設定 | permissions<br>權限 | 管理工具的允許、詢問和拒絕規則：依範圍檢視、新增或移除規則、管理工作資料夾，查看「Recently blocked」分頁（自動模式擋下的操作）和分類器規則。<br>別名: `/allowed-tools` | 每次都要核准 `npm test` 很煩：在這裡把它設為允許。 |
| `/auto-mode-setup`<br>⚑ 會變更安全設定 | auto mode setup<br>自動模式設定 | 根據你的專案和最近的工作階段，草擬 `autoMode.environment` 項目，讓你檢查後儲存。有版本和方案的限制。 | 自動模式一直擋下例行操作時。 |
| `/fewer-permission-prompts`<br>技能 · ⚑ 會變更安全設定 | fewer permission prompts<br>減少權限提示 | 掃描對話紀錄中常見的唯讀 Bash 和 MCP 呼叫，依優先順序把允許清單加到專案的 `.claude/settings.json`。 | 核准提示一直打斷你時，執行一次。 |
| `/hooks` | hooks<br>hook（在特定時機自動執行的腳本） | 檢視 hook 設定。 | 某個 hook 似乎讓每次編輯都出錯時，看看設定了什麼。 |
| `/privacy-settings` | privacy settings<br>隱私設定 | 檢視和更新隱私設定。只限 Pro、Max 和 Ultra。 | 想確認你的資料如何被使用時。 |
| `/sandbox`<br>⚑ 會變更安全設定 | sandbox<br>沙箱（隔離環境） | 開關沙箱模式，只在支援的平台上可用。 | 執行不熟悉的腳本之前先開啟。 |
| `/update-config`<br>`[request]`<br>技能 · ⚑ 會變更安全設定 | update config<br>更新設定 | 描述你想要的設定變更（允許某個指令、設定環境變數、加入 hook），Claude 就會編輯對應的 `settings.json`。主題和模型請用 `/config`。 | `/update-config 每次編輯檔案後執行 prettier`。 |

## 設定與介面

主題、顏色、狀態列、快速鍵、語音

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/color`<br>`[color\|default]` | color<br>顏色 | 設定這次工作階段輸入列的顏色：`red`、`blue`、`green`、`yellow`、`purple`、`orange`、`pink` 或 `cyan`；`default` 恢復預設，不加參數則隨機選一個顏色。 | 用 `/color red` 標示正式環境的工作階段。 |
| `/config`<br>`[key=value ...]` | config<br>設定 | 開啟設定畫面，調整主題、模型、輸出風格等，或直接設定 `key=value`，例如 `/config theme=dark`。`/config --help` 會列出可用的鍵。<br>別名: `/settings` | `/config theme=dark`。 |
| `/focus` | focus<br>專注 | 切換一種只顯示你最後一則提示、一行工具摘要和最終回答的畫面。只限全螢幕渲染模式。 | 隱藏中間步驟，只看結果。 |
| `/keybindings` | keybindings<br>快速鍵 | 開啟你的快速鍵設定檔。 | 把操作改成你習慣的按鍵。 |
| `/scroll-speed` | scroll speed<br>捲動速度 | 調整滑鼠滾輪的捲動速度。只限全螢幕渲染模式；JetBrains 終端機中無法使用。 | 滾一格就跳太遠時，把速度調慢。 |
| `/statusline` | status line<br>狀態列 | 設定狀態列；描述你想顯示的內容，或不加參數，從你的 shell 提示字元自動產生。 | `/statusline 顯示模型和 git 分支`。 |
| `/terminal-setup` | terminal setup<br>終端機設定 | 在 VS Code、Cursor、Devin Desktop、Alacritty 或 Zed 中設定 Shift+Enter 換行；在 Apple 終端機中啟用 Option+Enter 並關閉提示音；在 iTerm2 中開啟剪貼簿存取，讓 `/copy` 可以使用。 | 按 Enter 老是把寫到一半的提示送出去：執行一次這個指令。 |
| `/theme` | theme<br>主題配色 | 更換配色主題：`auto`、淺色和深色、色盲友善、ANSI 和自訂主題。 | 晚上切換成深色主題。 |
| `/tui`<br>`[default\|fullscreen]` | TUI (text user interface)<br>TUI（文字使用者介面） | 設定終端機的渲染方式，並在保留對話的情況下重新啟動。`fullscreen` 是不會閃爍的渲染方式。不加參數會顯示目前使用的渲染方式。 | 畫面閃爍時：`/tui fullscreen`。 |
| `/voice`<br>`[hold\|tap\|off]` | voice<br>語音 | 開關語音輸入，或設定模式（`hold`、`tap`）。需要 Claude.ai 帳號。 | 用說的下指示，不必打字。 |

## 帳號與用量

登入、查看上限和費用、升級

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/usage`<br>★ | usage<br>用量 | 顯示這次工作階段的費用、今天／本週／本月的花費、方案用量上限和活動統計，包括訂閱方案中哪些項目會計入上限。`/stats` 會開啟統計分頁。每則警告都會寫明原因和一句話的解決方法，按 `f` 即可套用這些修正。<br>別名: `/cost`, `/stats` | 決定要不要換成比較便宜的模型之前，先看一下 `/usage`。 |
| `/login` | log in<br>登入 | 登入你的 Anthropic 帳號。 | 換新電腦或登入過期時。 |
| `/logout` | log out<br>登出 | 登出你的 Anthropic 帳號。 | 用完共用電腦之後。 |
| `/passes` | passes<br>體驗券 | 和朋友分享一週免費的 Claude Code；只有符合資格的帳號才會顯示。 | 邀請朋友試用。 |
| `/rate-limit-options` | rate limit options<br>用量上限的應對選項 | 當 claude.ai 的用量上限擋住你時，顯示可以繼續工作的方法：等待並自動繼續、加購用量額度，或升級。需要 claude.ai 訂閱。 | 半夜被上限擋住：選擇在重設後自動繼續。 |
| `/status` | status<br>狀態 | 開啟設定的「狀態」分頁：版本、模型、帳號、連線狀況。Claude 正在回答時也能使用。 | 向別人求助之前，先截一張 `/status` 的畫面。 |
| `/upgrade` | upgrade<br>升級 | 在瀏覽器中開啟升級頁面。 | 老是碰到用量上限時。 |
| `/usage-credits`<br>¥ 可能產生費用 | usage credits<br>用量額度 | 設定或申請用量額度；沒有帳單權限的 Team 和 Enterprise 成員會向管理員送出申請。以前叫 `/extra-usage`。 | 團隊額度用完時，向管理員申請額度。 |

## 雲端、遠端與其他裝置

在桌面、手機、網頁和雲端之間接續工作

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/desktop` | desktop<br>桌面應用程式 | 在 Claude Code 桌面版 App 中繼續這次工作階段。需要 macOS 或 x64 Windows，以及 Claude 訂閱。<br>別名: `/app` | 從終端機換到桌面版 App。 |
| `/mobile` | mobile<br>手機 | 顯示下載 Claude 手機 App 的 QR code。<br>別名: `/ios`, `/android` | 想用手機跟上進度時。 |
| `/remote-control`<br>↗ 會傳送到外部 | remote control<br>遠端控制 | 讓這次工作階段可以從 claude.ai 進行遠端控制（Remote Control）。需要 claude.ai 訂閱。<br>別名: `/rc` | 讓工作繼續執行，用手機下指示：`/rc`。 |
| `/remote-env` | remote environment<br>遠端環境（雲端環境） | 選擇從 CLI 啟動雲端工作階段時預設使用的雲端環境。 | 有好幾個環境時，選一個當預設值。 |
| `/setup-bedrock` | set up Bedrock<br>設定 Amazon Bedrock | 透過精靈設定 Amazon Bedrock 的驗證、區域和固定使用的模型。設定 `CLAUDE_CODE_USE_BEDROCK=1` 之前不會出現在選單中；需要完整輸入。 | 你的公司透過 AWS 使用 Claude 時。 |
| `/setup-vertex` | set up Vertex<br>設定 Google Cloud | 透過精靈設定 Google Cloud 的 Agent Platform。設定 `CLAUDE_CODE_USE_VERTEX=1` 之前不會出現在選單中；需要完整輸入。 | 你的公司透過 Google Cloud 使用 Claude 時。 |
| `/teleport` | teleport<br>瞬間移動 | 把雲端工作階段拉到這個終端機，同時取得它的分支和對話。需要 claude.ai 訂閱。<br>別名: `/tp` | 在本機繼續從網頁版開始的工作。 |
| `/web-setup` | web setup<br>網頁版設定 | 用你本機的 `gh` 登入資訊，為雲端工作階段連接 GitHub。 | 第一次使用雲端工作階段之前。 |

## 診斷與意見回饋

出問題時先看這裡

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/doctor`<br>`[prompt-audit [path]]`<br>★ · 技能 | doctor<br>醫生（健檢） | 為安裝、設定、擴充功能和 `CLAUDE.md` 做健檢，並提出修正方案，經你確認後由 Claude 套用。`prompt-audit` 則改為審查你的說明內容。<br>別名: `/checkup` | 感覺哪裡怪怪的：先執行 `/doctor`。 |
| `/help`<br>★ | help<br>說明 | 顯示說明和可用的指令。 | 忘了某個指令：`/help`，或輸入 `/` 加幾個字母。 |
| `/powerup`<br>★ | power up<br>能力提升 | 附有動畫示範的互動式課程，教你 Claude Code 的各種功能。 | 新手有系統地入門的最佳起點。 |
| `/bug`<br>`[report]`<br>↗ 會傳送到外部 · ⚿ 可能洩漏機密 | bug<br>程式錯誤（bug） | 回報 bug 或分享你的對話；你可以選擇要附上多少紀錄，而且在送出任何內容前都會請你確認。<br>別名: `/share` | Claude Code 本身出現異常時。 |
| `/debug`<br>`[description]`<br>技能 | debug<br>除錯 | 從現在開始啟用除錯紀錄，並透過閱讀工作階段的除錯紀錄來排查問題。可以附上問題描述。 | `/debug MCP 伺服器一直連不上`。 |
| `/exit` | exit<br>離開 | 離開 CLI。在已連接的背景工作階段中，它只會中斷連接，工作階段會繼續執行。<br>別名: `/quit` | 今天的工作結束了。 |
| `/feedback`<br>`[report]`<br>↗ 會傳送到外部 · ⚿ 可能洩漏機密 | feedback<br>意見回饋 | 用和 `/bug` 相同的對話框和同意步驟送出產品意見。 | 想要求新功能時。 |
| `/heapdump`<br>⚿ 可能洩漏機密 | heap dump<br>堆積傾印（記憶體快照） | 把 heap 快照和記憶體明細寫到桌面，用來診斷記憶體用量過高的問題。只分享 `-diagnostics.json`；`.heapsnapshot` 含有你的對話和登入憑證。選單中不會顯示。 | 回報記憶體用量暴增的問題。 |
| `/release-notes` | release notes<br>版本更新說明 | 在版本選擇器中查看更新紀錄；內容會顯示出來，但不會進入 Claude 的上下文。 | 更新之後看看有什麼新功能。 |
| `/restart`<br>需要 v2.1.288+ | restart<br>重新啟動 | 重新啟動 Claude Code 並恢復工作階段，以套用已安裝的更新。需要 Pro、Max 或 Ultra，以及在 macOS 或 Linux 上的原生安裝（不支援 WSL）。<br>別名: `/update` | 更新後底部出現提示時。 |

## 其他

小功能

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/radio` | radio<br>電台 | 在瀏覽器中開啟 Claude FM lo-fi 電台，或顯示串流網址。 | 工作時的背景音樂。 |
| `/stickers` | stickers<br>貼紙 | 訂購 Claude Code 貼紙。 | 裝飾你的筆電。 |

## 已移除

舊的教學中可能還看得到，但已經無法使用

| 指令 | 英文原意 | 功能 | 最佳用法 |
|---|---|---|---|
| `/pr-comments`<br>`[PR]`<br>v2.1.91 已移除 | PR comments<br>PR 留言 | 已在 v2.1.91 移除。直接請 Claude 查看 pull request 的留言即可。 | 直接用中文提出要求。 |
| `/ultraplan`<br>`<prompt>` | ultra plan<br>超級計畫 | 已移除。請改用計畫模式（`/plan`）。 | 請改用 `/plan`。 |
| `/vim`<br>v2.1.92 已移除 | Vim<br>Vim（一種用鍵盤操作的編輯方式） | 已在 v2.1.92 移除。請改用 `/config` → Editor mode。 | 請改用 `/config`。 |

## 免責聲明

1. **非官方專案**: 這是社群專案，與 Anthropic 沒有隸屬關係，也沒有獲得 Anthropic 贊助或認可。「Claude」、「Claude Code」及相關標示是 Anthropic 的商標，這裡只用來指出所介紹的產品。
2. **內容可能過時或有誤**: 每一則說明都是官方文件的簡化改寫，依「現狀」提供，不提供任何明示或默示的保證。Claude Code 經常更新，指令會新增、改名或移除。本專案與官方文件不一致時，以官方文件為準。
3. **使用風險請自行承擔**: 部分指令會修改或還原檔案、執行指令、推送程式碼、把資料傳送到外部服務，或消耗付費用量。執行前請先了解指令會做什麼，並先提交或備份；未經檢查，請勿用在正式環境、重要資料或別人的儲存庫上。
4. **保護機密與隱私**: 請勿在提示中放入 API 金鑰、密碼、權杖或他人的個人資料。匯出的對話、錯誤回報和記憶體快照可能含有這些內容；分享前請先檢查。
5. **範例僅供說明**: 「最佳用法」中的範例是用來說明用途，並不是針對你的環境的操作指示。能否使用取決於版本、方案、平台和組織政策。
6. **本頁面不會追蹤你**: 本頁面不使用 Cookie、流量分析、第三方腳本或字型。只會在你的瀏覽器本機儲存語言和主題偏好。
7. **責任限制**: 在法律允許的最大範圍內，作者和貢獻者對於使用本專案所造成的任何損失不負責任，包括資料遺失、費用、安全事件或服務中斷。

## 關於本專案

- **來源**：依據官方[指令參考文件](https://code.claude.com/docs/en/commands)改寫，查核日期 2026-11-07。說明經過簡化，並非官方翻譯；如有出入，以官方文件為準。
- **資料**：所有內容都由 [`data/commands.json`](data/commands.json) 產生。編輯 JSON 後，執行 `python3 scripts/build.py`。
- **參與貢獻**：請見 [CONTRIBUTING.md](CONTRIBUTING.md)。
- **授權**：內容採用 [CC BY 4.0](LICENSE-CONTENT)，程式碼採用 [MIT](LICENSE)。
