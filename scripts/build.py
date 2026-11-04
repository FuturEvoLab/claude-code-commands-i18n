#!/usr/bin/env python3
"""Validate data/*.json and generate one README per language and the web page.

Usage: python3 scripts/build.py [--repo OWNER/NAME]
Outputs: README*.md (see data/languages.json), docs/index.html, dist/artifact.html
"""
import argparse
import base64
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KINDS = ("builtin", "skill", "workflow", "removed")

META = {
    "source": "https://code.claude.com/docs/en/commands",
    "checked": "2026-11-05",
}
REPO_FILE = ROOT / "repo.txt"  # holds OWNER/NAME so later builds remember it

def _read(name):
    return json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))


# Languages, in display order, come from data/languages.json; README strings from data/readme.json.
LANGINFO = _read("languages.json")
LANGS = tuple(x["code"] for x in LANGINFO)
T = {l: {**_read("readme.json")[l], "file": x["readme"]} for x in LANGINFO for l in [x["code"]]}
LANG_LINKS = " · ".join(f"[{x['name']}]({x['readme']})" for x in LANGINFO)



def load():
    read = lambda f: json.loads((ROOT / "data" / f).read_text(encoding="utf-8"))
    return {k: read(f"{k}.json") for k in ("categories", "commands", "scenarios", "risks", "disclaimer", "ui", "readme")}


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


# UI strings may carry a little markup; nothing else.
UI_TAGS = {"b", "code", "kbd", "p", "small"}
LINK_TARGETS = {"{source}", "data/commands.json", "CONTRIBUTING.md", "LICENSE-CONTENT", "LICENSE"}


def placeholders(text):
    return sorted(re.findall(r"\{[a-zA-Z]*\}", text))


def flat(v, path=""):
    """Yield (path, string) for every string inside nested lists/dicts."""
    if isinstance(v, str):
        yield path, v
    elif isinstance(v, list):
        for i, x in enumerate(v):
            yield from flat(x, f"{path}[{i}]")
    elif isinstance(v, dict):
        for k, x in v.items():
            yield from flat(x, f"{path}.{k}")


def check_strings(errors, where, table, check):
    # README tables have one more column (the English word) outside English.
    skip = lambda p: p.startswith(".cols")
    ref = {k: v for k, v in flat(table.get("en", {})) if not skip(k)}
    for l in LANGS:
        got = {k: v for k, v in flat(table.get(l, {})) if not skip(k)}
        if "cols" in table.get(l, {}) and len(table[l]["cols"]) != (3 if l == "en" else 4):
            errors.append(f"{where}.{l}.cols: expected {3 if l == 'en' else 4} columns")
        if set(got) != set(ref):
            errors.append(f"{where}.{l}: keys differ from en (missing {sorted(set(ref) - set(got))[:5]}, extra {sorted(set(got) - set(ref))[:5]})")
            continue
        for path, text in got.items():
            if not text.strip() and l != "en":  # English may leave a label empty (e.g. no "English word" gloss)
                errors.append(f"{where}.{l}{path}: empty")
            elif placeholders(text) != placeholders(ref[path]):
                errors.append(f"{where}.{l}{path}: placeholders {placeholders(text)} != en {placeholders(ref[path])}")
            else:
                check(errors, f"{where}.{l}{path}", text)


def check_ui_markup(errors, where, text):
    tags = set(re.findall(r"</?([a-zA-Z]+)[^>]*>", text))
    if tags - UI_TAGS or re.search(r"<[a-zA-Z]+\s", text) or re.search(r"https?:|javascript:", text, re.I):
        errors.append(f"{where}: only <b>, <code>, <kbd>, <p>, <small> without attributes are allowed")


def check_readme_markup(errors, where, text):
    if re.search(r"<|>|javascript:", re.sub(r"`[^`]*`", "", text)):
        errors.append(f"{where}: HTML is not allowed")
    for target in re.findall(r"\]\(([^)]*)\)", text):
        if target not in LINK_TARGETS:
            errors.append(f"{where}: link target {target!r} is not allowed")


def validate(d):
    cats, cmds, scens, risks, disc = (d[k] for k in ("categories", "commands", "scenarios", "risks", "disclaimer"))
    errors = []
    check_strings(errors, "ui", d["ui"], check_ui_markup)
    check_strings(errors, "readme", d["readme"], check_readme_markup)
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
        for l in LANGS[1:]:
            g = c.get("gloss", {}).get(l)
            if not g or unsafe(g):
                errors.append(f"{name}: missing or unsafe gloss.{l}")
        for f in ("desc", "use"):
            check_prose(errors, f"{name}.{f}", c.get(f))
        # Translations must mention the same commands, flags and values.
        spans = {l: sorted(set(re.findall(r"`([^`]+)`", c.get("desc", {}).get(l, "")))) for l in LANGS}
        if len({tuple(v) for v in spans.values()}) != 1:
            errors.append(f"{name}.desc: `code` spans differ between languages {spans}")
        if c.get("short"):
            check_prose(errors, f"{name}.short", c["short"])
        if c.get("pick") and not all(c.get("short", {}).get(l) for l in LANGS):
            errors.append(f"{name}: editor's pick needs short in every language")
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
           f"## {t['preview']}", "", t["preview_note"], "",
           f"### [{t['web']} →]({META['site']})", "",
           f"| {t['theme_default']} | {t['theme_matrix']} |", "|---|---|",
           f"| [![{t['theme_default']}](docs/assets/preview-en.png)]({META['site']}?theme=terminal) "
           f"| [![{t['theme_matrix']}](docs/assets/preview-matrix.png)]({META['site']}?theme=matrix) |", "",
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


