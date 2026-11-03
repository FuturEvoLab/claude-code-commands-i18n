#!/usr/bin/env bash
# Regenerate the README preview images in docs/assets/ with headless Chrome.
# Usage: scripts/screenshots.sh   (set CHROME=/path/to/chrome if it is not found)
set -euo pipefail
cd "$(dirname "$0")/.."
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
command -v "$CHROME" >/dev/null 2>&1 || [ -x "$CHROME" ] || { echo "Chrome not found; set CHROME=..." >&2; exit 1; }
OUT=docs/assets
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
mkdir -p "$OUT"
PAGE="file://$PWD/docs/index.html"
PAGE="${PAGE// /%20}"

# A copy of the page that types a query, for the search-mode preview.
sed -e 's#</html>##' -e '/Content-Security-Policy/d' docs/index.html > "$TMP/search.html"
echo '<script>const q=document.getElementById("q");q.value="巻き戻し";q.dispatchEvent(new Event("input"));q.dispatchEvent(new KeyboardEvent("keydown",{key:"ArrowDown"}));</script></html>' >> "$TMP/search.html"

shot() { # name size url
  "$CHROME" --headless=new --disable-gpu --no-first-run --user-data-dir="$TMP/profile" --hide-scrollbars \
    --force-prefers-reduced-motion --window-size="$2" --virtual-time-budget=4000 --screenshot="$OUT/$1.png" "$3" >/dev/null 2>&1
}
shot preview-en 1366,900 "$PAGE#en"
shot preview-search 1366,900 "file://$TMP/search.html#ja"
shot preview-mobile 500,1000 "$PAGE#zh"
ls -la "$OUT"
