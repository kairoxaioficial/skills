#!/bin/bash
# baixar.sh <pasta_trabalho> perfil... — só a parte de rede: espera a coleta, busca detalhes, baixa e marca .baixado
W="$1"; shift; S="$(cd "$(dirname "$0")" && pwd)"
for u in "$@"; do
  until [ -f "$W/users/$u.json" ]; do sleep 15; done
  [ -f "$W/videos/$u/.baixado" ] && continue
  node "$S/details.mjs" 9337 "$W/users" "$u"
  python3 "$S/download.py" "$W/users" "$W/videos" "$u" && touch "$W/videos/$u/.baixado"
  echo "BAIXADO $u"
done
