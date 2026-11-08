#!/usr/bin/env python3
"""Validate data/*.json and generate one README per language and the web page.

Usage: python3 scripts/build.py [--repo OWNER/NAME]
Outputs: README*.md (see data/languages.json), one docs/ page per language,
         one page per command and language (docs/[lang/]commands/NAME/), docs/404.html, sitemap.xml, robots.txt, llms.txt, llms-full.txt, dist/artifact.html
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
    "checked": "2026-11-09",
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
    return {k: read(f"{k}.json") for k in ("categories", "commands", "scenarios", "risks", "disclaimer", "ui", "readme", "seo")}


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


def check_seo_text(errors, where, text):
    # Plain text only; titles over ~70 and descriptions over ~170 characters get cut in results.
    if UNSAFE.search(text):
        errors.append(f"{where}: plain text only")
    limit = 70 if where.endswith(".title") else 170
    if len(text.replace("{n}", "000")) > limit:
        errors.append(f"{where}: longer than {limit} characters")


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
    check_strings(errors, "seo", d["seo"], check_seo_text)
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
           f"### [{t['web']} →]({page_url(lang)})", "",
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


def only(v, keep):
    """Copy of v with every per-language dict cut down to the languages in keep."""
    if isinstance(v, dict):
        if len(v) > 1 and set(v) <= set(LANGS):
            return {l: only(x, keep) for l, x in v.items() if l in keep}
        return {k: only(x, keep) for k, x in v.items()}
    if isinstance(v, list):
        return [only(x, keep) for x in v]
    return v


def page(cats, groups, scens, risks, disc, ui, keep=None):
    """The page body. keep=("ja", "en") embeds only those languages' text (a published
    language page); None embeds all of them (the self-contained artifact copy)."""
    flat = [c for _, rows in groups for c in rows]
    if keep:
        cats, flat, scens, risks, disc = (only(x, keep) for x in (cats, flat, scens, risks, disc))
    tpl = (ROOT / "site/template.html").read_text(encoding="utf-8")
    dump = lambda x: json.dumps(x, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return (tpl.replace("/*META*/null", dump(META))
               .replace("/*CATS*/[]", dump(cats))
               .replace("/*CMDS*/[]", dump(flat))
               .replace("/*SCENS*/[]", dump(scens))
               .replace("/*RISKS*/[]", dump(risks))
               .replace("/*DISC*/null", dump(disc))
               .replace("/*UI*/null", dump({l: ui[l] for l in LANGS if not keep or l in keep}))
               .replace("/*LANGS*/[]", dump(LANGINFO))
               .replace("/*TITLES*/{}", dump({l: seo_text(l, "title", flat) for l in LANGS})))


SEO = _read("seo.json")  # replaced by validated data in main()
HTML_ESC = str.maketrans({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"})


def esc(text):
    return text.translate(HTML_ESC)


def code_html(text):
    """Prose with `code` spans as HTML (prose is already validated free of markup)."""
    nw = lambda c: ('<code class="nw">' if len(c) <= 24 else "<code>") + c + "</code>"  # as md() in the page
    return re.sub(r"`([^`]+)`", lambda m: nw(m.group(1)), esc(text))


def plain(text):
    return text.replace("`", "")


def page_path(lang):
    """URL path of a language's page: English at the root, others in /ja/, /zh-cn/ ..."""
    return "" if lang == "en" else next(x["html"] for x in LANGINFO if x["code"] == lang).lower() + "/"


def page_url(lang):
    return META["site"] + page_path(lang)


def cmd_path(lang, c):
    """URL path of one command's page: commands/compact/ (English), ja/commands/compact/ ..."""
    return page_path(lang) + "commands/" + slug(c) + "/"


def cmd_url(lang, c):
    return META["site"] + cmd_path(lang, c)


def live_count(cmds):
    return sum(c["kind"] != "removed" for c in cmds)


def seo_text(lang, key, cmds):
    return SEO[lang][key].replace("{n}", str(live_count(cmds)))


# A "/" mark in the theme accent; a data: URL, so the CSP needs nothing new.
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='7' fill='%230b0f0c'/%3E"
           "%3Cpath d='M19.5 6 12.5 26' stroke='%2335e06f' stroke-width='3.4' stroke-linecap='round'/%3E%3C/svg%3E")


