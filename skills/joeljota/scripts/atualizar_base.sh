#!/bin/bash
# Atualiza a base da skill /joeljota a partir do Instagram (@joeljota).
# Coleta TODOS os reels (views, likes, comentários), busca os detalhes dos 150 mais vistos + 30 mais recentes + fixados,
# baixa esses vídeos e separa as legendas em lotes para a classificação. Reaproveita os scripts da skill modelagem.
#
# Uso:   bash atualizar_base.sh
#        IGPROFILE=<pasta de dados do navegador> BROWSER_BIN=<binário> bash atualizar_base.sh   (outro navegador logado)
#        ex. Opera GX: IGPROFILE="$HOME/Library/Application Support/com.operasoftware.OperaGX" \
#                      BROWSER_BIN="/Applications/Opera GX.app/Contents/MacOS/Opera"
# Tempo: cerca de 25 minutos (lista de reels, detalhes e download).
# Cuidado: usa uma sessão do Instagram já logada (copia só cookies e preferências para uma pasta temporária).
#          Rode no máximo 1 vez por mês; há pausas de 2 a 4 s entre páginas para não travar a conta.
# Depois: classificação (scripts/wf_classificar.js), selecionar.py, processar.sh e análise (scripts/wf_analise.js).
set -euo pipefail
S="$(cd "$(dirname "$0")" && pwd)"; M="$S/../../modelagem/scripts"
W="${JOELJOTA_TRABALHO:-$HOME/.cache/joeljota}"; U=joeljota
SRC="${IGPROFILE:-$HOME/.cache/chrome-devtools-mcp/chrome-profile}"
BIN="${BROWSER_BIN:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
[ -f "$SRC/Default/Cookies" ] || { echo "Perfil do navegador sem cookies em $SRC (defina IGPROFILE)"; exit 1; }
[ -f "$M/collect.mjs" ] || { echo "Faltam os scripts da skill modelagem em $M"; exit 1; }
rm -rf "$W/igprof"; mkdir -p "$W/igprof/Default" "$W/users" "$W/videos" "$W/logs"
rm -f "$W/users/$U.json"; rm -rf "$W/videos/$U"

echo "1/3 copiando a sessão logada e abrindo o navegador invisível"
for f in Cookies Cookies-journal Preferences "Local Storage"; do [ -e "$SRC/Default/$f" ] && cp -R "$SRC/Default/$f" "$W/igprof/Default/"; done
cp "$SRC/Local State" "$W/igprof/"
run() { "$BIN" --user-data-dir="$W/igprof" --remote-debugging-port=9338 --headless=new --no-first-run --disable-extensions \
  --window-size=1280,900 "$@" about:blank >>"$W/logs/browser.log" 2>&1 & BROWSER=$!; sleep 8; }
run; UA="$(curl -s 127.0.0.1:9338/json/version | python3 -c 'import json,sys; print(json.load(sys.stdin)["User-Agent"].replace("HeadlessChrome","Chrome"))')"
kill $BROWSER; sleep 3; run --user-agent="$UA"; trap 'kill $BROWSER 2>/dev/null || true' EXIT
echo "navegador: $UA"

echo "2/3 lista de reels e detalhes"
node "$M/collect.mjs" 9338 "$W/users" 300 "$U"
node "$S/detalhes.mjs" 9338 "$W/users/$U.json" 150 30
# apaga a cópia da sessão só depois que o navegador fechar (antes disso ele ainda grava na pasta)
kill $BROWSER 2>/dev/null || true; wait $BROWSER 2>/dev/null || true; sleep 2; rm -rf "$W/igprof" || true

echo "3/3 download dos vídeos e legendas em lotes para a classificação"
python3 "$M/download.py" "$W/users" "$W/videos" "$U" && touch "$W/videos/$U/.baixado"
python3 - "$W" <<'PY'
import json, os, sys, datetime as dt
W = sys.argv[1]; d = json.load(open(f'{W}/users/joeljota.json')); it = {i['code']: i for i in d['items']}; det = d['details']
pool = sorted([c for c, v in det.items() if v and v.get('ok')], key=lambda c: -(it[c].get('play_count') or 0))
os.makedirs(f'{W}/legendas', exist_ok=True)
for k in range(6):
    L = [f"## {c}\n- views {it[c].get('play_count')} | data {dt.datetime.fromtimestamp(det[c]['taken_at']):%Y-%m-%d} | duração {round(det[c].get('duration') or 0)}s | coautores {det[c].get('coauthors') or []} | música {'sim' if det[c].get('music') else 'não'}\n\n{(det[c].get('caption') or '(sem legenda)').strip()[:900]}\n" for c in pool[k::6]]
    open(f'{W}/legendas/lote-{k + 1}.md', 'w').write('\n'.join(L))
print('legendas em', f'{W}/legendas', len(pool), 'vídeos')
PY
echo "Pronto. Próximo passo: classificar as legendas (scripts/wf_classificar.js), depois selecionar.py e processar.sh"
