#!/bin/bash
# Atualiza a base de dados da skill /modelagem a partir do Instagram.
# Coleta TODOS os reels de cada perfil (views, likes, comentários), escolhe os 15 mais vistos + os 15 mais recentes,
# baixa, transcreve (Whisper), lê o texto da tela (OCR), mede cortes e monta um dossiê por criador.
#
# Uso:   bash atualizar_base.sh [perfil ...]      (sem argumentos = os 5 criadores modelados)
# Tempo: 1 a 3 horas num Mac de 8 GB (a transcrição é o gargalo). Deixe o Mac ligado na tomada.
# Cuidado: usa a sessão do Instagram já logada no perfil de automação do Chrome (chrome-devtools-mcp).
#          Rode no máximo 1 vez por mês; o script faz pausas de 2 a 4 s entre páginas para não travar a conta.
# Depois: rodar a análise por criador com scripts/prompt_analise.txt e refazer references/dna-dos-criadores.md.
set -euo pipefail
S="$(cd "$(dirname "$0")" && pwd)"
BASE="$(cd "$S/.." && pwd)/dados"
W="${MODELAGEM_TRABALHO:-$HOME/.cache/modelagem}"
SRC="${IGPROFILE:-$HOME/.cache/chrome-devtools-mcp/chrome-profile}"
USERS=("$@"); [ ${#USERS[@]} -eq 0 ] && USERS=(oalanicolas inventormiguel rodrigotadewald odanilogato ddiasmatt)
[ -f "$SRC/Default/Cookies" ] || { echo "Perfil do Chrome sem login do Instagram em $SRC (defina IGPROFILE)"; exit 1; }
mkdir -p "$W/igprof" "$W/users" "$W/videos" "$W/logs" "$BASE"
for u in "${USERS[@]}"; do rm -f "$W/users/$u.json"; rm -rf "$W/videos/$u"; done

echo "1/4 copiando o perfil logado e abrindo o Chrome invisível"
rsync -a --exclude 'Cache' --exclude 'Code Cache' --exclude 'GPUCache' --exclude 'Service Worker' "$SRC/Default" "$W/igprof/"
cp "$SRC/Local State" "$W/igprof/"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --user-data-dir="$W/igprof" --remote-debugging-port=9337 \
  --use-mock-keychain --password-store=basic --headless=new --no-first-run --disable-extensions --window-size=1280,900 \
  --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36" \
  about:blank >"$W/logs/chrome.log" 2>&1 &
CHROME=$!; trap 'kill $CHROME 2>/dev/null || true' EXIT; sleep 8

echo "2/4 coleta, detalhes, download, OCR, cortes e transcrição (em paralelo; logs em $W/logs)"
node "$S/collect.mjs" 9337 "$W/users" 220 "${USERS[@]}" >"$W/logs/collect.log" 2>&1 & P1=$!
bash "$S/baixar.sh" "$W" "${USERS[@]}" >"$W/logs/baixar.log" 2>&1 & P2=$!
bash "$S/processar.sh" "$W" "${USERS[@]}" >"$W/logs/processar.log" 2>&1 & P5=$!
python3 "$S/transcribe.py" "$W/videos" "$W/users" top mlx "${USERS[@]}" >"$W/logs/tr_gpu.log" 2>&1 & P3=$!
python3 "$S/transcribe.py" "$W/videos" "$W/users" recentes fw-small "${USERS[@]}" >"$W/logs/tr_cpu.log" 2>&1 & P4=$!
wait $P1 $P2; kill $CHROME 2>/dev/null || true
wait $P3 $P4 $P5 || true

echo "3/4 dossiês e números"
python3 "$S/dossie.py" "$W/users" "$W/videos" "$W/dossie" "${USERS[@]}"
python3 "$S/stats.py" "$W/users" "$W/videos" "$W/stats.json"
python3 "$S/tabelas.py" "$W/users" "$W/stats.json" "$W/tabelas.md"

echo "4/4 copiando para a skill ($BASE)"
mkdir -p "$BASE/users" "$BASE/midia" "$BASE/dossie"
for u in "${USERS[@]}"; do
  python3 -c "import json,sys; d=json.load(open(sys.argv[1])); [x.pop(k,None) for x in d.get('details',{}).values() if x for k in ('video_url','thumb_url')]; json.dump(d,open(sys.argv[2],'w'))" "$W/users/$u.json" "$BASE/users/$u.json"
  mkdir -p "$BASE/midia/$u"; cp "$W/videos/$u/"*.jpg "$W/videos/$u/"*.json "$BASE/midia/$u/" 2>/dev/null || true
  sed "s|$W/videos|$BASE/midia|g" "$W/dossie/$u.md" > "$BASE/dossie/$u.md"
done
cp "$W/stats.json" "$W/tabelas.md" "$BASE/"
echo "Pronto. Dossiês em $BASE/dossie. Os vídeos ficam em $W/videos (apague com: rm -rf $W/videos quando terminar a análise)."
