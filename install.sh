#!/usr/bin/env bash
# Instala as skills escolhidas em ~/.claude/skills (Claude Code).
# Uso: ./install.sh                 -> menu interativo
#      ./install.sh dailton viral   -> instala só as citadas
#      ./install.sh todas           -> instala todas
set -euo pipefail

ORIGEM="$(cd "$(dirname "$0")/skills" && pwd)"
DESTINO="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
SKILLS=(cienciatododia joeljota dailton criacao-conteudo modelagem viral)
DESC=(
  "Roteiros de tecnologia no estilo Ciência Todo Dia (Pedro Loos)"
  "Reels de mensagem de impacto no estilo Joel Jota"
  "Estrategista viral no método Dailton Rolim (8 formatos, roteiro de 44 s)"
  "Conteúdo de Instagram por funil (topo, meio, fundo / AIDA)"
  "Reels sobre IA com fatos pesquisados, no padrão de 5 criadores de IA"
  "Narrativa viral e edição no padrão Kallaway"
)

escolhidas=()
if [ $# -gt 0 ]; then
  if [ "$1" = "todas" ]; then escolhidas=("${SKILLS[@]}"); else escolhidas=("$@"); fi
else
  echo "Skills disponíveis:"
  for i in "${!SKILLS[@]}"; do printf "  %d) %-17s %s\n" $((i+1)) "${SKILLS[$i]}" "${DESC[$i]}"; done
  echo "  a) todas"
  read -rp "Escolha os números separados por espaço (ex.: 1 3 6) ou 'a': " resp
  if [ "$resp" = "a" ]; then escolhidas=("${SKILLS[@]}"); else
    for n in $resp; do
      [[ "$n" =~ ^[0-9]+$ ]] && [ "$n" -ge 1 ] && [ "$n" -le ${#SKILLS[@]} ] || { echo "Opção inválida: $n"; exit 1; }
      escolhidas+=("${SKILLS[$((n-1))]}")
    done
  fi
fi
[ ${#escolhidas[@]} -gt 0 ] || { echo "Nada escolhido."; exit 0; }

mkdir -p "$DESTINO"
for s in "${escolhidas[@]}"; do
  [ -d "$ORIGEM/$s" ] || { echo "Skill desconhecida: $s"; exit 1; }
  if [ -e "$DESTINO/$s" ]; then
    bak="$DESTINO/$s.bak-$(date +%Y%m%d%H%M%S)"
    mv "$DESTINO/$s" "$bak"
    echo "  já existia: backup em $bak"
  fi
  cp -R "$ORIGEM/$s" "$DESTINO/$s"
  # Os scripts citam caminhos da máquina original; troca pelo HOME de quem instala.
  if [ "$HOME" != "/Users/adriel" ]; then
    grep -rlI "/Users/adriel" "$DESTINO/$s" 2>/dev/null | while read -r f; do
      sed -i.tmp "s#/Users/adriel#$HOME#g" "$f" && rm -f "$f.tmp"
    done
  fi
  echo "✓ $s instalada"
done

if printf '%s\n' "${escolhidas[@]}" | grep -qx dailton && [ ! -d "$DESTINO/joeljota" ]; then
  echo "Aviso: a dailton usa scripts/detalhes.mjs da joeljota para atualizar a base. Instale a joeljota também se for usar 'atualizar'."
fi
echo "Pronto. Abra uma nova sessão do Claude Code e chame /<nome-da-skill>."
