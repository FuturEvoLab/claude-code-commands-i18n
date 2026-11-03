# Contributing · 貢献ガイド · 参与贡献

[English](#english) · [日本語](#日本語) · [中文](#中文)

## English

1. Edit `data/commands.json` (or `data/categories.json`, `data/scenarios.json`). Do not edit `README*.md` or `docs/index.html` by hand; they are generated.
2. Run `python3 scripts/build.py` and `python3 scripts/test_build.py` (first time: `python3 scripts/build.py --repo OWNER/NAME`, which is remembered in `repo.txt`). It validates the data (all three languages present, known categories, no duplicate names or aliases, balanced backticks) and regenerates every output. Python 3.8+ with no extra packages.
3. Open a pull request. In the description, link the official doc section that supports the change.

Rules for accuracy:

- Every claim must be traceable to the official [commands reference](https://code.claude.com/docs/en/commands) or a page it links to. Do not describe behavior from memory or from third-party blogs.
- Record version requirements in `since` and removals in `removedIn` (format `2.1.269`) only when the docs state them.
- Keep the three languages saying the same thing. If you can only write one language, open the PR anyway and mark the others with `TODO` in the PR description; a reviewer will finish them.
- When the docs change, update `META.checked` in `scripts/build.py`.
- Add a `risk` label (see `data/risks.json`) to any command that can cost money, send data out, expose secrets, change many files or loosen safety settings. When unsure, add it.
- Prose fields may use `code` spans but no HTML, Markdown links or URLs; the build rejects them. Never put real keys, tokens or personal data in examples.

Field reference (one object per command):

| Field | Meaning |
|---|---|
| `cmd`, `args` | Command name and argument syntax, copied from the docs |
| `cat` | Category id from `data/categories.json` |
| `kind` | `builtin`, `skill`, `workflow` or `removed` |
| `pick` | `true` for the beginner list; requires `short` |
| `aliases` | Other names for the same command |
| `risk` | Optional safety labels from `data/risks.json` |
| `since`, `removedIn` | Optional version strings |
| `word`, `gloss.zh/ja` | The English word(s) behind the name, and their meaning |
| `desc`, `use`, `short` | Description, best-use example, one-line summary, each in `zh`, `ja`, `en` |

### Add a language

1. Copy the shape of an existing language into `data/i18n/<code>.json`: `language` (`code`, `name`, `html`, `readme`), then every string keyed by command, category, scenario and risk id, plus `disclaimer`, `ui` and `readme`. The fastest way is to ask in an issue and a maintainer will generate a template.
2. Run `python3 scripts/language_tool.py check data/i18n/<code>.json` until it prints OK. It runs every build check with your language added.
3. Run `python3 scripts/language_tool.py merge data/i18n/<code>.json`, place the language where it belongs in `data/languages.json`, delete the `data/i18n/` file, then run the build and tests.

Right-to-left languages (Arabic, Hebrew) also need layout work; open an issue first.

## Maintainers

- **Publish the site**: Settings → Pages → Deploy from a branch → `main` / `/docs`. The page is then live at the URL in the README.
- **Enable private vulnerability reporting** (Settings → Code security), which `SECURITY.md` points reporters to.
- **Refresh screenshots** after visual changes: `scripts/screenshots.sh` (needs Google Chrome).
- **Release**: update `CHANGELOG.md` and `META.checked` in `scripts/build.py`, then tag `vX.Y.Z`.

## 日本語

1. `data/commands.json`（または `data/categories.json`・`data/scenarios.json`）を編集します。`README*.md` と `docs/index.html` は自動生成なので手で編集しないでください。
2. `python3 scripts/build.py` を実行します（初回は `--repo ユーザー名/リポジトリ名` を付けると `repo.txt` に保存されます）。データの検査（3 言語がそろっている、カテゴリーが存在する、名前や別名が重複しない、バッククォートが対になっている）を行い、すべてを再生成します。Python 3.8 以降のみで動きます。
3. Pull Request を作成し、変更の根拠となる公式ドキュメントのリンクを書いてください。

正確さのルール：

- すべての説明は公式の[コマンドリファレンス](https://code.claude.com/docs/en/commands)またはそのリンク先で確認できる内容にしてください。記憶や第三者のブログをもとに書かないでください。
- `since`（最低バージョン）と `removedIn`（削除されたバージョン）は、公式に明記されている場合のみ `2.1.269` の形式で記入します。
- 3 言語の内容をそろえてください。1 言語しか書けなくても歓迎します。PR の説明に未翻訳の言語を書いておいてください。
- 費用の発生、外部への送信、機密情報の露出、多数のファイル変更、安全設定の緩和につながるコマンドには `risk` マーク（`data/risks.json`）を付けてください。迷ったら付けます。
- 説明文では `コード` は使えますが、HTML・Markdown のリンク・URL は書けません（ビルドで拒否されます）。例に本物のキー・トークン・個人情報を書かないでください。

## 中文

1. 修改 `data/commands.json`（或 `data/categories.json`、`data/scenarios.json`）。不要手动改 `README*.md` 和 `docs/index.html`，它们是自动生成的。
2. 运行 `python3 scripts/build.py`（第一次运行加 `--repo 用户名/仓库名`，会记在 `repo.txt` 里）：会检查数据（三种语言齐全、分类存在、命令名和别名不重复、反引号成对），然后重新生成所有文件。只需 Python 3.8+，无需安装其他包。
3. 提交 Pull Request，并在说明中附上支持此修改的官方文档链接。

准确性要求：

- 每一条说明都必须能在官方[命令文档](https://code.claude.com/docs/en/commands)或其链接的页面中找到依据，不要凭记忆或第三方文章编写。
- 只有官方文档写明时，才填写 `since`（最低版本）和 `removedIn`（移除版本），格式如 `2.1.269`。
- 三种语言的意思必须一致。只会写一种语言也欢迎提交，在 PR 说明里注明其余语言待补充即可。
- 可能产生费用、向外部发送数据、暴露敏感信息、大范围修改文件或放宽安全设置的命令，必须加上 `risk` 标记（见 `data/risks.json`）。拿不准时就加。
- 说明文字中可以用 `代码`，但不能写 HTML、Markdown 链接或网址，构建会拒绝。示例中绝不能出现真实的密钥、令牌或个人信息。
