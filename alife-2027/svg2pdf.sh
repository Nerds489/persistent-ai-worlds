#!/usr/bin/env bash
# Convert the paper's SVG figures to vector PDFs for LaTeX, one page each, sized to the SVG.
# Usage: ./svg2pdf.sh            (writes figures/*.pdf from ../desktop-setup/figures/*.svg)
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
SRC="$HERE/../desktop-setup/figures"
OUT="$HERE/figures"
CHROME=${CHROME:-google-chrome}
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
mkdir -p "$OUT"

for name in fig-river-map fig-energy-flow fig-s7-inherit fig-s7-river fig-s7-long; do
  if [[ -f "$SRC/$name.svg" ]]; then
    svg="$SRC/$name.svg"
    read -r w h < <(grep -o -m1 '<svg[^>]*>' "$svg" | sed -E 's/.*width="([0-9.]+)".*height="([0-9.]+)".*/\1 \2/')
    body="<img src=\"file://$svg\" style=\"display:block;width:${w}px;height:${h}px\">"
  else
    png="$SRC/$name.png"
    read -r w h < <(python3 -c "import struct,sys;d=open(sys.argv[1],'rb').read(24);print(*struct.unpack('>II',d[16:24]))" "$png")
    body="<img src=\"file://$png\" style=\"display:block;width:${w}px;height:${h}px\">"
  fi
  cat > "$TMP/$name.html" <<EOF
<!doctype html><html><head><meta charset="utf-8"><style>
@page{size:${w}px ${h}px;margin:0}html,body{margin:0;padding:0;background:#fff}
</style></head><body>$body</body></html>
EOF
  "$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --allow-file-access-from-files \
    --print-to-pdf="$OUT/$name.pdf" "file://$TMP/$name.html" >/dev/null 2>&1
  pages=$(pdfinfo "$OUT/$name.pdf" | awk '/^Pages/{print $2}')
  [[ "$pages" == 1 ]] || { echo "FAIL $name: $pages pages" >&2; exit 1; }
  echo "ok  $name.pdf (${w}x${h})"
done
