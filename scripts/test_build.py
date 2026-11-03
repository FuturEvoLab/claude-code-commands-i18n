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
        cls.page = (ROOT / "docs/index.html").read_text(encoding="utf-8")
        cls.readmes = {l: (ROOT / build.T[l]["file"]).read_text(encoding="utf-8") for l in build.LANGS}
        cls.cmds = json.loads((ROOT / "data/commands.json").read_text(encoding="utf-8"))

    def test_csp_hashes_match_inline_code(self):
        csp = re.search(r'http-equiv="Content-Security-Policy" content="([^"]+)"', self.page).group(1)
        self.assertEqual(csp, build.csp(self.page))
        self.assertIn("default-src 'none'", csp)

    def test_page_loads_nothing_from_other_sites(self):
        for tag in re.findall(r"<(?:script|link|img|iframe)\b[^>]*>", self.page):
            self.assertNotRegex(tag, r"(src|href)=\"https?:", tag)

    def test_every_command_appears_in_every_readme(self):
        for lang, text in self.readmes.items():
            for c in self.cmds:
                self.assertIn(f"`{c['cmd']}`", text, f"{c['cmd']} missing from {lang}")

    def test_no_placeholder_links_left(self):
        for text in [self.page, *self.readmes.values()]:
            self.assertNotIn("OWNER/", text)


if __name__ == "__main__":
    unittest.main(verbosity=1)
