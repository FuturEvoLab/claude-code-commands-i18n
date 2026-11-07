# Changelog

## 1.4.0 — 2026-11-08

- Every command now has its own page in every language (826 pages): `/commands/compact/`, `/ja/commands/compact/` and so on. Each shows what the command does, its best use, aliases, safety notes, the situations it helps with, related commands in the same category, and previous/next links, with its own search title, description, canonical URL, `hreflang` links and JSON-LD (`TechArticle` and `BreadcrumbList`).
- The pages are static HTML with one shared stylesheet (`docs/assets/command.css`, generated from the main page's themes), so they load fast and follow the theme the visitor picked.
- Cards on the main page have a "Details" link, and "Copy link" now copies the command's own page, which shows a proper preview when shared.
- `sitemap.xml` lists every command page with its other languages; `llms.txt` lists every command page; `llms-full.txt` gives each command's address.

## 1.3.2 — 2026-11-07

- Counts agree everywhere: "All commands" and the search bar now show 115 like the banner; the 3 removed commands appear under their own "Removed" heading and in search.
- Short code such as `-diagnostics.json` or `--dry-run` no longer breaks at a hyphen; long examples still wrap.
- Phones: the search box gets more room (the idle count is hidden and the language menu is narrower), and the keyboard-shortcut hint is hidden on touch screens. On Windows and Linux the hint says Ctrl K instead of ⌘K.
- Without JavaScript: the notice is translated and says the full list is below; the badge and section headings are filled in; search, menus and the terminal demo are hidden instead of showing empty.

## 1.3.1 — 2026-11-07

- Faster pages: each language page now carries only its own text plus English (the Japanese page went from 484 KB to 267 KB, 78 KB compressed). Picking a language the page does not carry opens that language's page; a saved choice or a `#ko-…` link redirects to the right page and keeps `?theme=`.
- The full command list is built a few sections at a time, so phones stay responsive while it loads; deep links still render everything at once.
- Copied card links point at the language's own page.
- Accessibility: the "/cc" button's spoken name now includes its visible text.

## 1.3.0 — 2026-11-07

- Search engines (SEO): each language now has its own address (`/`, `/ja/`, `/zh-cn/`, `/zh-hant/`, `/ko/`, `/ru/`, `/es/`) with its own canonical URL, reciprocal `hreflang` links, `og:locale`, and a search-result title and description written for that language (`data/seo.json`, length-checked by the build).
- Every command, category and scenario is pre-rendered as plain HTML, so crawlers and AI tools that do not run JavaScript read the full guide; the script then takes over as before.
- AI answer engines (GEO): JSON-LD with the site, the article, every command as a `DefinedTerm` and the 16 scenarios as an `FAQPage`; `llms.txt` and `llms-full.txt` (all commands in Markdown); `sitemap.xml` and `robots.txt`.
- Switching language updates the address, so a reload or shared link keeps the language. Each README links to its own language page.

## 1.2.1 — 2026-11-07

- Fixed: on phones the command list was laid out 1200px wide and the page scrolled sideways.
- Phones: the four stats stay on one row, and "Copy link" buttons are 36px tall for easier tapping.
- Contrast: every text color now meets WCAG AA (4.5:1) in all 12 themes, light and dark; the "file changes" label and the Ember accent were darkened slightly.
- Checked against Claude Code 2.1.319: `/usage` shows spend for today, this week and this month; `/claude-api` has `latency-optimize`. All seven languages updated.

## 1.2.0 — 2026-11-05

- Checked against the official changelog up to 2.1.318: no commands missing. Updated `/permissions` (Recently blocked tab), `/usage` (warnings with one-line fixes, `f` applies them) and `/claude-api` (`api-version` subcommand) in all seven languages.
- Link previews: a 1200×630 share image (`docs/assets/social.png`) and large-image cards.
- Favicon, canonical URL and `hreflang` links for each language; a multilingual `404.html` with its own CSP.
- Keyboard: a translated "Skip to the command list" link appears on the first Tab.
- Screenshots are about 60% smaller; `scripts/optimize_images.py` (needs Pillow) makes the share image and shrinks the PNGs.
- CI uses `actions/checkout` v7.0.1, pinned by commit SHA.

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
