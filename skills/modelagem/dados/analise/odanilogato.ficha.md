# Ficha quantitativa — @odanilogato (Danilo Gato)

Professor e consultor de IA para negócios, criador do podcast Papo de IA · 895.021 seguidores · 1.788 posts · **1.263 reels com contagem de views** (1.552 itens na aba de reels; lista completa) · coleta em 29/09/2026 com login. Fontes: `users/odanilogato.json` (todos os reels), `dossie/odanilogato.md`, `videos/odanilogato/*.tr.json | *.ocr.json | *.vis.json`, as 30 folhas de contato (`*.sheet.jpg`) e os 30 frames de gancho (`*.hook.jpg`). Números calculados em Python a partir dos arquivos brutos. Nenhum trecho de fala ou de legenda com mais de 5 palavras seguidas foi copiado; manchetes de tela com até 12 palavras aparecem entre «».

## 0. Como os números foram medidos

- **Views** = `play_count`. Os 289 itens antigos de IGTV/feed (nov/2019 a jan/2023) não têm `play_count`, só `view_count` (métrica antiga, mediana 1.311), e ficaram fora, como no dossiê. Views, likes e comentários dos 30 vêm da lista `items`, igual ao dossiê.
- **Percentis**: interpolação linear sobre os 1.263 reels. A mediana é igual à do dossiê (33.716). O dossiê usa outro método de percentil, e p25/p75/p90 diferem menos de 0,1%. **Múltiplo** = views ÷ 33.716.
- **Tendência**: ordem da lista do Instagram (do mais novo para o mais velho), sem os 3 fixados (`DYyL_wOgoeX`, `DJpOGdevK9P`, `C5zWct_vNzn`). As datas saem do ID do post, no horário de Brasília (erro de poucos minutos).
- **Palavras/min** = palavras ÷ (fim do último trecho − início do primeiro) × 60, como no dossiê, mas com o fim limitado à duração do vídeo. Só muda o TOP#4: o último trecho do Whisper ("E aí") termina aos 115 s num vídeo de 85,9 s. O valor corrigido é 245 (o dossiê mostra 183).
- **Cortes/min**: bruto = cortes do `vis.json` ÷ duração. Agrupado = cortes a menos de 1 s um do outro contam como 1.
- **Tem fala**: flag `ok` do Whisper. **Fala dele em pt** (25 vídeos) exclui TOP#7 (áudio de stand-up de outro humorista; só as 2 últimas frases são dele) e TOP#8 (anúncio estrangeiro em inglês). Na seção 4 também saem os 0–41 s do TOP#3 (vídeo original de outra pessoa) e 15 falas sintéticas das IAs dentro da simulação do RECENTE#9. RECENTE#10 e #11 têm narração feita com IA (a legenda do #11 diz que a voz é clonada) e ficaram na conta.
- **Números citados**: dígitos e numerais por extenso na fala, incluindo versões de modelo e códigos (GPT‑4o, T‑800). Não contam "um/uma", a expressão "do zero" nem "milhões/bilhões" soltos sem número antes. **Perguntas**: quantidade de "?" na transcrição. **CTA falado**: candidatos achados por regex e conferidos à mão. O segundo é interpolado pela posição da palavra dentro do trecho do Whisper.
- **Formato, tarja e texto do 1º frame**: classificados vendo as 30 folhas de contato e os 30 frames de gancho. No OCR t=0 foram removidos o selo @odanilogato, a placa "100 mil" pendurada no fundo do cenário de 2026 e o ruído de interface.
- **Prováveis anúncios** (likes/views < 0,3%): nenhum dos 30. O menor likes/views dos 30 é 2,04% (RECENTE#6).
- **Limites**: os 15 recentes tinham de 0,4 a 10,7 dias na coleta, então as views deles ainda não fecharam. RECENTE#1 e #2 foram transcritos com faster-whisper-small, que erra nomes. O large também erra alguns ("Cloud" por Claude). Onde o Whisper pontua pouco (TOP#9), a média de palavras por frase sobe; a mediana por trecho é mais estável. O OCR roda a cada 2 s, então um texto pode ter entrado até 2 s antes do segundo indicado.

## 1. Distribuição de views (1.263 reels) e tendência

| p10 | p25 | p50 (mediana) | p75 | p90 | p99 | máximo | média |
|---|---|---|---|---|---|---|---|
| 8.198 | 14.898 | 33.716 | 85.812 | 220.030 | 2.267.300 | 14.090.506 | 137.529 |

- A mediana equivale a 3,77% dos seguidores. A média é 4,1x a mediana, ou seja, cauda longa. Acima de 50 mil: 494 reels (39,1%). Acima de 100 mil: 263 (20,8%). Acima de 500 mil: 49 (3,9%). Acima de 1 milhão: 28 (2,2%). Acima de 2 milhões: 17 (1,3%).
- Mediana de todos os reels: likes/views 2,85% e comentários/views 0,088%.
- Prováveis anúncios pela regra: 17 de 1.263 (1,3%). Desses, 13 têm exatamente 3 likes, padrão de curtidas ocultas, e a regra não consegue separar anúncio. Os outros 4 ficam entre 0,16% e 0,29% (3 de jun/2026 e 1 de out/2025). Há 0 no TOP 15, 1 no TOP 50 e 2 no TOP 100.
- Por ano de postagem, o TOP 15 tem 7 reels de 2024, 7 de 2025 e 1 de 2023, e **nenhum de 2026**. O TOP 50 tem 23 de 2025, 18 de 2024, 5 de 2026 e 4 de 2023.

**Mediana por blocos de 50 reels (mais novo → mais velho, sem fixados)**

| bloco | reels | período (mais novo → mais velho) | dias | reels/semana | mediana | x mediana geral | p90 | máximo | ≥ 1 mi | likes/views (mediana) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 50 | 2026-09-28 → 2026-07-29 | 61 | 5,7 | 30.063,5 | 0,89x | 195.995 | 961.575 | 0 | 3,44% |
| 2 | 50 | 2026-07-28 → 2026-06-06 | 52 | 6,7 | 28.335 | 0,84x | 139.406 | 497.614 | 0 | 2,37% |
| 3 | 50 | 2026-06-05 → 2026-04-13 | 53 | 6,6 | 33.678 | 1,00x | 114.681 | 388.178 | 0 | 2,43% |
| 4 | 50 | 2026-04-12 → 2026-02-09 | 62 | 5,6 | 58.102 | 1,72x | 277.612 | 810.134 | 0 | 2,83% |
| 5 | 50 | 2026-02-07 → 2025-12-06 | 64 | 5,5 | 85.577,5 | 2,54x | 303.283 | 3.043.897 | 2 | 2,72% |
| 6 | 50 | 2025-12-05 → 2025-10-21 | 45 | 7,7 | 76.419 | 2,27x | 639.547 | 2.424.041 | 5 | 2,86% |
| 7 | 50 | 2025-10-20 → 2025-08-17 | 64 | 5,4 | 55.802,5 | 1,66x | 201.460 | 586.337 | 0 | 2,35% |
| 8 | 50 | 2025-08-16 → 2025-06-29 | 48 | 7,2 | 76.489 | 2,27x | 267.158 | 2.379.028 | 3 | 2,60% |
| 9 | 50 | 2025-06-28 → 2025-04-29 | 59 | 5,9 | 65.261 | 1,94x | 277.767 | 587.866 | 0 | 2,96% |
| 10 | 50 | 2025-04-28 → 2025-02-14 | 73 | 4,8 | 97.866,5 | 2,90x | 780.059 | 2.479.871 | 4 | 3,38% |
| 11 | 50 | 2025-02-14 → 2024-12-18 | 58 | 6,1 | 58.139 | 1,72x | 210.102 | 975.969 | 0 | 3,09% |
| 12 | 50 | 2024-12-17 → 2024-10-05 | 73 | 4,8 | 127.531,5 | 3,78x | 720.572 | 3.934.177 | 4 | 3,12% |
| 13 | 50 | 2024-10-05 → 2024-07-02 | 95 | 3,7 | 54.690,5 | 1,62x | 947.839 | 14.090.506 | 4 | 2,51% |
| 14 | 50 | 2024-07-01 → 2024-04-02 | 90 | 3,9 | 16.804 | 0,50x | 62.442 | 1.242.980 | 1 | 2,39% |
| 15 | 50 | 2024-04-01 → 2024-01-26 | 66 | 5,3 | 18.298 | 0,54x | 110.091 | 5.060.539 | 3 | 2,67% |
| 16 | 50 | 2024-01-25 → 2023-11-21 | 65 | 5,4 | 10.332,5 | 0,31x | 62.835 | 516.424 | 0 | 2,68% |
| 17 | 50 | 2023-11-20 → 2023-07-14 | 129 | 2,7 | 18.526,5 | 0,55x | 141.403 | 2.955.637 | 1 | 3,21% |
| 18 | 50 | 2023-07-12 → 2023-03-31 | 103 | 3,4 | 23.141 | 0,69x | 132.111 | 487.062 | 0 | 2,78% |
| 19 | 50 | 2023-03-30 → 2022-09-26 | 185 | 1,9 | 29.161,5 | 0,86x | 118.784 | 424.949 | 0 | 3,17% |
| 20 | 50 | 2022-09-24 → 2022-06-19 | 97 | 3,6 | 33.425,5 | 0,99x | 82.400 | 364.097 | 0 | 3,12% |
| 21 | 50 | 2022-06-18 → 2022-02-23 | 115 | 3,0 | 28.527,5 | 0,85x | 78.764 | 309.726 | 0 | 4,21% |
| 22 | 50 | 2022-02-22 → 2021-11-10 | 104 | 3,4 | 25.681,5 | 0,76x | 88.310 | 196.942 | 0 | 4,53% |
| 23 | 50 | 2021-11-05 → 2021-06-03 | 155 | 2,3 | 21.944,5 | 0,65x | 44.986 | 66.228 | 0 | 3,82% |
| 24 | 50 | 2021-05-31 → 2020-10-27 | 216 | 1,6 | 9.968,5 | 0,30x | 23.782 | 62.417 | 0 | 2,43% |
| 25 | 50 | 2020-10-24 → 2020-07-20 | 96 | 3,6 | 6.081,5 | 0,18x | 12.160 | 24.378 | 0 | 1,35% |
| 26 | 10 | 2020-07-17 → 2020-06-30 | 17 | 4,2 | 9.104 | 0,27x | 11.874 | 13.111 | 0 | 2,02% |

| ano | reels | mediana | x mediana geral | ≥ 1 mi | máximo |
|---|---|---|---|---|---|
| 2020 | 79 | 6.411 | 0,19x | 0 | 32.396 |
| 2021 | 98 | 19.354 | 0,57x | 0 | 120.273 |
| 2022 | 168 | 30.320,5 | 0,90x | 0 | 364.097 |
| 2023 | 144 | 20.414,5 | 0,61x | 1 | 2.955.637 |
| 2024 | 237 | 32.394 | 0,96x | 12 | 14.090.506 |
| 2025 | 304 | 71.939,5 | 2,13x | 14 | 3.043.897 |
| 2026 | 233 | 43.502 | 1,29x | 1 (fixado) | 1.515.980 |

Leitura:

- A mediana tem três picos: out–dez/2024 (bloco 12: 127.531,5; 3,78x), fev–abr/2025 (bloco 10: 97.866,5) e dez/2025–fev/2026 (bloco 5: 85.577,5). Os blocos 10 e 12 saíram a 4,8 reels por semana.
- Desde abr/2026 (blocos 1 a 3, 150 reels), a mediana ficou entre 28 e 34 mil (0,84–1,00x), o mesmo nível de 2022, com mais postagem: 5,7 a 6,7 por semana.
- Em 2026, nenhum reel não fixado passou de 1 milhão. O maior foi `Dcj5SrDkkY1`, com 961.575 views em 27/08/2026, fora dos 30 e sem transcrição.
- Fixados: `DYyL_wOgoeX` (1.515.980; mai/2026), `C5zWct_vNzn` (134.709; abr/2024) e `DJpOGdevK9P` (94.126; mai/2025).

## 2. Os 30 selecionados

| código | grupo | data | dur (s) | views | x mediana | likes/views | coment./views | pal/min | cortes/min bruto (agrupado) | tem fala? | idioma | nº palavras | nº perguntas | nº números | CTA falado: 1º (s; % do vídeo) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-xeNM6u9XP | TOP#1 | 2024-08-17 | 5,2 | 14.090.506 | 417,9x | 3,30% | 0,011% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |
| C-YtsLFPQ3a | TOP#2 | 2024-08-07 | 50,2 | 6.738.390 | 199,9x | 2,49% | 0,018% | 205 | 2,4 (2,4) | sim | pt | 171 | 0 | 1 | 43,2 (86%) |
| C2lUA2EPDlE | TOP#3 | 2024-01-26 | 89,3 | 5.060.539 | 150,1x | 2,96% | 0,061% | 192 | 2,0 (2,0) | sim* | pt | 285 | 0 | 1 | 84,8 (95%) |
| DBC40xavHaP | TOP#4 | 2024-10-12 | 85,9 | 3.934.177 | 116,7x | 4,36% | 0,048% | 245 | 3,5 (3,5) | sim | pt | 351 | 0 | 3 | 21,0 (24%) |
| DABUMqUP-My | TOP#5 | 2024-09-17 | 63,2 | 3.701.417 | 109,8x | 4,17% | 0,010% | 214 | 0,0 (0,0) | sim | pt | 224 | 0 | 2 | 34,5 (55%) |
| C_y4_y-PZbK | TOP#6 | 2024-09-11 | 43,8 | 3.523.475 | 104,5x | 2,92% | 0,011% | 188 | 1,4 (1,4) | sim | pt | 136 | 0 | 0 | 32,0 (73%) |
| DSkx3dFkaxN | TOP#7 | 2025-12-22 | 153,4 | 3.043.897 | 90,3x | 6,42% | 0,086% | 122 | 23,9 (19,9) | sim* | pt | 312 | 12 | 25 | 151,2 (99%) |
| Cu28Y46t1pX | TOP#8 | 2023-07-18 | 88,7 | 2.955.637 | 87,7x | 4,24% | 0,034% | — | 1,4 (1,4) | sim* | en | 177 | 1 | 0 | — |
| DR6ABHwj23N | TOP#9 | 2025-12-06 | 71,7 | 2.859.481 | 84,8x | 2,96% | 0,018% | 146 | 5,0 (5,0) | sim | pt | 174 | 0 | 2 | 44,2 (62%) |
| DHpX8l_vftH | TOP#10 | 2025-03-25 | 174,9 | 2.479.871 | 73,6x | 5,95% | 0,280% | 262 | 8,6 (8,6) | sim | pt | 763 | 2 | 2 | 19,0 (11%) |
| DRGfDJXjx0M | TOP#11 | 2025-11-15 | 91,3 | 2.424.041 | 71,9x | 4,16% | 0,116% | 221 | 0,7 (0,7) | sim | pt | 331 | 1 | 2 | 62,1 (68%) |
| DMonN4JNaud | TOP#12 | 2025-07-27 | 15,9 | 2.379.028 | 70,6x | 2,54% | 0,012% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |
| DHuby_RvTBk | TOP#13 | 2025-03-27 | 146,2 | 2.370.593 | 70,3x | 4,87% | 0,042% | 261 | 6,2 (5,7) | sim | pt | 636 | 0 | 3 | 26,3 (18%) |
| C5J9aGsvPKq | TOP#14 | 2024-03-30 | 65,7 | 2.203.991 | 65,4x | 6,49% | 0,043% | — | 5,5 (4,6) | não | — | 0 | 0 | 0 | — |
| DInGtcovBTn | TOP#15 | 2025-04-18 | 110,3 | 2.122.725 | 63,0x | 6,91% | 0,167% | 221 | 4,4 (4,4) | sim | pt | 406 | 1 | 0 | 30,1 (27%) |
| Dd2ecFGDuU9 | RECENTE#1 | 2026-09-28 | 87,7 | 7.315 | 0,2x | 2,38% | 0,014% | 224 | 13,7 (13,0) | sim | pt | 327 | 1 | 5 | 84,4 (96%) |
| Dd1GuwUDESi | RECENTE#2 | 2026-09-28 | 150,6 | 19.054 | 0,6x | 3,73% | 0,121% | 200 | 13,5 (11,6) | sim | pt | 501 | 2 | 2 | 134,4 (89%) |
| Ddz9Xzoju6q | RECENTE#3 | 2026-09-27 | 131,3 | 28.286 | 0,8x | 2,57% | 0,173% | 211 | 8,2 (7,8) | sim | pt | 461 | 0 | 4 | 119,0 (91%) |
| DdyzHcECTyI | RECENTE#4 | 2026-09-27 | 117,1 | 194.341 | 5,8x | 4,61% | 0,030% | 193 | 12,8 (12,3) | sim | pt | 376 | 1 | 13 | 112,5 (96%) |
| DdxElXaE2Uc | RECENTE#5 | 2026-09-26 | 114,5 | 173.284 | 5,1x | 4,96% | 0,135% | 227 | 10,5 (8,4) | sim | pt | 433 | 0 | 5 | 112,0 (98%) |
| DdwRiX8EQso | RECENTE#6 | 2026-09-26 | 95,0 | 4.557 | 0,1x | 2,04% | 0,132% | 202 | 3,8 (3,8) | sim | pt | 312 | 1 | 1 | 89,2 (94%) |
| DdwHUgCjtm- | RECENTE#7 | 2026-09-26 | 153,4 | 376.839 | 11,2x | 8,10% | 0,395% | 203 | 26,2 (18,8) | sim | pt | 517 | 1 | 20 | 148,3 (97%) |
| Ddu1RobAscT | RECENTE#8 | 2026-09-25 | 78,1 | 103.367 | 3,1x | 2,82% | 0,054% | 190 | 7,7 (7,7) | sim | pt | 246 | 0 | 9 | 37,0 (47%) |
| Ddsas0AlQX2 | RECENTE#9 | 2026-09-24 | 178,9 | 13.602 | 0,4x | 4,12% | 0,154% | 253 | 0,3 (0,3) | sim* | pt | 753 | 2 | 10 | 175,6 (98%) |
| DdrVBELlxFi | RECENTE#10 | 2026-09-24 | 59,0 | 29.256 | 0,9x | 2,81% | 0,065% | 207 | 0,0 (0,0) | sim† | pt | 202 | 0 | 3 | 58,0 (98%) |
| Ddo1HWIjb99 | RECENTE#11 | 2026-09-23 | 41,8 | 11.036 | 0,3x | 2,13% | 0,045% | 203 | 0,0 (0,0) | sim† | pt | 140 | 0 | 1 | 39,6 (95%) |
| DdnLA3sDoDX | RECENTE#12 | 2026-09-22 | 128,7 | 87.467 | 2,6x | 8,21% | 0,433% | 212 | 14,4 (14,4) | sim | pt | 453 | 1 | 8 | 118,8 (92%) |
| DdmjZp3DMxX | RECENTE#13 | 2026-09-22 | 115,8 | 27.407 | 0,8x | 2,52% | 0,080% | 194 | 17,6 (16,1) | sim | pt | 373 | 0 | 13 | 113,0 (98%) |
| DdjgueRCPqX | RECENTE#14 | 2026-09-21 | 137,8 | 85.809 | 2,5x | 4,15% | 0,199% | 198 | 20,5 (17,4) | sim | pt | 453 | 0 | 12 | 133,9 (97%) |
| Ddb_W1wGsF3 | RECENTE#15 | 2026-09-18 | 100,4 | 30.871 | 0,9x | 5,33% | 0,353% | 223 | 19,7 (16,7) | sim | pt | 373 | 1 | 6 | 94,1 (94%) |

Notas da tabela:

- Nº de palavras, perguntas e números contam o vídeo inteiro, isto é, o que o espectador ouve.
- \* TOP#3: de 0 a 41 s fala a autora do vídeo original (@hgoficinajuridica); ele fala de 41,6 s até o fim.
- \* TOP#7: post em colaboração (ele entra como coautor). É uma paródia feita com IA sobre o áudio de stand-up de outro humorista, e os 25 números e as 12 perguntas são do stand-up. Só as 2 últimas frases (146–153 s) são dele.
- \* TOP#8: anúncio estrangeiro em inglês com legenda em português; ele aparece calado, reagindo.
- \* RECENTE#9: 15 trechos são falas sintéticas das IAs dentro da cena simulada.
- † RECENTE#10 e #11: animação feita por IA, sem rosto e com narração gerada. A legenda do #11 diz que a voz é clonada.
- TOP#1, #12 e #14 não têm fala. Neles o conteúdo está no texto da tela e na imagem: homenagem feita com IA, evolução "2022 → 2025" e "um ano atrás × hoje".

| grupo | mediana views | mediana x | mediana dur (s) | mediana likes/views | mediana coment./views | mediana pal/min | mediana cortes/min (bruto) | com fala dele em pt | prováveis anúncios | idade na coleta |
|---|---|---|---|---|---|---|---|---|---|---|
| TOP 15 | 2.955.637 | 87,7x | 85,9 | 4,17% | 0,042% | 214 (n = 11) | 2,4 | 10 | 0 | 281 a 1.168 dias |
| RECENTES 15 | 29.256 | 0,87x | 115,8 | 3,73% | 0,132% | 203 (n = 15) | 12,8 | 15 | 0 | 0,4 a 10,7 dias |

**Views por formato (nos 30)**, classificado pelas folhas de contato

| formato | grupo | n | mediana views | mínimo | máximo | vídeos |
|---|---|---|---|---|---|---|
| fala pra câmera na metade de baixo + prova visual em cima (tela dividida, legenda amarela) | TOP | 8 | 3.001.673 | 2.122.725 | 6.738.390 | 2, 4, 5, 6, 10, 11, 13, 15 |
| criação com IA sem fala (montagem + música/texto) | TOP | 3 | 2.379.028 | 2.203.991 | 14.090.506 | 1, 12, 14 |
| react a vídeo de terceiro + comentário dele em tela dividida | TOP | 1 | 5.060.539 | — | — | 3 |
| paródia feita com IA sobre áudio de terceiro (collab) | TOP | 1 | 3.043.897 | — | — | 7 |
| react mudo a anúncio estrangeiro legendado | TOP | 1 | 2.955.637 | — | — | 8 |
| criação com IA (25 s de antes/depois) + bastidor falado | TOP | 1 | 2.859.481 | — | — | 9 |
| experimento próprio (IA treinando em simulação 3D) + fala | RECENTE | 4 | 58.484 | 7.315 | 194.341 | 1, 4, 8, 9 |
| notícia/explicação: fala pra câmera + cenas e cartelas animadas intercaladas | RECENTE | 9 | 30.871 | 4.557 | 376.839 | 2, 3, 5, 6, 7, 12, 13, 14, 15 |
| animação feita por IA, sem rosto | RECENTE | 2 | 20.146 | 11.036 | 29.256 | 10, 11 |

- Tema do TOP: 12 dos 15 mostram na tela uma imagem ou um vídeo gerado por IA como prova. São antes/depois, "um ano atrás × hoje", homenagens (Silvio Santos e Chaves), paródia e testes do gerador de imagens do ChatGPT. Os outros 3 são alertas ou curiosidade: golpe (TOP#3), privacidade dos filhos (TOP#8) e um estudo sobre educação com o ChatGPT (TOP#15).
- Nenhum dos 15 do TOP é só rosto falando. Nos 8 em tela dividida, ele fala para a câmera na metade de baixo e a metade de cima mostra o resultado ou a tela da ferramenta.
- Nos recentes, 5 dos 6 mais vistos mostram IA com corpo ou objeto físico: robôs (RECENTE#7 e #14), bonecos simulados aprendendo a andar (#4 e #8) e o chaveiro-agente da Meta (#5). Os 7 recentes com corpo real ou simulado ou aparelho (#1, 4, 5, 7, 8, 9, 14) têm mediana de 103.367 views. Os 8 sem têm mediana de 27.846,5. Um dos 7 (#1) tinha 10 horas de vida na coleta.

**Contrastes TOP (10 com fala dele) × RECENTES (15)**

| métrica | TOP | RECENTES |
|---|---|---|
| duração mediana | 87,6 s | 115,8 s |
| pal/min da fala (mediana; faixa) | 221 (146–262) | 203 (190–227) |
| cortes/min bruto (mediana) | 2,9 | 12,8 |
| 1º CTA falado (mediana, % da duração) | 58% | 96% |
| pede para seguir antes de 75% do vídeo | 8 de 10 | 1 de 15 |
| apresentação "meu nome é / eu sou" | 4 vídeos, a 9–24% da duração | 7 vídeos, a 90–98% |
| números citados (mediana por vídeo; por minuto de fala) | 2; 1,2 | 6; 3,4 |
| frases com "eu" / com "vocês" | 25,5% / 8,3% | 9,1% / 1,6% |
| "inteligência artificial" × "IA" | 30 × 3 | 24 × 42 |
| frases de virada no meio (seção 4.6) | 5, em 4 vídeos | 19, em 11 vídeos |
| legenda (caracteres, mediana; TOP = 15 vídeos) | 233 | 1.473 |
| pede comentário (fala ou legenda; TOP = 15 vídeos) | 6 de 15 | 12 de 15 |

## 3. Ganchos: primeiros 5 s e texto na tela no 1º frame

| código | grupo | o que é dito em 0–5 s (paráfrase) | texto na tela no 1º frame (OCR t=0 limpo, conferido no frame de 0,4 s) | palavras da manchete | tipo da 1ª frase | manchete × 1ª frase falada |
|---|---|---|---|---|---|---|
| C-xeNM6u9XP | TOP#1 | sem fala (imagens da homenagem com som) | «Silvio Santos 1930 - 2024» + selo «Homenagem feita com IA» | 8 | — | — |
| C-YtsLFPQ3a | TOP#2 | Promete ensinar a trend de abraçar a própria versão criança usando IA | «FOTOS SE ABRAÇANDO COM I.A.» (branco com contorno, sobre foto gerada) | 5 | promessa de tutorial | resumida |
| C2lUA2EPDlE | TOP#3 | (voz da autora original) Mãe recebeu videochamada falsa no WhatsApp pedindo dinheiro | «ESSE GOLPE JÁ EXISTE?» (caixa) + legenda da fala da moça | 4 | react | diferente |
| DBC40xavHaP | TOP#4 | Conta que um seguidor achou vídeo dele melhor que efeito de filme | «MELHORANDO EFEITOS ESPECIAIS RUINS COM I.A.» (tarja vermelha) + legenda da fala | 6 | demonstração/desafio | diferente |
| DABUMqUP-My | TOP#5 | Exibe vídeo de IA antigo do famoso teste com o The Rock | «VÍDEO DE IA 1 ANO ATRÁS VS HOJE!» (tarja vermelha) | 8 | demonstração antes × depois | resumida |
| C_y4_y-PZbK | TOP#6 | Exibe vídeo de IA antigo do teste do Will Smith e espaguete | a mesma tarja do TOP#5 + rótulo «VÍDEO DE IA 1 ANO ATRÁS» no clipe | 8 | demonstração antes × depois | resumida |
| DSkx3dFkaxN | TOP#7 | (áudio de stand-up de terceiro) Líder convoca os 300 para a guerra | nenhum (só a legenda da fala aos 0,4 s) | 0 | — | — |
| Cu28Y46t1pX | TOP#8 | (inglês, anúncio de terceiro) Menina se apresenta aos pais em versão digital | «⚠ CUIDADO» + «75% DOS PAIS POSTAM FOTOS DOS FILHOS ONLINE» | 9 | — | — |
| DR6ABHwj23N | TOP#9 | Promete explicar como fez a homenagem aos personagens do Chaves | «ANTES / DEPOIS» sobre as imagens geradas (25 s de montagem) | 2 | promessa de bastidor | diferente |
| DHpX8l_vftH | TOP#10 | Decreta que o ChatGPT derrubou todos os geradores de imagem | «O CHAT GPT ACABOU DE MATAR TODAS AS IAS DE IMAGEM» (tarja vermelha) | 11 | notícia | igual |
| DRGfDJXjx0M | TOP#11 | Anuncia o desafio de consertar um efeito especial ruim com IA | «MELHORANDO EFEITOS ESPECIAIS RUINS COM IA!» (tarja vermelha) | 6 | demonstração/desafio | igual |
| DMonN4JNaud | TOP#12 | sem fala (trilha) | «"Os resultados da IA são ruins"» + «2022 → 2025» + data e modelo de cada imagem | 8 | — | — |
| DHuby_RvTBk | TOP#13 | Atualização do ChatGPT de dois dias atrás mudou o trabalho; poucos perceberam | «FAZ 48 HORAS QUE O MERCADO DE TRABALHO MUDOU» (tarja vermelha) | 9 | notícia | resumida |
| C5J9aGsvPKq | TOP#14 | sem fala (música licenciada) | «Vídeos de IA um ano atrás» (depois «vs» e «IA hoje») | 6 | — | — |
| DInGtcovBTn | TOP#15 | Pergunta se ser educado com o ChatGPT muda a resposta; promete surpresa | «FALAR POR FAVOR E OBRIGADO PRO CHATGPT FAZ DIFERENÇA?» (tarja vermelha) + meme em quadrinhos | 9 | pergunta | igual |
| Dd2ecFGDuU9 | RECENTE#1 | Treinou uma IA para pegar a bandeira desviando de outra que atira | «EU TREINEI UMA INTELIGÊNCIA ARTIFICIAL PRA TENTAR» (tarja vermelha, continua no quadro seguinte) + simulação com placas «CPDF.AI» | 7 | "eu fiz" | igual |
| Dd1GuwUDESi | RECENTE#2 | Pergunta se já vendem calculadora com ChatGPT escondido para colar | «TÃO VENDENDO CALCULADORAS COM CHATGPT ESCONDIDO DENTRO» (tarja vermelha) + foto do produto | 7 | pergunta | igual |
| Ddz9Xzoju6q | RECENTE#3 | Notícia: o Claude vai marcar até textos dos modelos antigos | cartão branco: «Claude vai colocar marca d'água» + (até nos textos dos modelos antigos) | 13 | notícia | igual |
| DdyzHcECTyI | RECENTE#4 | Ensinou três IAs com corpos diferentes a andar do zero | «EU ENSINEI TRÊS INTELIGÊNCIAS ARTIFICIAIS A ANDAR,» (tarja vermelha) + «sem treino» | 7 | "eu fiz" | igual |
| DdxElXaE2Uc | RECENTE#5 | Meta apresenta agente de IA de bolso com promessa de mudar tudo | «O NOVO AGENTE DE IA PORTÁTIL DA META PROMETE MUDAR O MERCADO!» (tarja vermelha) | 12 | notícia | igual |
| DdwRiX8EQso | RECENTE#6 | Pergunta por que a IA inventa respostas; lembra caso de advogado | título animado «Por que a inteligência artificial…» + exemplos de erro («2 + 2 = 5», «A Lua é feita de queijo!») | 7 | pergunta | igual |
| DdwHUgCjtm- | RECENTE#7 | Garante que as imagens de luta de robô são reais | «ESSE É UM VÍDEO REAL DE UM ROBÔ DA REK!» (tarja vermelha) | 10 | demonstração | igual |
| Ddu1RobAscT | RECENTE#8 | Deu um corpo a uma IA e a ensinou a andar | «EU DEI UM CORPO PRA UMA IA E ENSINEI ELA A ANDAR.» (tarja vermelha) | 12 | "eu fiz" | igual |
| Ddsas0AlQX2 | RECENTE#9 | Refaz com agentes de IA o resgate do filme Eu, Robô | «EU REPLIQUEI COM AGENTES DE INTELIGÊNCIA ARTIFICIAL A CENA DO EU ROBÔ» (letra amarela) + tela da simulação | 12 | "eu fiz" | igual |
| DdrVBELlxFi | RECENTE#10 | (narração gerada) Promete explicar risco de guerra na Europa em um minuto | «GUERRA NA EUROPA?» (tarja vermelha) + «Entenda a possível» + mapa animado | 3 | "entenda" | resumida |
| Ddo1HWIjb99 | RECENTE#11 | (voz clonada) Diz que o modo agente está tomando o lugar do chat | título escrito à mão, animado: «Por que o modo AGENTE tá substituindo o CHAT nas IAs?» | 11 | "entenda" | igual |
| DdnLA3sDoDX | RECENTE#12 | Print de chat com IA virou evidência em investigação da PF | print da conversa (relatório da PF) + «ESSA É UMA CONVERSA COM O CHATGPT» (tarja vermelha) | 7 | notícia | igual |
| DdmjZp3DMxX | RECENTE#13 | Saiu novo modelo líder custando menos da metade do anterior | «UM NOVO MELHOR MODELO DE INTELIGÊNCIA ARTIFICIAL» (tarja vermelha) + robô com etiqueta de preço riscado | 7 | notícia | igual |
| DdjgueRCPqX | RECENTE#14 | Aconteceu a primeira luta estilo UFC entre robô e humano | «REALIZARAM O PRIMEIRO UFC DE ROBÔ CONTRA HUMANO!» (tarja vermelha) | 8 | notícia | igual |
| Ddb_W1wGsF3 | RECENTE#15 | Pergunta se já existem agentes de IA sobrevivendo sozinhos na internet | «JÁ TEM AGENTES DE IA INDEPENDENTES VIVENDO NA INTERNET, LUTANDO PRA SOBREVIVER!» (tarja vermelha) | 12 | pergunta | igual |

Resumo:

- **Começo da fala**: nos 25 vídeos com fala dele, a fala começa em até 0,36 s (22 em 0,0 s). Nenhum abre com saudação nem com apresentação.
- **Densidade nos 5 primeiros segundos**: mediana de 17,1 palavras (TOP 16,8; recentes 17,2), calculada em 24 vídeos. O TOP#9 ficou fora porque o 1º trecho do Whisper cobre de 0 a 29,5 s.
- **Texto no 1º frame**: aparece em 29 de 30 vídeos (a exceção é o TOP#7). Em 18 é uma **tarja vermelha com letra branca em caixa alta** no meio do quadro, entre a imagem de cima e o rosto embaixo: 7 no TOP e 11 nos recentes. A manchete tem mediana de 8 palavras, tanto no TOP quanto nos recentes.
- **Manchete × 1ª frase falada** (25 vídeos com fala dele): igual ou quase igual em 17, versão resumida em 5 e diferente em 3. As 3 diferentes são o react (TOP#3) e 2 vídeos que usam tema ou rótulo em vez da frase (TOP#4 e #9). Nos recentes, 14 de 15 são iguais.
- **Tipo da 1ª frase** (25): notícia com "acabou de", "realizaram" ou "lançou" (7); demonstração, antes × depois ou desafio (5); "eu treinei / ensinei / dei um corpo / repliquei" (4, todos recentes); pergunta (4); promessa de tutorial ou de bastidor (2); "entenda" (2); react (1).
- **Promessa no início, entrega no fim**: em 2 do TOP ele pede para o espectador ficar até o final (TOP#4 aos 12,5 s e TOP#15 aos 4,1 s). No TOP#4 ele também avisa aos 31,9 s que ainda não vai mostrar o resultado. O TOP#9 abre com 25 s do resultado (antes/depois) e só depois explica.
- **Moldes** (com lacunas):
  - "[Empresa] acabou de [lançar/anunciar] [coisa] e [consequência para quem assiste]", com a mesma frase na tarja.
  - "Faz [N horas] que [mudança] e a maioria ainda não percebeu".
  - "Eu [treinei/ensinei] [IA/agente] a [tarefa física ou de decisão]" e depois "vamos ver isso na prática".
  - "Esse é [resultado de IA] de [um ano atrás]… e esse é o de hoje".
  - "[Hábito comum] com [ferramenta] faz diferença no [resultado]?" com promessa de resposta no fim.
  - "Essa é [a conversa/o print] que virou [prova/escândalo] em [caso conhecido]".

## 4. Linguagem (25 vídeos com fala dele em pt e flag ok; 9.186 palavras; 588 frases)

### 4.1 Top 30 expressões recorrentes de 2 a 4 palavras

Contagem por regex sobre a fala dele, sem combinações feitas só de palavras vazias (artigo, preposição, pronome, conjunção, formas de ser/estar/ter/ir). Variantes que só existem dentro de uma expressão maior foram fundidas (ex.: "de me seguir para" entra em "me seguir"), e "chat GPT"/"ChatGPT" contam juntos. A ordem é por nº de vídeos e, depois, por ocorrências. **Fórmula** = frase de CTA ou de apresentação; **conteúdo** = o resto.

| # | expressão | tipo | vídeos (de 25) | ocorrências | no TOP (de 10) | nos recentes (de 15) |
|---|---|---|---|---|---|---|
| 1 | inteligência artificial | conteúdo | 21 | 54 | 10 | 11 |
| 2 | me segue | fórmula | 14 | 14 | 2 | 12 |
| 3 | professor de | fórmula | 11 | 13 | 4 | 7 |
| 4 | nos comentários | fórmula | 11 | 11 | 5 | 6 |
| 5 | aprender tudo sobre | fórmula | 9 | 9 | 4 | 5 |
| 6 | Danilo Gato | fórmula | 9 | 9 | 4 | 5 |
| 7 | de verdade | conteúdo | 8 | 12 | 0 | 8 |
| 8 | a IA | conteúdo | 8 | 12 | 0 | 8 |
| 9 | meu nome é | fórmula | 8 | 8 | 4 | 4 |
| 10 | a gente | conteúdo | 7 | 17 | 3 | 4 |
| 11 | eu fiz | conteúdo | 7 | 11 | 6 | 1 |
| 12 | me seguir | fórmula | 7 | 10 | 7 | 0 |
| 13 | esse aqui / isso aqui | conteúdo (aponta a tela) | 7 | 8 | 5 | 2 |
| 14 | consultor de | fórmula | 7 | 7 | 2 | 5 |
| 15 | o primeiro | conteúdo | 7 | 7 | 3 | 4 |
| 16 | chat GPT | conteúdo | 6 | 33 | 3 | 3 |
| 17 | muito mais | conteúdo | 6 | 10 | 2 | 4 |
| 18 | na internet | conteúdo | 6 | 8 | 2 | 4 |
| 19 | o resultado | conteúdo | 6 | 8 | 4 | 2 |
| 20 | mais de | conteúdo | 6 | 8 | 1 | 5 |
| 21 | pós-graduação em | fórmula | 6 | 6 | 0 | 6 |
| 22 | minha escola online | fórmula | 6 | 6 | 2 | 4 |
| 23 | na prática | conteúdo | 6 | 6 | 2 | 4 |
| 24 | o texto | conteúdo | 5 | 14 | 2 | 3 |
| 25 | um vídeo | conteúdo | 5 | 8 | 4 | 1 |
| 26 | lembra de (me seguir) | fórmula | 5 | 7 | 5 | 0 |
| 27 | que ficou | conteúdo | 5 | 7 | 5 | 0 |
| 28 | o modelo | conteúdo | 5 | 7 | 1 | 4 |
| 29 | o que vocês acharam | fórmula | 5 | 6 | 4 | 1 |
| 30 | a própria | conteúdo | 5 | 6 | 0 | 5 |

- Fora do top 30:
  - Em 5 vídeos cada: "coisa que", "a mesma", "no dia" e "de IA".
  - Em 4 vídeos cada: "um robô", "The Rock", "acabou de", "dia a dia", "uma foto", "em menos de", "por exemplo", "ao mesmo tempo", "de novo", "todo mundo", "compartilhe esse vídeo" e "link da bio".
  - "olha que" aparece 9 vezes em 3 vídeos; "vocês podem ver", 4 vezes em 3 vídeos.
- 12 das 30 expressões são fórmula. A apresentação segue o molde "[meu nome é] [nome], sou [professor de IA / consultor de IA pra empresas] [instituição]", com "FGV" no TOP e o cargo de "professor de pós-graduação" (IA aplicada a negócios) em 2026. O pedido de follow junta o verbo ("me segue", "lembra de me seguir") a um benefício ("aprender tudo sobre", "não perder").
- "a própria [empresa]" (5 recentes) atribui a fonte de dentro da frase, como em "a própria [empresa] diz/admite". "de verdade" aparece 12 vezes, só em 2026.

### 4.2 Tamanho de frase

- **Pela pontuação do Whisper**: 588 frases, com média de **15,7** palavras e mediana de **13**. 66 frases têm até 5 palavras, 160 têm 20 ou mais e 46 têm 30 ou mais. No TOP: 204 frases, média 16,5 e mediana 14. Nos recentes: 384 frases, média 15,3 e mediana 13.
- **Por trecho do Whisper** (pausa de respiração): 828 trechos, média 11,1 e mediana **11** palavras, igual no TOP e nos recentes. O TOP#9, com pouca pontuação, tem 3 "frases" de média 58 palavras; a mediana por trecho é a medida mais estável.

### 4.3 Tratamento do espectador

| recorte | vídeos | frases | com "você" | com "vocês" | com "você" ou "vocês" | com "eu" | "a gente" (ocorrências) |
|---|---|---|---|---|---|---|---|
| TOP | 10 | 204 | 24 (11,8%) | 17 (8,3%) | 40 (19,6%) | 52 (25,5%) | 9 |
| RECENTES | 15 | 384 | 35 (9,1%) | 6 (1,6%) | 41 (10,7%) | 35 (9,1%) | 8 |
| total | 25 | 588 | 59 (10,0%) | 23 (3,9%) | 81 (13,8%) | 87 (14,8%) | 17 |

- Por mil palavras:

  | termo | total | TOP | recentes |
  |---|---|---|---|
  | "você" | 8,1 | 10,4 | 6,7 |
  | "vocês" | 2,6 | 5,3 | 1,0 |
  | "eu" | 11,2 | 18,4 | 7,0 |

- No TOP ele narra o que fez: "eu fiz", "eu pedi", "eu coloquei". Só o TOP#10 tem 21 "eu". Ele também fala com a plateia no plural ("vocês podem ver", "o que vocês acharam").
- Em 2026 a narração passou para a 3ª pessoa: a empresa, o robô, o agente.
- "a gente" aparece 17 vezes (1,9 por mil palavras) em 7 vídeos, e "pra gente" mais 2 vezes. "tu" não aparece nenhuma vez.

### 4.4 Marcadores de oralidade

| marcador | ocorrências | por mil palavras | vídeos (de 25) | TOP: ocorrências (por mil) | recentes: ocorrências (por mil) | observação |
|---|---|---|---|---|---|---|
| olha | 10 | 1,1 | 3 | 9 (2,7) | 1 (0,2) | 9 na forma "olha que [adjetivo]" (TOP#10, TOP#13, RECENTE#9); 5 delas fecham com "que ficou/ficam". Mais "olhem" 2 vezes no TOP |
| gente (vocativo) | 0 | 0 | 0 | 0 | 0 | as 23 ocorrências são "a gente" (17), "pra gente" (2), "muita gente" (2), "gente boa" (1) e "tem gente" (1) |
| cara | 7 | 0,8 | 6 | 1 (0,3) | 6 (1,0) | nenhum vocativo: 3 vezes "de cara no chão" e 4 vezes "o/esse/um cara" |
| tá | 12 | 1,3 | 7 | 2 (0,6) | 10 (1,7) | contração de "está" |
| né | 7 | 0,8 | 3 | 4 (1,2) | 3 (0,5) | só em TOP#10, TOP#11 e RECENTE#9 |
| sabe | 6 | 0,7 | 5 | 0 | 6 (1,0) | sempre verbo, nunca marcador |
| mano | 0 | 0 | 0 | 0 | 0 | |
| galera | 0 | 0 | 0 | 0 | 0 | |
| pessoal (vocativo) | 5 | 0,5 | 4 | 5 (1,5) | 0 | só no TOP (TOP#3, #5, #10 ×2, #11) |

Outras palavras que marcam o jeito dele:

| palavra | ocorrências | por mil | vídeos (de 25) | TOP (por mil) | recentes (por mil) |
|---|---|---|---|---|---|
| aí (inclui "e aí", 15 vezes em 11 vídeos) | 38 | 4,1 | 15 | 20 (5,9) | 18 (3,1) |
| então | 33 | 3,6 | 15 | 22 (6,5) | 11 (1,9) |
| porque | 23 | 2,5 | 14 | 6 (1,8) | 17 (2,9) |
| só que | 20 | 2,2 | 14 | 4 (1,2) | 16 (2,8) |
| agora | 31 | 3,4 | 16 | 13 (3,9) | 18 (3,1) |
| muito/muita(s) | 46 | 5,0 | 18 | 28 (8,3) | 18 (3,1) |
| sensacional | 10 | 1,1 | 4 | 10 (3,0) | 0 |
| de verdade | 12 | 1,3 | 8 | 0 | 12 (2,1) |
| absurdo/absurdamente | 5 | 0,5 | 3 | 3 (0,9) | 2 (0,3) |
| por exemplo | 5 | 0,5 | 4 | 4 (1,2) | 1 (0,2) |
| inclusive | 4 | 0,4 | 2 | 4 (1,2) | 0 |
| na prática | 6 | 0,7 | 6 | 2 (0,6) | 4 (0,7) |
| ou seja | 3 | 0,3 | 3 | 1 (0,3) | 2 (0,3) |
| "IA" (sigla) | 45 | 4,9 | 14 | 3 (0,9) | 42 (7,2) |
| "inteligência artificial" por extenso | 54 | 5,9 | 21 | 30 (8,9) | 24 (4,1) |

### 4.5 Construção "não é X, é Y"

- **Na fala (25 vídeos)**: a forma exata aparece 0 vezes. A mais próxima está no RECENTE#14: "não foi [X]." seguido de "foi [Y]", em duas frases.
- Há 13 variantes em 10 vídeos (1,4 por mil palavras): 2 no TOP (0,6 por mil) e 11 nos recentes (1,9 por mil).
  - "não [X], [ela/eles] [Y]": RECENTE#6, #7, #14 e #15.
  - "[Y], não [X]" ou "[X] e não [Y]": RECENTE#2, #9 e #10.
  - "não só [X], como [Y]" ou "não é só [X]": TOP#13 e RECENTE#9.
  - "em vez de [X], [Y]": RECENTE#2 e #8.
  - "uma coisa é [X], outra é [Y]": RECENTE#2.
  - "mais do que [X], [Y]": TOP#15.
- **Nas legendas (30)**: 10 legendas usam a construção, 1 do TOP e 9 recentes. A forma exata ("não é apenas [X], é [Y]") só aparece no TOP#13. As variantes estão nos recentes #1, #2, #3, #4, #6, #8, #9, #10 e #14: "[X] e não [Y]", "não fica em [X]; está em [Y]", "em vez de [X], [Y]", "não só [X], como também [Y]" e "[Y], não [X]".

### 4.6 Frases de virada (re-gancho no meio do vídeo)

Contadas à mão sobre candidatos achados por regex. São frases curtas que abrem um novo laço de curiosidade.

- **TOP**: 5 frases em 4 de 10 vídeos. São 2 pedidos para ficar até o final (aos 4% e 15% da duração), 1 "ainda não vou mostrar" (37%), 1 "vocês não vão acreditar" (36%) e 1 "olha que bizarro" (12%).
- **Recentes**: 19 frases em 11 de 15 vídeos, cerca de 1,3 por vídeo.
  - Pedido de explicação, "deixa eu (te) explicar": RECENTE#3 aos 16% e #14 aos 19%.
  - "vamos ver isso na prática": RECENTE#1 aos 30%, #4 aos 34% e #9 aos 24%.
  - "quase ninguém (percebeu/conhece)": RECENTE#2, #11 e #14.
  - "fica esquisito de verdade": RECENTE#12 aos 54% e #15 aos 56%.
  - "a parte que importa": RECENTE#13 aos 49%.
  - "o detalhe mais importante": RECENTE#14 aos 50%.
  - "presta atenção": RECENTE#14 aos 86%.
  - "o resultado?": RECENTE#4 aos 78%.
  - "repara que": RECENTE#8 aos 55%.
  - "o nível 1 da história": RECENTE#12 aos 47%.
  - Pergunta de aposta: RECENTE#1 aos 11%.
  - "o mais legal é que": RECENTE#1 aos 5%.
  - "o que eu quero mostrar": RECENTE#9 aos 93%.
- **Tempo de espera como CTA**: em 4 dos 10 vídeos do TOP, o tempo em que a ferramenta gera vira pedido de follow ou oferta ("enquanto gera", "enquanto carrega", "enquanto a gente espera"). Isso acontece no TOP#4 aos 57%, TOP#5 aos 43%, TOP#6 aos 71% e TOP#11 aos 68%.

### 4.7 Palavras por minuto e perfil de cada vídeo com fala dele em pt

| vídeo | formato | motor | palavras | fala (s) | pal/min (fala) | pal/min (duração total) | frases | média pal/frase | mediana | "você" | "vocês" | "eu" | "a gente" | números | "?" |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TOP#2 | tela dividida | large-v3-turbo | 171 | 50,1 | 205 | 204 | 7 | 24,6 | 17,0 | 11 | 2 | 1 | 0 | 1 | 0 |
| TOP#3 (só a parte dele) | react | large-v3-turbo | 176 | 47,6 | 222 | 118 | 11 | 16,0 | 16,0 | 1 | 2 | 0 | 6 | 0 | 0 |
| TOP#4 | tela dividida | large-v3-turbo | 351 | 85,9 | 245 | 245 | 23 | 15,3 | 14,0 | 2 | 2 | 10 | 0 | 3 | 0 |
| TOP#5 | tela dividida | large-v3-turbo | 224 | 62,9 | 214 | 213 | 10 | 22,5 | 21,5 | 1 | 4 | 1 | 2 | 2 | 0 |
| TOP#6 | tela dividida | large-v3-turbo | 136 | 43,5 | 188 | 186 | 7 | 19,4 | 14,0 | 0 | 0 | 4 | 0 | 0 | 0 |
| TOP#9 | criação + bastidor | large-v3-turbo | 174 | 71,6 | 146 | 146 | 3 | 58,0 | 20,0 | 2 | 1 | 3 | 0 | 2 | 0 |
| TOP#10 | tela dividida | large-v3-turbo | 763 | 174,8 | 262 | 262 | 68 | 11,2 | 9,0 | 3 | 1 | 21 | 1 | 2 | 2 |
| TOP#11 | tela dividida | large-v3-turbo | 331 | 89,7 | 221 | 218 | 19 | 17,4 | 13,0 | 1 | 4 | 13 | 0 | 2 | 1 |
| TOP#13 | tela dividida | large-v3-turbo | 636 | 146,1 | 261 | 261 | 37 | 17,2 | 15,0 | 9 | 1 | 7 | 0 | 3 | 0 |
| TOP#15 | tela dividida | large-v3-turbo | 406 | 110,2 | 221 | 221 | 19 | 21,4 | 18,0 | 5 | 1 | 2 | 0 | 0 | 1 |
| RECENTE#1 | experimento | small | 327 | 87,5 | 224 | 224 | 14 | 23,4 | 18,0 | 1 | 0 | 6 | 1 | 5 | 1 |
| RECENTE#2 | notícia | small | 501 | 150,6 | 200 | 200 | 23 | 21,9 | 18,0 | 3 | 1 | 1 | 0 | 2 | 2 |
| RECENTE#3 | notícia | large-v3-turbo | 461 | 131,1 | 211 | 211 | 27 | 17,4 | 16,0 | 5 | 0 | 2 | 0 | 4 | 0 |
| RECENTE#4 | experimento | large-v3-turbo | 376 | 116,9 | 193 | 193 | 27 | 14,0 | 14,0 | 1 | 0 | 4 | 0 | 13 | 1 |
| RECENTE#5 | notícia | large-v3-turbo | 433 | 114,3 | 227 | 227 | 29 | 15,1 | 14,0 | 7 | 0 | 0 | 1 | 5 | 0 |
| RECENTE#6 | explicação | large-v3-turbo | 312 | 92,7 | 202 | 197 | 21 | 14,9 | 15,0 | 3 | 0 | 1 | 0 | 1 | 1 |
| RECENTE#7 | notícia | large-v3-turbo | 517 | 153,0 | 203 | 202 | 39 | 13,4 | 13,0 | 3 | 0 | 1 | 0 | 20 | 1 |
| RECENTE#8 | experimento | large-v3-turbo | 246 | 77,8 | 190 | 189 | 14 | 17,6 | 14,0 | 2 | 0 | 3 | 0 | 9 | 0 |
| RECENTE#9 (sem as falas das IAs) | experimento | large-v3-turbo | 651 | 178,9 | 218 | 218 | 42 | 15,5 | 13,0 | 3 | 2 | 20 | 2 | 9 | 2 |
| RECENTE#10 | animação IA | large-v3-turbo | 202 | 58,6 | 207 | 205 | 17 | 11,9 | 13,0 | 0 | 0 | 0 | 0 | 3 | 0 |
| RECENTE#11 | animação IA | large-v3-turbo | 140 | 41,4 | 203 | 201 | 11 | 12,8 | 13,0 | 3 | 0 | 0 | 0 | 1 | 0 |
| RECENTE#12 | notícia | large-v3-turbo | 453 | 128,2 | 212 | 211 | 28 | 16,2 | 13,0 | 2 | 2 | 1 | 0 | 8 | 1 |
| RECENTE#13 | notícia | large-v3-turbo | 373 | 115,3 | 194 | 193 | 24 | 15,8 | 16,5 | 4 | 0 | 0 | 0 | 13 | 0 |
| RECENTE#14 | notícia | large-v3-turbo | 453 | 137,3 | 198 | 197 | 32 | 14,4 | 12,0 | 0 | 0 | 1 | 4 | 12 | 0 |
| RECENTE#15 | notícia | large-v3-turbo | 373 | 100,1 | 223 | 223 | 36 | 10,5 | 10,0 | 2 | 1 | 1 | 0 | 6 | 1 |

- **Palavras/min**: mediana de **211** nos 25 vídeos. No TOP (10) a mediana é 221, com faixa de 146 a 262. Nos recentes (15) é 203, com faixa de 190 a 227.
- **Palavras por vídeo**: mediana de 277,5 no TOP e 376 nos recentes.
- **Números**: 126 no total. No TOP a mediana é 2 por vídeo (0 a 3), ou 1,2 por minuto de fala. Nos recentes é 6 (1 a 20), ou 3,4 por minuto. O RECENTE#7 (linha do tempo dos robôs, ano a ano) cita 20.
- **Perguntas**: 14 sinais "?" em 9.186 palavras, ou 0,15 por 100 palavras. Ele afirma muito mais do que pergunta.

## 5. Legenda (caption) dos 30

| código | grupo | caracteres | linhas | emojis | hashtags | CTA na legenda | "?" | menção @ | fontes citadas |
|---|---|---|---|---|---|---|---|---|---|
| C-xeNM6u9XP | TOP#1 | 300 | 1 | 0 | 0 | — | 0 | — | — |
| C-YtsLFPQ3a | TOP#2 | 384 | 2 | 0 | 0 | comenta opinião + link na bio | 0 | — | — |
| C2lUA2EPDlE | TOP#3 | 210 | 3 | 0 | 3 | comenta opinião | 1 | @hgoficinajuridica (crédito) | — |
| DBC40xavHaP | TOP#4 | 131 | 1 | 0 | 0 | link na bio | 0 | — | — |
| DABUMqUP-My | TOP#5 | 316 | 2 | 0 | 0 | link na bio | 0 | — | — |
| C_y4_y-PZbK | TOP#6 | 80 | 1 | 0 | 0 | — (só pergunta) | 1 | — | — |
| DSkx3dFkaxN | TOP#7 | 84 | 2 | 2 | 0 | — | 0 | @othiagoventura, @odanilogato (collab) | — |
| Cu28Y46t1pX | TOP#8 | 384 | 1 | 0 | 10 | — | 0 | — | — |
| DR6ABHwj23N | TOP#9 | 233 | 1 | 0 | 0 | segue + comenta opinião | 0 | — | — |
| DHpX8l_vftH | TOP#10 | 100 | 1 | 0 | 0 | — | 0 | — | — |
| DRGfDJXjx0M | TOP#11 | 329 | 1 | 0 | 0 | comenta para receber link (desconto) | 0 | — | — |
| DMonN4JNaud | TOP#12 | 700 | 2 | 0 | 0 | link na bio | 0 | — | — |
| DHuby_RvTBk | TOP#13 | 588 | 2 | 0 | 0 | link na bio | 0 | — | — |
| C5J9aGsvPKq | TOP#14 | 207 | 2 | 0 | 2 | link na bio | 0 | — | — |
| DInGtcovBTn | TOP#15 | 100 | 1 | 0 | 0 | — (título em pergunta) | 1 | — | — |
| Dd2ecFGDuU9 | RECENTE#1 | 1.732 | 7 | 0 | 0 | comenta opinião + segue | 1 | @odanilogato | — |
| Dd1GuwUDESi | RECENTE#2 | 1.739 | 4 | 0 | 0 | comenta opinião + segue + link externo (site) | 1 | @odanilogato | — |
| Ddz9Xzoju6q | RECENTE#3 | 1.320 | 4 | 0 | 0 | — (só pergunta final) | 1 | — | — |
| DdyzHcECTyI | RECENTE#4 | 1.505 | 5 | 0 | 0 | comenta opinião + segue | 1 | @odanilogato | — |
| DdxElXaE2Uc | RECENTE#5 | 1.149 | 8 | 0 | 0 | comenta opinião + segue | 1 | — | sim |
| DdwRiX8EQso | RECENTE#6 | 863 | 6 | 0 | 0 | comenta opinião + segue | 2 | — | — |
| DdwHUgCjtm- | RECENTE#7 | 1.765 | 5 | 0 | 0 | comenta opinião + compartilha + segue | 1 | — | — |
| Ddu1RobAscT | RECENTE#8 | 1.473 | 4 | 0 | 0 | comenta opinião + compartilha + segue | 1 | @odanilogato | — |
| Ddsas0AlQX2 | RECENTE#9 | 972 | 7 | 0 | 0 | segue (+ pergunta) | 1 | @odanilogato | — |
| DdrVBELlxFi | RECENTE#10 | 2.162 | 19 | 0 | 0 | link na bio | 0 | — | sim (9 links) |
| Ddo1HWIjb99 | RECENTE#11 | 739 | 4 | 0 | 0 | link na bio | 0 | — | — |
| DdnLA3sDoDX | RECENTE#12 | 1.628 | 4 | 0 | 0 | comenta opinião + segue | 1 | @odanilogato | — |
| DdmjZp3DMxX | RECENTE#13 | 1.299 | 4 | 0 | 0 | comenta opinião + segue | 1 | @odanilogato | — |
| DdjgueRCPqX | RECENTE#14 | 1.286 | 7 | 0 | 0 | segue | 0 | — | — |
| Ddb_W1wGsF3 | RECENTE#15 | 2.168 | 10 | 0 | 0 | comenta opinião + segue | 1 | @odanilogato | sim |

| recorte | caracteres (média / mediana) | linhas (média / mediana) | emojis por legenda (média) | legendas com hashtag | hashtags (total) | legendas com "?" | "?" (total) | legendas com @ |
|---|---|---|---|---|---|---|---|---|
| TOP 15 | 276 / 233 | 1,5 / 1 | 0,13 | 3 | 15 | 3 | 3 | 2 |
| RECENTES 15 | 1.453 / 1.473 | 6,5 / 5 | 0 | 0 | 0 | 12 | 13 | 8 |
| 30 | 865 / 720 | 4,0 / 3,5 | 0,07 | 3 | 15 | 15 | 16 | 10 |

**Tipos de CTA (legendas com o tipo)**

| tipo | TOP 15 | RECENTES 15 | 30 |
|---|---|---|---|
| comenta palavra ou comenta para receber link | 1 | 0 | 1 |
| comenta opinião / "me conta aqui embaixo" | 3 | 10 | 13 |
| link na bio (aula grátis, imersão, comunidade, escola) | 6 | 2 | 8 |
| link externo na própria legenda | 0 | 1 | 1 |
| segue (a maioria com "@odanilogato" escrito) | 1 | 12 | 13 |
| salva | 0 | 0 | 0 |
| compartilha / manda pra alguém | 0 | 2 | 2 |
| direct | 0 | 0 | 0 |
| **qualquer CTA explícito** | 9 | 14 | 23 |

- **Emojis**: 0 nas 29 legendas escritas por ele. Os 2 emojis estão na legenda da collab (TOP#7). **Hashtags**: 15, em 3 legendas de 2023–24; nenhuma em 2026.
- **Recentes**: 13 de 15 legendas começam repetindo o gancho do vídeo em forma de manchete; as 2 exceções são as animações feitas por IA, cuja legenda fala de como o vídeo foi feito. 12 de 15 fecham com uma pergunta direta ao espectador, e a pergunta é o convite ao comentário. 8 escrevem o próprio @ no pedido de follow. 3 listam fontes (RECENTE#5, #10 e #15), e o #5 declara que o vídeo foi produzido com ajuda de IA.
- **TOP**: legenda curta, em geral 1 frase exclamativa de título seguida de "link na bio" para aula grátis, imersão ou comunidade (6 de 15). O único "comenta que eu mando o link" é o TOP#11, da Black Friday, que tem 0,116% de comentários/views, 2,8x a mediana do TOP (0,042%).

**CTA falado, apresentação e oferta, vídeo a vídeo** (segundos interpolados)

| código | grupo | dur (s) | CTAs falados (segundo: tipo) | apresentação "meu nome é / eu sou" (s; % do vídeo) | oferta de produto falada (s) | CTA ou marca na tela |
|---|---|---|---|---|---|---|
| C-YtsLFPQ3a | TOP#2 | 50,2 | 43,2: compartilha; 45,0: segue | — | — | — |
| C2lUA2EPDlE | TOP#3 | 89,3 | 84,8: comenta; 87,3: curte; 87,8: segue | — | — | — |
| DBC40xavHaP | TOP#4 | 85,9 | 21,0: segue; 70,2: link (inscrição); 78,3: comenta; 79,8: compartilha | 15,1; 18% | 49,2 (imersão) | print do perfil aos 16 s; página de inscrição aos 70 s |
| DABUMqUP-My | TOP#5 | 63,2 | 34,5: segue; 37,8: compartilha | — | — | «LINK NOS COMENTÁRIOS» aos 60 s |
| C_y4_y-PZbK | TOP#6 | 43,8 | 32,0: segue; 35,0: compartilha; 42,5: link (nos comentários) | — | — | — |
| DSkx3dFkaxN | TOP#7 | 153,4 | 151,2: segue | — | — | — |
| DR6ABHwj23N | TOP#9 | 71,7 | 44,2: segue; 69,2: segue; 70,2: comenta | — | 29,5 (escola, desconto) | — |
| DHpX8l_vftH | TOP#10 | 174,9 | 19,0: segue; 172,9: compartilha | 16,1; 9% | — | print do perfil aos 16 s |
| DRGfDJXjx0M | TOP#11 | 91,3 | 62,1: segue; 78,1: comenta; 80,6: comenta p/ receber link; 83,4: comenta; 84,4: comenta p/ receber link; 85,9: segue | — | 65,8 (escola, desconto) | — |
| DHuby_RvTBk | TOP#13 | 146,2 | 26,3: segue; 31,5: direct (contratar treinamento); 141,5: segue; 145,7: link na bio | 20,2; 14% | 28,8 e 142,7 (treinamento, curso) | print do perfil aos 20 s |
| DInGtcovBTn | TOP#15 | 110,3 | 30,1: segue; 105,2: segue; 108,4: comenta | 26,2; 24% | — | print do perfil aos 26–30 s |
| Dd2ecFGDuU9 | RECENTE#1 | 87,7 | 84,4: segue; 87,0: link na bio | 79,2; 90% | 85,1 (escola) | placas «CPDF.AI» dentro da simulação |
| Dd1GuwUDESi | RECENTE#2 | 150,6 | 134,4: comenta; 147,1: link na bio; 148,3: segue | 135,5; 90% | 141,9 (escola) | — |
| Ddz9Xzoju6q | RECENTE#3 | 131,3 | 119,0: comenta; 127,7: segue | 128,3; 98% (credencial dentro do CTA) | — | — |
| DdyzHcECTyI | RECENTE#4 | 117,1 | 112,5: segue; 115,9: link na bio | 108,0; 92% | 113,5 (escola) | placas «CPDF.AI» dentro da simulação |
| DdxElXaE2Uc | RECENTE#5 | 114,5 | 112,0: segue | 106,8; 93% | — | — |
| DdwRiX8EQso | RECENTE#6 | 95,0 | 89,2: segue; 90,0: comenta | — | — | — |
| DdwHUgCjtm- | RECENTE#7 | 153,4 | 148,3: comenta; 148,9: compartilha; 150,9: segue | — | — | — |
| Ddu1RobAscT | RECENTE#8 | 78,1 | 37,0: segue; 74,3: comenta | — | — | placa «Profissionais do Futuro» na simulação |
| Ddsas0AlQX2 | RECENTE#9 | 178,9 | 175,6: segue; 177,3: comenta | — | — | — |
| DdrVBELlxFi | RECENTE#10 | 59,0 | 58,0: link na bio | — | 52,7 (escola) | selo «ESCOLA ONLINE DE IA» no fim |
| Ddo1HWIjb99 | RECENTE#11 | 41,8 | 39,6: segue | — | — | — |
| DdnLA3sDoDX | RECENTE#12 | 128,7 | 118,8: comenta; 124,4: segue | — | — | — |
| DdmjZp3DMxX | RECENTE#13 | 115,8 | 113,0: segue | 106,5; 92% | — | — |
| DdjgueRCPqX | RECENTE#14 | 137,8 | 133,9: segue | — | — | — |
| Ddb_W1wGsF3 | RECENTE#15 | 100,4 | 94,1: segue; 98,1: comenta | 90,8; 90% | — | — |

(TOP#1, #8, #12 e #14 não têm CTA falado.)

- **TOP (10 com fala dele)**:
  - O 1º CTA falado sai, na mediana, a 58% da duração, e 8 de 10 pedem para seguir antes de 75%.
  - O pedido vem logo depois da apresentação com credencial, a 9–24% do vídeo e com print do perfil na tela (TOP#4, #10, #13 e #15), ou no tempo morto em que a ferramenta gera (TOP#4, #5, #6 e #11).
  - Média de 1,4 pedidos de follow por vídeo (14 em 10). O pedido de comentário vem no fim: "o que vocês acharam" em 4 vídeos.
  - 4 de 10 oferecem produto na fala: escola, desconto, imersão ou treinamento.
- **RECENTES (15)**:
  - O 1º CTA sai, na mediana, a 96% da duração; em 14 de 15 isso acontece depois de 89%. A exceção é o RECENTE#8, que pede follow aos 47%.
  - A apresentação foi para o fim (7 vídeos, a 90–98%). Média de 0,93 pedido de follow por vídeo.
  - Pedido de comentário na fala em 8 de 15; somando a legenda, 12 de 15. 4 de 15 oferecem a escola.

## 6. Correlações de Spearman entre views e cada variável

ρ de Spearman (empates com posto médio) e p bicaudal do scipy. **Com n = 30, ou 15 dentro de cada grupo, isto é indício, não prova.** Foram 29 testes com variação (4 variáveis ficam constantes nos recentes), e a p < 0,05 espera-se cerca de 1,5 "significância" só por acaso. Nos 30, o TOP (2023–2025, views fechadas) se mistura com os recentes (set/2026, 0,4 a 10,7 dias de vida). Por isso o recorte dos 30 mede sobretudo época e idade do post, não uma alavanca de roteiro.

| variável | 30 (n; ρ; p) | dentro do TOP (n; ρ; p) | dentro dos recentes (n; ρ; p) |
|---|---|---|---|
| duração (s) | 30; −0,33; 0,075 | 15; −0,41; 0,128 | 15; 0,25; 0,376 |
| palavras/min (fala pt, flag ok) | 26; −0,10; 0,619 | 11; −0,36; 0,272 | 15; −0,22; 0,420 |
| cortes/min bruto | 30; −0,31; 0,095 | 15; −0,36; 0,190 | 15; 0,42; 0,119 |
| cortes/min agrupado | 30; −0,30; 0,112 | 15; −0,34; 0,214 | 15; 0,45; 0,091 |
| tamanho da legenda (caracteres) | **30; −0,71; < 0,001** | 15; −0,04; 0,884 | 15; 0,36; 0,191 |
| texto no 1º frame (0/1) | 30; −0,18; 0,335 | 15; −0,06; 0,827 | constante (15 de 15) |
| tarja vermelha no 1º frame (0/1) | 30; −0,17; 0,383 | 15; −0,25; 0,374 | **15; 0,59; 0,020** |
| fala, qualquer idioma (0/1) | 30; −0,25; 0,182 | 15; 0,12; 0,681 | constante |
| fala dele em pt (0/1) | **30; −0,37; 0,046** | 15; 0,07; 0,817 | constante |
| pedido de comentário, na fala ou na legenda (0/1) | 30; −0,30; 0,109 | 15; 0,13; 0,655 | 15; 0,12; 0,681 |
| pedido de comentário só na fala (0/1) | 30; −0,19; 0,314 | 15; −0,07; 0,817 | 15; 0,00; 1,000 |

Em negrito: p < 0,05. Nos recentes, views × idade do post dá ρ 0,12 (p 0,657), ou seja, a idade não explica sozinha a ordem dos recentes.

**Mediana de views com × sem (nos 30)**

| variável | com (n; mediana) | sem (n; mediana) | dentro do TOP: com × sem | dentro dos recentes: com × sem |
|---|---|---|---|---|
| texto no 1º frame | 29; 376.839 | 1; 3.043.897 | 14: 2.907.559 × 1: 3.043.897 | 15: 29.256 × 0: — |
| tarja vermelha no 1º frame | 18; 183.812 | 12; 2.619.254 | 7: 2.479.871 × 8: 2.999.767 | 11: 85.809 × 4: 12.319 |
| fala (qualquer idioma) | 27; 194.341 | 3; 2.379.028 | 12: 2.999.767 × 3: 2.379.028 | 15: 29.256 × 0: — |
| fala dele em pt | 25; 173.284 | 5; 2.955.637 | 10: 3.191.478 × 5: 2.955.637 | 15 × 0 |
| pedido de comentário (fala ou legenda) | 18; 138.326 | 12; 2.429.450 | 6: 3.396.829 × 9: 2.955.637 | 12: 29.578 × 3: 29.256 |

Com comentários/views no lugar de views:

| variável | 30 (ρ; p) | TOP (ρ; p) | recentes (ρ; p) |
|---|---|---|---|
| duração | **0,73; < 0,001** | **0,86; < 0,001** | **0,60; 0,018** |
| pedido de comentário (0/1) | **0,37; 0,044** | 0,35; 0,206 | 0,15; 0,583 |

Leitura:

- **Tamanho da legenda** (−0,71 nos 30) e **fala dele** (−0,37 nos 30) são efeito de época. As legendas longas e a fala em 100% dos vídeos são de set/2026, quando as views ainda estavam abertas. Dentro de cada grupo o sinal some (TOP −0,04) ou inverte (recentes +0,36).
- **Tarja vermelha no 1º frame**: é a única associação com p < 0,05 dentro de um grupo. Nos recentes, 11 vídeos com tarja têm mediana de 85.809 views; os 4 sem tarja (cartão branco, título animado ou letra amarela) têm 12.319. No TOP não aparece (ρ −0,25), porque os 3 maiores não têm tarja vermelha, e o maior nem tem fala.
- **Cortes/min** tem sinal oposto nos dois grupos (TOP −0,36; recentes +0,45; p 0,19 e 0,09). A tela dividida quase parada do TOP funcionou em 2024–25. Em 2026, com cenas intercaladas, mais corte andou junto com mais view. Nenhum dos dois é significativo.
- **Duração não prevê views** (−0,41 no TOP, +0,25 nos recentes), mas **prevê comentário por view** nos dois grupos (0,86 e 0,60). Vídeo mais longo, com explicação, rende conversa. Os curtos sem fala (5 a 16 s) têm 0,011–0,012%.

## 7. Os 7 achados quantitativos para quem vai roteirizar

1. **O alcance grande está em 2024–25, e 2026 voltou ao patamar de 2022.** A mediana é de 33.716 views (3,8% dos 895.021 seguidores), o p90 é 220.030, e só 28 de 1.263 reels (2,2%) passaram de 1 milhão. Nenhum dos 15 maiores é de 2026 (7 de 2024, 7 de 2025). A mediana por bloco de 50 chegou a 127.531 em out–dez/2024 (3,78x) e a 97.867 em fev–abr/2025. Os 150 reels desde abr/2026 ficaram entre 28 e 34 mil (0,84–1,00x), postando 5,7 a 6,7 por semana, contra 4,8 nos blocos de pico. Os 15 recentes somam mediana de 29.256 (0,87x), mas tinham de 0,4 a 10,7 dias na coleta.
2. **O que viralizou foi um resultado de IA visível, com ele narrando para a câmera.** 12 dos 15 maiores mostram imagem ou vídeo gerado por IA como prova: antes/depois, "um ano atrás × hoje", homenagem, paródia e testes de lançamento. 8 dos 15 usam tela dividida, com ele falando na metade de baixo e a prova na de cima (mediana de 3,0 milhões; de 2,1 a 6,7 milhões), e 3 são montagens sem fala, incluindo o maior de todos: 14,1 milhões em 5,2 s. Nenhum dos 15 é só rosto falando. Nos recentes, 5 dos 6 mais vistos mostram IA com corpo ou objeto (robô, boneco simulado, chaveiro-agente); os 7 com corpo têm mediana de 103.367 views, contra 27.847 dos 8 sem.
3. **O gancho é a manchete dita no segundo zero, e a tarja repete a frase.** A fala começa em até 0,36 s em 25 de 25 vídeos, com mediana de 17,1 palavras nos primeiros 5 s e nenhuma saudação. 29 de 30 têm texto no 1º frame; em 18 é uma tarja vermelha com letra branca em caixa alta, com mediana de 8 palavras. Em 17 de 25 a tarja é a própria 1ª frase falada; em 5, uma versão resumida. Os tipos de abertura são notícia com "acabou de" (7), demonstração ou antes/depois (5), "eu treinei / ensinei / dei um corpo" (4) e pergunta (4). Nos recentes, vídeos com tarja vermelha têm mediana de 85.809 contra 12.319 sem (ρ 0,59; p 0,02; n = 15; indício).
4. **O ritmo é denso e afirmativo: 211 palavras/min, frase de 13 palavras, números concretos e quase nenhuma pergunta.** A mediana de palavras por minuto é 221 no TOP (146–262) e 203 nos recentes (190–227). A frase tem média de 15,7 palavras e mediana de 13, e a pausa de respiração, mediana de 11. São só 0,15 "?" por 100 palavras. Os recentes citam 6 números por vídeo (3,4 por minuto), contra 2 no TOP (1,2 por minuto); o recente mais visto (376.839) cita 20, numa linha do tempo ano a ano. Em 2026 entram frases de virada no meio: 19 em 11 de 15 vídeos, como "fica esquisito de verdade", "a parte que importa" e "quase ninguém percebeu". No TOP foram 5, em 4 de 10.
5. **No TOP, o pedido de follow vem no meio; em 2026, todo CTA foi para o fim.** Nos 10 do TOP com fala dele, o 1º CTA sai na mediana de 58% da duração, e 8 de 10 pedem para seguir antes de 75%. O pedido vem logo depois da apresentação com credencial ("meu nome é… professor de IA na FGV", a 9–24% do vídeo e com print do perfil na tela, em 4 vídeos) ou no tempo morto "enquanto gera" (4 vídeos), com 1,4 pedido de follow por vídeo. Nos recentes, o 1º CTA sai a 96%, 14 de 15 depois de 89%, e a apresentação foi para 90–98%. O pedido de comentário subiu de 6 de 15 (TOP) para 12 de 15 (recentes). Comentário por view cresce com a duração (ρ 0,86 no TOP; 0,60 nos recentes).
6. **A linguagem é de professor didático, sem gíria, e mudou da 1ª para a 3ª pessoa.**
   - As expressões mais repetidas são fórmula de CTA e apresentação: "me segue" (14 vídeos), "professor de" (11), "nos comentários" (11), "aprender tudo sobre" (9) e "meu nome é" (8).
   - No TOP: "eu" em 25,5% das frases, "vocês" em 8,3%, "sensacional" 10 vezes, "olha que [adjetivo]" 8 vezes, "pessoal" como vocativo 5 vezes, e "inteligência artificial" por extenso 30 vezes contra 3 de "IA".
   - Em 2026: "eu" em 9,1% das frases, "vocês" em 1,6%, "de verdade" 12 vezes, "a própria [empresa]" em 5 vídeos e "IA" 42 vezes contra 24 por extenso.
   - "mano", "galera" e "gente" como vocativo aparecem 0 vezes; "né" 7 e "tá" 12.
   - "Não é X, é Y": 0 na forma exata na fala e 13 variantes em 10 vídeos (1,4 por mil palavras; 11 nos recentes). Na legenda, 10 de 30 usam a construção.
7. **Em 2026 a legenda virou um texto de apoio, sem efeito mensurável, e toda correlação aqui é indício.**
   - No TOP a legenda tem mediana de 233 caracteres e 1 linha, hashtags em 3 legendas e "link na bio" em 6.
   - Nos recentes são 1.473 caracteres (6,3x) em 5 linhas, com 0 hashtag e 0 emoji. 13 de 15 abrem repetindo o gancho, 12 fecham com pergunta ao espectador, 12 pedem follow (8 com o @ escrito) e 3 citam fontes.
   - O tamanho da legenda dá ρ −0,71 nos 30 (efeito de época), −0,04 dentro do TOP e +0,36 dentro dos recentes.
   - Com n = 30, ou 15 por grupo, e 29 testes, espera-se cerca de 1,5 falso positivo. Só a tarja vermelha nos recentes passa de p < 0,05 dentro de um grupo.
   - Nenhum dos 30 é provável anúncio (menor likes/views: 2,04%).
