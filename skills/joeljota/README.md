# joeljota

Skill do Claude Code que escreve roteiros de Reels no estilo do Joel Jota (@joeljota), com uma mensagem de impacto, a partir da análise de 70 reels dele coletados em 03/10/2026: os 30 mais vistos de todos os tempos, os 20 mais recentes e os 20 motivacionais mais vistos fora desses dois grupos.

## Usar

```
/joeljota <tema ou situação>
/joeljota
/joeljota curto <tema>
/joeljota ganchos <tema>
/joeljota revisar <roteiro>
/joeljota atualizar
```

As instruções completas estão em `SKILL.md`. O padrão do estilo, com números, está em `references/dna-joeljota.md`, e os moldes de roteiro, em `references/moldes.md`.

## O que não vai para o repositório

`dados/fichas/`, `dados/midia/` e `dados/joeljota.json` guardam transcrições, legendas e quadros dos vídeos do Joel. Esses arquivos ficam só na máquina local. Para recriá-los, rode `bash scripts/atualizar_base.sh` (cerca de 1 a 2 horas; no máximo 1 vez por mês) e depois os passos da seção "atualizar" do `SKILL.md`.

## Depende de

A coleta reaproveita os scripts da skill `modelagem` (`~/.claude/skills/modelagem/scripts`: coleta, download, transcrição, OCR e cortes), o `ffmpeg` e o `mlx_whisper`.