def head(lang, cmds):
    """Per-language link-preview tags, canonical URL and hreflang alternates."""
    info = next(x for x in LANGINFO if x["code"] == lang)
    title, desc = seo_text(lang, "title", cmds), seo_text(lang, "description", cmds)
    locale = lambda x: x["html"].replace("-", "_")
    metas = [
        ("property", "og:type", "website"),
        ("property", "og:site_name", "Claude Code Commands"),
        ("property", "og:title", title),
        ("property", "og:description", desc),
        ("property", "og:url", page_url(lang)),
        ("property", "og:locale", locale(info)),
        *[("property", "og:locale:alternate", locale(x)) for x in LANGINFO if x is not info],
        ("property", "og:image", META["site"] + "assets/social.png"),
        ("property", "og:image:width", "1200"),
        ("property", "og:image:height", "630"),
        ("property", "og:image:alt", "Claude Code Commands: searchable guide in " + str(len(LANGINFO)) + " languages"),
        ("name", "twitter:card", "summary_large_image"),
        ("name", "twitter:title", title),
        ("name", "twitter:description", desc),
        ("name", "robots", "index, follow, max-snippet:-1, max-image-preview:large"),
    ]
    out = [f'<meta {k}="{n}" content="{esc(v)}">' for k, n, v in metas]
    out += [f'<link rel="icon" href="{FAVICON}">', f'<link rel="canonical" href="{page_url(lang)}">']
    out += [f'<link rel="alternate" hreflang="{x["html"]}" href="{page_url(x["code"])}">' for x in LANGINFO]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{META["site"]}">')
    return "\n".join(out) + "\n"


def slug(c):
    return c["cmd"][1:].replace(" ", "-")


def first_sentence(text):
    m = re.match(r"(.+?[.。！？!?])(\s|$)", text)
    return (m.group(1) if m else text).strip()


def json_ld(lang, groups, scens, ui):
    """schema.org graph: the site, this page, every command as a DefinedTerm, scenarios as an FAQ."""
    info = next(x for x in LANGINFO if x["code"] == lang)
    url, cmds = page_url(lang), [c for _, rows in groups for c in rows]
    by_cmd = {c["cmd"]: c for c in cmds}
    org = {"@type": "Organization", "@id": META["site"] + "#org", "name": META["repo"].split("/")[-2],
           "url": META["repo"].rsplit("/", 1)[0]}
    graph = [
        org,
        {"@type": "WebSite", "@id": META["site"] + "#website", "url": META["site"], "name": "Claude Code Commands",
         "inLanguage": [x["html"] for x in LANGINFO], "publisher": {"@id": org["@id"]}},
        {"@type": "TechArticle", "@id": url + "#article", "url": url, "mainEntityOfPage": url,
         "headline": seo_text(lang, "title", cmds), "description": seo_text(lang, "description", cmds),
         "inLanguage": info["html"], "dateModified": META["checked"], "image": META["site"] + "assets/social.png",
         "isPartOf": {"@id": META["site"] + "#website"}, "author": {"@id": org["@id"]}, "publisher": {"@id": org["@id"]},
         "license": "https://creativecommons.org/licenses/by/4.0/", "isBasedOn": META["source"],
         "about": {"@type": "SoftwareApplication", "name": "Claude Code", "applicationCategory": "DeveloperApplication",
                   "url": "https://code.claude.com/"},
         "hasPart": {"@id": url + "#commands"}},
        {"@type": "DefinedTermSet", "@id": url + "#commands", "name": ui[lang]["h1"], "inLanguage": info["html"],
         "hasDefinedTerm": [{"@type": "DefinedTerm", "name": c["cmd"], "termCode": c["cmd"],
                             "description": plain(c["desc"][lang]), "url": cmd_url(lang, c)}
                            for c in cmds if c["kind"] != "removed"]},
        {"@type": "FAQPage", "@id": url + "#faq", "inLanguage": info["html"],
         "mainEntity": [{"@type": "Question", "name": s["q"][lang],
                         "acceptedAnswer": {"@type": "Answer", "text": " ".join(
                             f"{c}: {plain(first_sentence(by_cmd[c]['desc'][lang]))}" for c in s["cmds"] if c in by_cmd)}}
                        for s in scens]},
    ]
    data = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    return '<script type="application/ld+json">' + data.replace("</", "<\\/") + "</script>\n"


