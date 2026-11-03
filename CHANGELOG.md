# Changelog

## 1.1.0 — 2026-11-03

- Live preview on GitHub Pages; `?theme=` and `?lang=` in the link open a theme or language directly. README screenshots are now in English, with the default and Matrix themes side by side.
- Seven languages, in this order: English, Japanese, Simplified Chinese, Traditional Chinese, Korean, Russian, Spanish. Each has its own README; the page title and search follow the chosen language.
- Languages, page strings and README strings now live in `data/`; `scripts/language_tool.py` checks and merges a new language with the same rules as the build.
- Proofreading: clearer `/subtask` description in five languages; README intros list all languages; the language count on the page follows the data.
- Full review of all seven languages against English: 70 fixes (meaning errors, omitted facts, terminology, grammar). English gained missing facts for `/tui` and `/batch`; the privacy note now says the page stores both language and theme.
- Full-dark themes Cyberpunk, Matrix (with a banner rain that spells real slash commands and respects reduced motion) and Midnight keep the whole page dark.
- Eight more color themes besides the default Terminal: Graphite, Indigo, Ocean, Ember, Rose and Mono with a dark banner, and Paper and Frost, which stay light even in system dark mode. The choice is remembered per browser.
- Language and theme switches are dropdowns; the language one stays in the top bar on phones.
- The hero's terminal demo keeps a fixed height, so the headline no longer shifts while it types.

## 1.0.0 — 2026-11-03

First public release.

- 115 current Claude Code slash commands (plus 3 removed ones), checked against the official commands reference on 2026-11-03.
- English, Japanese and Chinese for every description, example and one-line summary; build fails if the languages drift apart.
- 16 “I want to…” scenarios, editor's picks for beginners, and safety labels on 22 commands.
- Searchable single-file web page (`docs/index.html`): pinned search, keyboard selection, per-command links, light and dark themes, no third-party requests, strict Content-Security-Policy.
- Generated READMEs in three languages, test suite, CI with read-only permissions.
