# Claude Code Commands

[English](README.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-Hant.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md)

![Unofficial](https://img.shields.io/badge/Anthropic-unofficial-lightgrey) [![check](https://github.com/FuturEvoLab/claude-code-commands-i18n/actions/workflows/check.yml/badge.svg)](https://github.com/FuturEvoLab/claude-code-commands-i18n/actions/workflows/check.yml) [![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-blue)](LICENSE-CONTENT) [![Code: MIT](https://img.shields.io/badge/code-MIT-green)](LICENSE) ![Commands](https://img.shields.io/badge/commands-115-teal)

> An unofficial, plain-language reference to every Claude Code slash command, in **7 languages: English, Japanese, Simplified Chinese, Traditional Chinese, Korean, Russian and Spanish**. It is written for people who find the official English docs hard to read: each command gets a short explanation and a realistic example of when to use it.

## Live preview

One static page you can try right away: search, switch language and theme, copy commands. Nothing to install.

### [Searchable web version →](https://commands.futurevolab.com/)

| Default theme | Matrix theme |
|---|---|
| [![Default theme](docs/assets/preview-en.png)](https://commands.futurevolab.com/?theme=terminal) | [![Matrix theme](docs/assets/preview-matrix.png)](https://commands.futurevolab.com/?theme=matrix) |

<p><img src="docs/assets/preview-search.png" alt="search" width="68%"> <img src="docs/assets/preview-mobile.png" alt="mobile" width="28%"></p>

## How to read the syntax

- Type `/` in the prompt to open the command menu; keep typing to filter.
- `[ ]` = optional, `< >` = required, `|` = one of.
- **Skill** = a bundled prompt handed to Claude. **Workflow** = runs several agents in the background.
- Many commands depend on version, plan, platform or an enabled feature. The menu you see is authoritative; check your version with `/status`.

## ★ Start here

The editor's picks for a first week with Claude Code.

- `/clear` · Start a fresh conversation (the old one stays resumable)
- `/compact` · Summarize a long conversation to free space
- `/context` · See what is filling the context window
- `/plan` · Get a plan first; edits wait for your approval
- `/resume` · Go back to an earlier conversation
- `/rewind` · Undo: roll code and conversation back
- `/model` · Switch models
- `/init` · Create the project's CLAUDE.md
- `/code-review` · Check for bugs before committing, optionally fix them
- `/loop` · Repeat a prompt on an interval
- `/mcp` · Manage external tool connections
- `/permissions` · Decide what Claude may do without asking
- `/usage` · Check cost and plan limits
- `/doctor` · Run a checkup when something is wrong
- `/help` · Show help and all commands
- `/powerup` · Learn features through interactive lessons

## Find a command by what you want to do

Pick the situation; the commands are listed in the order to try them.

- **Claude broke something and I want to undo it** → `/rewind` · `/diff`
- **Start an unrelated task from scratch** → `/clear` · `/resume`
- **The conversation is long and Claude is slow or forgetful** → `/context` · `/compact` · `/autocompact`
- **Continue yesterday's unfinished work** → `/resume` · `/rename` · `/recap`
- **See a plan before a big change** → `/plan` · `/effort` · `/model`
- **Make Claude always answer in my language** → `/init` · `/memory`
- **Spend less money and usage** → `/usage` · `/model` · `/effort` · `/context`
- **Check work before committing or shipping** → `/diff` · `/code-review` · `/security-review` · `/verify`
- **Do several things at once or run in the background** → `/fork` · `/subtask` · `/background` · `/tasks` · `/batch`
- **Repeat a task or run it on a schedule** → `/loop` · `/schedule` · `/goal`
- **Too many permission prompts** → `/permissions` · `/fewer-permission-prompts`
- **Connect tools or add new abilities** → `/mcp` · `/plugin` · `/skills`
- **Make slides, designs or charts** → `/slides` · `/design` · `/dataviz` · `/artifacts`
- **Leave the computer and continue on my phone** → `/remote-control` · `/mobile` · `/desktop`
- **Claude Code itself is misbehaving** → `/doctor` · `/status` · `/debug` · `/bug`
- **Learn Claude Code properly** → `/powerup` · `/help` · `/insights`

## Safety labels

Commands marked with these labels need extra care.

- **¥ May cost money**: Can consume paid usage or incur extra charges. Check `/usage` and the official pricing first.
- **↗ Sends data out**: Sends conversation, code or comments to another service (Anthropic, GitHub, cloud sessions, sites in your browser) or pushes to a remote. Check what goes where first.
- **⚿ May expose secrets**: Output (files, clipboard, reports) can contain conversation text, keys, passwords or personal data. Review and redact before sharing.
- **⇄ Broad file changes**: Can change or revert many files at once. Commit or back up first, and review with `/diff` afterwards.
- **⚑ Changes safety settings**: Changes what Claude may do without asking, or other safety settings. Only allow actions you understand and trust.

## Contents

- [Conversation & context](#conversation--context) (15)
- [Model & reasoning](#model--reasoning) (5)
- [Project & files](#project--files) (7)
- [Review & verification](#review--verification) (7)
- [Parallel & background work](#parallel--background-work) (10)
- [Automation & scheduling](#automation--scheduling) (4)
- [Artifacts, slides & design](#artifacts-slides--design) (9)
- [Plugins, skills & integrations](#plugins-skills--integrations) (13)
- [Permissions & safety](#permissions--safety) (7)
- [Settings & interface](#settings--interface) (10)
- [Account & usage](#account--usage) (8)
- [Cloud, remote & other devices](#cloud-remote--other-devices) (8)
- [Diagnostics & feedback](#diagnostics--feedback) (10)
- [Other](#other) (2)
- [Removed](#removed) (3)

## Conversation & context

Start, compact, rewind and resume conversations; manage the context window

| Command | What it does | Best use |
|---|---|---|
| `/clear`<br>`[name]`<br>★ | Starts a new conversation with empty context while keeping project memory. The previous conversation is kept and can be reopened with `/resume`; pass a name to label it in the picker.<br>Aliases: `/reset`, `/new` | When you finish one feature and move to an unrelated task: `/clear login-feature`. Old context stops interfering and usage drops. |
| `/compact`<br>`[instructions]`<br>★ | Summarizes the conversation so far to free context space, continuing the same conversation. Optional instructions steer what the summary keeps. | After a long session: `/compact keep the database schema and the list of open bugs`. |
| `/context`<br>`[all]`<br>★ | Shows context usage as a colored grid with optimization suggestions and capacity warnings. `all` expands the per-item breakdown. | When Claude seems forgetful or usage climbs fast, run `/context` to see whether large files or tool output are filling the window. |
| `/plan`<br>`[description]`<br>★ | Enters plan mode, where Claude researches and proposes a plan before editing. Pass a description to start on that task immediately. | Before a big change: `/plan fix the auth bug`, review, then approve. |
| `/resume`<br>`[session]`<br>★ | Resumes a conversation by ID or name, or opens the session picker. Background sessions are marked `bg`.<br>Aliases: `/continue` | You closed the laptop mid-task yesterday: `/resume` and pick yesterday's conversation. |
| `/rewind`<br>★ · ⇄ Broad file changes | Rolls the conversation and/or code back to an earlier checkpoint, or summarizes from a selected message.<br>Aliases: `/checkpoint`, `/undo` | Claude broke several files: run `/rewind`, pick the message before the edits, and restore both code and conversation. |
| `/autocompact`<br>`[auto\|<tokens>]`<br>Requires v2.1.221+ | Sets how full the context window gets before automatic compaction, e.g. `500k`; `auto` restores the model-tuned default. Saved to user settings and applied immediately. | Long task interrupted by frequent compaction: `/autocompact 500k`. |
| `/branch`<br>`[name]` | Creates a branch of the conversation at this point and switches into it; the original is preserved and reachable via `/resume`. (A conversation branch, not a Git branch.) | Unsure between two approaches: `/branch try-plan-b`; if it fails, go back and continue plan A. |
| `/btw`<br>`[question]` | Asks a side question about the current session without adding it to the conversation. Without a question, shows your most recent side question. | Mid-task you want to understand an error: `/btw what does this 404 mean` without derailing the main thread. |
| `/copy`<br>`[N]` | Copies the last response to the clipboard; `/copy 2` copies the second-to-last. With code blocks, a picker lets you copy one block; press `w` to write to a file instead (useful over SSH). | Claude drafted a snippet or command: `/copy` and paste it wherever you need it. |
| `/export`<br>`[filename]`<br>⚿ May expose secrets | Exports the conversation as plain text, directly to a file if you give a name, otherwise via a copy/save dialog. | Archive a valuable debugging session: `/export debugging-notes.txt`. |
| `/goal`<br>`[condition\|clear]` | Sets a goal: Claude keeps working across turns until the condition is met or the goal clears. No argument shows the current goal; `clear` (or `stop`, `off`, …) removes it. | `/goal all tests pass`, then let it iterate until the suite is green. |
| `/memory` | Edits `CLAUDE.md` memory files, toggles auto memory, and shows auto memory entries. | Want every answer in your language: open `/memory` and add a line such as “Always reply in Japanese.” |
| `/recap` | Generates a one-line summary of the current session on demand. | Back from a meeting and lost track: `/recap`. |
| `/rename`<br>`[name]` | Renames the session and shows the name on the prompt bar; without a name, generates one from the conversation. | With many sessions open: `/rename backtest` so it stands out in `/resume`. |

## Model & reasoning

Switch models, reasoning effort and speed

| Command | What it does | Best use |
|---|---|---|
| `/model`<br>`[model]`<br>★ | Switches the model and saves it as the default for new sessions. No argument opens a picker; left/right adjusts effort on supported models; press `s` on a row to switch for this session only. | Use a faster model for small edits; switch with `/model opus` when a bug gets hard. |
| `/advisor`<br>`[model\|off]` | Enables or disables the advisor tool, which consults a second model at key moments. Accepts `fable`, `opus`, `sonnet` or a full model ID (`fable` requires access). No argument opens a picker. | Work on a faster model but get a stronger second opinion at key decisions: `/advisor opus`. |
| `/effort`<br>`[level\|auto\|status\|ultracode [on\|off]]` | Sets the effort level: `low` to `xhigh`, `max`, or `auto`; `status` prints it. `max` is session-only. `ultracode on\|off` toggles ultracode. | Hunting a flaky bug: `/effort high`; fixing a typo: `/effort low`. |
| `/fast`<br>`[on\|off]` | Toggles fast mode (same model, faster output). It can be toggled mid-response; the running turn finishes at its original speed. See the official fast mode docs for pricing. | Under time pressure: `/fast on`; otherwise `/fast off`. |
| `/output-style`<br>`[style]`<br>Requires v2.1.269+ | Lists output styles or switches to one, e.g. `/output-style concise`. | Run `/output-style` with no argument to see what is available, then pick one (for example a more concise style). |

## Project & files

Set up project memory, add directories, review changes

| Command | What it does | Best use |
|---|---|---|
| `/init`<br>★ | Initializes the project with a `CLAUDE.md` guide that every new session reads. Offers `/import` if it finds Codex or Gemini CLI configuration. | First thing in a new repo: `/init`, then refine it with `/memory`. |
| `/add-dir`<br>`<path>` | Adds a working directory for file access this session without moving. Partial paths autocomplete with `Tab`. Most `.claude/` config in the added directory isn't discovered, and most network paths can't be added. | Frontend and backend live side by side: `/add-dir ../backend`. |
| `/cd`<br>`<path>` | Moves the session to a new working directory, keeping the conversation. Unlike `/add-dir`, `/cd` changes where the session lives. | Started in the wrong folder: `/cd ~/projects/website` instead of starting over. |
| `/diff` | Reviews changes in your working tree, including Claude's edits so far. | Before committing, `/diff` to see exactly what changed. |
| `/import`<br>`[codex\|gemini\|cursor] [--dry-run] [--yes]`<br>⇄ Broad file changes | Imports instruction files, MCP servers, commands, subagents and skills from OpenAI Codex, Gemini CLI or Cursor. `--dry-run` previews. Unavailable on some cloud providers; Cursor import requires v2.1.265+. | Moving from Cursor: `/import cursor --dry-run` first, then import for real. |
| `/insights` | Generates an HTML report of your recent sessions on this machine: projects, habits, where things go wrong, features to try. Not available in cloud sessions. | After a few weeks, run `/insights` to discover features you never tried. |
| `/team-onboarding`<br>⚿ May expose secrets | Analyzes your last 30 days of sessions, commands and MCP usage and writes a Markdown guide a teammate can paste as their first message. | A new teammate joins: run `/team-onboarding` and send them the guide. |

## Review & verification

Find bugs and vulnerabilities, clean up code, run the app to verify

| Command | What it does | Best use |
|---|---|---|
| `/code-review`<br>`[low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [--max-findings n\|all\|default] [pr#\|branch\|path]`<br>★ · Skill · ¥ May cost money · ↗ Sends data out · ⇄ Broad file changes | Reviews the current diff, or a PR, branch or path, for correctness bugs. `--fix` applies findings, `--comment` posts to the GitHub PR or GitLab MR, `ultra` runs a deep cloud review.<br>Aliases: `/review` | Before committing: `/code-review high --fix`. For a PR: `/code-review high 1234`. |
| `/run`<br>Skill | Launches and drives your project's app to see a change working. | `/run` to start the site and screenshot the new homepage. |
| `/run-skill-generator`<br>Skill | Writes a per-project skill that teaches `/run` and `/verify` how to build, launch and drive your app from a clean environment. | Startup needs several steps (database first, etc.): run this once, then `/run` just works. |
| `/security-review` | Analyzes your branch's diff against origin's default branch for vulnerabilities such as injection, auth issues and data exposure. Needs an `origin` remote. | Before shipping anything touching auth, payments or user data. |
| `/simplify`<br>`[target]`<br>Skill · ⇄ Broad file changes | Four parallel agents review changed code for reuse, simplification, efficiency and abstraction level, then apply fixes. It does not look for correctness bugs; use `/code-review` for that. | The feature works and you want cleaner code: `/simplify`. |
| `/ultrareview`<br>`[PR or branch]`<br>¥ May cost money | Deep multi-agent review in a cloud sandbox. The preferred form is `/code-review ultra`; `/ultrareview` is an alias. Includes 3 free runs on Pro, Max and Ultra, then requires usage credits. | Before a major release: `/code-review ultra`. |
| `/verify`<br>Skill | Builds, runs and observes your app to confirm a change works, rather than relying on tests or type checks. Runs only when you invoke it. | Changed a button's behavior: `/verify` so it actually clicks it. |

## Parallel & background work

Run several agents at once or detach work to the background

| Command | What it does | Best use |
|---|---|---|
| `/agents` | Prints a reminder to ask Claude to create or manage subagents, or to edit `.claude/agents/` directly. On v2.1.197 and earlier, opened an interactive manager. | Just ask: “Create a subagent that only writes tests.” |
| `/background`<br>`[prompt]` | Detaches the session to run as a background agent and frees the terminal. Optionally sends one more instruction first. Monitor with `claude agents`.<br>Aliases: `/bg` | A 30-minute job: `/bg write the results to report.md when done`. |
| `/batch`<br>`<instruction>`<br>Skill · ⇄ Broad file changes | Orchestrates large changes in parallel: researches the codebase, decomposes the work into 5–30 independent units and presents a plan; after approval, one background subagent per unit implements and tests it in its own worktree. Requires a git repository or a WorktreeCreate hook. | `/batch migrate src/ from JavaScript to TypeScript`. |
| `/fork`<br>`[prompt]` | Copies the conversation into a new background session while you keep working here. With a prompt, the copy starts immediately; it is normally told to create its own worktree first. | Working on feature A and want a side fix in parallel: `/fork fix the footer alignment`. |
| `/list-agents`<br>Requires v2.1.224+ | Lists subagents, teammates and other sessions Claude can message, with the name to use for each. Only where cross-session messaging is enabled.<br>Aliases: `/peers` | Coordinating several sessions: check what each is called. |
| `/stop` | Stops the background session you're attached to; transcript and worktree are kept. To detach without stopping, use `/exit` or press `←`. | A background job went off course: `/stop`. |
| `/subtask`<br>`<task>` | Spawns a forked subagent that inherits the conversation and reports its result back here. The difference from `/fork`: `/subtask` reports back here, while `/fork` starts a separate session. | `/subtask document these API endpoints` while you keep coding. |
| `/tasks` | Views and manages background work in this session, including finished subagents.<br>Aliases: `/bashes` | Check progress on background tests or subagents with `/tasks`. |
| `/workflow-authoring`<br>Skill | Loads the reference for writing dynamic workflow scripts. Claude normally loads it itself; run it before hand-editing a saved script. Only where dynamic workflows are enabled. | Before hand-editing a saved workflow script. |
| `/workflows` | Opens the workflow progress view to watch, pause, resume or save running and completed workflows. | Keep an eye on a long-running workflow. |

## Automation & scheduling

Repeat on an interval, run on a schedule, auto-fix pull requests

| Command | What it does | Best use |
|---|---|---|
| `/loop`<br>`[interval] [prompt]`<br>★ · Skill | Runs a prompt repeatedly while the session stays open. Omit the interval and Claude self-paces; omit the prompt and it runs the built-in maintenance prompt or your `loop.md`.<br>Aliases: `/proactive` | `/loop 5m check if the deploy finished`. For runs that continue when your computer is off, use `/schedule`. |
| `/autofix-pr`<br>`[prompt]`<br>↗ Sends data out | Spawns a cloud session that watches the current branch's PR and pushes fixes on CI failures or review comments. Requires the `gh` CLI and cloud sessions. | `/autofix-pr only fix lint and type errors`. |
| `/deep-research`<br>`<question>`<br>Workflow | A bundled workflow that fans out web searches, fetches and cross-checks sources, and writes a cited report. Runs in the background. | `/deep-research compare pricing and quality of leading AI video tools`. |
| `/schedule`<br>`[description]` | Creates, updates, lists or runs cloud scheduled tasks (formerly routines) through a guided conversation. Not available with a Console API key.<br>Aliases: `/routines` | `/schedule every weekday at 9am, summarize new issues in the repo`. |

## Artifacts, slides & design

Produce shareable pages, decks, designs and charts

| Command | What it does | Best use |
|---|---|---|
| `/artifact-capabilities`<br>Skill | Loads the reference for artifact runtime capabilities, such as calling connectors or offering downloads, and which your account has. Claude usually loads it itself. | Before building a page that many people fill in. |
| `/artifact-diagramming`<br>Skill · Requires v2.1.221+ | Loads diagramming guidance for artifacts: when a diagram helps, what to draw, and SVG that stays legible in light and dark themes. | When you need a clear architecture diagram. |
| `/artifacts` | Lists artifacts you own or that are shared with you, then attaches one, opens it, or copies its link. Where artifacts are available. | Find last week's dashboard and keep editing it. |
| `/dataviz`<br>`[request]`<br>Skill | Chart design guidance: picks the chart form, assigns color by role, and validates the palette for colorblind safety and contrast with a bundled script. | `/dataviz turn this monthly sales table into a trend chart`. |
| `/design`<br>`[brief]`<br>Skill · Requires v2.1.265+ | Drafts UI mockups, flows, landing pages or posters as artboards on one canvas (a Claude Design artifact); edit in a desktop browser and export PNG or PDF. Unavailable on Bedrock, Vertex and other third-party platforms. | `/design a settings screen for a mobile banking app`. |
| `/design consent` | Grants or withdraws Claude's access to Claude Design. When Claude asks you to run `/design consent`, type it yourself.<br>Aliases: `/design revoke` | When prompted, type `/design consent` yourself. |
| `/design-login` | Authorizes design-system access for `/design-sync` with your claude.ai account, when `/design-sync` or `/design consent` asks you to. | Run it when `/design-sync` asks you to sign in. |
| `/design-sync`<br>`[hint]`<br>Skill · ↗ Sends data out | Converts and uploads your repo's React design system to Claude Design so designs use your real components. First sync can take hours on large repos. It targets the standalone claude.ai/design site, which closes by December 14, 2026. | `/design-sync Acme DS` (mind the closing date above). |
| `/slides`<br>`[brief]`<br>Skill · Requires v2.1.265+ | Makes a Claude Slides artifact from your brief. Requires a session with artifacts and an account where the Slides template is available. | `/slides a quarterly review for leadership, 8 slides`. |

## Plugins, skills & integrations

Extend Claude with plugins, skills, MCP servers, browser and IDE integrations

| Command | What it does | Best use |
|---|---|---|
| `/mcp`<br>`[reconnect (<server>\|all)\|enable\|disable [<server>\|all]]`<br>★ | Manages MCP server connections and OAuth. No argument opens the list; `reconnect`, `enable` or `disable` with a server name or `all` acts directly. | A connector failed or needs auth: `/mcp reconnect all`. |
| `/chrome` | Configures Claude in Chrome settings. | When first connecting the Chrome extension. |
| `/claude-api`<br>`[subcommand]`<br>Skill | Loads Claude API and Managed Agents reference for your project's language; activates automatically when code imports `anthropic`. Subcommands include `migrate`, `upgrade`, `api-version`, `cost-optimize`, `latency-optimize`, `build-eval`, `prompt-audit`, `managed-agents-onboard`, `managed-agents-secure`, `hillclimb`, `preserved-thinking-migration`. | Cut API spend in your app: `/claude-api cost-optimize`. |
| `/claude-in-chrome`<br>`[task]`<br>Skill · ↗ Sends data out | Has Claude carry out a task in your browser through Claude in Chrome, such as testing a page or reading console logs. Requires Chrome integration (e.g. `claude --chrome`). | `/claude-in-chrome test the sign-up flow on my local site and report errors`. |
| `/ide` | Manages IDE integrations and shows status. | Check the connection when edits don't show in your editor. |
| `/install-github-app`<br>↗ Sends data out · ⚑ Changes safety settings | Installs the Claude GitHub App for a repository, optionally setting up GitHub Actions workflows and secrets. github.com only. | To mention Claude in issues and PRs and have it work there. |
| `/install-slack-app` | Installs the Claude Slack app via a browser OAuth flow. | Your team wants Claude in Slack. |
| `/plugin`<br>`[subcommand]` | Manages plugins. No argument opens the menu; `list`, `install`, `enable`, `disable` act directly. Run `/reload-plugins` if the install summary says so. | Browse with `/plugin` and install one that fits your work. |
| `/plugin-authoring`<br>Skill · Requires v2.1.287+ | Loads the reference for writing a mod. A skill from a built-in plugin, which you can turn off in `/plugin`. | When you want a small side panel that stays beside the chat. |
| `/reload-plugins`<br>`[--force]` | Reloads active plugins without restarting and reports load errors. If the reload would change loaded MCP tools and invalidate the prompt cache, it warns and skips unless you pass `--force`. | Right after installing a plugin that asks for it. |
| `/reload-skills` | Re-scans skill and command directories so skills added or changed during the session are available without restarting. | You just wrote a custom skill and want it now. |
| `/skill-doctor`<br>Requires v2.1.252+ | Shows each skill's context cost and usage so you can find skills to turn off. | Run periodically to prune unused skills. |
| `/skills` | Lists skills with filtering. `t` sorts by token count, `Space`/`Enter` cycles a skill's visibility to Claude and the `/` menu, `Esc` saves and closes. | Too many skills: `/skills`, press `t`, hide the heavy unused ones. |

## Permissions & safety

Control what Claude may do and what needs your approval

| Command | What it does | Best use |
|---|---|---|
| `/permissions`<br>★ · ⚑ Changes safety settings | Manages allow, ask and deny rules for tools: view by scope, add or remove rules, manage working directories, and check the Recently blocked tab (calls auto mode refused) and classifier rules.<br>Aliases: `/allowed-tools` | Tired of approving `npm test` every time: allow it here. |
| `/auto-mode-setup`<br>⚑ Changes safety settings | Drafts `autoMode.environment` entries from your project and recent sessions for you to review and save. Has version and plan requirements. | When auto mode keeps blocking routine actions. |
| `/fewer-permission-prompts`<br>Skill · ⚑ Changes safety settings | Scans transcripts for common read-only Bash and MCP calls and adds a prioritized allowlist to project `.claude/settings.json`. | Run once when approval prompts keep interrupting you. |
| `/hooks` | Views hook configurations. | Check what's configured when a hook seems to break every edit. |
| `/privacy-settings` | Views and updates privacy settings. Pro, Max and Ultra only. | To check how your data is used. |
| `/sandbox`<br>⚑ Changes safety settings | Toggles sandbox mode, on supported platforms only. | Turn it on before running unfamiliar scripts. |
| `/update-config`<br>`[request]`<br>Skill · ⚑ Changes safety settings | Describe a settings change (allow a command, set an env var, add a hook) and Claude edits the matching `settings.json`. Use `/config` for theme and model. | `/update-config run prettier after every file edit`. |

## Settings & interface

Theme, colors, status line, keybindings, voice

| Command | What it does | Best use |
|---|---|---|
| `/color`<br>`[color\|default]` | Sets the prompt bar color for this session: `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink` or `cyan`; `default` resets, no argument picks a random color. | Mark a production session with `/color red`. |
| `/config`<br>`[key=value ...]` | Opens Settings for theme, model, output style and more, or sets `key=value` pairs directly, e.g. `/config theme=dark`. `/config --help` lists keys.<br>Aliases: `/settings` | `/config theme=dark`. |
| `/focus` | Toggles a view showing only your last prompt, a one-line tool summary and the final response. Fullscreen rendering only. | Hide intermediate steps and see only the result. |
| `/keybindings` | Opens your keyboard shortcuts file. | Rebind actions to keys you're used to. |
| `/scroll-speed` | Adjusts mouse wheel scroll speed. Fullscreen rendering only; not in the JetBrains terminal. | Slow it down when one notch jumps too far. |
| `/statusline` | Configures the status line; describe what you want, or run without arguments to derive it from your shell prompt. | `/statusline show the model and git branch`. |
| `/terminal-setup` | Installs Shift+Enter for newlines in VS Code, Cursor, Devin Desktop, Alacritty or Zed; in Apple Terminal enables Option+Enter and disables the bell; in iTerm2 enables clipboard access for `/copy`. | Enter keeps sending half-written prompts: run this once. |
| `/theme` | Changes the color theme: `auto`, light and dark, colorblind-accessible, ANSI and custom themes. | Switch to a dark theme at night. |
| `/tui`<br>`[default\|fullscreen]` | Sets the terminal renderer and relaunches with the conversation intact. `fullscreen` is the flicker-free renderer. No argument shows the current renderer. | Screen flickers: `/tui fullscreen`. |
| `/voice`<br>`[hold\|tap\|off]` | Toggles voice dictation or sets a mode (`hold`, `tap`). Requires a Claude.ai account. | Dictate instructions instead of typing. |

## Account & usage

Sign in, check limits and cost, upgrade

| Command | What it does | Best use |
|---|---|---|
| `/usage`<br>★ | Shows session cost, spend for today, this week and this month, plan usage limits and activity stats, including what counts against plan limits on subscriptions. `/stats` opens the Stats tab. Each warning names its cause and a one-line fix; press `f` to apply the fixes.<br>Aliases: `/cost`, `/stats` | Check `/usage` before deciding whether to switch to a cheaper model. |
| `/login` | Signs in to your Anthropic account. | New machine or expired session. |
| `/logout` | Signs out of your Anthropic account. | After using a shared computer. |
| `/passes` | Shares a free week of Claude Code with friends; only shown to eligible accounts. | Invite a friend to try it. |
| `/rate-limit-options` | Shows ways to keep working when a claude.ai limit blocks you: wait and auto-continue, add usage credits, or upgrade. Requires a claude.ai subscription. | Blocked overnight: choose auto-continue after reset. |
| `/status` | Opens Settings on the Status tab: version, model, account, connectivity. Works while Claude is responding. | Screenshot `/status` before asking for help. |
| `/upgrade` | Opens the upgrade page in your browser. | When you keep hitting limits. |
| `/usage-credits`<br>¥ May cost money | Configures or requests usage credits; Team and Enterprise members without billing access send a request to their admin. Previously `/extra-usage`. | Request credits from your admin when the team runs out. |

## Cloud, remote & other devices

Hand work between desktop, mobile, web and cloud

| Command | What it does | Best use |
|---|---|---|
| `/desktop` | Continues the session in the Claude Code Desktop app. Requires macOS or x64 Windows and a Claude subscription.<br>Aliases: `/app` | Move from the terminal to the desktop app. |
| `/mobile` | Shows a QR code to download the Claude mobile app.<br>Aliases: `/ios`, `/android` | To follow along from your phone. |
| `/remote-control`<br>↗ Sends data out | Makes this session available for Remote Control from claude.ai. Requires a claude.ai subscription.<br>Aliases: `/rc` | Leave the task running and steer it from your phone: `/rc`. |
| `/remote-env` | Chooses the default cloud environment for cloud sessions started from the CLI. | Pick a default when you have several environments. |
| `/setup-bedrock` | Configures Amazon Bedrock auth, region and model pins via a wizard. Hidden from the menu until `CLAUDE_CODE_USE_BEDROCK=1` is set; type it in full. | Your company uses Claude through AWS. |
| `/setup-vertex` | Configures Google Cloud's Agent Platform via a wizard. Hidden until `CLAUDE_CODE_USE_VERTEX=1` is set; type it in full. | Your company uses Claude through Google Cloud. |
| `/teleport` | Pulls a cloud session into this terminal, fetching its branch and conversation. Requires a claude.ai subscription.<br>Aliases: `/tp` | Continue a web-started task locally. |
| `/web-setup` | Connects GitHub for cloud sessions using your local `gh` credentials. | Before your first cloud session. |

## Diagnostics & feedback

Start here when something is wrong

| Command | What it does | Best use |
|---|---|---|
| `/doctor`<br>`[prompt-audit [path]]`<br>★ · Skill | Runs a setup checkup for installation, settings, extensions and `CLAUDE.md`, proposing fixes Claude applies after you confirm. `prompt-audit` audits your instructions instead.<br>Aliases: `/checkup` | Something feels broken: start with `/doctor`. |
| `/help`<br>★ | Shows help and available commands. | Forgot a command: `/help`, or type `/` plus a few letters. |
| `/powerup`<br>★ | Interactive lessons with animated demos that teach Claude Code features. | The best structured starting point for newcomers. |
| `/bug`<br>`[report]`<br>↗ Sends data out · ⚿ May expose secrets | Reports a bug or shares your conversation; you choose how much history to include and confirm before anything is sent.<br>Aliases: `/share` | When Claude Code itself misbehaves. |
| `/debug`<br>`[description]`<br>Skill | Enables debug logging from this point and troubleshoots by reading the session debug log. Optionally describe the issue. | `/debug the MCP server keeps failing to connect`. |
| `/exit` | Exits the CLI. In an attached background session it detaches and the session keeps running.<br>Aliases: `/quit` | Done for the day. |
| `/feedback`<br>`[report]`<br>↗ Sends data out · ⚿ May expose secrets | Sends product feedback using the same dialog and consent step as `/bug`. | Request a feature. |
| `/heapdump`<br>⚿ May expose secrets | Writes a heap snapshot and memory breakdown to the Desktop for diagnosing high memory. Share only the `-diagnostics.json`; the `.heapsnapshot` contains your conversation and credentials. Hidden from the menu. | Report a memory blow-up. |
| `/release-notes` | Views the changelog in a version picker; notes appear without entering Claude's context. | See what's new after an update. |
| `/restart`<br>Requires v2.1.288+ | Restarts Claude Code and resumes the session to apply an installed update. Requires Pro, Max or Ultra and a native macOS or Linux install (not WSL).<br>Aliases: `/update` | When the footer offers it after an update. |

## Other

Small extras

| Command | What it does | Best use |
|---|---|---|
| `/radio` | Opens Claude FM lo-fi radio in your browser, or prints the stream URL. | Background music while you work. |
| `/stickers` | Orders Claude Code stickers. | Decorate your laptop. |

## Removed

Still mentioned in older guides but no longer available

| Command | What it does | Best use |
|---|---|---|
| `/pr-comments`<br>`[PR]`<br>Removed in v2.1.91 | Removed in v2.1.91. Ask Claude directly to view pull request comments. | Ask in plain language. |
| `/ultraplan`<br>`<prompt>` | Removed. Use plan mode (`/plan`) instead. | Use `/plan`. |
| `/vim`<br>Removed in v2.1.92 | Removed in v2.1.92. Use `/config` → Editor mode. | Use `/config`. |

## Disclaimer

1. **Unofficial project**: A community project, not affiliated with, sponsored or endorsed by Anthropic. “Claude”, “Claude Code” and related marks are trademarks of Anthropic, used here only to identify the product being described.
2. **May be outdated or wrong**: Every description is a simplified paraphrase of the official documentation, provided “as is” without warranty of any kind, express or implied. Claude Code changes often; commands are added, renamed and removed. Where this project and the official docs disagree, the official docs win.
3. **Use at your own risk**: Some commands change or revert files, run commands, push code, send data to external services or consume paid usage. Understand what a command does before running it, commit or back up first, and do not use it on production systems, important data or other people's repositories without review.
4. **Protect secrets and privacy**: Do not put API keys, passwords, tokens or other people's personal data in prompts. Exported conversations, bug reports and memory snapshots can contain them; review before sharing.
5. **Examples are illustrative**: The “best use” examples explain purpose; they are not instructions for your environment. Availability depends on version, plan, platform and organization policy.
6. **This page does not track you**: This page uses no cookies, analytics, third-party scripts or fonts. It stores only your language and theme preferences, locally in your browser.
7. **Limitation of liability**: To the maximum extent permitted by law, the authors and contributors are not liable for any loss arising from use of this project, including data loss, charges, security incidents or service interruption.

## About this project

- **Source**: paraphrased from the official [commands reference](https://code.claude.com/docs/en/commands), checked 2026-11-09. Descriptions are simplified, not official translations; where they differ, the official docs win.
- **Data**: everything is generated from [`data/commands.json`](data/commands.json). Edit the JSON, then run `python3 scripts/build.py`.
- **Contributing**: see [CONTRIBUTING.md](CONTRIBUTING.md).
- **License**: content [CC BY 4.0](LICENSE-CONTENT), code [MIT](LICENSE).
