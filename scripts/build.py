#!/usr/bin/env python3
"""Validate data/*.json and generate the three READMEs and the web page.

Usage: python3 scripts/build.py [--repo OWNER/NAME]
Outputs: README.md, README.zh-CN.md, README.ja.md, docs/index.html, dist/artifact.html
"""
import argparse
import base64
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ("en", "ja", "zh")
KINDS = ("builtin", "skill", "workflow", "removed")

META = {
    "source": "https://code.claude.com/docs/en/commands",
    "checked": "2026-11-03",
}
REPO_FILE = ROOT / "repo.txt"  # holds OWNER/NAME so later builds remember it

# Strings used in the generated Markdown, one entry per language.
T = {
    "en": {
        "file": "README.md",
        "risk_h": "Safety labels",
        "risk_d": "Commands marked with these labels need extra care.",
        "disc_h": "Disclaimer",
        "scen": "Find a command by what you want to do",
        "scen_desc": "Pick the situation; the commands are listed in the order to try them.",
        "title": "Claude Code Commands",
        "intro": "An unofficial, plain-language reference to every Claude Code slash command, in **English, Japanese and Chinese**. It is written for people who find the official English docs hard to read: each command gets a short explanation and a realistic example of when to use it.",
        "web": "Searchable web version",
        "start": "Start here",
        "start_desc": "The editor's picks for a first week with Claude Code.",
        "toc": "Contents",
        "syntax": "How to read the syntax",
        "syntax_body": "- Type `/` in the prompt to open the command menu; keep typing to filter.\n- `[ ]` = optional, `< >` = required, `|` = one of.\n- **Skill** = a bundled prompt handed to Claude. **Workflow** = runs several agents in the background.\n- Many commands depend on version, plan, platform or an enabled feature. The menu you see is authoritative; check your version with `/status`.",
        "cols": ("Command", "What it does", "Best use"),
        "alias": "Aliases", "since": "Requires v{}+", "removed_in": "Removed in v{}",
        "skill": "Skill", "workflow": "Workflow",
        "about": "About this project",
        "about_body": "- **Source**: paraphrased from the official [commands reference]({source}), checked {checked}. Descriptions are simplified, not official translations; where they differ, the official docs win.\n- **Data**: everything is generated from [`data/commands.json`](data/commands.json). Edit the JSON, then run `python3 scripts/build.py`.\n- **Contributing**: see [CONTRIBUTING.md](CONTRIBUTING.md).\n- **License**: content [CC BY 4.0](LICENSE-CONTENT), code [MIT](LICENSE).",
    },
    "zh": {
        "file": "README.zh-CN.md",
        "risk_h": "安全标记",
        "risk_d": "带有以下标记的命令需要格外小心。",
        "disc_h": "免责声明",
        "scen": "按场景找命令",
        "scen_desc": "按你想做的事来找，命令按建议尝试的顺序排列。",
        "title": "Claude Code 命令大全",
        "intro": "非官方的 Claude Code 斜杠命令速查手册，提供**英文、日文、中文**三种语言，专门写给读英文官方文档吃力的用户：每个命令都有英文原意、简单易懂的说明，以及一个真实的「什么时候用」的例子。",
        "web": "可搜索的网页版",
        "start": "新手推荐",
        "start_desc": "编者为刚开始使用 Claude Code 的人挑选的命令。",
        "toc": "目录",
        "syntax": "如何看懂命令写法",
        "syntax_body": "- 在输入框输入 `/` 会弹出命令列表，继续输入字母可以筛选。\n- `[ ]` 表示可写可不写，`< >` 表示必须写，`|` 表示几选一。参数可以直接用中文写。\n- **技能**：交给 Claude 执行的一套提示流程。**工作流**：派出多个代理在后台运行。\n- 很多命令只在特定版本、套餐、平台或开启某功能后才出现。以你自己看到的列表为准，可用 `/status` 查看版本。",
        "cols": ("命令", "英文原意", "说明", "最佳用法"),
        "alias": "同义命令", "since": "需 v{}+", "removed_in": "v{} 移除",
        "skill": "技能", "workflow": "工作流",
        "about": "关于本项目",
        "about_body": "- **来源**：依据官方[命令文档]({source})意译整理，核对日期 {checked}。说明经过简化，不是官方翻译；如有出入，以官方文档为准。\n- **数据**：所有内容由 [`data/commands.json`](data/commands.json) 生成。修改 JSON 后运行 `python3 scripts/build.py`。\n- **参与贡献**：见 [CONTRIBUTING.md](CONTRIBUTING.md)。\n- **许可**：内容 [CC BY 4.0](LICENSE-CONTENT)，代码 [MIT](LICENSE)。",
    },
    "ja": {
        "file": "README.ja.md",
        "risk_h": "安全マーク",
        "risk_d": "次のマークが付いたコマンドは特に注意が必要です。",
        "disc_h": "免責事項",
        "scen": "やりたいことから探す",
        "scen_desc": "状況を選んでください。コマンドは試す順に並んでいます。",
        "title": "Claude Code コマンド一覧",
        "intro": "Claude Code のスラッシュコマンドを**英語・日本語・中国語**で説明する非公式のリファレンスです。英語の公式ドキュメントが読みにくい方のために、各コマンドの英語の意味、やさしい説明、「いつ使うと便利か」の具体例を載せています。",
        "web": "検索できる Web 版",
        "start": "初心者向け",
        "start_desc": "Claude Code を使い始めた方向けに編者が選んだコマンドです。",
        "toc": "目次",
        "syntax": "書き方の読み方",
        "syntax_body": "- 入力欄に `/` と打つと一覧が出ます。続けて文字を打つと絞り込めます。\n- `[ ]` は省略可、`< >` は必須、`|` は「どれか 1 つ」。引数は日本語で書いてかまいません。\n- **スキル**：Claude に渡す決まった手順書。**ワークフロー**：複数のエージェントをバックグラウンドで動かします。\n- 多くのコマンドはバージョン・プラン・環境・機能の有効化によって表示が変わります。自分の画面に出る一覧が正です。バージョンは `/status` で確認できます。",
        "cols": ("コマンド", "英語の意味", "説明", "おすすめの使い方"),
        "alias": "別名", "since": "v{} 以降", "removed_in": "v{} で削除",
        "skill": "スキル", "workflow": "ワークフロー",
        "about": "このプロジェクトについて",
        "about_body": "- **出典**：公式の[コマンドリファレンス]({source})をもとに意訳（確認日 {checked}）。説明は簡略化したもので公式の翻訳ではありません。違いがある場合は公式ドキュメントが優先です。\n- **データ**：すべて [`data/commands.json`](data/commands.json) から生成しています。JSON を編集して `python3 scripts/build.py` を実行してください。\n- **貢献**：[CONTRIBUTING.md](CONTRIBUTING.md) を参照。\n- **ライセンス**：内容は [CC BY 4.0](LICENSE-CONTENT)、コードは [MIT](LICENSE)。",
    },
}

