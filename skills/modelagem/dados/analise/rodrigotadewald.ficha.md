# Ficha quantitativa — @rodrigotadewald (Rodrigo Tadewald)

Sócio-fundador da Asimov Academy (bio: ensina a usar IA; +30 mil alunos) · 238.858 seguidores · 106 posts · **94 reels** (lista completa) · coleta em 29/09/2026 com login. Fontes: `users/rodrigotadewald.json` (todos os reels), `dossie/rodrigotadewald.md`, `videos/rodrigotadewald/*.tr.json | *.ocr.json | *.vis.json | *.mp4`. Números calculados em Python a partir dos brutos; nenhum trecho de fala ou legenda com mais de 5 palavras foi copiado (texto de tela com até 12 palavras aparece entre «»).

## 0. Como os números foram medidos

- **views** = `play_count` (igual ao dossiê). Ele soma as exibições no Facebook quando o reel é cruzado para lá. O `ig_play_count` (só Instagram) existe apenas nos 33 detalhados: nos 15 do TOP é ≥ 95,9% do total; em 7 dos 15 recentes fica abaixo de 95% (RECENTE#15: 84.857 de 251.299 = 34%; RECENTE#4: 42%; RECENTE#11: 67%; RECENTE#3: 77%; RECENTE#2: 83%; RECENTE#1 e #14: 91%).
- **Percentis**: interpolação linear sobre os 94 reels. O dossiê usa posto mais próximo (p25 26.836, p75 172.846, p90 430.324); a mediana é a mesma (70.612,5). **Múltiplo** = views ÷ 70.612,5.
- **Tendência**: ordem da lista do Instagram (mais novo → mais velho) sem os 3 fixados (`DZn2AvhnWOC`, `DZIv5MJkc0g`, `DSBUUzdkTUi`); datas dos blocos tiradas do ID do post (erro de minutos a 1,5 h).
- **Palavras/min** = palavras ÷ (fim do último trecho − início do 1º) × 60, como no dossiê. Os 30 têm fala em português com flag ok. RECENTE#15 é um diálogo dele com um agente de voz (metade das falas é da IA): fica fora da seção 4 e das medianas de ritmo. Em TOP#15, as 2 frases finais são amostras de voz sintética: fora da seção 4.
- **Cortes/min**: bruto = cortes do `vis.json` ÷ duração. Agrupado = cortes a menos de 1 s um do outro contam como 1.
- **Rosto na tela** (medida extra, não pedida): detector de rosto do Apple Vision em frames a cada 0,5 s dos `.mp4` (rosto com largura ≥ 12% do quadro). "Tela dividida" = rosto na metade de baixo (centro abaixo de 45% da altura) com print ou vídeo em cima; "rosto cheio" = rosto no centro ou no alto. Rosto de perfil não é detectado (TOP#6 dá 0%: ele aparece de lado no computador).
- **Números citados**: dígitos e numerais por extenso, incluindo versões de modelo (GPT-6, 4.6); sem "um/uma", sem "do zero" e sem nomes que só contêm dígito (N8N, MP4). **Perguntas**: quantidade de "?" na transcrição. **CTA falado**: conferido à mão; o segundo é o início do trecho em que o verbo aparece.
- **1º frame**: OCR em t = 0 (`ocr.json`) + frame de 0,4 s (`hook.jpg`), conferidos em 2 mosaicos com os 30 ganchos; 5 folhas de contato conferidas (TOP#1, TOP#3, TOP#6, TOP#12, RECENTE#15).
- **Limites**: RECENTE#1 a #3 foram transcritos pelo faster-whisper-small (erra nomes: "lovo", "Zmove", "Prompete"); o Whisper grafa Claude como "Cloud"/"Cláudio" e N8N como "Neo8n". A pontuação do Whisper falha em trechos longos (TOP#6, TOP#14), por isso também mostro o tamanho por trecho de respiração. OCR a cada 2 s.

## 1. Distribuição de views (94 reels) e tendência

| p10 | p25 | p50 (mediana) | p75 | p90 | p99 | máximo | média |
|---|---|---|---|---|---|---|---|
| 11.188 | 26.958 | 70.612,5 | 169.595 | 422.977 | 1.114.566 | 1.375.079 | 172.120 |

- Mediana = 29,6% dos seguidores. Média 2,4x a mediana. ≥ 50 mil: 54 reels (57,4%); ≥ 100 mil: 36 (38,3%); ≥ 250 mil: 19; ≥ 500 mil: 7; ≥ 1 milhão: 3 (3,2%).
- Mediana de likes/views de todos os reels: 1,98%; comentários/views: 0,036%.
- Prováveis anúncios (likes/views < 0,3%): **0 de 94**. Nenhum dos 30 tem a tag.
- Reels com comentários/views ≥ 1% (assinatura do "comenta PALAVRA"): 10 de 94, entre eles os 3 fixados; mediana de 4,2% de comentários/views. Nos 6 que têm legenda e transcrição o pedido de palavra-chave está confirmado: os 3 fixados na legenda (ARQUITETO, CLAUDE, IA), RECENTE#4 só na fala (design), RECENTE#10 e #14 na fala e na legenda (skill, REMOTION); os outros 4 não têm legenda coletada. Views: mediana 55.193,5 contra 76.404 dos outros 84.
- Colaborações com @asimov.academy (coautor): 21 dos 91 não fixados, mediana 40.705 contra 83.653,5 sem coautor. Dentro de cada bloco de 50 a colaboração também fica abaixo (bloco 1: 15 com mediana 27.323 × 35 com 42.396; bloco 2: 6 com 44.204,5 × 35 com 159.842).

**Mediana por blocos de 50 reels (mais novo → mais velho, sem fixados)**

| bloco | reels | período (mais novo → mais velho) | dias | reels/semana | mediana | x mediana geral | p90 | máximo | ≥ 100 mil | do TOP 15 | colab. | "comenta PALAVRA" |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 50 | 2026-09-25 → 2026-02-14 | 223 | 1,5 | 39.504,5 | 0,56x | 153.498 | 1.093.606 | 10 | 2 | 15 | 5 |
| 2 | 41 | 2026-02-12 → 2025-08-29 | 167 | 1,7 | 148.132 | 2,10x | 811.608 | 1.375.079 | 25 | 13 | 6 | 2 |

Com só 91 reels, dois blocos de 50 escondem a curva. Mesma conta em blocos de 15:

| bloco de 15 | período (mais novo → mais velho) | reels/semana | mediana | x mediana geral | máximo | ≥ 100 mil | do TOP 15 |
|---|---|---|---|---|---|---|---|
| 1 | 2026-09-25 → 2026-08-12 | 2,2 | 19.893 | 0,28x | 251.299 | 2 | 0 |
| 2 | 2026-08-11 → 2026-05-18 | 1,2 | 26.836 | 0,38x | 141.855 | 1 | 0 |
| 3 | 2026-05-17 → 2026-03-12 | 1,5 | 45.125 | 0,64x | 274.225 | 3 | 0 |
| 4 | 2026-03-11 → 2025-12-26 | 1,3 | 143.866 | 2,04x | 1.093.606 | 9 | 4 |
| 5 | 2025-12-23 → 2025-11-07 | 2,1 | 121.786 | 1,72x | 1.375.079 | 8 | 5 |
| 6 | 2025-11-04 → 2025-08-31 | 1,5 | 253.895 | 3,60x | 948.846 | 12 | 6 |

(O reel mais antigo, de 29/08/2025, sobra sozinho: 40.705 views.)

**Por mês de publicação (sem fixados; os 3 fixados são de dez/2025 e jun/2026)**

| mês | reels | mediana | máximo | ≥ 100 mil | do TOP 15 |
|---|---|---|---|---|---|
| 2026-09 | 9 | 14.674 | 60.339 | 0 | 0 |
| 2026-08 | 10 | 34.859,5 | 251.299 | 2 | 0 |
| 2026-07 | 6 | 23.191,5 | 141.855 | 1 | 0 |
| 2026-06 | 3 | 11.099 | 44.068 | 0 | 0 |
| 2026-05 | 7 | 36.613 | 85.765 | 0 | 0 |
| 2026-04 | 7 | 53.251 | 274.225 | 1 | 0 |
| 2026-03 | 5 | 143.866 | 183.768 | 3 | 0 |
| 2026-02 | 4 | 323.526,5 | 1.093.606 | 3 | 2 |
| 2026-01 | 7 | 110.150 | 351.986 | 4 | 2 |
| 2025-12 | 9 | 87.764 | 435.430 | 4 | 1 |
| 2025-11 | 9 | 343.301 | 1.375.079 | 6 | 5 |
| 2025-10 | 6 | 418.079 | 948.846 | 5 | 4 |
| 2025-09 | 7 | 213.071 | 384.506 | 6 | 1 |
| 2025-08 | 2 | 44.204,5 | 47.704 | 0 | 0 |

Leitura: os 15 mais vistos saíram todos em 5 meses, de 19/09/2025 a 25/02/2026 (36 reels não fixados nessa janela, mediana 153.987). Os 48 reels não fixados publicados depois têm máximo de 274.225 e nenhum entra no TOP 15. O pico mensal foi out–nov/2025 (medianas de 418.079 e 343.301); desde mar/2026 a mediana mensal não passa de 144 mil e em set/2026 está em 14.674. O ritmo de postagem ficou parado em 1,5 a 1,7 reel por semana nos dois blocos de 50, então a queda não vem de postar mais. O bloco mais novo de 15 (12/08 a 25/09/2026) tem a menor mediana da série (19.893; 0,28x).

## 2. Os 30 selecionados

| código | grupo | data | dur (s) | views | x mediana | likes/views | coment./views | pal/min | cortes/min bruto (agrupado) | tem fala? | idioma | nº palavras | nº perguntas | nº números | CTA falado (s) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DRVZ9YskX9R | TOP#1 | 2025-11-21 | 85,3 | 1.375.079 | 19,47x | 2,23% | 0,011% | 220 | 9,1 (9,1) | sim | pt | 312 | 4 | 3 | — |
| DRkhY-3EXSH | TOP#2 | 2025-11-27 | 89,8 | 1.094.958 | 15,51x | 2,38% | 0,026% | 207 | 16,0 (16,0) | sim | pt | 309 | 1 | 1 | 85,6 (95% do vídeo) |
| DVL-2GtjEmn | TOP#3 | 2026-02-25 | 75,4 | 1.093.606 | 15,49x | 2,69% | 0,027% | 267 | 11,9 (11,1) | sim | pt | 335 | 0 | 8 | — |
| DP6chn3je86 | TOP#4 | 2025-10-17 | 53,9 | 948.846 | 13,44x | 1,98% | 0,019% | 199 | 12,2 (12,2) | sim | pt | 179 | 0 | 3 | — |
| DQo2ZajkcsJ | TOP#5 | 2025-11-04 | 43,1 | 879.910 | 12,46x | 1,71% | 0,006% | 190 | 16,7 (13,9) | sim | pt | 136 | 0 | 0 | — |
| DRLBPLlkanH | TOP#6 | 2025-11-17 | 57,9 | 811.608 | 11,49x | 1,96% | 0,008% | 226 | 9,3 (9,3) | sim | pt | 218 | 0 | 1 | — |
| DPlyTlMkSSg | TOP#7 | 2025-10-09 | 89,5 | 751.835 | 10,65x | 1,54% | 0,009% | 222 | 14,7 (14,7) | sim | pt | 331 | 3 | 5 | — |
| DUvhpvDk-ju | TOP#8 | 2026-02-14 | 89,8 | 496.918 | 7,04x | 2,13% | 0,020% | 233 | 18,0 (14,7) | sim | pt | 348 | 1 | 7 | — |
| DSUwnmTkT0R | TOP#9 | 2025-12-16 | 80,2 | 435.430 | 6,17x | 4,88% | 0,017% | 212 | 7,5 (7,5) | sim | pt | 283 | 1 | 7 | — |
| DPeHqHvDfCK | TOP#10 | 2025-10-06 | 109,5 | 430.324 | 6,09x | 1,46% | 0,015% | 232 | 17,5 (16,4) | sim | pt | 423 | 0 | 7 | 105,4 (96% do vídeo) |
| DQPWbVhkcuN | TOP#11 | 2025-10-25 | 85,3 | 405.834 | 5,75x | 2,63% | 0,036% | 210 | 11,3 (11,3) | sim | pt | 298 | 1 | 12 | — |
| DOzEZ2zkdL7 | TOP#12 | 2025-09-19 | 87,3 | 384.506 | 5,45x | 1,36% | 0,021% | 233 | 27,5 (23,4) | sim | pt | 338 | 2 | 2 | — |
| DTAv-KdkQBB | TOP#13 | 2026-01-02 | 76,0 | 351.986 | 4,98x | 2,55% | 0,011% | 227 | 15,0 (11,1) | sim | pt | 286 | 1 | 7 | 73,8 (97% do vídeo) |
| DQ92iwaEYl4 | TOP#14 | 2025-11-12 | 38,3 | 343.301 | 4,86x | 1,32% | 0,022% | 214 | 15,7 (14,1) | sim | pt | 136 | 0 | 1 | — |
| DTIR9ONkS-m | TOP#15 | 2026-01-05 | 65,3 | 330.071 | 4,67x | 2,33% | 0,094% | 181 | 19,3 (13,8) | sim** | pt | 196 | 1 | 2 | — |
| DdufhvOgh2n | RECENTE#1 | 2026-09-25 | 60,4 | 12.309 | 0,17x | 2,18% | 0,122% | 223 | 20,9 (20,9) | sim | pt | 226 | 1 | 5 | — (57,0: acesso ao prompt "aqui embaixo", sem verbo da lista) |
| Ddm0XEqDXcM | RECENTE#2 | 2026-09-22 | 142,7 | 31.166 | 0,44x | 3,40% | 0,064% | 207 | 13,5 (13,0) | sim | pt | 492 | 1 | 4 | — |
| DdkGyrlG9oO | RECENTE#3 | 2026-09-21 | 79,1 | 9.310 | 0,13x | 2,29% | 0,021% | 234 | 9,1 (8,3) | sim | pt | 308 | 0 | 2 | 75,7 (96% do vídeo) |
| DdZ09KIj-Op | RECENTE#4 | 2026-09-17 | 221,8 | 56.678 | 0,80x | 3,04% | 3,834% | 222 | 13,0 (12,2) | sim | pt | 819 | 0 | 11 | 216,5 (98% do vídeo) |
| DdXT4SkCCM5 | RECENTE#5 | 2026-09-16 | 89,7 | 7.559 | 0,11x | 2,65% | 0,066% | 216 | 12,7 (12,0) | sim | pt | 322 | 1 | 1 | — |
| DdHwQVLgY2A | RECENTE#6 | 2026-09-10 | 142,6 | 19.893 | 0,28x | 3,86% | 0,080% | 213 | 20,6 (20,2) | sim | pt | 506 | 3 | 3 | — |
| DdCqD4RCPTk | RECENTE#7 | 2026-09-08 | 53,9 | 14.674 | 0,21x | 2,37% | 0,020% | 220 | 16,7 (13,4) | sim | pt | 197 | 1 | 0 | — |
| Dc11gx6lXTx | RECENTE#8 | 2026-09-03 | 52,9 | 7.899 | 0,11x | 1,70% | 0,013% | 245 | 18,2 (18,2) | sim | pt | 216 | 1 | 1 | — |
| Dcv7xpPAWmq | RECENTE#9 | 2026-09-01 | 37,0 | 60.339 | 0,85x | 2,77% | 0,015% | 216 | 13,0 (13,0) | sim | pt | 133 | 0 | 1 | — |
| DcjwjLtj2Th | RECENTE#10 | 2026-08-27 | 68,7 | 53.709 | 0,76x | 2,95% | 4,325% | 225 | 15,7 (15,7) | sim | pt | 257 | 0 | 3 | 65,7 (96% do vídeo) |
| DcefJ7MlVZR | RECENTE#11 | 2026-08-25 | 53,6 | 42.396 | 0,60x | 2,47% | 0,083% | 209 | 22,4 (20,2) | sim | pt | 186 | 0 | 2 | — |
| DcMh8AyCSUe | RECENTE#12 | 2026-08-18 | 60,3 | 111.189 | 1,57x | 3,93% | 0,022% | 208 | 13,9 (13,9) | sim | pt | 209 | 1 | 3 | — |
| DcJ9EInDQYN | RECENTE#13 | 2026-08-17 | 58,9 | 14.527 | 0,21x | 2,11% | 0,076% | 224 | 23,4 (20,4) | sim | pt | 220 | 1 | 3 | — |
| Db-xS-AkSVq | RECENTE#14 | 2026-08-13 | 47,8 | 8.650 | 0,12x | 2,71% | 3,642% | 238 | 25,1 (25,1) | sim | pt | 189 | 0 | 0 | 45,8 (96% do vídeo) |
| Db8azYFCAdB | RECENTE#15 | 2026-08-12 | 60,0 | 251.299 | 3,56x | 2,03% | 0,070% | 94* | 0,0 (0,0) | sim* | pt | 141 | 3 | 6 | — |

\* RECENTE#15: diálogo com um agente de voz (as respostas são da IA); o ritmo e as contagens misturam as duas vozes. \*\* TOP#15: inclui 2 frases de amostra de voz sintética no fim. Nenhum dos 30 é provável anúncio.

| grupo | mediana views | mediana x | mediana dur (s) | mediana likes/views | mediana coment./views | mediana pal/min (faixa) | mediana cortes/min bruto (agrup.) | mediana palavras | mediana números | CTA falado | colab. @asimov.academy |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TOP 15 | 496.918 | 7,04x | 80,2 | 2,13% | 0,019% | 220 (181–267) | 15,0 (13,8) | 298 | 3,0 | 3 | 1 |
| RECENTES 15 | 19.893 | 0,28x | 60,3 | 2,65% | 0,070% | 221 (207–245) | 15,7 (13,9) | 223 | 2,5 | 4 | 6 |

(Palavras, ritmo e números dos recentes sem RECENTE#15.)

**Formato visual (medida extra): quanto tempo o rosto dele aparece e o que abre o vídeo**

| código | grupo | rosto na tela (% do tempo) | tela dividida | rosto cheio | sem rosto de frente | o que ocupa o 1º frame |
|---|---|---|---|---|---|---|
| DRVZ9YskX9R | TOP#1 | 45% | 6% | 39% | 55% | print de código + rosto embaixo |
| DRkhY-3EXSH | TOP#2 | 49% | 3% | 46% | 51% | print do ChatGPT + rosto embaixo |
| DVL-2GtjEmn | TOP#3 | 3% | 1% | 2% | 97% | objeto (a caneta) + rosto |
| DP6chn3je86 | TOP#4 | 83% | 58% | 25% | 17% | print do site automatizado + rosto embaixo |
| DQo2ZajkcsJ | TOP#5 | 34% | 22% | 12% | 66% | print do GitHub, sem rosto |
| DRLBPLlkanH | TOP#6 | 0% | 0% | 0% | 100% | B-roll dele de perfil no computador |
| DPlyTlMkSSg | TOP#7 | 36% | 9% | 27% | 64% | print de post do Reddit + rosto pequeno |
| DUvhpvDk-ju | TOP#8 | 56% | 38% | 18% | 44% | print do site resultado, sem rosto |
| DSUwnmTkT0R | TOP#9 | 81% | 24% | 56% | 19% | rosto cheio (caixinha de pergunta aos 2 s) |
| DPeHqHvDfCK | TOP#10 | 38% | 2% | 36% | 62% | vídeo de demonstração + rosto embaixo |
| DQPWbVhkcuN | TOP#11 | 62% | 12% | 50% | 38% | B-roll do computador (placas de vídeo) |
| DOzEZ2zkdL7 | TOP#12 | 53% | 4% | 49% | 47% | B-roll dele na loja de roupas |
| DTAv-KdkQBB | TOP#13 | 47% | 15% | 32% | 53% | rosto cheio |
| DQ92iwaEYl4 | TOP#14 | 49% | 22% | 27% | 51% | logo do Lovable riscado + rosto embaixo |
| DTIR9ONkS-m | TOP#15 | 55% | 13% | 42% | 45% | print de site + rosto embaixo |
| DdufhvOgh2n | RECENTE#1 | 68% | 56% | 12% | 32% | animação 3D (resultado) + rosto embaixo |
| Ddm0XEqDXcM | RECENTE#2 | 70% | 27% | 43% | 30% | gráfico + rosto embaixo |
| DdkGyrlG9oO | RECENTE#3 | 77% | 50% | 27% | 23% | print do site "antes" + rosto embaixo |
| DdZ09KIj-Op | RECENTE#4 | 41% | 19% | 22% | 59% | ilustração SKILL.MD + rosto embaixo |
| DdXT4SkCCM5 | RECENTE#5 | 85% | 66% | 19% | 15% | print de preços + card de comentário + rosto |
| DdHwQVLgY2A | RECENTE#6 | 80% | 45% | 35% | 20% | terminal + card de comentário + rosto |
| DdCqD4RCPTk | RECENTE#7 | 69% | 55% | 15% | 31% | site + caixinha de pergunta + rosto |
| Dc11gx6lXTx | RECENTE#8 | 64% | 47% | 17% | 36% | documento + card de comentário + rosto |
| Dcv7xpPAWmq | RECENTE#9 | 86% | 61% | 26% | 14% | print do GitHub + rosto embaixo |
| DcjwjLtj2Th | RECENTE#10 | 74% | 39% | 36% | 26% | cartela-título + rosto embaixo |
| DcefJ7MlVZR | RECENTE#11 | 72% | 46% | 26% | 28% | print do GitHub + rosto embaixo |
| DcMh8AyCSUe | RECENTE#12 | 66% | 56% | 10% | 34% | ícone do app + card de comentário + rosto |
| DcJ9EInDQYN | RECENTE#13 | 75% | 44% | 31% | 25% | logo + card de comentário + rosto |
| Db-xS-AkSVq | RECENTE#14 | 83% | 62% | 21% | 17% | animação da aula (resultado) + rosto embaixo |
| Db8azYFCAdB | RECENTE#15 | 34% | 0% | 34% | 66% | manchete + demo filmada no notebook, sem rosto |

- Mediana do tempo com rosto: TOP 49% (tela dividida 12%; rosto cheio 32%); recentes 72% (tela dividida 47%; rosto cheio 26%).
- Nos TOP, metade do tempo a tela mostra a prova (print de GitHub/site/ChatGPT, resultado gerado, B-roll do objeto) com a voz dele por cima; em 2 dos 15 o rosto quase não aparece (TOP#3 3%, TOP#6 0%). Nos recentes, a tela dividida (print em cima, rosto embaixo) virou o padrão.
- 1º frame: rosto visível em 11 de 15 do TOP e 14 de 15 recentes; print de tela em 7 e 8; manchete, cartela ou pergunta de seguidor legível em 1 e 8.
- Áudio: som original nos 30; nenhuma música licenciada, nenhuma parceria paga.

## 3. Ganchos: primeiros 5 s e texto na tela no 1º frame

| código | grupo | tipo de abertura | o que é dito em 0–5 s (paráfrase) | texto na tela no 1º frame (OCR t=0 / frame 0,4 s) | tipo do texto |
|---|---|---|---|---|---|
| DRVZ9YskX9R | TOP#1 | pergunta retórica sobre tendência | Pergunta se um formato novo (TOON) aposenta o prompt em JSON | código JSON de exemplo + legenda «aqui agora» (0,4 s: «Será que esse») | print + legenda |
| DRkhY-3EXSH | TOP#2 | lista numerada | Erro de iniciante: estudar IA sem conhecer os 4 caminhos | print do ChatGPT: «Escreva um artigo sobre inteligencia artificial no esporte» + resposta; legenda «começando a» | print + legenda |
| DVL-2GtjEmn | TOP#3 | resultado pronto + "é assim que eu fiz" | Site pronto criado a partir de uma foto da caneta, em menos de 1 h | legenda «transformei uma simples» (0,4 s: «E é assim que eu») + caneta na mão | objeto + legenda |
| DP6chn3je86 | TOP#4 | ferramenta ou método + o que resolve | Biblioteca que automatiza a navegação na web só com um prompt | site de supermercado sendo navegado + legenda «essa biblioteca» | print + legenda |
| DQo2ZajkcsJ | TOP#5 | ferramenta ou método + o que resolve | Microsoft solta conversor grátis de PDF, planilha e imagem para Markdown | README do GitHub «MarkItDown» + legenda «A Microsoft»; sem rosto | print + legenda |
| DRLBPLlkanH | TOP#6 | ferramenta ou método + o que resolve | Anuncia a melhor estratégia que achou para gerar interfaces de app | legenda «estratégia que» (0,4 s: «A melhor») sobre B-roll dele no computador | B-roll + legenda |
| DPlyTlMkSSg | TOP#7 | debate / opinião | Traz a briga da comunidade: N8N ou Python para criar agentes | post do Reddit com o título «n8n ou Python puro?» + rosto pequeno | print (título em pergunta) |
| DUvhpvDk-ju | TOP#8 | lista numerada | Escala de 3 níveis para sites criados com IA; abre no básico | site «A caneta mais tecnológica do mundo.» + legenda «sites feitos com IA»; sem rosto | print + legenda |
| DSUwnmTkT0R | TOP#9 | resposta a pergunta de seguidor | Antecipa a crítica e lê o desafio de um dev veterano | legenda «ser criticado aqui, mas» + rosto; aos 2 s entra a caixinha «Faça uma pergunta» com o desafio | legenda (card aos 2 s) |
| DPeHqHvDfCK | TOP#10 | lista numerada | Promete 5 projetos para aprender agentes, em ordem de dificuldade | nenhum texto sobreposto (só o rótulo «SERSANI» do produto no vídeo de demonstração) | sem texto |
| DQPWbVhkcuN | TOP#11 | bastidor / objeto | Apresenta o supercomputador que a equipe montou só para rodar IA | legenda «o supercomputador» sobre as placas «GEFORCE RTX» | B-roll + legenda |
| DOzEZ2zkdL7 | TOP#12 | resultado pronto + "é assim que eu fiz" | Descoberta pessoal: experimentar roupas da loja usando apenas uma foto | legenda «uma forma de» sobre B-roll dele na loja | B-roll + legenda |
| DTAv-KdkQBB | TOP#13 | lista numerada | Promete 3 dicas que dobram a produtividade programando em Python | «3 dicas» (legenda da fala) + rosto cheio, mostrando o número com a mão | legenda |
| DQ92iwaEYl4 | TOP#14 | ferramenta ou método + o que resolve | Manda largar o Lovable: o Google soltou alternativa grátis de design | logo do Lovable riscado em vermelho + rosto | gráfico com a marca |
| DTIR9ONkS-m | TOP#15 | ferramenta ou método + o que resolve | Voz com IA deixou de custar; cita ElevenLabs e OpenAI como pagos | site de locução «Create the perfect voiceover for your video» + rosto (0,4 s: página da AWS + «precisa») | print + legenda |
| DdufhvOgh2n | RECENTE#1 | resultado pronto + "é assim que eu fiz" | O que está no alto da tela é slide, não jogo nem filme | legenda «vendo aqui em cima» + animação 3D + rosto | resultado + legenda |
| Ddm0XEqDXcM | RECENTE#2 | ferramenta ou método + o que resolve | Apresenta a IA do momento, que curiosamente não escreve texto | gráfico «Intelligence / Cost» comparando modelos + legenda «é» | print + legenda |
| DdkGyrlG9oO | RECENTE#3 | resultado pronto + "é assim que eu fiz" | Mostra site sem graça virando site com cara de agência | site «antes»: «Negocie cripto com velocidade e segurança» + legenda «transforma esse site» | print + legenda |
| DdZ09KIj-Op | RECENTE#4 | resultado pronto + "é assim que eu fiz" | Diz ter criado skill para um grande problema de design com IA | ícone «SKILL.MD» + legenda «skill que resolve» | ilustração + legenda |
| DdXT4SkCCM5 | RECENTE#5 | resposta a pergunta de seguidor | Lê a dúvida: por que assinar ChatGPT/Claude se há hub de IAs? | print de preços do ChatGPT + card de comentário com a dúvida (35 palavras, parafraseada na coluna ao lado) | print + card de comentário |
| DdHwQVLgY2A | RECENTE#6 | resposta a pergunta de seguidor | Pergunta qual skill do Claude escolheria se só pudesse ter uma | terminal do Claude Code; aos 0,4 s entra o card de comentário com a pergunta (13 palavras, parafraseada) | print + card de comentário |
| DdCqD4RCPTk | RECENTE#7 | resposta a pergunta de seguidor | Lê pergunta sobre site secreto de prompts e confirma que existe | site «PROMPTS IA BIBLIOTECA» + caixinha «Faça uma pergunta» com a pergunta | print + caixinha de pergunta |
| Dc11gx6lXTx | RECENTE#8 | resposta a pergunta de seguidor | Pergunta se engenharia de prompt morreu e já relativiza | documento de prompt («CONTEXTO…») + card «Engenharia de prompts morreu mesmo?» | print + card de comentário |
| Dcv7xpPAWmq | RECENTE#9 | ferramenta ou método + o que resolve | Arquivo do GitHub, 30 mil estrelas, que tira o tom de IA | repositório do GitHub (Humanizer) + legenda «Existe» | print + legenda |
| DcjwjLtj2Th | RECENTE#10 | lista numerada | Proíbe usar o Claude Code sem cinco plugins | cartela «5 plugins ESSENCIAIS» + legenda «Não use o» | cartela-título |
| DcefJ7MlVZR | RECENTE#11 | ferramenta ou método + o que resolve | Um dos melhores jeitos que achou para gastar menos tokens | repositório «Graphify» no GitHub («#3 Repository Of The Day») + legenda «uma» | print + legenda |
| DcMh8AyCSUe | RECENTE#12 | resposta a pergunta de seguidor | Lê a dúvida: como saber se o app feito com IA é seguro | ícone do app + card «Como saber se o aplicativo q criei usando ia é seguro?» | card de comentário |
| DcJ9EInDQYN | RECENTE#13 | resposta a pergunta de seguidor | Responde a quem pediu Cursor de graça: a saída é o OpenRouter | logo do Cursor + card «Como que vc usa o Cursor de graça??» | card de comentário |
| Db-xS-AkSVq | RECENTE#14 | resultado pronto + "é assim que eu fiz" | Mostra o Claude virando estúdio de animação para aulas | animação de aula «O átomo e seus elétrons» + legenda «transformei o» | resultado + legenda |
| Db8azYFCAdB | RECENTE#15 | demo de diálogo com agente de voz | Abre em diálogo: chama o agente de voz, que responde | manchete «Os Agentes de IA que você já pode criar são bizarros» + demo no notebook; sem rosto | manchete |

**Views por tipo de abertura**

| tipo de abertura | grupo | n | mediana views | mínimo | máximo |
|---|---|---|---|---|---|
| ferramenta ou método + o que resolve | TOP | 5 | 811.608 | 330.071 | 948.846 |
| lista numerada | TOP | 4 | 463.621 | 351.986 | 1.094.958 |
| resultado pronto + "é assim que eu fiz" | TOP | 2 | 739.056 | 384.506 | 1.093.606 |
| pergunta retórica sobre tendência | TOP | 1 | 1.375.079 | 1.375.079 | 1.375.079 |
| debate / opinião | TOP | 1 | 751.835 | 751.835 | 751.835 |
| resposta a pergunta de seguidor | TOP | 1 | 435.430 | 435.430 | 435.430 |
| bastidor / objeto | TOP | 1 | 405.834 | 405.834 | 405.834 |
| resposta a pergunta de seguidor | RECENTES | 6 | 14.600,5 | 7.559 | 111.189 |
| resultado pronto + "é assim que eu fiz" | RECENTES | 4 | 10.809,5 | 8.650 | 56.678 |
| ferramenta ou método + o que resolve | RECENTES | 3 | 42.396 | 31.166 | 60.339 |
| demo de diálogo com agente de voz | RECENTES | 1 | 251.299 | 251.299 | 251.299 |
| lista numerada | RECENTES | 1 | 53.709 | 53.709 | 53.709 |

Contagens do gancho:

- Início da fala: 29 de 30 começam a falar em 0,0 s (RECENTE#15 em 0,2 s). Nenhum abre com saudação, "fala galera", nome ou apresentação.
- "aqui" nos trechos que começam até 5 s: 15 de 30 (TOP 7, recentes 8): a 1ª frase aponta para o que está na tela ("esse aqui", "essa aqui", "aqui em cima"). Número nos primeiros 5 s: 9 de 30 (TOP 5, recentes 4); 5 deles são a quantidade da lista (4 caminhos, 3 níveis, 5 projetos, 3 dicas, 5 plugins).
- Abre com pergunta falada: 6 de 29 (TOP#1 retórica; RECENTE#5, #6, #7, #8 e #12 leem a pergunta de um seguidor), sem contar o "tu tá aí?" do diálogo de RECENTE#15. Nos 7 vídeos de resposta a seguidor, 5 respostas começam com "Cara," logo depois da pergunta (TOP#9, RECENTE#5 a #8).
- Texto no 1º frame: 29 de 30 (só TOP#10 sem texto sobreposto). A legenda palavra a palavra da fala (1 a 4 palavras numa caixa preta no meio da tela) já está no 1º frame em 21 de 30; nos outros o texto é o do próprio print, uma cartela ou um card de comentário. Manchete ou pergunta legível no 1º frame: 1 de 15 no TOP (TOP#7) e 8 de 15 nos recentes.
- Resposta a pergunta de seguidor: 1 no TOP (TOP#9, 435.430) e 6 nos recentes, com mediana de 14.600,5 contra 42.396 dos outros 9 recentes.
- Moldes (com lacunas): "[Empresa] liberou uma ferramenta grátis, [nome], que [faz tarefa chata ou cara]"; "Essa aqui é [a melhor forma] que eu encontrei de [resultado]"; "É assim que eu transformei [insumo simples] em [resultado de agência], em menos de [tempo]"; "[N] [níveis/projetos/dicas] para [objetivo]. Número 1: [...]"; "Será que [novidade] é o fim de [prática popular]?" (e fecha com "provavelmente não"); "Esqueça [ferramenta famosa], porque [empresa] liberou [alternativa grátis]".

## 4. Linguagem (29 vídeos com fala dele em pt e flag ok; 8.390 palavras; 446 frases)

Fora: RECENTE#15 (diálogo com agente de voz) e as 2 frases de voz sintética de TOP#15. TOP#1 a #15 e RECENTE#4 a #14 pelo mlx-whisper-large-v3-turbo; RECENTE#1 a #3 pelo faster-whisper-small.

### 4.1 Top 30 expressões recorrentes de 2 a 4 palavras

Contadas dentro da frase, descartando combinações feitas só de palavras vazias (artigo, preposição, pronome, conjunção, formas de ser/estar/ter/ir/haver) e as que só existem dentro de outra maior com a mesma contagem. Ordem: nº de vídeos, depois ocorrências. "Cloud" é como o Whisper grafa Claude.

| # | expressão | vídeos (de 29) | ocorrências | função | onde |
|---|---|---|---|---|---|
| 1 | a gente | 16 | 49 | pronome coletivo | TOP#1, TOP#2, TOP#3, TOP#8, TOP#9, TOP#10, TOP#11, TOP#13, RECENTE#1, RECENTE#2, RECENTE#3, RECENTE#4, RECENTE#5, RECENTE#6, RECENTE#8, RECENTE#14 |
| 2 | aqui é | 14 | 19 | dêixis (aponta a tela) | TOP#1, TOP#2, TOP#3, TOP#6, TOP#8, TOP#10, TOP#11, TOP#12, TOP#13, RECENTE#2, RECENTE#4, RECENTE#7, RECENTE#11, RECENTE#13 |
| 3 | inteligência artificial | 11 | 19 | tema | TOP#2, TOP#7, TOP#10, TOP#11, TOP#12, RECENTE#4, RECENTE#5, RECENTE#7, RECENTE#9, RECENTE#12, RECENTE#13 |
| 4 | o cloud | 10 | 16 | tema (o Claude) | TOP#6, TOP#9, RECENTE#1, RECENTE#2, RECENTE#4, RECENTE#5, RECENTE#6, RECENTE#7, RECENTE#9, RECENTE#10 |
| 5 | e aí | 9 | 17 | ponte | TOP#3, TOP#6, TOP#7, TOP#8, TOP#10, RECENTE#3, RECENTE#4, RECENTE#12, RECENTE#13 |
| 6 | modelos de | 9 | 14 | tema | TOP#1, TOP#2, TOP#5, TOP#9, TOP#10, TOP#11, TOP#15, RECENTE#3, RECENTE#13 |
| 7 | que a gente | 9 | 13 | pronome coletivo | TOP#1, TOP#2, TOP#3, TOP#8, RECENTE#2, RECENTE#4, RECENTE#6, RECENTE#8, RECENTE#14 |
| 8 | por exemplo | 9 | 11 | ponte / exemplo | TOP#5, TOP#12, TOP#13, RECENTE#2, RECENTE#4, RECENTE#6, RECENTE#8, RECENTE#13, RECENTE#14 |
| 9 | ao invés | 9 | 9 | contraste | TOP#1, TOP#6, TOP#8, TOP#13, RECENTE#1, RECENTE#3, RECENTE#4, RECENTE#6, RECENTE#7 |
| 10 | de inteligência artificial | 9 | 9 | tema | TOP#2, TOP#7, TOP#10, TOP#11, TOP#12, RECENTE#4, RECENTE#5, RECENTE#12, RECENTE#13 |
| 11 | só que | 8 | 15 | virada (= "mas") | TOP#1, RECENTE#2, RECENTE#4, RECENTE#5, RECENTE#6, RECENTE#7, RECENTE#8, RECENTE#13 |
| 12 | isso aqui | 8 | 14 | dêixis | TOP#2, TOP#9, TOP#12, TOP#13, RECENTE#2, RECENTE#3, RECENTE#4, RECENTE#11 |
| 13 | tu pode | 8 | 13 | 2ª pessoa + possibilidade | TOP#2, TOP#6, TOP#10, TOP#14, RECENTE#7, RECENTE#11, RECENTE#12, RECENTE#13 |
| 14 | não é | 8 | 10 | negação / contraste | TOP#11, TOP#13, RECENTE#1, RECENTE#2, RECENTE#4, RECENTE#5, RECENTE#8, RECENTE#9 |
| 15 | a gente vai | 7 | 14 | passo a passo | TOP#1, TOP#8, TOP#10, RECENTE#3, RECENTE#4, RECENTE#6, RECENTE#8 |
| 16 | cloud code | 7 | 10 | tema (Claude Code) | TOP#6, TOP#13, RECENTE#2, RECENTE#4, RECENTE#6, RECENTE#10, RECENTE#11 |
| 17 | criar um | 7 | 10 | verbo de fazer | TOP#2, TOP#6, TOP#8, TOP#10, RECENTE#6, RECENTE#8, RECENTE#10 |
| 18 | ao invés de | 7 | 7 | contraste | TOP#6, TOP#8, TOP#13, RECENTE#1, RECENTE#3, RECENTE#6, RECENTE#7 |
| 19 | menos de | 7 | 7 | prova de tempo | TOP#1, TOP#3, TOP#4, TOP#8, TOP#13, RECENTE#3, RECENTE#6 |
| 20 | esse aqui | 6 | 12 | dêixis | TOP#1, TOP#3, TOP#6, TOP#8, TOP#11, RECENTE#7 |
| 21 | o resultado | 6 | 9 | prova | TOP#3, TOP#4, TOP#6, TOP#8, RECENTE#1, RECENTE#4 |
| 22 | do mundo | 6 | 8 | superlativo | TOP#15, RECENTE#4, RECENTE#5, RECENTE#6, RECENTE#10, RECENTE#13 |
| 23 | o design | 6 | 7 | tema | TOP#3, TOP#6, TOP#8, TOP#14, RECENTE#3, RECENTE#8 |
| 24 | você pode | 6 | 7 | 2ª pessoa + possibilidade | TOP#2, TOP#7, TOP#10, TOP#13, RECENTE#11, RECENTE#14 |
| 25 | aqui embaixo | 6 | 6 | CTA | TOP#2, TOP#10, RECENTE#1, RECENTE#3, RECENTE#4, RECENTE#10 |
| 26 | em menos de | 6 | 6 | prova de tempo | TOP#1, TOP#3, TOP#4, TOP#8, TOP#13, RECENTE#3 |
| 27 | esses modelos | 6 | 6 | tema | TOP#2, TOP#10, TOP#12, RECENTE#3, RECENTE#5, RECENTE#13 |
| 28 | o mais | 6 | 6 | superlativo ("o mais legal") | TOP#5, TOP#6, TOP#15, RECENTE#2, RECENTE#9, RECENTE#10 |
| 29 | na hora | 5 | 12 | ponte ("na hora de") | TOP#5, TOP#13, RECENTE#1, RECENTE#4, RECENTE#8 |
| 30 | muito mais | 5 | 11 | intensificador | TOP#7, RECENTE#1, RECENTE#4, RECENTE#6, RECENTE#8 |

Fora do top 30, com 5 vídeos cada: "esse aqui é", "isso aqui é", "design system", "extrair o", "de linguagem", "dentro do". Prova social numérica aparece em 4 vídeos ("mil estrelas" no GitHub: TOP#1, TOP#4, RECENTE#6, RECENTE#9). "Grátis/gratuito/de graça/open source" aparece em 4 do TOP (mediana 611.605,5) e 2 recentes (62.858).

### 4.2 Tamanho de frase

- Por pontuação do Whisper: média **18,8** palavras, mediana **16** (446 frases; 45 com até 5 palavras, 160 com 20 ou mais). TOP: média 16,7, mediana 14 (246 frases); recentes: média 21,4, mediana 17 (200 frases).
- Por trecho do Whisper (pausa de respiração): média 11,5, mediana 11 palavras (730 trechos). Como a pontuação falha em trechos longos (TOP#6 e TOP#14 viram 4 a 5 "frases" gigantes), a mediana por trecho é a medida mais estável.

### 4.3 Tratamento do espectador

| recorte | vídeos | frases | frases com "você" | frases com "tu" | frases com 2ª pessoa (você/tu/te/teu/tua/ti) | "você(s)" | "tu" | "te/teu/tua/ti" | "a gente" |
|---|---|---|---|---|---|---|---|---|---|
| TOP | 15 | 246 | 27 (11,0%) | 28 (11,4%) | 67 (27,2%) | 34 | 36 | 40 | 17 |
| RECENTES | 14 | 200 | 35 (17,5%) | 16 (8,0%) | 61 (30,5%) | 49 | 25 | 27 | 32 |
| total | 29 | 446 | 62 (13,9%) | 44 (9,9%) | 128 (28,7%) | 83 | 61 | 67 | 49 |

"a gente": 49 vezes (5,8 por mil palavras), em 16 de 29 vídeos, mais 2 "da gente". Usa "a gente" como narrador do passo a passo ("a gente vai…" 14 vezes em 7 vídeos). "tu" e "você" convivem no mesmo vídeo em 13 dos 29 (gaúcho: "tu pode", "tu vai", "se tu quer").

### 4.4 Marcadores de oralidade

| marcador | ocorrências | por mil palavras | vídeos (de 29) | observação |
|---|---|---|---|---|
| cara | 22 | 2,6 | 13 | 14 como interjeição, em 11 vídeos ("Cara, [resposta]"); 8 como substantivo ("esse cara" = o computador, "o cara" = a IA, "cara de IA") |
| tá | 14 | 1,7 | 11 | contração de "está"; como pedido de confirmação ("…, tá?") só 1 vez |
| olha | 4 | 0,5 | 4 | as 4 apontam o resultado na tela ("olha só a animação", "olha o resultado") |
| sabe | 4 | 0,5 | 4 | sempre verbo ("não sei se tu sabe"), nunca marcador |
| né | 1 | 0,1 | 1 | "Legal, né?" fechando TOP#8 |
| galera | 1 | 0,1 | 1 | substantivo ("a galera que lê papers"), nunca vocativo |
| mano | 0 | 0,0 | 0 |  |
| gente (vocativo) | 0 | 0,0 | 0 | as 5 ocorrências fora de "a gente" são "muita gente" (3) e "da gente" (2) |

Outros marcadores que aparecem nos dados:

| palavra | ocorrências | por mil palavras | vídeos (de 29) |
|---|---|---|---|
| aqui | 118 | 14,1 | 25 |
| esse/essa/isso aqui | 31 | 3,7 | 15 |
| porque | 30 | 3,6 | 19 |
| então | 21 | 2,5 | 12 |
| e aí | 17 | 2,0 | 9 |
| só que | 15 | 1,8 | 8 |
| número (1, 2, 3…) numerando a lista | 14 | 1,7 | 5 |
| por exemplo | 11 | 1,3 | 9 |
| ao invés de / em vez de | 10 | 1,2 | 10 |
| eu encontrei / eu percebi / eu tenho percebido | 7 | 0,8 | 6 |
| de repente | 6 | 0,7 | 3 |
| bom, (abrindo frase) | 6 | 0,7 | 6 |
| o mais legal / a melhor parte / o legal é | 6 | 0,7 | 5 |
| bizarro / absurdo | 4 | 0,5 | 3 |
| tipo | 4 | 0,5 | 3 |
| o segredo | 3 | 0,4 | 2 |
| enfim | 3 | 0,4 | 3 |
| inclusive | 3 | 0,4 | 3 |
| na prática | 3 | 0,4 | 3 |
| basicamente | 2 | 0,2 | 2 |
| ou seja | 2 | 0,2 | 2 |
| imagina | 2 | 0,2 | 2 |
| repara | 2 | 0,2 | 2 |
| véi | 1 | 0,1 | 1 |

"aqui" é o marcador mais denso (14,1 por mil palavras; 1 a cada 71 palavras): a fala foi escrita para apontar a imagem ("esse aqui", "isso aqui", "aqui embaixo").

### 4.5 Construção "não é X, é Y"

- **Na fala (29 vídeos)**: 1 na forma exata, em série ("não é [A], não é [B], é [C]", RECENTE#1), mais 1 citada como exemplo de vício de texto de IA (RECENTE#9). 10 variantes em 9 vídeos: "não [faz X], mas [faz Y]" (TOP#2), "nem parece [X], mas sim [Y]" (TOP#8), "não é explicado por [X]… e sim por [Y]" (TOP#11), "não é [X], usa [Y]" e "não [conversa], [decide]" (RECENTE#2), "não é porque [X], mas é porque [Y]" (RECENTE#4), "não depende só de [X]; depende de [Y]" (RECENTE#5), "não é que [X], mas [Y]" (RECENTE#8), "não tenta [X]; faz o contrário" (RECENTE#9), "não funciona como [X]; age como [Y]" (RECENTE#12). Total 11 em 10 de 29 vídeos (1,3 por mil palavras): 3 no TOP, 8 nos recentes.
- **O contraste preferido é outro**: "ao invés de [jeito comum], [jeito melhor]" aparece em 10 de 29 vídeos (TOP#1, #6, #8, #13; RECENTE#1, #3, #4, #6, #7, #11), quase sempre para apresentar o método.
- **Nas legendas (30)**: 13 usam a construção. Exata ("não é X. É Y"): 6 (TOP#3, TOP#7, TOP#9, RECENTE#1, RECENTE#6, RECENTE#9). Variantes: 10 legendas ("não está em X. Está em Y", "não porque X, mas porque Y", "não é só X", "não está usando só X. Está usando Y", "não são X. Eles fazem Y", "não é X. Ele faz Y"). Por grupo: 3 de 15 no TOP e 10 de 15 nos recentes. "Em vez de / ao invés de" em 6 legendas.

### 4.6 Palavras por minuto e perfil de cada vídeo com fala

| vídeo | motor | palavras | fala (s) | pal/min (fala) | pal/min (duração total) | frases | média pal/frase | mediana | "tu" | "você" | "a gente" | "aqui" | "cara" | números | "?" |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TOP#1 | large-v3-turbo | 312 | 85,3 | 220 | 219 | 19 | 16,4 | 19,0 | 0 | 1 | 3 | 5 | 0 | 3 | 4 |
| TOP#2 | large-v3-turbo | 309 | 89,7 | 207 | 207 | 15 | 20,6 | 16,0 | 3 | 5 | 2 | 4 | 0 | 1 | 1 |
| TOP#3 | large-v3-turbo | 335 | 75,3 | 267 | 267 | 22 | 15,3 | 14,5 | 0 | 0 | 1 | 7 | 0 | 8 | 0 |
| TOP#4 | large-v3-turbo | 179 | 53,9 | 199 | 199 | 11 | 16,3 | 13,0 | 0 | 1 | 0 | 2 | 0 | 3 | 0 |
| TOP#5 | large-v3-turbo | 136 | 43,0 | 190 | 189 | 7 | 19,4 | 18,0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| TOP#6 | large-v3-turbo | 218 | 57,8 | 226 | 226 | 5 | 43,8 | 16,0 | 2 | 3 | 0 | 3 | 2 | 1 | 0 |
| TOP#7 | large-v3-turbo | 331 | 89,4 | 222 | 222 | 24 | 13,8 | 10,0 | 6 | 6 | 0 | 1 | 0 | 5 | 3 |
| TOP#8 | large-v3-turbo | 348 | 89,6 | 233 | 232 | 24 | 14,6 | 12,5 | 3 | 1 | 6 | 6 | 0 | 7 | 1 |
| TOP#9 | large-v3-turbo | 283 | 80,1 | 212 | 212 | 16 | 17,8 | 16,0 | 0 | 5 | 1 | 3 | 3 | 7 | 1 |
| TOP#10 | large-v3-turbo | 423 | 109,3 | 232 | 232 | 28 | 15,1 | 14,0 | 11 | 4 | 1 | 11 | 1 | 7 | 0 |
| TOP#11 | large-v3-turbo | 298 | 85,1 | 210 | 210 | 19 | 15,7 | 16,0 | 0 | 6 | 2 | 4 | 2 | 12 | 1 |
| TOP#12 | large-v3-turbo | 338 | 87,0 | 233 | 232 | 16 | 21,2 | 17,0 | 0 | 0 | 0 | 8 | 2 | 2 | 2 |
| TOP#13 | large-v3-turbo | 286 | 75,8 | 227 | 226 | 28 | 10,2 | 7,0 | 4 | 1 | 1 | 5 | 1 | 7 | 1 |
| TOP#14 | large-v3-turbo | 136 | 38,1 | 214 | 213 | 4 | 34,0 | 35,5 | 5 | 0 | 0 | 0 | 1 | 1 | 0 |
| TOP#15 | large-v3-turbo | 196 | 65,0 | 181 | 180 | 8 | 22,2 | 20,5 | 0 | 1 | 0 | 0 | 0 | 2 | 1 |
| RECENTE#1 | small | 226 | 60,7 | 223 | 225 | 8 | 28,2 | 30,0 | 1 | 2 | 2 | 5 | 0 | 5 | 1 |
| RECENTE#2 | small | 492 | 142,4 | 207 | 207 | 22 | 22,4 | 15,5 | 0 | 8 | 4 | 7 | 0 | 4 | 1 |
| RECENTE#3 | small | 308 | 78,9 | 234 | 234 | 11 | 28,0 | 25,0 | 3 | 1 | 5 | 8 | 0 | 2 | 0 |
| RECENTE#4 | large-v3-turbo | 819 | 221,6 | 222 | 222 | 47 | 17,5 | 15,0 | 1 | 9 | 4 | 12 | 4 | 11 | 0 |
| RECENTE#5 | large-v3-turbo | 322 | 89,6 | 216 | 215 | 14 | 23,0 | 18,5 | 2 | 3 | 4 | 4 | 1 | 1 | 1 |
| RECENTE#6 | large-v3-turbo | 506 | 142,3 | 213 | 213 | 21 | 24,1 | 16,0 | 0 | 4 | 7 | 6 | 2 | 3 | 3 |
| RECENTE#7 | large-v3-turbo | 197 | 53,8 | 220 | 219 | 11 | 17,9 | 12,0 | 3 | 4 | 0 | 1 | 1 | 0 | 1 |
| RECENTE#8 | large-v3-turbo | 216 | 52,8 | 245 | 245 | 6 | 36,0 | 31,0 | 0 | 0 | 5 | 0 | 1 | 1 | 1 |
| RECENTE#9 | large-v3-turbo | 133 | 36,9 | 216 | 216 | 7 | 19,0 | 17,0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 |
| RECENTE#10 | large-v3-turbo | 257 | 68,4 | 225 | 225 | 16 | 16,1 | 12,0 | 0 | 8 | 0 | 4 | 0 | 3 | 0 |
| RECENTE#11 | large-v3-turbo | 186 | 53,4 | 209 | 208 | 9 | 21,0 | 18,0 | 4 | 2 | 0 | 4 | 0 | 2 | 0 |
| RECENTE#12 | large-v3-turbo | 209 | 60,2 | 208 | 208 | 13 | 16,1 | 14,0 | 3 | 0 | 0 | 3 | 0 | 3 | 1 |
| RECENTE#13 | large-v3-turbo | 220 | 58,9 | 224 | 224 | 9 | 24,8 | 13,0 | 8 | 1 | 0 | 3 | 0 | 3 | 1 |
| RECENTE#14 | large-v3-turbo | 189 | 47,6 | 238 | 237 | 6 | 31,5 | 28,5 | 0 | 6 | 1 | 1 | 0 | 0 | 0 |
| RECENTE#15 | large-v3-turbo | 141 | 89,8 | 94* | 141 | — | — | — | — | — | — | — | — | 6 | 3 |

\* diálogo com agente de voz. TOP#15: palavras e ritmo contam as 2 frases de voz sintética; frases e contagens de palavras-marcador, não. Mediana TOP: 220 pal/min (faixa 181–267), 298 palavras, 80,2 s. Recentes (14): 221 pal/min (faixa 207–245). O ritmo sobre a duração total fica a até 2 pal/min do ritmo sobre a fala: não há silêncio nem vinheta. Perguntas: 25 "?" nos 29 vídeos (8.408 palavras; 0,30 por 100 palavras; 4 das 25 em TOP#1, que se estrutura em perguntas retóricas). Números: 105 no total; mediana 3 por vídeo no TOP (0 a 12) e 2,5 nos recentes (0 a 11).

## 5. Legenda (caption) dos 30

| código | grupo | caracteres | linhas | 1ª linha (caracteres) | emojis | hashtags | CTA na legenda | "?" | menção @ | "não é X, é Y" |
|---|---|---|---|---|---|---|---|---|---|---|
| DRVZ9YskX9R | TOP#1 | 1.011 | 8 | 251 | 0 | 0 | — | 0 | — | — |
| DRkhY-3EXSH | TOP#2 | 1.560 | 17 | 117 | 0 | 0 | link na bio | 0 | — | — |
| DVL-2GtjEmn | TOP#3 | 1.036 | 15 | 9 | 0 | 0 | — | 0 | — | exata + variante |
| DP6chn3je86 | TOP#4 | 305 | 1 | 305 | 0 | 0 | — | 0 | — | — |
| DQo2ZajkcsJ | TOP#5 | 1.007 | 5 | 262 | 0 | 0 | — | 1 | — | — |
| DRLBPLlkanH | TOP#6 | 930 | 2 | 816 | 0 | 0 | — | 0 | — | — |
| DPlyTlMkSSg | TOP#7 | 712 | 6 | 33 | 0 | 0 | — | 1 | — | exata |
| DUvhpvDk-ju | TOP#8 | 1.757 | 5 | 108 | 0 | 0 | — | 1 | — | — |
| DSUwnmTkT0R | TOP#9 | 969 | 3 | 292 | 0 | 0 | — | 0 | — | exata + variante |
| DPeHqHvDfCK | TOP#10 | 954 | 7 | 72 | 0 | 0 | menção ao curso (sem link) | 0 | — | — |
| DQPWbVhkcuN | TOP#11 | 818 | 12 | 119 | 0 | 0 | — | 0 | — | — |
| DOzEZ2zkdL7 | TOP#12 | 528 | 4 | 72 | 0 | 0 | menção à trilha do curso (sem link) | 0 | — | — |
| DTAv-KdkQBB | TOP#13 | 26 | 1 | 26 | 0 | 0 | pergunta ao público (legenda inteira) | 1 | — | — |
| DQ92iwaEYl4 | TOP#14 | 654 | 7 | 179 | 0 | 0 | pergunta + comenta opinião | 1 | — | — |
| DTIR9ONkS-m | TOP#15 | 838 | 3 | 378 | 0 | 0 | — | 0 | — | — |
| DdufhvOgh2n | RECENTE#1 | 1.750 | 15 | 55 | 0 | 0 | entrega na legenda (prompt completo) | 0 | — | exata |
| Ddm0XEqDXcM | RECENTE#2 | 1.887 | 22 | 62 | 0 | 0 | — | 5 | — | variante |
| DdkGyrlG9oO | RECENTE#3 | 805 | 8 | 38 | 0 | 0 | — | 0 | — | — |
| DdZ09KIj-Op | RECENTE#4 | 1.909 | 19 | 69 | 0 | 0 | — | 0 | — | variante |
| DdXT4SkCCM5 | RECENTE#5 | 1.296 | 9 | 190 | 0 | 0 | — | 0 | — | variante |
| DdHwQVLgY2A | RECENTE#6 | 1.606 | 14 | 138 | 0 | 0 | — | 0 | — | exata + variante |
| DdCqD4RCPTk | RECENTE#7 | 1.282 | 8 | 48 | 0 | 0 | — | 0 | — | variante |
| Dc11gx6lXTx | RECENTE#8 | 1.158 | 6 | 39 | 0 | 0 | — | 0 | — | — |
| Dcv7xpPAWmq | RECENTE#9 | 861 | 4 | 136 | 0 | 0 | — | 0 | — | exata (+ citação como vício de IA) |
| DcjwjLtj2Th | RECENTE#10 | 1.135 | 6 | 262 | 0 | 0 | comenta PALAVRA ("skill") | 0 | — | variante |
| DcefJ7MlVZR | RECENTE#11 | 1.162 | 9 | 182 | 0 | 0 | link direto na legenda (GitHub) | 0 | — | variante |
| DcMh8AyCSUe | RECENTE#12 | 1.276 | 10 | 98 | 0 | 0 | — | 0 | — | — |
| DcJ9EInDQYN | RECENTE#13 | 1.416 | 17 | 70 | 0 | 0 | — | 0 | — | variante |
| Db-xS-AkSVq | RECENTE#14 | 93 | 1 | 93 | 0 | 0 | comenta PALAVRA ("REMOTION") | 0 | — | — |
| Db8azYFCAdB | RECENTE#15 | 768 | 7 | 63 | 0 | 0 | — | 0 | — | — |

| recorte | caracteres (média / mediana) | linhas (média / mediana) | 1ª linha (mediana) | legendas ≥ 1.000 caracteres | emojis | hashtags | legendas com "?" | "?" (total) | menções @ |
|---|---|---|---|---|---|---|---|---|---|
| TOP 15 | 874 / 930 | 6,4 / 5,0 | 119 | 5 | 0 | 0 | 5 | 5 | 0 |
| RECENTES 15 | 1.227 / 1.276 | 10,3 / 9,0 | 70 | 11 | 0 | 0 | 1 | 5 | 0 |
| 30 | 1.050 / 1.009 | 8,4 / 7,0 | 103 | 16 | 0 | 0 | 6 | 10 | 0 |

**Tipos de CTA (legendas com o tipo)**

| tipo | TOP 15 | RECENTES 15 | 30 |
|---|---|---|---|
| comenta PALAVRA-chave para receber algo | 0 | 2 | 2 |
| comenta opinião / pergunta ao público | 2 | 0 | 2 |
| link na bio | 1 | 0 | 1 |
| link direto na legenda (GitHub) | 0 | 1 | 1 |
| segue | 0 | 0 | 0 |
| salva | 0 | 0 | 0 |
| compartilha / manda para alguém | 0 | 0 | 0 |
| direct | 0 | 0 | 0 |
| **qualquer CTA explícito** | 3 | 3 | 6 |
| menção ao curso ou à trilha da Asimov, sem link | 2 | 0 | 2 |
| entrega do material na própria legenda (prompt completo) | 0 | 1 | 1 |

- Legenda longa e escrita (parágrafos explicativos, listas com "→" em 3): mediana de 1.009 caracteres e 7 linhas; 16 de 30 passam de 1.000. Duas exceções curtíssimas: TOP#13 (26 caracteres, só uma pergunta) e RECENTE#14 (93, só o pedido de palavra-chave).
- **Zero** emoji, **zero** hashtag e **zero** menção a @ nas 30 legendas.
- O pedido de comentário quase sempre vem na fala, não na legenda: dos 8 vídeos que pedem comentário (fala ou legenda), 4 pedem só na fala (TOP#2, TOP#10, RECENTE#3, RECENTE#4), 1 só na legenda (TOP#14) e 3 nos dois (TOP#13, RECENTE#10, RECENTE#14).
- Comentários/views: os 3 com "comenta PALAVRA" (RECENTE#4 3,834%, #10 4,325%, #14 3,642%) ficam 170x a 201x a mediana dos outros 27 (0,021%). Pedido de opinião sem palavra-chave não muda a taxa (TOP#2 0,026%, TOP#10 0,015%, TOP#13 0,011%, TOP#14 0,022%, RECENTE#3 0,021%).

## 6. Correlações de Spearman entre views e cada variável

ρ de Spearman (empates com posto médio) e p bicaudal do scipy. Com n = 30 ou 15 isto é **indício, não prova**: são 43 testes calculáveis e, a p < 0,05, espera-se cerca de 2 "significâncias" só por acaso. Os 30 misturam duas épocas (TOP de set/2025 a fev/2026 e recentes de ago–set/2026), então uma correlação nos 30 pode medir só a época.

| variável | 30 (n; ρ; p) | dentro do TOP (n; ρ; p) | dentro dos recentes (n; ρ; p) |
|---|---|---|---|
| duração (s) | 30; 0,15; 0,426 | 15; 0,11; 0,694 | 15; 0,05; 0,860 |
| palavras/min (sem RECENTE#15) | 29; −0,21; 0,264 | 15; −0,01; 0,970 | 14; −0,53; 0,054 |
| cortes/min bruto | 30; −0,34; 0,069 | 15; −0,43; 0,111 | 15; −0,33; 0,232 |
| cortes/min agrupado | 30; −0,32; 0,088 | 15; −0,19; 0,499 | 15; −0,31; 0,254 |
| tamanho da legenda (caracteres) | 30; −0,25; 0,179 | **15; 0,57; 0,027** | 15; −0,03; 0,919 |
| texto no 1º frame (0/1) | 30; −0,12; 0,535 | 15; 0,12; 0,660 | 15; constante (não calculável) |
| manchete, cartela ou pergunta no 1º frame (0/1) | **30; −0,43; 0,017** | 15; 0,06; 0,827 | 15; 0,00; 1,000 |
| print de tela no 1º frame (0/1) | 30; −0,03; 0,888 | 15; 0,43; 0,107 | 15; −0,31; 0,262 |
| rosto no 1º frame (0/1) | 30; −0,33; 0,079 | 15; −0,07; 0,805 | 15; −0,43; 0,107 |
| % do tempo com rosto | **30; −0,59; 0,001** | 15; −0,29; 0,289 | 15; −0,36; 0,182 |
| fala (0/1) | 30; constante (não calculável) | 15; constante (não calculável) | 15; constante (não calculável) |
| pedido de comentário, fala ou legenda (0/1) | 30; −0,08; 0,681 | 15; −0,24; 0,380 | 15; −0,07; 0,805 |
| "comenta PALAVRA" (0/1) | 30; −0,26; 0,160 | 15; constante (não calculável) | 15; 0,08; 0,785 |
| formato resposta a pergunta de seguidor (0/1) | **30; −0,44; 0,015** | 15; −0,06; 0,827 | 15; −0,31; 0,253 |
| números citados na fala | 30; 0,27; 0,149 | 15; −0,10; 0,729 | **15; 0,52; 0,047** |
| nº de palavras | 30; 0,08; 0,659 | 15; 0,13; 0,634 | 15; −0,26; 0,341 |

Em negrito: p < 0,05. "Fala" é constante (os 30 têm fala dele em pt). "Texto no 1º frame" só varia em 1 vídeo (TOP#10). "Comenta PALAVRA" não aparece no TOP.

**Mediana de views com × sem**

| variável | com (n; mediana) | sem (n; mediana) | dentro do TOP: com × sem | dentro dos recentes: com × sem |
|---|---|---|---|---|
| texto no 1º frame | 29; 251.299 | 1; 430.324 | 14; 624.376,5 × 1; 430.324 | 15; 19.893 × 0; — |
| manchete, cartela ou pergunta no 1º frame | 9; 19.893 | 21; 384.506 | 1; 751.835 × 14; 466.174 | 8; 17.283,5 × 7; 31.166 |
| print de tela no 1º frame | 15; 60.339 | 15; 343.301 | 7; 879.910 × 8; 418.079 | 8; 17.283,5 × 7; 53.709 |
| rosto no 1º frame | 25; 60.339 | 5; 496.918 | 11; 435.430 × 4; 654.263 | 14; 17.283,5 × 1; 251.299 |
| pedido de comentário | 8; 199.989,5 | 22; 290.685 | 4; 391.155 × 11; 751.835 | 4; 31.509,5 × 11; 19.893 |
| "comenta PALAVRA" | 3; 53.709 | 27; 343.301 | 0; — × 15; 496.918 | 3; 53.709 × 12; 17.283,5 |
| resposta a pergunta de seguidor | 7; 14.674 | 23; 351.986 | 1; 435.430 × 14; 624.376,5 | 6; 14.600,5 × 9; 42.396 |

Leitura:

- O sinal mais consistente é o **tempo de rosto na tela**, negativo nos três recortes (ρ −0,59 nos 30, p 0,001; −0,29 no TOP; −0,36 nos recentes): os vídeos mais vistos passam mais tempo mostrando a prova (print, resultado, objeto) do que o rosto. Nos 30, parte disso é época: a tela dividida com rosto embaixo é o padrão de 2026.
- **Cortes por minuto** também têm sinal negativo nos três recortes (−0,34; −0,43; −0,33; nenhum com p < 0,05): editar mais rápido não trouxe mais views. Os TOP e os recentes cortam no mesmo ritmo (mediana 15,0 e 15,7 por minuto).
- **Manchete/cartela/pergunta no 1º frame** e **resposta a pergunta de seguidor** são negativos nos 30 (p 0,017 e 0,015), mas somem dentro de cada grupo: medem o formato de 2026, não uma alavanca comprovada. Mesmo assim, dentro dos recentes, as 6 respostas a seguidor têm a menor mediana (14.600,5 × 42.396).
- **Duração, palavras/min, pedido de comentário e nº de palavras** não mostram relação com views (|ρ| ≤ 0,21 nos 30). O ritmo é quase fixo (181 a 267 pal/min) e não separa virais de não virais.
- **Tamanho da legenda** muda de sinal: +0,57 no TOP (p 0,027) e −0,03 nos recentes. **Números citados**: +0,52 nos recentes (p 0,047), −0,10 no TOP. Sinais instáveis com n = 15; não tratar como regra.

## 7. Os 7 achados quantitativos para quem vai roteirizar

1. **O molde a copiar é o de set/2025 a fev/2026, não o atual.** Mediana de 70.612,5 views (29,6% dos 238.858 seguidores), p90 de 422.977 e 3 reels acima de 1 milhão, num perfil com só 94 reels. Os 15 mais vistos saíram todos entre 19/09/2025 e 25/02/2026 (36 reels na janela, mediana 153.987); nenhum dos 48 posteriores passou de 274.225. O bloco de 50 mais novo tem mediana 39.504,5 (0,56x) contra 148.132 (2,1x) do anterior e, em blocos de 15, a mediana caiu de 253.895 para 19.893. O ritmo de postagem ficou parado em 1,5 a 1,7 reel por semana: a queda não vem de volume. Os recentes trocaram "ferramenta nova + demonstração" por "resposta a pergunta de seguidor" (6 de 15, mediana 14.600,5).
2. **Os virais mostram a prova metade do tempo; a fala é a narração da prova.** Nos TOP, o rosto de frente aparece em 49% do tempo (mediana), contra 72% nos recentes; 7 dos 15 TOP abrem num print (GitHub, site, ChatGPT, Reddit) e 2 quase não mostram o rosto (3% e 0%). Tempo de rosto × views dá ρ −0,59 nos 30 e fica negativo dentro do TOP (−0,29) e dos recentes (−0,36). "aqui" aparece 14,1 vezes por mil palavras (em 25 de 29 vídeos) e "olha" só aponta resultado. Quem grava só falando para a câmera precisa pôr na fala o que ele mostra na tela: o nome da ferramenta, o número (quantas estrelas o projeto tem, o tempo que levou, "10x mais rápido") e o resultado descrito. Números citados têm ρ +0,52 com views nos recentes (p 0,047), mas −0,10 no TOP.
3. **Ritmo fixo de ~220 palavras por minuto, do segundo 0 ao fim, sem saudação.** Mediana de 220 pal/min no TOP (181 a 267) e 221 nos recentes (207 a 245); o ritmo sobre a duração total é quase igual, ou seja, não há silêncio nem vinheta. 29 de 30 começam a falar em 0,0 s e nenhum se apresenta. O TOP tem mediana de 298 palavras em 80 s (38 a 110 s); o trecho de respiração tem mediana de 11 palavras. Duração e ritmo não se correlacionam com views (ρ 0,15 e −0,21 nos 30).
4. **O gancho nomeia a coisa e o ganho na 1ª frase, apontando para ela.** Nos TOP: "ferramenta ou método + o que resolve" em 5 de 15 (mediana 811.608; 4 falam "grátis/gratuito" e 3 dizem o nome da empresa ou da ferramenta nos primeiros 5 s), lista numerada em 4 (463.621), resultado pronto + "é assim que eu fiz" em 2 (739.056), e o mais visto (1.375.079) abre com pergunta retórica sobre uma tendência. 15 de 30 falam "aqui" nos primeiros 5 s; 9 de 30 dizem um número (5 são o tamanho da lista). Texto no 1º frame em 29 de 30, quase sempre a legenda palavra a palavra.
5. **A voz é de professor-colega: "a gente", "tu" e "você" misturados, poucos tiques.** Por mil palavras: "aqui" 14,1, "a gente" 5,8 (16 de 29 vídeos; "a gente vai" narra o passo a passo), "porque" 3,6, "então" 2,5, "cara" como interjeição 1,7 (14 vezes; 5 dos 7 vídeos de pergunta respondem começando com "Cara,"), "tá" 1,7, "né" 0,1, "mano" 0 e "galera"/"gente" como vocativo 0. 2ª pessoa em 28,7% das frases ("você" 83 vezes, "tu" 61; os dois no mesmo vídeo em 13 de 29). O contraste favorito é "ao invés de [jeito comum], [jeito melhor]" (10 de 29 vídeos), e não "não é X, é Y" (1 exata + 10 variantes; 1,3 por mil palavras).
6. **A legenda é um texto longo à parte: sem hashtag, sem emoji, e é onde mora o "não é X, é Y".** Mediana de 1.009 caracteres e 7 linhas (TOP 930; recentes 1.276); 16 de 30 passam de 1.000 caracteres; 0 hashtags, 0 emojis e 0 menções nas 30. A construção "não é X, é Y" (exata ou variante) está em 13 legendas: 3 do TOP e 10 dos recentes. No RECENTE#9 o próprio criador cita esse contraste como sinal de texto escrito por IA. Tamanho da legenda × views muda de sinal entre grupos (+0,57 no TOP, −0,03 nos recentes).
7. **CTA só no fim e raro; "comenta PALAVRA" rende comentário, não alcance.** CTA falado em 7 dos 30 (3 do TOP, 4 recentes), sempre entre 95% e 98% do vídeo (2,0 a 5,3 s antes do fim); 22 dos 30 não pedem comentário em lugar nenhum. O molde é "Se você quiser [material], comenta [PALAVRA] que eu te mando [o material]". Os 3 com palavra-chave (todos recentes) têm 3,6% a 4,3% de comentários/views, 170x a 201x a mediana dos outros 27 (0,021%), mas mediana de 53.709 views. Nos 94 reels, os 10 com ≥ 1% de comentários/views (os 3 fixados entre eles) têm mediana de 55.193,5 views, contra 76.404 dos outros. Pedido de opinião sem palavra-chave não muda a taxa (0,011% a 0,026%). "Link na bio" em 1 legenda; segue, salva, compartilha e direct em nenhuma.
