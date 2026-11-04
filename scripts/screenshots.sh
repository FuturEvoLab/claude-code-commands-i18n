#!/usr/bin/env bash
# Regenerate the README preview images in docs/assets/ with headless Chrome (English UI).
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

# Test copies of the page (the CSP line is dropped so the helper scripts can run).
copy() { sed -e 's#</html>##' -e '/Content-Security-Policy/d' "${2:-docs/index.html}" > "$TMP/$1.html"; }

# Search mode with a query typed in.
copy search
echo '<script>const q=document.getElementById("q");q.value="undo";q.dispatchEvent(new Event("input"));q.dispatchEvent(new KeyboardEvent("keydown",{key:"ArrowDown"}));</script></html>' >> "$TMP/search.html"

# Matrix theme: headless capture does not show canvas animation, so drive frames with a
# timer for 3 s and then freeze the canvas into an image before the screenshot.
sed -e 's#</html>##' -e '/Content-Security-Policy/d' \
    -e 's#<meta charset="utf-8">#<meta charset="utf-8"><script>requestAnimationFrame=cb=>setTimeout(()=>cb(performance.now()),16);cancelAnimationFrame=clearTimeout;</script>#' \
    docs/index.html > "$TMP/matrix.html"
echo '<script>setSkin("matrix");setTimeout(()=>{const c=document.querySelector(".rain"),i=new Image();i.src=c.toDataURL();i.className="rain";c.replaceWith(i)},3000)</script></html>' >> "$TMP/matrix.html"

shot() { # name size url
  "$CHROME" --headless=new --disable-gpu --no-first-run --user-data-dir="$TMP/profile-$1" --hide-scrollbars \
    "${@:4}" --window-size="$2" --virtual-time-budget=5000 --screenshot="$OUT/$1.png" "$3" >/dev/null 2>&1
}
shot preview-en 1366,900 "$PAGE#en" --force-prefers-reduced-motion
shot preview-matrix 1366,900 "file://$TMP/matrix.html#en"
shot preview-search 1366,900 "file://$TMP/search.html#en" --force-prefers-reduced-motion
shot preview-mobile 500,1000 "$PAGE#en" --force-prefers-reduced-motion
ls -la "$OUT"

# Optional: shrink the PNGs and refresh the social card (needs Pillow).
python3 -c "import PIL" 2>/dev/null && python3 scripts/optimize_images.py || echo "Pillow not installed: skipped scripts/optimize_images.py"