LANG_LINKS = "[English](README.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md)"


def load():
    read = lambda f: json.loads((ROOT / "data" / f).read_text(encoding="utf-8"))
    return {k: read(f"{k}.json") for k in ("categories", "commands", "scenarios", "risks", "disclaimer")}


# Prose fields may use `code` spans but no raw HTML, Markdown links or URLs, so a
# pull request cannot smuggle markup or off-site links into the READMEs or the page.
UNSAFE = re.compile(r"[<>]|\]\(|https?:|javascript:|data:", re.I)
NAME = re.compile(r"/[a-z0-9-]+( [a-z0-9-]+)?")


def unsafe(text):
    return bool(UNSAFE.search(re.sub(r"`[^`]*`", "", text)))


def check_prose(errors, where, field):
    for l in LANGS:
        text = (field or {}).get(l)
        if not text:
            errors.append(f"{where}: missing {l}")
        elif text.count("`") % 2:
            errors.append(f"{where}.{l}: unbalanced backticks")
        elif unsafe(text):
            errors.append(f"{where}.{l}: raw HTML, link or URL is not allowed")


def validate(d):
    cats, cmds, scens, risks, disc = (d[k] for k in ("categories", "commands", "scenarios", "risks", "disclaimer"))
    errors = []
    risk_ids = {r["id"] for r in risks}
    for r in risks:
        check_prose(errors, f"risk {r['id']}.name", r.get("name"))
        check_prose(errors, f"risk {r['id']}.desc", r.get("desc"))
    for l in LANGS:
        for i, item in enumerate(disc.get(l, [])):
            for f in ("t", "b"):
                if not item.get(f) or unsafe(item[f]):
                    errors.append(f"disclaimer.{l}[{i}].{f}: missing or unsafe")
    if len({len(disc.get(l, [])) for l in LANGS}) != 1:
        errors.append("disclaimer: languages have different numbers of items")
    names = {c["cmd"] for c in cmds}
    for sc in scens:
        check_prose(errors, f"scenario {sc['id']}.q", sc.get("q"))
        for n in sc["cmds"]:
            if n not in names:
                errors.append(f"scenario {sc['id']}: unknown command {n}")
    cat_ids = [c["id"] for c in cats]
    seen = set()
    for c in cats:
        for f in ("name", "desc"):
            check_prose(errors, f"category {c['id']}.{f}", c.get(f))
    for c in cmds:
        name = c.get("cmd", "?")
        for key in (name, *c.get("aliases", [])):
            if key in seen:
                errors.append(f"{name}: duplicate name or alias {key}")
            seen.add(key)
        for key in (name, *c.get("aliases", [])):
            if not NAME.fullmatch(key):
                errors.append(f"{name}: bad command name {key}")
        if unsafe(c.get("word", "")):
            errors.append(f"{name}: unsafe word")
        for r in c.get("risk", []):
            if r not in risk_ids:
                errors.append(f"{name}: unknown risk {r}")
        if c.get("cat") not in cat_ids:
            errors.append(f"{name}: unknown category {c.get('cat')}")
        if c.get("kind") not in KINDS:
            errors.append(f"{name}: unknown kind {c.get('kind')}")
        if not c.get("word"):
            errors.append(f"{name}: missing word")
        for l in ("zh", "ja"):
            g = c.get("gloss", {}).get(l)
            if not g or unsafe(g):
                errors.append(f"{name}: missing or unsafe gloss.{l}")
        for f in ("desc", "use"):
            check_prose(errors, f"{name}.{f}", c.get(f))
        # Translations must mention the same commands, flags and values.
        spans = {l: sorted(set(re.findall(r"`([^`]+)`", c.get("desc", {}).get(l, "")))) for l in LANGS}
        if not spans["zh"] == spans["ja"] == spans["en"]:
            errors.append(f"{name}.desc: `code` spans differ between languages {spans}")
        if c.get("short"):
            check_prose(errors, f"{name}.short", c["short"])
        if c.get("pick") and not all(c.get("short", {}).get(l) for l in LANGS):
            errors.append(f"{name}: editor's pick needs short.zh/ja/en")
        for f in ("since", "removedIn"):
            if c.get(f) and not re.fullmatch(r"\d+\.\d+\.\d+", c[f]):
                errors.append(f"{name}: bad version in {f}")
    return errors


