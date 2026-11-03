# Changelog

## 1.1.0 — 2026-11-03

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
