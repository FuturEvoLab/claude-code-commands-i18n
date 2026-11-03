# Security Policy · セキュリティポリシー · 安全策略

## English

**Scope.** This repository contains documentation, a static web page and a build script. It does not run a server or collect data.

**Report a problem privately** through GitHub's “Report a vulnerability” button (Security tab → Advisories) rather than a public issue, for example:

- markup or script injection that gets past `scripts/build.py` validation into the READMEs or `docs/index.html`;
- advice in this guide that could lead users to expose secrets, lose data or weaken their Claude Code safety settings.

We aim to reply within 7 days. Vulnerabilities in Claude Code itself are out of scope; report them to Anthropic through the channels listed in Anthropic's official documentation.

**Safeguards in place**

- The page loads no third-party scripts, fonts or trackers, and stores only a language preference in `localStorage`.
- `docs/index.html` ships a Content-Security-Policy that allows only its own inline style and script (by SHA-256 hash), no network requests, no forms and no `<base>`.
- All data is HTML-escaped before display. The build rejects raw HTML, Markdown links and URLs in prose fields, and restricts command names to `/lowercase-words`.
- CI runs with read-only repository permissions and fails if generated files are out of date.

## 日本語

このリポジトリにはドキュメント、静的な Web ページ、ビルドスクリプトしかなく、サーバーの運用やデータ収集は行いません。セキュリティ上の問題（ビルド時の検査をすり抜ける HTML・スクリプトの挿入、利用者が秘密情報を漏らしたりデータを失ったり安全設定を弱めたりしかねない誤った説明など）は、公開の Issue ではなく GitHub の「Report a vulnerability」から非公開で報告してください。7 日以内の返信を目指します。Claude Code 自体の脆弱性は対象外です。Anthropic の公式ドキュメントに記載された窓口に報告してください。

## 中文

本仓库只有文档、静态网页和构建脚本，不运行服务器，也不收集数据。发现安全问题（如绕过构建校验的 HTML/脚本注入，或可能导致用户泄露密钥、丢失数据、削弱安全设置的错误建议），请通过 GitHub 的「Report a vulnerability」私下报告，不要公开提 Issue。我们会尽量在 7 天内回复。Claude Code 本身的漏洞不在本项目范围内，请按 Anthropic 官方文档中的渠道报告。
