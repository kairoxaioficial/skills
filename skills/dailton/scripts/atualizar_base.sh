#!/bin/bash
# Atualiza a base medida da skill /dailton (dados/reels-dailton.md) a partir do Instagram do @dailton_rolim.
# Usa uma CÓPIA da sessão do Opera GX (só cookies e preferências, apagada no fim). Pergunte ao Adriel antes de usar a sessão dele.
# Passos: abre o Opera invisível, lista os ~400 reels mais recentes (aba de reels), busca os detalhes dos 25 mais vistos
# e dos 10 mais novos, baixa e transcreve esses vídeos com o transcritor nativo do macOS e regrava a base.
# Tempo: 10 a 20 minutos. Há pausas entre páginas; se aparecer erro 429 (limite do Instagram), pare e tente em outro dia.
set -euo pipefail
K="$(cd "$(dirname "$0")/.." && pwd)"; SC="$K/scripts"; W="${DAILTON_TRABALHO:-$HOME/.cache/dailton}"
J="$HOME/.claude/skills/joeljota/scripts"
[ -f "$J/detalhes.mjs" ] || { echo "Falta $J/detalhes.mjs (skill joeljota)"; exit 1; }
mkdir -p "$W/ig/users" "$W/ig/videos"
bash "$SC/abrir_opera.sh" "$W" > "$W/opera.log" 2>&1 &
trap 'pkill -f "user-data-dir=$W/igprof" || true; sleep 4; pkill -9 -f "user-data-dir=$W/igprof" || true; rm -rf "$W/igprof"' EXIT
for i in $(seq 1 120); do grep -q "pid=" "$W/opera.log" 2>/dev/null && break; sleep 1; done
grep -q "pid=" "$W/opera.log" || { echo "O Opera invisível não abriu (veja $W/opera.log)"; exit 1; }
echo "1/4 lista de reels"; node "$SC/collect2.mjs" 9340 "$W/ig/users" 32 dailton_rolim
echo "2/4 detalhes"; node "$J/detalhes.mjs" 9340 "$W/ig/users/dailton_rolim.json" 25 10
echo "3/4 download e transcrição"; python3 "$SC/baixar_transcrever.py" "$W/ig/users/dailton_rolim.json" "$W/ig/videos/dailton" 25 10
echo "4/4 base"; python3 "$SC/base_dailton.py" "$W" "$K"
echo "Pronto: $K/dados/reels-dailton.md"
