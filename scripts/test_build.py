#!/usr/bin/env python3
"""Tests for the build: data validity, injection guards and generated output.

Usage: python3 scripts/test_build.py
"""
import copy
import json
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

ROOT = build.ROOT


class DataTests(unittest.TestCase):
    def setUp(self):
        self.d = build.load()

    def test_real_data_is_valid(self):
        self.assertEqual(build.validate(self.d), [])

    def test_every_pick_has_a_summary(self):
        for c in self.d["commands"]:
            if c["pick"]:
                self.assertTrue(all(c["short"][l] for l in build.LANGS), c["cmd"])

    def test_scenarios_only_use_known_commands(self):
        names = {c["cmd"] for c in self.d["commands"]}
        for s in self.d["scenarios"]:
            self.assertTrue(set(s["cmds"]) <= names, s["id"])


class GuardTests(unittest.TestCase):
    def setUp(self):
        self.d = build.load()

    def broken(self, mutate):
        d = copy.deepcopy(self.d)
        mutate(d)
        return build.validate(d)

    def test_unsafe_text_is_detected(self):
        for bad in ["<img src=x onerror=alert(1)>", "[x](https://evil.example)", "see https://evil.example", "javascript:alert(1)"]:
            self.assertTrue(build.unsafe(bad), bad)
        self.assertFalse(build.unsafe("argument `<path>` is required"))

    def test_html_in_description_fails_the_build(self):
        errs = self.broken(lambda d: d["commands"][0]["desc"].__setitem__("ja", "<script>alert(1)</script>"))
        self.assertTrue(any("not allowed" in e for e in errs))

    def test_missing_translation_fails_the_build(self):
        errs = self.broken(lambda d: d["commands"][0]["use"].pop("ja"))
        self.assertTrue(any("missing ja" in e for e in errs))

    def test_translation_drift_fails_the_build(self):
        errs = self.broken(lambda d: d["commands"][0]["desc"].__setitem__("en", d["commands"][0]["desc"]["en"] + " Also `--new-flag`."))
        self.assertTrue(any("differ between languages" in e for e in errs))

    def test_bad_command_name_fails_the_build(self):
        errs = self.broken(lambda d: d["commands"][0].__setitem__("cmd", "/Bad<Name>"))
        self.assertTrue(any("bad command name" in e for e in errs))

    def test_unknown_risk_fails_the_build(self):
        errs = self.broken(lambda d: d["commands"][0].__setitem__("risk", ["nuclear"]))
        self.assertTrue(any("unknown risk" in e for e in errs))


class OutputTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        build.repo_meta(None)  # fills META["site"] from repo.txt, as the build does
        cls.page = (ROOT / "docs/index.html").read_text(encoding="utf-8")
        cls.readmes = {l: (ROOT / build.T[l]["file"]).read_text(encoding="utf-8") for l in build.LANGS}
        cls.cmds = json.loads((ROOT / "data/commands.json").read_text(encoding="utf-8"))

    def test_csp_hashes_match_inline_code(self):
        csp = re.search(r'http-equiv="Content-Security-Policy" content="([^"]+)"', self.page).group(1)
        self.assertEqual(csp, build.csp(self.page))
        self.assertIn("default-src 'none'", csp)

    def test_page_loads_nothing_from_other_sites(self):
        for tag in re.findall(r"<(?:script|link|img|iframe)\b[^>]*>", self.page):
            if re.search(r'rel="(canonical|alternate)"', tag):
                self.assertRegex(tag, r'href="https://[\w-]+\.github\.io/', tag)  # metadata only, never fetched
                continue
            self.assertNotRegex(tag, r"(src|href)=\"https?:", tag)

    def test_phone_layout_cannot_overflow_sideways(self):
        # A 1fr column grows to its widest child, and contain-intrinsic-size with one
        # length also sets a placeholder width; either one made phones scroll sideways.
        self.assertNotRegex(self.page, r"grid-template-columns:1fr[;}]")
        self.assertNotIn("contain-intrinsic-size:", self.page)

    def test_404_page_is_built_with_its_own_csp(self):
        page = (ROOT / "docs/404.html").read_text(encoding="utf-8")
        self.assertIn("default-src 'none'", page)
        self.assertEqual(len(re.findall(r'<li lang=', page)), len(build.LANGINFO))

    # --- search engines and AI answer engines -------------------------------------

    def lang_pages(self):
        for x in build.LANGINFO:
            yield x, (ROOT / "docs" / build.page_path(x["code"]) / "index.html").read_text(encoding="utf-8")

    def test_every_language_has_its_own_page_with_its_own_canonical(self):
        for x, page in self.lang_pages():
            self.assertIn(f'<html lang="{x["html"]}">', page)
            canon = re.search(r'<link rel="canonical" href="([^"]+)">', page).group(1)
            self.assertEqual(canon, build.page_url(x["code"]))
            # hreflang must be reciprocal: every page lists every language plus x-default.
            self.assertEqual(len(re.findall(r'rel="alternate" hreflang=', page)), len(build.LANGINFO) + 1)
            csp = re.search(r'http-equiv="Content-Security-Policy" content="([^"]+)"', page).group(1)
            self.assertEqual(csp, build.csp(page), x["code"])

    def test_pages_are_readable_without_javascript(self):
        for x, page in self.lang_pages():
            main = re.search(r'<main id="list"[^>]*>(.*?)</main>', page, re.S).group(1)
            for c in self.cmds:
                self.assertIn(f"<code>{c['cmd']}</code>", main, f"{c['cmd']} not pre-rendered on {x['code']}")
            self.assertRegex(page, r'<span id="h1">[^<]+</span>')

    def test_structured_data_parses_and_covers_every_command(self):
        live = {c["cmd"] for c in self.cmds if c["kind"] != "removed"}
        for x, page in self.lang_pages():
            blob = re.search(r'<script type="application/ld\+json">(.*?)</script>', page, re.S).group(1)
            graph = {n["@type"]: n for n in json.loads(blob.replace("<\\/", "</"))["@graph"]}
            self.assertEqual({t["name"] for t in graph["DefinedTermSet"]["hasDefinedTerm"]}, live)
            self.assertEqual(len(graph["FAQPage"]["mainEntity"]), len(json.loads((ROOT / "data/scenarios.json").read_text())))
            self.assertEqual(graph["TechArticle"]["inLanguage"], x["html"])

    def test_each_page_embeds_only_its_language_and_english(self):
        ui = json.loads((ROOT / "data/ui.json").read_text(encoding="utf-8"))
        for x, page in self.lang_pages():
            script = page[page.index("const UI ="):]
            keep = {x["code"], "en"}
            for l in build.LANGS:
                found = f'"{l}":{{"badge"' in script
                self.assertEqual(found, l in keep, f"{l} UI on the {x['code']} page")
        artifact = (ROOT / "dist/artifact.html").read_text(encoding="utf-8")
        for l in build.LANGS:  # the self-contained copy still switches language in place
            self.assertIn(ui[l]["h1"], artifact)

    def test_sitemap_and_llms_txt_list_every_language_page(self):
        sitemap = (ROOT / "docs/sitemap.xml").read_text(encoding="utf-8")
        llms = (ROOT / "docs/llms.txt").read_text(encoding="utf-8")
        full = (ROOT / "docs/llms-full.txt").read_text(encoding="utf-8")
        for x in build.LANGINFO:
            self.assertIn(f"<loc>{build.page_url(x['code'])}</loc>", sitemap)
            self.assertIn(f"]({build.page_url(x['code'])})", llms)
        for c in self.cmds:
            self.assertIn(f"### {c['cmd']}", full)

    # --- one page per command -------------------------------------------------------

    def command_pages(self):
        for x in build.LANGINFO:
            for c in self.cmds:
                path = ROOT / "docs" / build.page_path(x["code"]) / "commands" / build.slug(c) / "index.html"
                yield x, c, path, path.read_text(encoding="utf-8")

    def test_every_command_has_a_page_in_every_language(self):
        n = 0
        for x, c, path, page in self.command_pages():
            n += 1
            where = f"{x['code']} {c['cmd']}"
            self.assertIn(f'<html lang="{x["html"]}">', page, where)
            self.assertIn(f'<link rel="canonical" href="{build.cmd_url(x["code"], c)}">', page, where)
            self.assertEqual(len(re.findall(r'rel="alternate" hreflang=', page)), len(build.LANGINFO) + 1, where)
            self.assertRegex(page, rf"<h1>{re.escape(c['cmd'])}[<]", where)
            title = re.search(r"<title>([^<]*)</title>", page).group(1)
            self.assertLessEqual(len(title), 70, where)
            csp = re.search(r'http-equiv="Content-Security-Policy" content="([^"]+)"', page).group(1)
            self.assertEqual(csp, build.csp(page, style_self=True), where)
            json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', page, re.S).group(1).replace("<\\/", "</"))
        self.assertEqual(n, len(build.LANGINFO) * len(self.cmds))
        self.assertEqual(sum(1 for _ in (ROOT / "docs").glob("**/commands/*/index.html")), n)  # no stale pages

    def test_command_page_links_all_resolve(self):
        for x, c, path, page in self.command_pages():
            for href in re.findall(r'<a [^>]*href="([^"#]*)(?:#[^"]*)?"', page) + re.findall(r'<link rel="stylesheet" href="([^"]+)"', page):
                if href.startswith("https://"):
                    continue
                target = (path.parent / href).resolve()
                if href == "" or href.endswith("/"):
                    target = target / "index.html"
                self.assertTrue(target.exists(), f"{x['code']} {c['cmd']}: broken link {href}")

    def test_language_pages_link_every_command_page(self):
        for x, page in self.lang_pages():
            main = re.search(r'<main id="list"[^>]*>(.*?)</main>', page, re.S).group(1)
            for c in self.cmds:
                self.assertIn(f'href="commands/{build.slug(c)}/"', main, f"{x['code']} {c['cmd']}")

    def test_sitemap_and_llms_txt_list_every_command_page(self):
        sitemap = (ROOT / "docs/sitemap.xml").read_text(encoding="utf-8")
        llms = (ROOT / "docs/llms.txt").read_text(encoding="utf-8")
        for c in self.cmds:
            for x in build.LANGINFO:
                self.assertIn(f"<loc>{build.cmd_url(x['code'], c)}</loc>", sitemap)
            self.assertIn(f"]({build.cmd_url('en', c)})", llms)

    def test_every_command_appears_in_every_readme(self):
        for lang, text in self.readmes.items():
            for c in self.cmds:
                self.assertIn(f"`{c['cmd']}`", text, f"{c['cmd']} missing from {lang}")

    def test_no_placeholder_links_left(self):
        for text in [self.page, *self.readmes.values()]:
            self.assertNotIn("OWNER/", text)


if __name__ == "__main__":
    unittest.main(verbosity=1)
