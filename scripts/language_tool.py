#!/usr/bin/env python3
"""Check or merge a new-language file into data/*.json.

A language file (data/i18n/<code>.json) holds every translated string for one
language, keyed by command, category, scenario and risk id; see CONTRIBUTING.md.

Usage:
  python3 scripts/language_tool.py check data/i18n/ko.json   # run all build checks with it added
  python3 scripts/language_tool.py merge data/i18n/ko.json   # write it into data/*.json
"""
import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

DATA = build.ROOT / "data"


def apply(d, langs, x):
    """Return copies of the data and language list with language file x merged in."""
    d, langs = copy.deepcopy(d), copy.deepcopy(langs)
    info = x["language"]
    code = info["code"]
    langs = [l for l in langs if l["code"] != code] + [info]
    by_cmd = x["commands"]
    for c in d["commands"]:
        t = by_cmd.get(c["cmd"], {})
        c["gloss"][code] = t.get("gloss", "")
        c["desc"][code] = t.get("desc", "")
        c["use"][code] = t.get("use", "")
        if "short" in c:
            c["short"][code] = t.get("short", "")
    for cat in d["categories"]:
        t = x["categories"].get(cat["id"], {})
        cat["name"][code], cat["desc"][code] = t.get("name", ""), t.get("desc", "")
    for s in d["scenarios"]:
        s["q"][code] = x["scenarios"].get(s["id"], "")
    for r in d["risks"]:
        t = x["risks"].get(r["id"], {})
        r["name"][code], r["desc"][code] = t.get("name", ""), t.get("desc", "")
    d["disclaimer"][code] = x["disclaimer"]
    d["ui"][code] = x["ui"]
    d["readme"][code] = x["readme"]
    extra = sorted(set(by_cmd) - {c["cmd"] for c in d["commands"]})
    return d, langs, code, extra


def check(path):
    x = json.loads(Path(path).read_text(encoding="utf-8"))
    d, langs, code, extra = apply(build.load(), build.LANGINFO, x)
    build.LANGS = tuple(l["code"] for l in langs)
    errors = [e for e in build.validate(d) if code in e or "differ" in e]
    errors += [f"unknown command in language file: {n}" for n in extra]
    if errors:
        print(f"{len(errors)} problem(s):\n  " + "\n  ".join(errors[:80]))
        sys.exit(1)
    print(f"OK: {code} passes every build check")


def merge(path):
    check(path)
    x = json.loads(Path(path).read_text(encoding="utf-8"))
    d, langs, _, _ = apply(build.load(), build.LANGINFO, x)
    for name in ("commands", "categories", "scenarios", "risks", "disclaimer", "ui", "readme"):
        (DATA / f"{name}.json").write_text(json.dumps(d[name], ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (DATA / "languages.json").write_text(json.dumps(langs, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"Merged {x['language']['code']}; reorder data/languages.json if needed, then run scripts/build.py")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("check", "merge"):
        sys.exit(__doc__)
    {"check": check, "merge": merge}[sys.argv[1]](sys.argv[2])