def ordered(cats, cmds):
    """Commands grouped by category: editor's picks first, then alphabetical."""
    return [(cg, sorted((c for c in cmds if c["cat"] == cg["id"]), key=lambda c: (not c["pick"], c["cmd"])))
            for cg in cats]


def cell(s):
    return s.replace("|", "\\|").replace("\n", " ")


def anchor(text):
    # GitHub-style heading anchor: lowercase, drop punctuation, spaces to hyphens.
    a = re.sub(r"[^\w\- ]", "", text.lower(), flags=re.UNICODE)
    return a.strip().replace(" ", "-")


def command_cell(c, t, lang, risks):
    s = f"`{c['cmd']}`"
    if c["args"]:
        s += f"<br>`{c['args']}`"
    marks = []
    if c["pick"]:
        marks.append("★")
    if c["kind"] in ("skill", "workflow"):
        marks.append(t[c["kind"]])
    if c.get("since"):
        marks.append(t["since"].format(c["since"]))
    if c.get("removedIn"):
        marks.append(t["removed_in"].format(c["removedIn"]))
    marks += [f"{risks[r]['icon']} {risks[r]['name'][lang]}" for r in c.get("risk", [])]
    if marks:
        s += "<br>" + " · ".join(marks)
    return cell(s)


def desc_cell(c, lang, t):
    s = c["desc"][lang]
    if c["aliases"]:
        s += f"<br>{t['alias']}: " + ", ".join(f"`{a}`" for a in c["aliases"])
    return cell(s)