def prerender(lang, groups, scens, ui):
    """Static HTML of the list and scenarios, so crawlers and AI tools that do not run
    JavaScript still read every command. The page script replaces it on load."""
    t = ui[lang]
    secs = []
    for cg, rows in groups:
        arts = "".join(
            f'<article id="{lang}-{slug(c)}"><h3><a href="commands/{slug(c)}/"><code>{esc(c["cmd"])}</code></a>'
            + (f' <code>{esc(c["args"])}</code>' if c.get("args") else "")
            + (f' <small>{esc(t["removed"])}</small>' if c["kind"] == "removed" else "")
            + f'</h3><p>{code_html(c["desc"][lang])}</p><p><b>{esc(t["use"])}:</b> {code_html(c["use"][lang])}</p></article>'
            for c in rows)
        secs.append(f'<section><h2>{esc(cg["name"][lang])}</h2><p>{esc(cg["desc"][lang])}</p>{arts}</section>')
    scen = "<ul>" + "".join(f'<li>{esc(s["q"][lang])}: {esc(" ".join(s["cmds"]))}</li>' for s in scens) + "</ul>"
    return "".join(secs), scen


def localize(body, lang, cmds, groups, scens, ui):
    """Fill one language's title, description, hero text and pre-rendered content into the page."""
    t, (lst, scen) = ui[lang], prerender(lang, groups, scens, ui)
    swaps = [
        (re.compile(r"<title>.*?</title>"), f"<title>{esc(seo_text(lang, 'title', cmds))}</title>"),
        (re.compile(r'<meta name="description" content="[^"]*">'),
         f'<meta name="description" content="{esc(seo_text(lang, "description", cmds))}">'),
        ("/*PAGELANG*/null", json.dumps(lang) if lang != "en" else "null"),  # the root keeps a visitor's saved choice
        ('<span class="badge" id="badge"></span>', f'<span class="badge" id="badge">{esc(t["badge"])}</span>'),
        ('<h2 id="scen-h"></h2><p id="scen-d"></p>', f'<h2 id="scen-h">{esc(t["scen"])}</h2><p id="scen-d">{esc(t["scenD"])}</p>'),
        ('<h2 id="safety-h"></h2><p id="safety-d"></p>', f'<h2 id="safety-h">{esc(t["safety"])}</h2><p id="safety-d">{esc(t["safetyD"])}</p>'),
        ('<span id="h1"></span>', f'<span id="h1">{esc(t["h1"])}</span>'),
        (re.compile(r'<noscript><p class="noscript">.*?</p></noscript>'),
         f'<noscript><p class="noscript">{esc(t["noscript"])}</p></noscript>'),
        ('<p class="lead" id="lead"></p>', f'<p class="lead" id="lead">{esc(t["lead"])}</p>'),
        ('<main id="list" tabindex="-1"></main>', f'<main id="list" tabindex="-1">{lst}</main>'),
        ('<div class="scens" id="scens"></div>', f'<div class="scens" id="scens">{scen}</div>'),
    ]
    for old, new in swaps:
        if isinstance(old, str):
            assert old in body, old
            body = body.replace(old, new, 1)
        else:
            body, n = old.subn(lambda _m, new=new: new, body, count=1)
            assert n == 1, old.pattern
    return body


def sitemap(cmds):
    def block(url_of):
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{x["html"]}" href="{url_of(x["code"])}"/>' for x in LANGINFO)
        alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{url_of("en")}"/>'
        return "".join(f'<url><loc>{url_of(x["code"])}</loc><lastmod>{META["checked"]}</lastmod>{alts}</url>\n' for x in LANGINFO)
    urls = block(page_url) + "".join(block(lambda l, c=c: cmd_url(l, c)) for c in cmds)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + urls + "</urlset>\n")


def llms_txt(cmds):
    """llms.txt (llmstxt.org): a short map of the site for AI assistants and answer engines."""
    raw = META["repo"].replace("https://github.com/", "https://raw.githubusercontent.com/") + "/main/"
    lines = [
        "# Claude Code Commands",
        "",
        f"> Unofficial, plain-language guide to all {live_count(cmds)} Claude Code slash commands, in "
        f"{len(LANGINFO)} languages. For each command: what it does, its best use, and safety notes. "
        f"Checked against the official commands reference ({META['source']}) on {META['checked']}; "
        "where they differ, the official docs win.",
        "",
        "## Pages",
        "",
        *[f"- [{x['name']}]({page_url(x['code'])}): {SEO[x['code']]['title'].replace('{n}', str(live_count(cmds)))}" for x in LANGINFO],
        "",
        "## Commands (English; each page links its other languages)",
        "",
        *[f"- [{c['cmd']}]({cmd_url('en', c)}): {plain(first_sentence(c['desc']['en']))}"
          + (" (removed)" if c["kind"] == "removed" else "") for c in cmds],
        "",
        "## Full text (Markdown)",
        "",
        f"- [All commands, English]({META['site']}llms-full.txt): every command with description and best use",
        *[f"- [{x['name']}]({raw}{x['readme']})" for x in LANGINFO],
        "",
        "## Optional",
        "",
        f"- [Source data, JSON]({raw}data/commands.json)",
        f"- [Repository]({META['repo']}): content CC BY 4.0, code MIT",
        "",
    ]
    return "\n".join(lines)