def page(cats, groups, scens, risks, disc, ui):
    flat = [c for _, rows in groups for c in rows]
    tpl = (ROOT / "site/template.html").read_text(encoding="utf-8")
    dump = lambda x: json.dumps(x, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return (tpl.replace("/*META*/null", dump(META))
               .replace("/*CATS*/[]", dump(cats))
               .replace("/*CMDS*/[]", dump(flat))
               .replace("/*SCENS*/[]", dump(scens))
               .replace("/*RISKS*/[]", dump(risks))
               .replace("/*DISC*/null", dump(disc))
               .replace("/*UI*/null", dump({l: ui[l] for l in LANGS}))
               .replace("/*LANGS*/[]", dump(LANGINFO)))


def social():
    """Link-preview tags for community posts (Open Graph / Twitter)."""
    names = " / ".join(x["name"] for x in LANGINFO)
    desc = f"Every Claude Code slash command explained in {len(LANGINFO)} languages: {names}. Unofficial."
    return "".join(f'<meta {k}="{n}" content="{v}">\n' for k, n, v in (
        ("property", "og:type", "website"),
        ("property", "og:title", "Claude Code Commands · " + names),
        ("property", "og:description", desc),
        ("property", "og:url", META["site"]),
        ("property", "og:image", META["site"] + "assets/social.png"),
        ("property", "og:image:width", "1200"),
        ("property", "og:image:height", "630"),
        ("property", "og:image:alt", "Claude Code Commands: searchable guide in " + str(len(LANGINFO)) + " languages"),
        ("name", "twitter:card", "summary_large_image"),
    )) + links()


# A "/" mark in the theme accent; a data: URL, so the CSP needs nothing new.
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='7' fill='%230b0f0c'/%3E"
           "%3Cpath d='M19.5 6 12.5 26' stroke='%2335e06f' stroke-width='3.4' stroke-linecap='round'/%3E%3C/svg%3E")


def links():
    """Favicon, canonical URL and one alternate per language for search engines."""
    out = [f'<link rel="icon" href="{FAVICON}">', f'<link rel="canonical" href="{META["site"]}">']
    out += [f'<link rel="alternate" hreflang="{x["html"]}" href="{META["site"]}?lang={x["code"]}">' for x in LANGINFO]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{META["site"]}">')
    return "\n".join(out) + "\n"


def not_found(ui):
    """docs/404.html: GitHub Pages serves it for any unknown path."""
    msg = {"en": "Page not found", "ja": "ページが見つかりません", "zh": "找不到页面", "zh-hant": "找不到頁面",
           "ko": "페이지를 찾을 수 없습니다", "ru": "Страница не найдена", "es": "Página no encontrada"}
    css = ("body{margin:0;min-height:100vh;display:grid;place-items:center;background:#0b0f0c;color:#d7e3da;"
           "font:16px/1.6 ui-monospace,SFMono-Regular,Menlo,monospace}main{padding:24px;max-width:36em}"
           "h1{color:#35e06f;font-size:28px;margin:0 0 12px}a{color:#35e06f}ul{padding-left:1.2em}")
    items = "".join(f'<li lang="{x["html"]}">{msg[x["code"]]} · <a href="{META["site"]}?lang={x["code"]}">{ui[x["code"]]["h1"]}</a></li>'
                    for x in LANGINFO)
    body = f'<style>{css}</style>\n<main><h1>/404</h1><ul>{items}</ul></main>'
    return ('<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<meta http-equiv="Content-Security-Policy" content="{csp(body)}">\n'
            f'<meta name="robots" content="noindex">\n<title>404 · Claude Code Commands</title>\n'
            f'<link rel="icon" href="{FAVICON}">\n{body}\n</html>\n')


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
    body = page(cats, groups, scens, d["risks"], d["disclaimer"], d["ui"])
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
    (ROOT / "docs/404.html").write_text(not_found(d["ui"]), encoding="utf-8")
    print(f"OK: {len(cmds)} commands, {len(cats)} categories, {len(scens)} scenarios; wrote {len(LANGS)} READMEs, docs/index.html, dist/artifact.html")
    if placeholder:
        print("Note: repository links use the placeholder OWNER. Run again with --repo OWNER/NAME.")


if __name__ == "__main__":
    main()
