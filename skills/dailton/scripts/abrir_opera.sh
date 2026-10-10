#!/bin/bash
# Abre o Opera GX invisível com uma CÓPIA da sessão (só cookies e preferências), porta 9340.
# A cópia fica em <pasta>/igprof e deve ser apagada no fim (fechar_opera.sh).
set -euo pipefail
W="$1"; PORT=9340
SRC="$HOME/Library/Application Support/com.operasoftware.OperaGX"
BIN="/Applications/Opera GX.app/Contents/MacOS/Opera"
rm -rf "$W/igprof"; mkdir -p "$W/igprof/Default"
for f in Cookies Cookies-journal Preferences "Local Storage"; do [ -e "$SRC/Default/$f" ] && cp -R "$SRC/Default/$f" "$W/igprof/Default/"; done
cp "$SRC/Local State" "$W/igprof/"
run() { "$BIN" --user-data-dir="$W/igprof" --remote-debugging-port=$PORT --headless=new --no-first-run --disable-extensions \
  --window-size=1280,900 "$@" about:blank >>"$W/browser.log" 2>&1 & BROWSER=$!
  for i in $(seq 1 60); do python3 -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:$PORT/json/version', timeout=1)" 2>/dev/null && return 0; sleep 1; done; echo "porta não abriu"; exit 1; }
run; UA="$(python3 -c "import json,urllib.request; print(json.load(urllib.request.urlopen('http://127.0.0.1:$PORT/json/version'))['User-Agent'].replace('HeadlessChrome','Chrome'))")"
kill $BROWSER; wait $BROWSER 2>/dev/null || true; sleep 2; run --user-agent="$UA"
echo "pid=$BROWSER ua=$UA"
wait $BROWSER