def llms_full(groups, cmds, ui):
    t = ui["en"]
    out = [f"# Claude Code Commands: all {live_count(cmds)} slash commands in plain English", "",
           f"Unofficial guide. Source: {META['source']} (checked {META['checked']}). Site: {META['site']}", ""]
    for cg, rows in groups:
        out += [f"## {cg['name']['en']}", "", cg["desc"]["en"], ""]
        for c in rows:
            name = c["cmd"] + (f" {c['args']}" if c.get("args") else "")
            out += [f"### {name}" + (" (removed)" if c["kind"] == "removed" else ""), "", c["desc"]["en"], "",
                    f"{t['use']}: {c['use']['en']}", "", f"Page: {cmd_url('en', c)}", ""]
            if c.get("aliases"):
                out += [f"{t['alias']}: {', '.join(c['aliases'])}", ""]
    return "\n".join(out)


def not_found(ui):
    """docs/404.html: GitHub Pages serves it for any unknown path."""
    msg = {"en": "Page not found", "ja": "ページが見つかりません", "zh": "找不到页面", "zh-hant": "找不到頁面",
           "ko": "페이지를 찾을 수 없습니다", "ru": "Страница не найдена", "es": "Página no encontrada"}
    css = ("body{margin:0;min-height:100vh;display:grid;place-items:center;background:#0b0f0c;color:#d7e3da;"
           "font:16px/1.6 ui-monospace,SFMono-Regular,Menlo,monospace}main{padding:24px;max-width:36em}"
           "h1{color:#35e06f;font-size:28px;margin:0 0 12px}a{color:#35e06f}ul{padding-left:1.2em}")
    items = "".join(f'<li lang="{x["html"]}">{msg[x["code"]]} · <a href="{page_url(x["code"])}">{ui[x["code"]]["h1"]}</a></li>'
                    for x in LANGINFO)
    body = f'<style>{css}</style>\n<main><h1>/404</h1><ul>{items}</ul></main>'
    return ('<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<meta http-equiv="Content-Security-Policy" content="{csp(body)}">\n'
            f'<meta name="robots" content="noindex">\n<title>404 · Claude Code Commands</title>\n'
            f'<link rel="icon" href="{FAVICON}">\n{body}\n</html>\n')


# --- one page per command ---------------------------------------------------------

