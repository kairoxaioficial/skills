#!/bin/bash
# processar.sh — depois de selecionar.py: separa o corpus (viral + recentes + motivacionais) dos outros vídeos baixados,
# transcreve com tempo por palavra, lê o texto da tela (OCR), mede cortes e gera prosódia, fichas e números de linguagem.
# Tempo: cerca de 1 hora num Mac de 8 GB (a transcrição é o gargalo). Saída em ../dados/.
set -euo pipefail
S="$(cd "$(dirname "$0")" && pwd)"; M="$S/../../modelagem/scripts"
W="${JOELJOTA_TRABALHO:-$HOME/.cache/joeljota}"; U=joeljota
python3 - "$W" <<'PY'
import json, glob, os, shutil, sys
W = sys.argv[1]; V = f'{W}/videos'; os.makedirs(f'{V}/joeljota_resto', exist_ok=True)
s = json.load(open(f'{W}/users/joeljota.json'))['sel']; corpus = set(s['viral'] + s['recentes'] + s.get('motivacionais', []))
for f in glob.glob(f'{V}/joeljota/*') + glob.glob(f'{V}/joeljota_resto/*'):
    c = os.path.basename(f).split('.')[0]; dest = f'{V}/joeljota' if c in corpus else f'{V}/joeljota_resto'
    if os.path.dirname(f) != dest: shutil.move(f, dest)
print('corpus', len(glob.glob(f'{V}/joeljota/*.mp4')), 'vídeos')
PY
python3 "$S/transcrever_corpus.py" "$W" >"$W/logs/tr_corpus.log" 2>&1
python3 "$M/ocr_frames.py" "$W/videos" "$U" >"$W/logs/processar.log" 2>&1
bash "$M/visual.sh" "$W/videos" "$U" >>"$W/logs/processar.log" 2>&1
python3 "$S/prosodia.py" "$W" >"$W/logs/prosodia.log" 2>&1
python3 "$S/fichas.py" "$W"; python3 "$S/linguagem.py" "$W"
echo "Pronto. Fichas, prosódia e linguagem em $S/../dados"