def readme(lang, cats, groups, scens, risk_list, disc):
    risks = {r["id"]: r for r in risk_list}
    t = T[lang]
    badges = " ".join([
        "![Unofficial](https://img.shields.io/badge/Anthropic-unofficial-lightgrey)",
        f"[![check]({META['repo']}/actions/workflows/check.yml/badge.svg)]({META['repo']}/actions/workflows/check.yml)",
        "[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-blue)](LICENSE-CONTENT)",
        "[![Code: MIT](https://img.shields.io/badge/code-MIT-green)](LICENSE)",
        f"![Commands](https://img.shields.io/badge/commands-{sum(c['kind'] != 'removed' for _, r in groups for c in r)}-teal)",
    ])
    out = [f"# {t['title']}", "", LANG_LINKS, "", badges, "",
           f"> {t['intro']}", "",
           f"### [{t['web']} →]({META['site']})", "",
           f"[![{t['title']}](docs/assets/preview-en.png)]({META['site']})", "",
           "<p>"
           f'<img src="docs/assets/preview-search.png" alt="search" width="68%"> '
           f'<img src="docs/assets/preview-mobile.png" alt="mobile" width="28%">'
           "</p>", ""]
    out += [f"## {t['syntax']}", "", t["syntax_body"], ""]

    picks = [c for _, rows in groups for c in rows if c["pick"]]
    out += [f"## ★ {t['start']}", "", t["start_desc"], ""]
    out += [f"- `{c['cmd']}` · {c['short'][lang]}" for c in picks]
    out.append("")

    out += [f"## {t['scen']}", "", t["scen_desc"], ""]
    for sc in scens:
        out.append(f"- **{sc['q'][lang]}** → " + " · ".join(f"`{n}`" for n in sc["cmds"]))
    out.append("")

    out += [f"## {t['risk_h']}", "", t["risk_d"], ""]
    out += [f"- **{r['icon']} {r['name'][lang]}**: {r['desc'][lang]}" for r in risk_list]
    out.append("")

    out += [f"## {t['toc']}", ""]
    out += [f"- [{cg['name'][lang]}](#{anchor(cg['name'][lang])}) ({len(rows)})" for cg, rows in groups if rows]
    out.append("")

    for cg, rows in groups:
        if not rows:
            continue
        out += [f"## {cg['name'][lang]}", "", cg["desc"][lang], ""]
        cols = t["cols"]
        out += ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
        for c in rows:
            cells = [command_cell(c, t, lang, risks)]
            if lang != "en":
                cells.append(cell(f"{c['word']}<br>{c['gloss'][lang]}"))
            cells += [desc_cell(c, lang, t), cell(c["use"][lang])]
            out.append("| " + " | ".join(cells) + " |")
        out.append("")

    out += [f"## {t['disc_h']}", ""]
    out += [f"{i}. **{item['t']}**: {item['b']}" for i, item in enumerate(disc[lang], 1)]
    out.append("")
    out += [f"## {t['about']}", "", t["about_body"].format(**META), ""]
    return "\n".join(out)