CMD_CSS = """
*{box-sizing:border-box}
html{--body-font:var(--font-en)}
html[lang="ja"]{--body-font:var(--font-ja)}
html[lang="zh-CN"]{--body-font:var(--font-zh)}
html[lang="zh-Hant"]{--body-font:var(--font-tc)}
html[lang="ko"]{--body-font:var(--font-ko)}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.75 var(--body-font);-webkit-text-size-adjust:100%}
a{color:var(--accent);text-underline-offset:3px}
a:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:4px}
code{font-family:var(--font-mono);font-size:.9em;background:var(--surface-2);border:1px solid var(--line);padding:0 5px;border-radius:5px;overflow-wrap:anywhere}
code.nw{white-space:nowrap}
.top{background:var(--hero);color:var(--hero-ink);border-bottom:1px solid var(--hero-line)}
.in{max-width:820px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left));padding-right:max(16px,env(safe-area-inset-right))}
.top .in{display:flex;flex-wrap:wrap;align-items:center;gap:8px 16px;padding-top:12px;padding-bottom:12px}
.brand{color:var(--phos);font:700 15px/1.4 var(--font-mono);text-decoration:none}
.brand span{color:var(--hero-muted);font-weight:500}
.langs{margin:0 0 0 auto;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:2px 12px;font-size:13px}
.langs a{font-family:var(--font-en);color:var(--hero-muted);text-decoration:none;display:inline-block;padding:4px 0}
.langs a:hover{color:var(--hero-ink)}
.langs a[aria-current]{color:var(--phos);font-weight:600}
main{padding-top:20px;padding-bottom:28px}
.crumb{margin:0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:4px;font-size:13px;color:var(--muted)}
.crumb li+li::before{content:"›";margin-right:4px}
.crumb a{color:var(--muted)}
h1{font:700 clamp(30px,7vw,44px)/1.15 var(--font-mono);margin:14px 0 4px;overflow-wrap:anywhere}
h1 .args{display:block;font-size:.45em;font-weight:500;color:var(--muted);margin-top:6px}
.lead{font-size:18px;margin:8px 0 0}
.gloss{font-size:14px;color:var(--muted);margin:6px 0 0}
.tags{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 0}
.tag{font-size:12.5px;line-height:1.6;padding:1px 9px;border-radius:999px;background:var(--surface-2);color:var(--muted)}
.tag.pick{background:var(--star-soft);color:var(--star)}
.tag.skill,.tag.workflow{background:var(--info-soft);color:var(--info)}
.tag.removed{background:var(--r-perms-bg);color:var(--r-perms)}
/*RISKTAGS*/
.box{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin:16px 0 0;box-shadow:var(--shadow)}
.box h2{font-size:13px;letter-spacing:.04em;text-transform:uppercase;margin:0 0 4px;color:var(--accent)}
.box p{margin:0}
.box.warn{border-left:4px solid var(--r-perms)}
.risk+.risk{margin-top:8px}
.list{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.list a{font:600 15px var(--font-mono);text-decoration:none}
.list a:hover{text-decoration:underline}
.list small{display:block;color:var(--muted);font-size:14px;line-height:1.55}
.pn{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin:22px 0 0}
.pn a{display:block;padding:10px 14px;border:1px solid var(--line);border-radius:10px;background:var(--surface);font-family:var(--font-mono);text-decoration:none;overflow-wrap:anywhere}
.pn a:hover{border-color:var(--accent)}
.pn .next{text-align:right;grid-column:2}
.all{display:inline-block;margin-top:20px;font-weight:600}
footer{border-top:1px solid var(--line);margin-top:8px;padding-top:16px;padding-bottom:40px;font-size:13px;color:var(--muted)}
footer a{color:var(--muted)}
footer p{margin:0 0 8px}
"""


def theme_script():
    """The page's own skin loader, so a command page shows the theme the visitor picked."""
    tpl = (ROOT / "site/template.html").read_text(encoding="utf-8")
    return re.search(r"<script>\(function\(\)\{document\.documentElement\.className.*?</script>", tpl, re.S).group(0)


def command_css(risks):
    """docs/assets/command.css: the theme palette of the main page plus the command-page layout.
    One shared file, so the browser caches it across all command pages."""
    tpl = (ROOT / "site/template.html").read_text(encoding="utf-8")
    style = re.search(r"<style>(.*?)</style>", tpl, re.S).group(1)
    palette = style[style.index(":root{"):style.index("\n.rain{")]
    palette = re.sub(r"\n:root\[data-skin=\"[a-z]+\"\] [^{\n]*\{[^}\n]*\}", "", palette)  # page-specific flourishes
    tags = "\n".join(f".tag.r-{r['id']}{{background:var(--r-{r['id']}-bg);color:var(--r-{r['id']})}}" for r in risks)
    return "/* Generated by scripts/build.py from site/template.html. */\n" + palette.strip() + "\n" + CMD_CSS.replace("/*RISKTAGS*/", tags)


def cmd_head_title(lang, c):
    base = SEO[lang]["cmd_title"].replace("{cmd}", c["cmd"])
    extra = (c.get("short") or {}).get(lang) or plain(first_sentence(c["desc"][lang])).rstrip(".。")
    sep = "｜" if lang in ("ja", "zh", "zh-hant") else " – "
    for title in (base + sep + extra, c["cmd"] + sep + extra + sep + "Claude Code", base):
        if len(title) <= 70:
            return title


def clip(text, n=160):
    text = plain(text)
    return text if len(text) <= n else text[:n - 1].rsplit(" ", 1)[0].rstrip(",，、;；") + "…" if " " in text[:n] else text[:n - 1] + "…"


