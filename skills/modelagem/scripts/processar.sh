#!/bin/bash
# processar.sh <pasta_trabalho> perfil... — depois do download (.baixado): texto na tela (OCR) e cortes/folhas de contato
W="$1"; shift; S="$(cd "$(dirname "$0")" && pwd)"
for u in "$@"; do
  until [ -f "$W/videos/$u/.baixado" ]; do sleep 15; done
  python3 "$S/ocr_frames.py" "$W/videos" "$u"
  bash "$S/visual.sh" "$W/videos" "$u"
  echo "PROCESSADO $u"
done