def page(cats, groups, scens, risks, disc):
    flat = [c for _, rows in groups for c in rows]
    tpl = (ROOT / "site/template.html").read_text(encoding="utf-8")
    dump = lambda x: json.dumps(x, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return (tpl.replace("/*META*/null", dump(META))
               .replace("/*CATS*/[]", dump(cats))
               .replace("/*CMDS*/[]", dump(flat))
               .replace("/*SCENS*/[]", dump(scens))
               .replace("/*RISKS*/[]", dump(risks))
               .replace("/*DISC*/null", dump(disc)))


def social():
    """Link-preview tags for community posts (Open Graph / Twitter)."""
    desc = "Every Claude Code slash command explained in English, Japanese and Chinese. Unofficial."
    return "".join(f'<meta {k}="{n}" content="{v}">\n' for k, n, v in (
        ("property", "og:type", "website"),
        ("property", "og:title", "Claude Code Commands · English / 日本語 / 中文"),
        ("property", "og:description", desc),
        ("property", "og:url", META["site"]),
        ("name", "twitter:card", "summary"),
    ))


def csp(body):
    """Content-Security-Policy that allows only this page's own inline style and script."""
    h = lambda src: "'sha256-" + base64.b64encode(hashlib.sha256(src.encode("utf-8")).digest()).decode() + "'"
    styles = re.findall(r"<style>(.*?)</style>", body, re.S)
    scripts = re.findall(r"<script>(.*?)</script>", body, re.S)
    return ("default-src 'none'; img-src 'self' data:; "
            f"style-src {' '.join(map(h, styles))}; script-src {' '.join(map(h, scripts))}; "
            "base-uri 'none'; form-action 'none'")


def repo_meta(arg):
    """Resolve OWNER/NAME from --repo, else repo.txt, else a placeholder."""
    if arg:
        if not re.fullmatch(r"[\w.-]+/[\w.-]+", arg):
            sys.exit("--repo must look like OWNER/NAME")
        REPO_FILE.write_text(arg + "\n", encoding="utf-8")
    slug = arg or (REPO_FILE.read_text(encoding="utf-8").strip() if REPO_FILE.exists() else "OWNER/claude-code-commands-i18n")
    owner, name = slug.split("/")
    META["repo"] = f"https://github.com/{slug}"
    META["site"] = f"https://{owner.lower()}.github.io/{name}/"
    return slug.startswith("OWNER/")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", help="GitHub OWNER/NAME; saved to repo.txt for later builds")
    placeholder = repo_meta(ap.parse_args().repo)
    d = load()
    cats, cmds, scens = d["categories"], d["commands"], d["scenarios"]
    errors = validate(d)
    if errors:
        print("Data errors:\n  " + "\n  ".join(errors), file=sys.stderr)
        sys.exit(1)
    groups = ordered(cats, cmds)
    for lang in LANGS:
        (ROOT / T[lang]["file"]).write_text(readme(lang, cats, groups, scens, d["risks"], d["disclaimer"]), encoding="utf-8")
    body = page(cats, groups, scens, d["risks"], d["disclaimer"])
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "docs").mkdir(exist_ok=True)
    # The artifact host supplies its own document skeleton; GitHub Pages needs a full one.
    (ROOT / "dist/artifact.html").write_text(body, encoding="utf-8")
    (ROOT / "docs/index.html").write_text(
        '<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        f'<meta http-equiv="Content-Security-Policy" content="{csp(body)}">\n'
        + social()
        + body + "\n</html>\n", encoding="utf-8")
    print(f"OK: {len(cmds)} commands, {len(cats)} categories, {len(scens)} scenarios; wrote 3 READMEs, docs/index.html, dist/artifact.html")
    if placeholder:
        print("Note: repository links use the placeholder OWNER. Run again with --repo OWNER/NAME.")


if __name__ == "__main__":
    main()