def command_page(lang, c, i, flat, cats, scens, risks, ui, theme):
    """Static HTML for one command in one language. No script but the theme loader."""
    t, info = ui[lang], next(x for x in LANGINFO if x["code"] == lang)
    cat = next(cg for cg in cats if cg["id"] == c["cat"])
    by_cmd = {x["cmd"]: x for x in flat}
    home = "../../"  # the language page, relative so local previews stay local
    link = lambda x: f"../{slug(x)}/"
    summary = lambda x: (x.get("short") or {}).get(lang) or plain(first_sentence(x["desc"][lang]))
    title = cmd_head_title(lang, c)
    desc = clip(((c.get("short") or {}).get(lang, "") + " " if c.get("short") else "") + c["desc"][lang])
    url = cmd_url(lang, c)
    risk_by = {r["id"]: r for r in risks}

    tags = []
    if c["pick"]:
        tags.append(f'<span class="tag pick">{esc(t["pick"])}</span>')
    if c["kind"] in ("skill", "workflow"):
        tags.append(f'<span class="tag {c["kind"]}">{esc(t[c["kind"]])}</span>')
    if c["kind"] == "removed":
        tags.append(f'<span class="tag removed">{esc(t["removedIn"].replace("{v}", c["removedIn"]) if c.get("removedIn") else t["removed"])}</span>')
    if c.get("since"):
        tags.append(f'<span class="tag">{esc(t["since"].replace("{v}", c["since"]))}</span>')
    tags += [f'<span class="tag r-{r}">{esc(risk_by[r]["icon"] + " " + risk_by[r]["name"][lang])}</span>' for r in c.get("risk", [])]

    parts = [f'<p class="lead">{esc(c["short"][lang])}</p>' if c.get("short") else "",
             f'<p class="gloss">{esc(t["word"])} <b>{esc(c["word"])}</b> ＝ {esc(c["gloss"][lang])}</p>' if lang != "en" else "",
             f'<div class="tags">{"".join(tags)}</div>' if tags else "",
             f'<section class="box"><p>{code_html(c["desc"][lang])}</p></section>',
             f'<section class="box"><h2>{esc(t["use"])}</h2><p>{code_html(c["use"][lang])}</p></section>']
    if c["aliases"]:
        parts.append(f'<section class="box"><h2>{esc(t["alias"])}</h2><p>{" · ".join(f"<code>{esc(a)}</code>" for a in c["aliases"])}</p></section>')
    if c.get("risk"):
        parts.append(f'<section class="box warn"><h2>{esc(t["safety"])}</h2>' + "".join(
            f'<p class="risk"><b>{esc(risk_by[r]["icon"] + " " + risk_by[r]["name"][lang])}</b>: {code_html(risk_by[r]["desc"][lang])}</p>'
            for r in c["risk"]) + "</section>")
    seen = [s for s in scens if c["cmd"] in s["cmds"]]
    if seen:
        parts.append(f'<section class="box"><h2>{esc(t["inScen"])}</h2><ul class="list">' + "".join(
            f'<li>{esc(s["q"][lang])}<small>' + " → ".join(
                f'<code>{esc(n)}</code>' if n == c["cmd"] else f'<a href="{link(by_cmd[n])}">{esc(n)}</a>' for n in s["cmds"])
            + "</small></li>" for s in seen) + "</ul></section>")
    rel = [x for x in flat if x["cat"] == c["cat"] and x is not c and (x["kind"] != "removed" or c["kind"] == "removed")][:8]
    if rel:
        parts.append(f'<section class="box"><h2>{esc(t["related"])} · {esc(cat["name"][lang])}</h2><ul class="list">' + "".join(
            f'<li><a href="{link(x)}">{esc(x["cmd"])}</a><small>{esc(summary(x))}</small></li>' for x in rel) + "</ul></section>")
    prev, nxt = (flat[i - 1] if i else None), (flat[i + 1] if i + 1 < len(flat) else None)
    parts.append('<nav class="pn" aria-label="' + esc(t["nav"]) + '">'
                 + (f'<a class="prev" href="{link(prev)}" rel="prev">← {esc(prev["cmd"])}</a>' if prev else "")
                 + (f'<a class="next" href="{link(nxt)}" rel="next">{esc(nxt["cmd"])} →</a>' if nxt else "") + "</nav>")
    parts.append(f'<a class="all" href="{home}#{lang}-{slug(c)}">← {esc(t["allCmds"])}</a>')

    langs = "".join(
        f'<li><a href="../../{"../" if lang != "en" else ""}{cmd_path(x["code"], c)}" lang="{x["html"]}" hreflang="{x["html"]}"'
        + (' aria-current="page"' if x is info else "") + f'>{esc(x["name"])}</a></li>' for x in LANGINFO)
    foot = (t["foot"].replace("{sourceLink}", f'<a href="{esc(META["source"])}" rel="noopener noreferrer">{esc(META["source"])}</a>')
                     .replace("{repoLink}", f'<a href="{esc(META["repo"])}" rel="noopener noreferrer">{esc(META["repo"])}</a>')
                     .replace("{checked}", META["checked"]))
    body = (f'{theme}\n<link rel="stylesheet" href="{"../" * (3 if lang != "en" else 2)}assets/command.css">\n'
            f'<header class="top"><div class="in"><a class="brand" href="{home}">/cc <span>· {esc(t["h1"])}</span></a>'
            f'<ul class="langs" aria-label="{esc(t["langLabel"])}">{langs}</ul></div></header>\n'
            f'<main class="in"><ol class="crumb"><li><a href="{home}">{esc(t["home"])}</a></li>'
            f'<li><a href="{home}#{lang}-{slug(c)}">{esc(cat["name"][lang])}</a></li><li aria-current="page">{esc(c["cmd"])}</li></ol>'
            f'<h1>{esc(c["cmd"])}' + (f'<span class="args">{esc(c["args"])}</span>' if c.get("args") else "") + "</h1>"
            + "".join(parts) + "</main>\n"
            f'<footer class="in">{foot}</footer>')

    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "TechArticle", "@id": url + "#article", "url": url, "headline": title, "description": desc,
         "inLanguage": info["html"], "dateModified": META["checked"], "image": META["site"] + "assets/social.png",
         "isPartOf": {"@id": META["site"] + "#website"}, "author": {"@id": META["site"] + "#org"},
         "license": "https://creativecommons.org/licenses/by/4.0/", "isBasedOn": META["source"],
         "about": {"@type": "DefinedTerm", "name": c["cmd"], "termCode": c["cmd"], "description": plain(c["desc"][lang]),
                   "inDefinedTermSet": page_url(lang) + "#commands"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": t["h1"], "item": page_url(lang)},
            {"@type": "ListItem", "position": 2, "name": cat["name"][lang], "item": page_url(lang) + f"#{lang}-{slug(c)}"},
            {"@type": "ListItem", "position": 3, "name": c["cmd"], "item": url}]}]}
    metas = [("property", "og:type", "article"), ("property", "og:site_name", "Claude Code Commands"),
             ("property", "og:title", title), ("property", "og:description", desc), ("property", "og:url", url),
             ("property", "og:locale", info["html"].replace("-", "_")),
             ("property", "og:image", META["site"] + "assets/social.png"),
             ("property", "og:image:width", "1200"), ("property", "og:image:height", "630"),
             ("name", "twitter:card", "summary_large_image"), ("name", "twitter:title", title),
             ("name", "twitter:description", desc), ("name", "robots", "index, follow, max-snippet:-1")]
    head_tags = "\n".join(
        [f'<title>{esc(title)}</title>', f'<meta name="description" content="{esc(desc)}">',
         '<meta name="referrer" content="no-referrer">',
         *[f'<meta {k}="{n}" content="{esc(v)}">' for k, n, v in metas],
         f'<link rel="icon" href="{FAVICON}">', f'<link rel="canonical" href="{url}">',
         *[f'<link rel="alternate" hreflang="{x["html"]}" href="{cmd_url(x["code"], c)}">' for x in LANGINFO],
         f'<link rel="alternate" hreflang="x-default" href="{cmd_url("en", c)}">',
         '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>"])
    return (f'<!doctype html>\n<html lang="{info["html"]}">\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<meta http-equiv="Content-Security-Policy" content="{csp(body, style_self=True)}">\n'
            f"{head_tags}\n{body}\n</html>\n")


def csp(body, style_self=False):
    """Content-Security-Policy that allows only this page's own inline style and script."""
    h = lambda src: "'sha256-" + base64.b64encode(hashlib.sha256(src.encode("utf-8")).digest()).decode() + "'"
    styles = re.findall(r"<style>(.*?)</style>", body, re.S)
    scripts = re.findall(r"<script>(.*?)</script>", body, re.S)
    style = "'self'" if style_self else " ".join(map(h, styles))  # command pages share one stylesheet
    return ("default-src 'none'; img-src 'self' data:; "
            f"style-src {style}; script-src {' '.join(map(h, scripts))}; "
            "base-uri 'none'; form-action 'none'")


def repo_meta(arg):
    """Resolve OWNER/NAME from --repo, else repo.txt, else a placeholder; the site address
    comes from docs/CNAME when the site has a custom domain."""
    if arg:
        if not re.fullmatch(r"[\w.-]+/[\w.-]+", arg):
            sys.exit("--repo must look like OWNER/NAME")
        REPO_FILE.write_text(arg + "\n", encoding="utf-8")
    slug = arg or (REPO_FILE.read_text(encoding="utf-8").strip() if REPO_FILE.exists() else "OWNER/claude-code-commands-i18n")
    owner, name = slug.split("/")
    META["repo"] = f"https://github.com/{slug}"
    META["site"] = f"https://{owner.lower()}.github.io/{name}/"
    cname = ROOT / "docs/CNAME"  # a custom domain for GitHub Pages, e.g. commands.example.com
    if cname.exists():
        domain = cname.read_text(encoding="utf-8").strip().lower()
        if not re.fullmatch(r"[a-z0-9-]+(\.[a-z0-9-]+)+", domain):
            sys.exit("docs/CNAME must hold one domain name")
        META["site"] = f"https://{domain}/"
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
    flat_cmds = [c for _, rows in groups for c in rows]
    if len({slug(c) for c in cmds}) != len(cmds):
        sys.exit("Two commands share a page name (slug)")
    SEO.update(d["seo"])
    for lang in LANGS:
        (ROOT / T[lang]["file"]).write_text(readme(lang, cats, groups, scens, d["risks"], d["disclaimer"]), encoding="utf-8")
    body = page(cats, groups, scens, d["risks"], d["disclaimer"], d["ui"])  # all languages
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "docs").mkdir(exist_ok=True)
    # The artifact host supplies its own document skeleton; GitHub Pages needs a full one.
    (ROOT / "dist/artifact.html").write_text(localize(body, "en", cmds, groups, scens, d["ui"]), encoding="utf-8")
    for x in LANGINFO:
        own = page(cats, groups, scens, d["risks"], d["disclaimer"], d["ui"], keep=(x["code"], "en"))
        lb = localize(own, x["code"], cmds, groups, scens, d["ui"])
        out = ROOT / "docs" / page_path(x["code"]) / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(
            f'<!doctype html>\n<html lang="{x["html"]}">\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<meta http-equiv="Content-Security-Policy" content="{csp(lb)}">\n'
            + head(x["code"], cmds) + json_ld(x["code"], groups, scens, d["ui"])
            + lb + "\n</html>\n", encoding="utf-8")
    theme = theme_script()
    (ROOT / "docs/assets/command.css").write_text(command_css(d["risks"]), encoding="utf-8")
    for x in LANGINFO:
        root = ROOT / "docs" / page_path(x["code"]) / "commands"
        for old in root.glob("*/index.html") if root.exists() else []:  # a renamed or dropped command leaves no stale page
            old.unlink()
            old.parent.rmdir()
        for i, c in enumerate(flat_cmds):
            out = ROOT / "docs" / cmd_path(x["code"], c) / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(command_page(x["code"], c, i, flat_cmds, cats, scens, d["risks"], d["ui"], theme), encoding="utf-8")
    (ROOT / "docs/404.html").write_text(not_found(d["ui"]), encoding="utf-8")
    (ROOT / "docs/sitemap.xml").write_text(sitemap(flat_cmds), encoding="utf-8")
    (ROOT / "docs/robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {META['site']}sitemap.xml\n", encoding="utf-8")
    (ROOT / "docs/llms.txt").write_text(llms_txt(flat_cmds), encoding="utf-8")
    (ROOT / "docs/llms-full.txt").write_text(llms_full(groups, cmds, d["ui"]), encoding="utf-8")
    print(f"OK: {len(cmds)} commands, {len(cats)} categories, {len(scens)} scenarios; wrote {len(LANGS)} READMEs, {len(LANGS)} pages, {len(LANGS) * len(cmds)} command pages, sitemap, llms.txt, dist/artifact.html")
    if placeholder:
        print("Note: repository links use the placeholder OWNER. Run again with --repo OWNER/NAME.")


if __name__ == "__main__":
    main()
