# modelagem

Skill do Claude Code que escreve roteiros de Reels sobre IA para o Adriel no padrão de 5 criadores brasileiros de IA (Danilo Gato, Inventor Miguel, Alan Nicolas, Rodrigo Tadewald e Mateus Dias), a partir de 150 reels coletados em 29/09/2026. Antes de escrever, pesquisa os fatos do dia e cita fonte e data.

## Instalar

```bash
git clone https://github.com/kairoxaioficial/skill-modelagem.git ~/.claude/skills/modelagem
```

## Usar

```
/modelagem novidades [dias]
/modelagem <tema>
/modelagem semana
/modelagem estilo <criador> <tema>
/modelagem revisar <roteiro>
/modelagem atualizar
```

As instruções completas estão em `SKILL.md`. O relatório da análise está em `dados/relatorio/`.

## O que não vai para o repositório

`dados/midia/` e `dados/dossie/` guardam quadros, transcrições e legendas completas dos vídeos dos criadores, e `scripts/ocr` é um binário compilado. Esses arquivos ficam só na máquina local. Para recriá-los, rode `bash scripts/atualizar_base.sh` (de 1 a 3 horas; no máximo 1 vez por mês).
