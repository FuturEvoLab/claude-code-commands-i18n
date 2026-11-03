# Claude Code 命令大全

[English](README.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-Hant.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md)

![Unofficial](https://img.shields.io/badge/Anthropic-unofficial-lightgrey) [![check](https://github.com/FuturEvoLab/claude-code-commands-i18n/actions/workflows/check.yml/badge.svg)](https://github.com/FuturEvoLab/claude-code-commands-i18n/actions/workflows/check.yml) [![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-blue)](LICENSE-CONTENT) [![Code: MIT](https://img.shields.io/badge/code-MIT-green)](LICENSE) ![Commands](https://img.shields.io/badge/commands-115-teal)

> 非官方的 Claude Code 斜杠命令速查手册，提供**英文、日文、简体中文、繁体中文、韩语、俄语、西班牙语**七种语言，专门写给读英文官方文档吃力的用户：每个命令都有英文原意、简单易懂的说明，以及一个真实的「什么时候用」的例子。

### [可搜索的网页版 →](https://futurevolab.github.io/claude-code-commands-i18n/)

[![Claude Code 命令大全](docs/assets/preview-en.png)](https://futurevolab.github.io/claude-code-commands-i18n/)

<p><img src="docs/assets/preview-search.png" alt="search" width="68%"> <img src="docs/assets/preview-mobile.png" alt="mobile" width="28%"></p>

## 如何看懂命令写法

- 在输入框输入 `/` 会弹出命令列表，继续输入字母可以筛选。
- `[ ]` 表示可写可不写，`< >` 表示必须写，`|` 表示几选一。参数可以直接用中文写。
- **技能**：交给 Claude 执行的一套提示流程。**工作流**：派出多个代理在后台运行。
- 很多命令只在特定版本、套餐、平台或开启某功能后才出现。以你自己看到的列表为准，可用 `/status` 查看版本。

## ★ 新手推荐

编者为刚开始使用 Claude Code 的人挑选的命令。

- `/clear` · 开始全新对话，旧对话可找回
- `/compact` · 压缩长对话，腾出空间继续聊
- `/context` · 查看记忆空间被什么占满
- `/plan` · 先出方案、你批准后再动手
- `/resume` · 回到以前的对话
- `/rewind` · 撤销：把代码和对话退回之前
- `/model` · 切换模型
- `/init` · 生成项目说明书 CLAUDE.md
- `/code-review` · 提交前检查 bug，可自动修复
- `/loop` · 按间隔重复执行一条指令
- `/mcp` · 管理外部工具连接
- `/permissions` · 设置哪些操作可以直接做
- `/usage` · 查看费用和额度
- `/doctor` · 出问题时先体检
- `/help` · 查看帮助和全部命令
- `/powerup` · 互动课程，系统学习功能

## 按场景找命令

按你想做的事来找，命令按建议尝试的顺序排列。

- **Claude 改坏了，我想撤销** → `/rewind` · `/diff`
- **换一件不相关的事，从头开始** → `/clear` · `/resume`
- **对话太长，Claude 变慢或开始忘事** → `/context` · `/compact` · `/autocompact`
- **接着做昨天没做完的** → `/resume` · `/rename` · `/recap`
- **大改动前，想先看方案再让它动手** → `/plan` · `/effort` · `/model`
- **让 Claude 一直用中文回答** → `/init` · `/memory`
- **省钱、省额度** → `/usage` · `/model` · `/effort` · `/context`
- **提交或上线前做检查** → `/diff` · `/code-review` · `/security-review` · `/verify`
- **同时做几件事 / 放后台跑** → `/fork` · `/subtask` · `/background` · `/tasks` · `/batch`
- **让它反复做或定时做** → `/loop` · `/schedule` · `/goal`
- **权限确认弹窗太多** → `/permissions` · `/fewer-permission-prompts`
- **连接外部工具或安装新能力** → `/mcp` · `/plugin` · `/skills`
- **做幻灯片、设计稿或图表** → `/slides` · `/design` · `/dataviz` · `/artifacts`
- **离开电脑，用手机继续** → `/remote-control` · `/mobile` · `/desktop`
- **Claude Code 本身出问题了** → `/doctor` · `/status` · `/debug` · `/bug`
- **系统学习怎么用** → `/powerup` · `/help` · `/insights`

## 安全标记

带有以下标记的命令需要格外小心。

- **¥ 可能产生费用**: 可能消耗付费额度或产生额外费用。使用前用 `/usage` 确认额度，并查看官方价格说明。
- **↗ 会发送到外部**: 会把对话、代码或评论发送到其他服务（如 Anthropic、GitHub、云端会话、浏览器中的网站），或推送到远程仓库。确认内容和目标后再运行。
- **⚿ 可能包含敏感信息**: 生成的文件、剪贴板内容或报告中可能含有对话内容、密钥、密码或个人信息。分享前务必检查并删除敏感内容。
- **⇄ 会大范围修改文件**: 可能一次修改或还原很多文件。运行前先用 Git 提交或备份，运行后用 `/diff` 检查。
- **⚑ 会改变安全设置**: 会改变 Claude 无需询问就能执行的操作范围，或其他安全相关设置。只放行你理解且信任的操作。

## 目录

- [对话与上下文](#对话与上下文) (15)
- [模型与推理](#模型与推理) (5)
- [项目与文件](#项目与文件) (7)
- [审查与验证](#审查与验证) (7)
- [并行与后台](#并行与后台) (10)
- [定时与自动化](#定时与自动化) (4)
- [网页、幻灯片与设计](#网页幻灯片与设计) (9)
- [插件、技能与外部连接](#插件技能与外部连接) (13)
- [权限与安全](#权限与安全) (7)
- [设置与界面](#设置与界面) (10)
- [账号与用量](#账号与用量) (8)
- [云端、远程与其他设备](#云端远程与其他设备) (8)
- [诊断与反馈](#诊断与反馈) (10)
- [其他](#其他) (2)
- [已移除](#已移除) (3)

## 对话与上下文

新开、压缩、撤销、找回对话，管理 Claude 的「记忆空间」

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/clear`<br>`[name]`<br>★ | clear<br>清空 | 开始一个上下文为空的新对话。项目记忆（CLAUDE.md）仍然有效。旧对话不会删除，可以用 `/resume` 找回；写上名字可以给旧对话加标签。<br>同义命令: `/reset`, `/new` | 做完一个功能、要开始一件无关的新任务时：`/clear 登录功能`。避免旧内容干扰，也更省用量。 |
| `/compact`<br>`[instructions]`<br>★ | compact<br>压缩 | 把到目前为止的对话总结成摘要，腾出上下文空间，对话继续。可以附上「摘要要重点保留什么」。 | 长时间对话后：`/compact 保留数据库结构和尚未修复的 bug 列表`。 |
| `/context`<br>`[all]`<br>★ | context<br>上下文（Claude 当前能「记住」的内容） | 用彩色方格图显示上下文用了多少、被什么占用，并给出节省建议和容量警告。`all` 展开全部明细。 | 感觉 Claude 变「健忘」或用量涨得快时，先 `/context` 看是不是被大文件或工具输出占满。 |
| `/plan`<br>`[description]`<br>★ | plan<br>计划 | 直接进入计划模式：Claude 先调查并提出方案，你批准后才开始修改文件。可附上任务描述立即开始。 | 大改动之前：`/plan 修复登录报错`，看完方案再放手让它改。 |
| `/resume`<br>`[session]`<br>★ | resume<br>继续、恢复 | 按 ID 或名字恢复以前的对话，不写参数则打开对话列表。后台会话会标记为 `bg`。<br>同义命令: `/continue` | 昨天没做完就关了电脑：今天 `/resume`，选昨天的对话接着做。 |
| `/rewind`<br>★ · ⇄ 会大范围修改文件 | rewind<br>倒带 | 把对话和/或代码退回到之前的某个检查点，或者从选中的消息开始做摘要。类似游戏「读档」。<br>同义命令: `/checkpoint`, `/undo` | Claude 把文件改坏了：`/rewind`，选择改动之前的那条消息，代码和对话一起恢复。 |
| `/autocompact`<br>`[auto\|<tokens>]`<br>需 v2.1.221+ | auto compact<br>自动压缩 | 设置上下文用到多满时自动压缩，例如 `500k`；`auto` 恢复为模型默认值。保存到用户设置并立即生效。 | 长任务不想被频繁压缩打断：`/autocompact 500k`。 |
| `/branch`<br>`[name]` | branch<br>分支 | 在当前位置为对话建一个分支并切换过去，用来尝试另一个方向；原对话保留，可用 `/resume` 回去。（这是对话分支，不是 Git 分支。） | 方案 A 和 B 拿不准：`/branch 试方案B`，不行就回到原对话继续 A。 |
| `/btw`<br>`[question]` | by the way<br>顺便问一下 | 就当前会话问一个旁支问题，答案不会加入对话历史。不带问题则显示最近一次旁支问答。 | Claude 正在写代码，你想知道一个报错的意思：`/btw 这个 404 是什么意思`，不打乱主任务。 |
| `/copy`<br>`[N]` | copy<br>复制 | 把最近一条回答复制到剪贴板；`/copy 2` 复制倒数第二条。有代码块时会弹出选择器，可只复制某一块；按 `w` 写入文件（SSH 远程时有用）。 | Claude 写好一段文案或命令，`/copy` 直接粘贴到别处。 |
| `/export`<br>`[filename]`<br>⚿ 可能包含敏感信息 | export<br>导出 | 把当前对话导出为纯文本。写文件名则直接保存，不写则弹出「复制或保存」对话框。 | 一次很有价值的排错过程：`/export 排错记录.txt` 存档或发给同事。 |
| `/goal`<br>`[condition\|clear]` | goal<br>目标 | 设定一个完成条件，Claude 会跨多轮持续工作，直到条件满足或目标被清除。不带参数显示当前目标；`clear`、`stop`、`off` 等可提前取消。 | `/goal 所有测试都通过`，然后让它自己一轮轮修，直到全绿。 |
| `/memory` | memory<br>记忆 | 编辑 `CLAUDE.md` 记忆文件，开关「自动记忆」，查看自动记住的条目。 | 想让 Claude 每次都用中文回答：`/memory` 打开 CLAUDE.md，写入「请始终用简体中文回答」。 |
| `/recap` | recap<br>回顾、概括 | 立即生成当前会话的一句话总结。 | 开完会回来忘了做到哪：`/recap`。 |
| `/rename`<br>`[name]` | rename<br>重命名 | 给当前会话改名，并显示在输入栏上方。不写名字则根据对话内容自动生成。 | 同时开着多个会话时：`/rename 量化回测`，之后在 `/resume` 里一眼认出。 |

## 模型与推理

换模型、调思考力度、调速度

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/model`<br>`[model]`<br>★ | model<br>模型 | 切换 AI 模型，并保存为新会话的默认模型。不带参数打开选择器；支持的模型可用左右方向键调思考力度；在某一行按 `s` 只对当前会话生效。 | 简单改文案用较快较省的模型；遇到难 bug 时 `/model opus` 换更强的模型。 |
| `/advisor`<br>`[model\|off]` | advisor<br>顾问 | 开关「顾问工具」：任务关键时刻请第二个模型提供建议。可填 `fable`、`opus`、`sonnet` 或完整模型 ID（`fable` 需要相应权限）。不带参数打开选择器。 | 平时用较快的模型干活，又怕关键决策出错：`/advisor opus`。 |
| `/effort`<br>`[level\|auto\|status\|ultracode [on\|off]]` | effort<br>努力程度（思考力度） | 设置推理力度：`low` 到 `xhigh`、`max` 或 `auto`；`status` 显示当前值。`max` 只对当前会话有效。`ultracode on\|off` 开关 ultracode 模式。 | 排查难以复现的 bug：`/effort high`；只是改错别字：`/effort low`。 |
| `/fast`<br>`[on\|off]` | fast<br>快速 | 开关快速模式（同一个模型，输出更快）。在 Claude 回复中途也能切换，但正在进行的这一轮仍按原速度完成。计费方式请以官方 fast mode 说明为准。 | 赶时间需要大量生成时 `/fast on`，不急时 `/fast off`。 |
| `/output-style`<br>`[style]`<br>需 v2.1.269+ | output style<br>输出风格 | 列出或切换输出风格（回答的写法），例如 `/output-style concise`。 | 先不带参数运行 `/output-style` 看有哪些风格，再选一个适合你的（例如更简洁的）。 |

## 项目与文件

让 Claude 认识你的项目、访问文件夹、查看改动

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/init`<br>★ | initialize<br>初始化 | 读取项目并生成 `CLAUDE.md`「项目说明书」，之后每次新对话都会先读它。如果发现 Codex 或 Gemini CLI 的配置，会提议用 `/import` 迁移。 | 接手新项目时第一件事：`/init`，然后用 `/memory` 补充「请用中文回答」等个人要求。 |
| `/add-dir`<br>`<path>` | add directory<br>添加文件夹 | 本次会话额外允许访问另一个文件夹，当前工作位置不变。输入部分路径会提示补全，按 `Tab` 接受。被添加文件夹里的大部分 `.claude/` 配置不会被读取；多数网络路径不能添加。 | 前端和后端分在两个文件夹：`/add-dir ../backend`，让它同时看两边。 |
| `/cd`<br>`<path>` | change directory<br>切换文件夹 | 把当前会话移到另一个工作文件夹，对话保留。和 `/add-dir` 的区别：`/cd` 是搬家，`/add-dir` 是多开一扇门。 | 在错误的文件夹里开始了对话：`/cd ~/projects/website`，不用重来。 |
| `/diff` | difference<br>差异、改动对比 | 查看工作区的改动，包括 Claude 目前做的修改。 | Claude 说「改好了」后，提交前先 `/diff` 亲眼确认改了什么。 |
| `/import`<br>`[codex\|gemini\|cursor] [--dry-run] [--yes]`<br>⇄ 会大范围修改文件 | import<br>导入 | 把本机 OpenAI Codex、Google Gemini CLI 或 Cursor 的配置（说明文件、MCP 服务器、命令、子代理、技能）导入 Claude Code。`--dry-run` 只预览不写入。部分云平台不可用；从 Cursor 导入需 v2.1.265+。 | 从 Cursor 转过来：先 `/import cursor --dry-run` 看会导入什么，没问题再正式导入。 |
| `/insights` | insights<br>洞察、分析 | 生成一份 HTML 报告，分析你在本机的近期使用：常用项目、使用方式、容易出错的地方、值得尝试的功能。云端会话中不可用。 | 用了一段时间后 `/insights`，发现自己从没用过的好功能。 |
| `/team-onboarding`<br>⚿ 可能包含敏感信息 | team onboarding<br>团队新人入门 | 分析你过去 30 天的会话、命令和 MCP 使用情况，生成一份 Markdown 入门指南，新同事可以直接作为第一条消息粘贴。 | 团队来了新人：`/team-onboarding`，把生成的指南发给 TA。 |

## 审查与验证

找 bug、找安全漏洞、清理代码、实际运行验证

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/code-review`<br>`[low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [--max-findings n\|all\|default] [pr#\|branch\|path]`<br>★ · 技能 · ¥ 可能产生费用 · ↗ 会发送到外部 · ⇄ 会大范围修改文件 | code review<br>代码审查 | 检查当前改动（或指定的 PR、分支、路径）有没有正确性 bug。可选力度；`--fix` 让 Claude 直接修，`--comment` 发到 GitHub PR 或 GitLab MR；`ultra` 在云端做深度审查。<br>同义命令: `/review` | 提交前：`/code-review high --fix`，找出问题并顺手修好。审查别人的 PR：`/code-review high 1234`。 |
| `/run`<br>技能 | run<br>运行 | 启动并操作你的项目应用，看改动的实际效果。 | `/run`，让它启动网站并截图新首页给你看。 |
| `/run-skill-generator`<br>技能 | skill generator<br>技能生成器 | 为本项目写一个专属技能，教会 `/run` 和 `/verify` 如何从干净环境构建、启动和操作你的应用。 | 项目启动步骤复杂（要先起数据库等），跑一次，以后 `/run` 一步到位。 |
| `/security-review` | security review<br>安全审查 | 对比当前分支与远程默认分支的差异，找出安全隐患，如注入、认证问题、数据泄露。需要名为 `origin` 的远程仓库。 | 涉及登录、支付、用户数据的改动上线前跑一次。 |
| `/simplify`<br>`[target]`<br>技能 · ⇄ 会大范围修改文件 | simplify<br>简化 | 4 个审查代理并行检查改动：能否复用现有代码、能否更简单、效率、抽象层级是否合适，并直接改好。不查正确性 bug（那是 `/code-review` 的事）。 | 功能已经能跑，想让代码更好维护：`/simplify`。 |
| `/ultrareview`<br>`[PR or branch]`<br>¥ 可能产生费用 | ultra review<br>超深度审查 | 在云端沙箱里用多个代理深度审查代码。推荐写法是 `/code-review ultra`，`/ultrareview` 是别名。Pro、Max、Ultra 含 3 次免费，之后需要用量额度。 | 重要版本发布前：`/code-review ultra`。 |
| `/verify`<br>技能 | verify<br>验证 | 真正构建并运行你的应用、观察结果，确认改动有效，而不是只看测试或类型检查。只在你手动调用时运行。 | 改了按钮逻辑：`/verify`，让它亲自打开应用点一下。 |

## 并行与后台

同时让多个 Claude 干活，或放到后台运行

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/agents` | agents<br>代理（智能体） | 新版本中只显示一条提示：直接让 Claude 创建或管理子代理，或编辑 `.claude/agents/` 文件夹。v2.1.197 及更早版本会打开管理界面。 | 直接说：「帮我建一个专门写测试的子代理」。 |
| `/background`<br>`[prompt]` | background<br>后台 | 把当前会话转为后台代理继续运行，释放终端。可附带最后一条指令。用 `claude agents` 查看。<br>同义命令: `/bg` | 一个要跑半小时的整理任务：`/bg 完成后把结果写进 report.md`。 |
| `/batch`<br>`<instruction>`<br>技能 · ⇄ 会大范围修改文件 | batch<br>批量 | 大规模并行改代码：先研究代码库，把工作拆成 5～30 个独立单元并给出计划；你批准后，每个单元由一个后台子代理在独立 worktree 中实现、测试并提交。需要 Git 仓库（或相应 hook）。 | `/batch 把 src/ 从 JavaScript 迁移到 TypeScript`。 |
| `/fork`<br>`[prompt]` | fork<br>分叉（复制一份） | 把当前对话复制成一个新的后台会话，这边继续工作。带上指令则副本立即开始。副本一般会先创建自己的 worktree 再改代码。 | 正在做功能 A，想同时修一个小问题：`/fork 修复页脚错位`。 |
| `/list-agents`<br>需 v2.1.224+ | list agents<br>列出代理 | 列出 Claude 可以发消息的子代理、团队成员和其他会话，以及各自的名字。仅在启用跨会话消息时可用。<br>同义命令: `/peers` | 多个会话协作时，确认彼此的名字。 |
| `/stop` | stop<br>停止 | 停止你当前连接的后台会话，记录和 worktree 保留。只想断开不停止，用 `/exit` 或按 `←`。 | 后台任务方向跑偏：`/stop`。 |
| `/subtask`<br>`<task>` | subtask<br>子任务 | 派出一个继承完整对话的后台子代理去做任务，完成后结果回到当前对话。与 `/fork` 的区别：`/subtask` 的结果会汇报回来，`/fork` 是独立的会话。 | `/subtask 为这些接口写 API 文档`，你这边继续写代码。 |
| `/tasks` | tasks<br>任务 | 查看和管理当前会话的后台工作，包括已完成的子代理。<br>同义命令: `/bashes` | 后台跑着测试或子代理时，用 `/tasks` 看进度。 |
| `/workflow-authoring`<br>技能 | workflow authoring<br>编写工作流 | 加载编写动态工作流脚本的参考资料。Claude 一般会自动加载；手动修改已保存脚本前可以自己运行。仅在启用动态工作流时可用。 | 想手动调整一个保存的工作流脚本前。 |
| `/workflows` | workflows<br>工作流 | 打开工作流进度视图，查看、暂停、继续、保存正在运行或已完成的多代理工作流。 | 跑大型研究或改造工作流时，用它盯进度。 |

## 定时与自动化

让它按间隔反复做、按时间表做、自动修 PR

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/loop`<br>`[interval] [prompt]`<br>★ · 技能 | loop<br>循环 | 在会话开着时反复执行一条指令。不写间隔则由 Claude 自己掌握节奏；不写指令则运行内置维护提示或你的 `loop.md`。关闭会话就停止。<br>同义命令: `/proactive` | `/loop 5m 检查部署是否完成`。需要电脑关机也执行的话用 `/schedule`。 |
| `/autofix-pr`<br>`[prompt]`<br>↗ 会发送到外部 | auto-fix PR<br>自动修复 PR | 开一个云端会话盯住当前分支的 PR，CI 失败或有人留评审意见时自动推送修复。需要 `gh` 命令行工具和云端会话权限。 | 只想让它修格式问题：`/autofix-pr 只修 lint 和类型错误`。 |
| `/deep-research`<br>`<question>`<br>工作流 | deep research<br>深度研究 | 多代理工作流：大量搜索网页、抓取并交叉核对来源，写成带引用的报告。在后台运行。 | `/deep-research 主流 AI 视频生成工具的价格与画质对比`。 |
| `/schedule`<br>`[description]` | schedule<br>日程、定时 | 创建、修改、列出或运行云端定时任务（以前叫 routines），通过对话引导设置，也可以问最近的运行记录。使用 Console API 密钥时不可用。<br>同义命令: `/routines` | `/schedule 每个工作日早上 9 点检查仓库新 issue 并总结`。 |

## 网页、幻灯片与设计

产出可以分享的网页、演示文稿、设计稿和图表

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/artifact-capabilities`<br>技能 | artifact capabilities<br>成品页面的高级能力 | 加载 artifact 运行时可用能力的参考，例如调用你的连接器、给访客提供文件下载，以及你的账号有哪些。Claude 一般会自动加载。 | 打算做一个多人填写的报名表页面之前。 |
| `/artifact-diagramming`<br>技能 · 需 v2.1.221+ | artifact diagramming<br>成品页面中的绘图 | 加载在 artifact 中画示意图的规范：何时需要图、画什么、如何写出在浅色和深色主题下都清楚的 SVG。 | 需要一张清楚的系统流程图时。 |
| `/artifacts` | artifacts<br>成品（发布的网页） | 列出你拥有或别人分享给你的 artifact（网页成品），可以接入当前会话、在浏览器打开或复制链接。仅在支持 artifact 的环境可用。 | 找回上周做的那个仪表盘页面，接着修改。 |
| `/dataviz`<br>`[request]`<br>技能 | data visualization<br>数据可视化 | 图表设计指南：为数据选择合适的图表形式、按用途配色，用自带脚本检查色盲友好和对比度。 | `/dataviz 把这份月度销售表做成趋势图`。 |
| `/design`<br>`[brief]`<br>技能 · 需 v2.1.265+ | design<br>设计 | 在一张画布上绘制界面草图、页面流程、落地页或海报（Claude Design artifact），可在桌面浏览器编辑并导出 PNG 或 PDF。Bedrock、Vertex 等第三方平台不可用。 | `/design 手机记账 App 的设置页`。 |
| `/design consent` | consent / revoke<br>同意授权 / 撤销 | 授予或撤销 Claude 对 Claude Design 的访问权限。当 Claude 的回复要求你运行 `/design consent` 时，需要你自己在输入框中输入。<br>同义命令: `/design revoke` | Claude 提示需要授权时，手动输入 `/design consent`。 |
| `/design-login` | design login<br>设计登录 | 为 `/design-sync` 用 claude.ai 账号授权。当 `/design-sync` 或 `/design consent` 提示时使用。 | `/design-sync` 提示需要登录时运行。 |
| `/design-sync`<br>`[hint]`<br>技能 · ↗ 会发送到外部 | design sync<br>设计同步 | 把仓库中的 React 设计系统转换并上传到 Claude Design，让生成的设计使用你真实的组件。首次同步会逐个验证组件，大仓库可能要几个小时。上传目标是独立的 claude.ai/design 网站，该网站将于 2026 年 12 月 14 日前关闭。 | 公司有自己的组件库：`/design-sync Acme DS`。注意上述关闭日期。 |
| `/slides`<br>`[brief]`<br>技能 · 需 v2.1.265+ | slides<br>幻灯片 | 根据你的描述生成一套 Claude Slides 演示文稿（artifact）。需要支持 artifact 的会话和可用的 Slides 模板。 | `/slides 季度业绩回顾，8 页，面向管理层`。 |

## 插件、技能与外部连接

给 Claude 装新能力：插件、技能、MCP 连接器、浏览器、编辑器

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/mcp`<br>`[reconnect (<server>\|all)\|enable\|disable [<server>\|all]]`<br>★ | MCP (Model Context Protocol)<br>模型上下文协议（连接外部工具的标准） | 管理 MCP 服务器连接和 OAuth 登录。不带参数打开列表；`reconnect`、`enable`、`disable` 加服务器名或 `all` 可直接操作。 | 连接器报错或需要登录：`/mcp reconnect all`。 |
| `/chrome` | Chrome<br>Chrome 浏览器 | 配置 Claude in Chrome 的设置。 | 第一次连接 Chrome 扩展时。 |
| `/claude-api`<br>`[subcommand]`<br>技能 | Claude API<br>Claude 编程接口 | 加载与你项目语言对应的 Claude API 和 Managed Agents 资料；代码导入 `anthropic` 时会自动启用。子命令包括 `migrate`、`upgrade`、`cost-optimize`、`build-eval`、`prompt-audit` 等。 | 自己开发 AI 应用、想降低 API 费用：`/claude-api cost-optimize`。 |
| `/claude-in-chrome`<br>`[task]`<br>技能 · ↗ 会发送到外部 | Claude in Chrome<br>在 Chrome 浏览器中使用 Claude | 通过 Claude in Chrome 扩展让 Claude 在你的浏览器里执行任务，如测试页面、填写表单、读取控制台日志。需启用 Chrome 集成（如 `claude --chrome`）。 | `/claude-in-chrome 打开本地网站，测试注册流程并报告错误`。 |
| `/ide` | IDE (integrated development environment)<br>集成开发环境（代码编辑器） | 管理与 VS Code、JetBrains 等编辑器的集成并显示状态。 | 编辑器里看不到 Claude 的改动时，检查是否连上。 |
| `/install-github-app`<br>↗ 会发送到外部 · ⚑ 会改变安全设置 | install GitHub app<br>安装 GitHub 应用 | 为仓库安装 Claude GitHub App，可选设置 GitHub Actions 工作流和密钥。仅适用于 github.com 仓库。 | 希望在 GitHub 的 issue 或 PR 中 @claude 让它干活。 |
| `/install-slack-app` | install Slack app<br>安装 Slack 应用 | 安装 Claude Slack 应用，会打开浏览器完成 OAuth 授权。 | 团队想在 Slack 里直接叫 Claude。 |
| `/plugin`<br>`[subcommand]` | plugin<br>插件 | 管理插件（一包命令、技能、代理、工具）。不带参数打开菜单，或用 `list`、`install`、`enable`、`disable` 直接操作。安装后若提示，需要 `/reload-plugins`。 | `/plugin` 浏览插件市场，装一个适合你工作的插件。 |
| `/plugin-authoring`<br>技能 · 需 v2.1.287+ | plugin authoring<br>编写扩展 | 加载编写「mod」（修改 Claude 界面或行为的小扩展）的参考资料。来自内置插件，可在 `/plugin` 中关闭。 | 想做一个常驻侧边栏的小面板时。 |
| `/reload-plugins`<br>`[--force]` | reload plugins<br>重新加载插件 | 不重启就应用插件改动，并报告加载数量和错误。如果会改变已加载的 MCP 工具（导致提示缓存失效），会警告并跳过，除非加 `--force`。 | 刚装完插件、提示需要重新加载时。 |
| `/reload-skills` | reload skills<br>重新加载技能 | 重新扫描技能和命令文件夹，让会话中新增或修改的技能立即可用，并报告增减数量。 | 刚写好一个自定义技能文件，不重启就想用。 |
| `/skill-doctor`<br>需 v2.1.252+ | skill doctor<br>技能体检 | 显示每个技能占用多少上下文、使用频率如何，帮你找出可以关闭的技能。 | 定期体检，清理长期不用的技能。 |
| `/skills` | skills<br>技能 | 列出可用技能，可按名称、描述、来源筛选；按 `t` 按占用 token 排序；`Space`/`Enter` 切换技能对 Claude 和 `/` 菜单是否可见；`Esc` 保存关闭。 | 技能太多占空间：`/skills` 按 `t` 排序，隐藏用不到的。 |

## 权限与安全

控制 Claude 能做什么、什么要先问你

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/permissions`<br>★ · ⚑ 会改变安全设置 | permissions<br>权限 | 管理工具权限的「允许 / 询问 / 禁止」规则：按范围查看、增删规则、管理工作目录、查看自动模式最近的拦截记录和分类规则。<br>同义命令: `/allowed-tools` | 每次都被问「能否运行 npm test」很烦：在这里把它设为允许。 |
| `/auto-mode-setup`<br>⚑ 会改变安全设置 | auto mode setup<br>自动模式设置 | 根据你的项目和近期会话起草 `autoMode.environment` 条目，审核后保存到用户设置，帮助自动模式更准确地判断。有版本和套餐要求。 | 自动模式总是误拦你常用的操作时。 |
| `/fewer-permission-prompts`<br>技能 · ⚑ 会改变安全设置 | fewer permission prompts<br>减少权限弹窗 | 扫描历史记录中常用的只读 Bash 和 MCP 调用，把它们按优先级加入项目 `.claude/settings.json` 的允许清单。 | 被权限确认打断太多次时跑一次。 |
| `/hooks` | hooks<br>钩子（特定时刻自动运行的脚本） | 查看 hook 配置。 | 怀疑某个 hook 导致每次编辑都报错时，先看看配置了什么。 |
| `/privacy-settings` | privacy settings<br>隐私设置 | 查看和修改隐私设置，仅限 Pro、Max、Ultra 订阅用户。 | 想确认自己的数据使用设置时。 |
| `/sandbox`<br>⚑ 会改变安全设置 | sandbox<br>沙箱（隔离环境） | 开关沙箱模式，仅在支持的平台上可用。 | 要运行来源不太熟悉的脚本时先开启。 |
| `/update-config`<br>`[request]`<br>技能 · ⚑ 会改变安全设置 | update config<br>更新配置 | 用自然语言描述设置改动（允许某命令、设置环境变量、添加 hook），Claude 修改对应的 `settings.json`。主题、模型等用 `/config`。 | `/update-config 每次编辑文件后自动运行 prettier`。 |

## 设置与界面

主题、颜色、状态栏、快捷键、语音输入

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/color`<br>`[color\|default]` | color<br>颜色 | 设置当前会话输入栏的颜色：`red`、`blue`、`green`、`yellow`、`purple`、`orange`、`pink`、`cyan`；`default` 恢复；不带参数随机。 | 操作生产环境的会话设成 `/color red`，时刻提醒自己小心。 |
| `/config`<br>`[key=value ...]` | config<br>配置、设置 | 打开设置界面（主题、模型、输出风格等）。也可直接写 `key=value` 修改，例如 `/config theme=dark`。`/config --help` 列出可用的键。<br>同义命令: `/settings` | `/config theme=dark`，一步切换深色主题。 |
| `/focus` | focus<br>专注视图 | 切换专注视图：只显示你的最后一条提问、一行工具调用摘要和最终回答。仅全屏渲染模式可用。 | 不想看大量中间过程，只看结论。 |
| `/keybindings` | keybindings<br>快捷键 | 打开快捷键配置文件。 | 把常用操作改成你习惯的按键。 |
| `/scroll-speed` | scroll speed<br>滚动速度 | 交互式调整鼠标滚轮速度。仅全屏渲染模式可用，JetBrains 终端中不可用。 | 滚一下跳太多行时调慢。 |
| `/statusline` | status line<br>状态栏 | 配置底部状态栏。用文字描述想显示的内容，或不带参数从你的 shell 提示符自动配置。 | `/statusline 显示当前模型和 git 分支`。 |
| `/terminal-setup` | terminal setup<br>终端设置 | 在 VS Code、Cursor、Devin Desktop、Alacritty、Zed 中安装 Shift+Enter 换行；Apple 终端改为 Option+Enter 并关闭提示音；iTerm2 中开启剪贴板权限让 `/copy` 可用。 | 一按回车就把没写完的需求发出去了？跑一次它。 |
| `/theme` | theme<br>主题配色 | 更换配色主题：`auto` 跟随终端、浅色/深色、色觉友好主题、ANSI 主题和自定义主题。 | 晚上看屏幕累，换深色主题。 |
| `/tui`<br>`[default\|fullscreen]` | TUI (text user interface)<br>终端文字界面 | 设置终端界面渲染方式并保留对话重新启动。`fullscreen` 为不闪烁的全屏模式；不带参数显示当前方式。 | 终端画面闪烁时：`/tui fullscreen`。 |
| `/voice`<br>`[hold\|tap\|off]` | voice<br>语音 | 开关语音输入，或指定模式：`hold` 按住说话、`tap` 点按开始。需要 Claude.ai 账号。 | 打字慢、英文键盘不熟时，直接说中文下指令。 |

## 账号与用量

登录、查额度、看费用、升级套餐

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/usage`<br>★ | usage<br>用量 | 显示本次会话费用、套餐用量上限和活动统计。订阅套餐会显示哪些消耗计入额度。`/stats` 打开统计标签页。<br>同义命令: `/cost`, `/stats` | 担心额度不够时 `/usage` 看一眼，再决定是否换较省的模型。 |
| `/login` | log in<br>登录 | 登录 Anthropic 账号。 | 换电脑或登录过期时。 |
| `/logout` | log out<br>退出登录 | 退出 Anthropic 账号。 | 在共用电脑上用完后。 |
| `/passes` | passes<br>体验券 | 把一周免费 Claude Code 分享给朋友。仅在账号符合条件时显示。 | 推荐朋友试用。 |
| `/rate-limit-options` | rate limit options<br>用量上限的应对选项 | claude.ai 用量上限阻止请求时显示选项：等待重置后自动继续、添加用量额度或升级套餐。需要 claude.ai 订阅。 | 深夜跑任务被限额卡住：选择「重置后自动继续」，第二天醒来已完成。 |
| `/status` | status<br>状态 | 打开设置的「状态」页：版本、模型、账号、连接情况。Claude 回复中也能运行。 | 向别人求助前先截一张 `/status` 的图。 |
| `/upgrade` | upgrade<br>升级 | 在浏览器打开升级套餐的页面。 | 额度经常不够用时。 |
| `/usage-credits`<br>¥ 可能产生费用 | usage credits<br>用量额度 | 达到上限时配置或申请用量额度：打开账单设置页；Team/Enterprise 无账单权限的成员则向管理员发送申请。旧名 `/extra-usage`。 | 团队账号用完额度，向管理员申请。 |

## 云端、远程与其他设备

在桌面 App、手机、网页、云端之间接力

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/desktop` | desktop<br>桌面应用 | 在 Claude Code 桌面 App 中继续当前会话。需要 macOS 或 x64 Windows 及 Claude 订阅。<br>同义命令: `/app` | 终端里聊着想换成有图形界面的 App。 |
| `/mobile` | mobile<br>手机 | 显示下载 Claude 手机 App 的二维码。<br>同义命令: `/ios`, `/android` | 想在手机上查看进度或远程操作。 |
| `/remote-control`<br>↗ 会发送到外部 | remote control<br>远程控制 | 让本会话可以从 claude.ai（网页或手机）远程操作。需要 claude.ai 订阅。<br>同义命令: `/rc` | 电脑上开着任务出门，用手机继续指挥：`/rc`。 |
| `/remote-env` | remote environment<br>云端环境 | 选择从命令行启动云端会话时默认使用的云端环境。 | 有多个云端环境时设一个默认值。 |
| `/setup-bedrock` | set up Bedrock<br>配置 Amazon Bedrock | 通过向导配置 Amazon Bedrock 的认证、区域和模型。设置 `CLAUDE_CODE_USE_BEDROCK=1` 之前不会出现在菜单中，需要完整输入。 | 公司通过 AWS 使用 Claude 时。 |
| `/setup-vertex` | set up Vertex<br>配置 Google Cloud | 通过向导配置 Google Cloud Agent Platform 的认证、项目、区域和模型。设置 `CLAUDE_CODE_USE_VERTEX=1` 之前不会出现在菜单中，需要完整输入。 | 公司通过 Google Cloud 使用 Claude 时。 |
| `/teleport` | teleport<br>瞬间移动 | 把云端会话拉到本地终端：选择后获取分支和对话。需要 claude.ai 订阅。<br>同义命令: `/tp` | 在网页版开始的任务，拉回本地继续。 |
| `/web-setup` | web setup<br>网页版设置 | 用本地 `gh` 命令行的登录信息，为云端会话连接 GitHub 账号。 | 第一次使用云端会话前。 |

## 诊断与反馈

出问题时先看这里

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/doctor`<br>`[prompt-audit [path]]`<br>★ · 技能 | doctor<br>医生（体检） | 体检：诊断安装、设置、扩展和 `CLAUDE.md` 的问题并提出修复方案，你确认后 Claude 才会修改。`prompt-audit` 改为审查你的说明文件。<br>同义命令: `/checkup` | Claude Code 出现莫名其妙的问题时，第一步 `/doctor`。 |
| `/help`<br>★ | help<br>帮助 | 显示帮助和可用命令。 | 忘了命令名时先打 `/help`，或打 `/` 加几个字母筛选。 |
| `/powerup`<br>★ | power up<br>能力提升 | 通过带动画演示的互动小课程学习 Claude Code 的功能。 | 新手系统学习的最佳入口。 |
| `/bug`<br>`[report]`<br>↗ 会发送到外部 · ⚿ 可能包含敏感信息 | bug<br>程序缺陷 | 报告 bug 或分享对话。你可以选择附带多少会话记录，并在同意页面确认后才会发送。<br>同义命令: `/share` | 遇到明显是 Claude Code 本身的故障时。 |
| `/debug`<br>`[description]`<br>技能 | debug<br>调试 | 为当前会话开启调试日志，并通过阅读日志排查问题。从运行时刻开始记录；可附上问题描述。 | `/debug MCP 服务器一直连不上`。 |
| `/exit` | exit<br>退出 | 退出命令行。在已连接的后台会话中，它只是断开，会话继续运行。<br>同义命令: `/quit` | 今天收工。 |
| `/feedback`<br>`[report]`<br>↗ 会发送到外部 · ⚿ 可能包含敏感信息 | feedback<br>反馈 | 发送产品反馈，使用与 `/bug` 相同的对话框和同意步骤。 | 想要某个新功能时告诉官方。 |
| `/heapdump`<br>⚿ 可能包含敏感信息 | heap dump<br>内存快照 | 把 JavaScript 内存快照和内存明细写到桌面，用于排查内存占用过高。报告问题时只附 `-diagnostics.json`；`.heapsnapshot` 含完整对话和凭据，不要分享。菜单中隐藏，需完整输入。 | Claude Code 占用好几 GB 内存时，用于向官方报告。 |
| `/release-notes` | release notes<br>版本更新说明 | 在版本选择器中查看更新日志。内容显示在记录里，但不会进入 Claude 的上下文。 | 升级后看看有什么新功能。 |
| `/restart`<br>需 v2.1.288+ | restart<br>重启 | 重启 Claude Code 并恢复当前会话，以应用已安装的更新。需要 Pro、Max 或 Ultra，以及 macOS/Linux 的原生安装（不支持 WSL）。<br>同义命令: `/update` | 底部提示更新已安装时运行。 |

## 其他

与日常工作无关的小功能

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/radio` | radio<br>电台 | 在浏览器打开 Claude FM 低保真音乐电台；无浏览器时打印音频流地址。 | 写代码时来点背景音乐。 |
| `/stickers` | stickers<br>贴纸 | 订购 Claude Code 贴纸。 | 装饰笔记本电脑。 |

## 已移除

旧教程里可能还有，但新版本已经不能用

| 命令 | 英文原意 | 说明 | 最佳用法 |
|---|---|---|---|
| `/pr-comments`<br>`[PR]`<br>v2.1.91 移除 | PR comments<br>PR 评论 | v2.1.91 起移除。直接对 Claude 说「查看这个 PR 的评论」即可。 | 直接用中文请求。 |
| `/ultraplan`<br>`<prompt>` | ultra plan<br>超级计划 | 已移除。请改用计划模式 `/plan`。 | 改用 `/plan`。 |
| `/vim`<br>v2.1.92 移除 | Vim<br>Vim（一种键盘编辑方式） | v2.1.92 起移除。切换 Vim/普通编辑模式请用 `/config` → Editor mode。 | 改用 `/config`。 |

## 免责声明

1. **非官方项目**: 本项目由社区制作，与 Anthropic 无关联，也未获其赞助或认可。「Claude」「Claude Code」及相关标识是 Anthropic 的商标，此处仅用于说明所介绍的产品。
2. **内容可能过时或有误**: 所有说明均为对官方文档的意译和简化，按「现状」提供，不作任何明示或默示的保证。Claude Code 更新频繁，命令可能新增、改名或移除。如与官方文档不一致，以官方文档为准。
3. **使用风险由你自行承担**: 部分命令会修改或还原文件、执行命令、推送代码、把数据发送到外部服务，或消耗付费额度。运行前请确认你理解它会做什么；先用 Git 提交或备份；不要在未经审查的情况下对生产环境、重要数据或他人的仓库使用。
4. **保护密钥和隐私**: 不要把 API 密钥、密码、令牌或他人的个人信息写进提示词。导出的对话、问题报告、内存快照等文件可能包含这些内容，分享前务必检查。
5. **示例仅供参考**: 「最佳用法」中的例子用于说明用途，不是针对你的环境的操作指令。命令是否可用取决于版本、套餐、平台和组织策略。
6. **本页面不追踪你**: 本页面不使用 Cookie、统计分析或第三方脚本、字体，只在你的浏览器本地保存语言偏好。
7. **责任限制**: 在法律允许的最大范围内，作者和贡献者不对因使用本项目内容而导致的任何损失负责，包括数据丢失、费用、安全事件或服务中断。

## 关于本项目

- **来源**：依据官方[命令文档](https://code.claude.com/docs/en/commands)意译整理，核对日期 2026-11-03。说明经过简化，不是官方翻译；如有出入，以官方文档为准。
- **数据**：所有内容由 [`data/commands.json`](data/commands.json) 生成。修改 JSON 后运行 `python3 scripts/build.py`。
- **参与贡献**：见 [CONTRIBUTING.md](CONTRIBUTING.md)。
- **许可**：内容 [CC BY 4.0](LICENSE-CONTENT)，代码 [MIT](LICENSE)。
