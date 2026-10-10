# @inventormiguel (Miguel Lannes): ficha quantitativa

Fonte: coleta de 29/09/2026 com login (1.930 reels, lista completa), dossiê e arquivos brutos por vídeo (transcrição Whisper, OCR a cada 2 s, cortes). Seguidores: 397.274. Cálculo em Python 3 (numpy/scipy); números exatos, arredondados só na exibição.

Definições usadas em toda a ficha:
- **views** = `play_count` da lista completa (o mesmo número do dossiê). 34 reels antigos (2017 a 2022, IGTV/feed) não têm `play_count` e ficam fora das estatísticas de views.
- **mediana geral** = 8.893,5 views (o dossiê mostra 8.893 porque trunca). **Múltiplo** = views ÷ 8.893,5.
- **PROVÁVEL-ANÚNCIO** = likes/views < 0,3%: TOP#9 (DPruqH5ibBj) e TOP#11 (DPyxGjagMYz). Entram nas tabelas, mas são criativo impulsionado, não viral orgânico.
- **palavras/min** = palavras ÷ (fim do último trecho falado − início do primeiro) × 60, só para fala em português com flag ok e mais de 5 s de fala. Antes de contar, removi o trecho final que é alucinação típica do Whisper sobre música ("E aí" em TOP#14, RECENTE#7 e RECENTE#10; "Thank you." em TOP#1) e cortei trechos que passavam da duração do vídeo. Por isso TOP#14 dá 201 pal/min aqui e 139 no dossiê (lá o "E aí" de 30 s esticava a fala até 111 s num vídeo de 82 s).
- **cortes/min** = mudanças de cena (limiar 0,3, arquivo `vis.json`) ÷ duração × 60.
- RECENTE#1 a #6 foram transcritos com o faster-whisper-small, que erra mais nomes próprios (ex.: "Cidense" = Seedance, "eave" = IA). Contagens de palavras e marcadores desses 6 podem variar alguns por cento.
- Views dos RECENTES ainda não maduraram: RECENTE#1 tinha 0,6 dia no ar e RECENTE#2, 0,9 dia na coleta.

## 1. Distribuição de views e tendência

Base: 1.896 reels com views (de 1.930 coletados). Percentis por interpolação linear.

| p10 | p25 | p50 (mediana) | p75 | p90 | p99 | máximo | média |
|---|---|---|---|---|---|---|---|
| 2.273 | 4.127 | 8.893,5 | 19.621 | 52.240 | 795.236 | 13.211.376 | 54.685 |

- Concentração: só **15 reels (0,8%) passaram de 1 milhão**, e são exatamente os 15 do TOP. Eles somam **52,7% de todas as views** do perfil. O 1% mais visto (19 reels) soma 55,9%; os 10% mais vistos somam 81,3%.
- 105 reels (5,5%) passaram de 100 mil. A média (54.685) é 6,1 vezes a mediana: a média não descreve o vídeo típico.
- Nos últimos 12 meses (blocos 1 a 15, out/2025 a set/2026) saíram 13 reels acima de 1 milhão em 750 publicados: **1 a cada 58 reels**, em ritmo de cerca de 2 reels por dia.

**Mediana por ano** (data tirada do ID do post):

| ano | reels com views | mediana | reels ≥ 1 mi |
|---|---|---|---|
| 2022 | 40 | 499 | 0 |
| 2023 | 165 | 2.202 | 1 |
| 2024 | 351 | 4.554 | 0 |
| 2025 | 779 | 10.873 | 5 |
| 2026 | 561 | 12.663 | 9 |

**Mediana por blocos de 50 reels, do mais novo para o mais velho** (ordem cronológica pelo ID do post; o fixado entra na sua data real, não no topo):

| bloco | posições | período | dias | reels com views | mediana | p90 | máximo | ≥100 mil | ≥1 mi |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1-50 | 2026-09-02 a 2026-09-28 | 26 | 50 | 7.142 | 45.841 | 229.942 | 3 | 0 |
| 2 | 51-100 | 2026-08-12 a 2026-09-02 | 21 | 50 | 14.952 | 155.275 | 4.589.112 | 7 | 1 |
| 3 | 101-150 | 2026-07-29 a 2026-08-12 | 14 | 50 | 5.602 | 24.422 | 3.861.355 | 2 | 1 |
| 4 | 151-200 | 2026-07-04 a 2026-07-29 | 25 | 50 | 17.384 | 51.370 | 2.110.052 | 3 | 1 |
| 5 | 201-250 | 2026-06-09 a 2026-07-03 | 25 | 50 | 14.010 | 76.843 | 1.762.527 | 5 | 1 |
| 6 | 251-300 | 2026-05-14 a 2026-06-08 | 26 | 50 | 15.398 | 45.156 | 13.211.376 | 2 | 1 |
| 7 | 301-350 | 2026-04-17 a 2026-05-13 | 26 | 50 | 11.594 | 63.961 | 3.248.317 | 3 | 1 |
| 8 | 351-400 | 2026-03-23 a 2026-04-17 | 25 | 50 | 10.218 | 31.045 | 5.547.762 | 2 | 2 |
| 9 | 401-450 | 2026-02-27 a 2026-03-23 | 24 | 50 | 23.094 | 68.960 | 467.430 | 3 | 0 |
| 10 | 451-500 | 2026-02-01 a 2026-02-26 | 25 | 50 | 15.000 | 72.753 | 212.921 | 4 | 0 |
| 11 | 501-550 | 2026-01-06 a 2026-02-01 | 26 | 50 | 12.152 | 63.932 | 3.425.825 | 2 | 1 |
| 12 | 551-600 | 2025-12-13 a 2026-01-06 | 24 | 50 | 14.512 | 90.488 | 528.047 | 5 | 0 |
| 13 | 601-650 | 2025-11-19 a 2025-12-13 | 25 | 50 | 11.100 | 58.456 | 3.202.650 | 3 | 1 |
| 14 | 651-700 | 2025-10-25 a 2025-11-18 | 25 | 50 | 11.152 | 26.991 | 186.198 | 1 | 0 |
| 15 | 701-750 | 2025-10-04 a 2025-10-25 | 22 | 50 | 10.372 | 42.493 | 4.794.552 | 3 | 3 |
| 16 | 751-800 | 2025-09-11 a 2025-10-04 | 23 | 50 | 11.616 | 120.993 | 302.696 | 6 | 0 |
| 17 | 801-850 | 2025-08-23 a 2025-09-11 | 20 | 50 | 10.128 | 72.137 | 216.027 | 4 | 0 |
| 18 | 851-900 | 2025-07-30 a 2025-08-21 | 23 | 50 | 8.912 | 43.695 | 182.010 | 3 | 0 |
| 19 | 901-950 | 2025-07-08 a 2025-07-30 | 22 | 50 | 9.592 | 32.629 | 150.837 | 1 | 0 |
| 20 | 951-1000 | 2025-06-15 a 2025-07-08 | 23 | 50 | 12.694 | 45.077 | 120.801 | 3 | 0 |
| 21 | 1001-1050 | 2025-05-22 a 2025-06-15 | 25 | 50 | 15.470 | 85.485 | 1.195.877 | 5 | 1 |
| 22 | 1051-1100 | 2025-05-01 a 2025-05-22 | 21 | 50 | 14.617 | 25.960 | 462.314 | 1 | 0 |
| 23 | 1101-1150 | 2025-04-06 a 2025-04-30 | 25 | 50 | 9.773 | 33.531 | 404.192 | 2 | 0 |
| 24 | 1151-1200 | 2025-03-14 a 2025-04-06 | 23 | 50 | 7.798 | 129.194 | 326.762 | 6 | 0 |
| 25 | 1201-1250 | 2025-02-19 a 2025-03-14 | 24 | 50 | 8.057 | 44.634 | 443.442 | 3 | 0 |
| 26 | 1251-1300 | 2025-01-26 a 2025-02-18 | 24 | 50 | 11.437 | 51.375 | 470.091 | 2 | 0 |
| 27 | 1301-1350 | 2024-12-27 a 2025-01-26 | 30 | 50 | 6.092 | 54.341 | 444.824 | 4 | 0 |
| 28 | 1351-1400 | 2024-12-03 a 2024-12-27 | 25 | 50 | 4.243 | 15.411 | 178.631 | 3 | 0 |
| 29 | 1401-1450 | 2024-11-05 a 2024-12-02 | 28 | 50 | 5.488 | 51.154 | 441.328 | 3 | 0 |
| 30 | 1451-1500 | 2024-09-17 a 2024-11-05 | 49 | 50 | 4.566 | 26.375 | 461.404 | 2 | 0 |
| 31 | 1501-1550 | 2024-06-11 a 2024-09-16 | 98 | 50 | 16.290 | 93.412 | 810.826 | 5 | 0 |
| 32 | 1551-1600 | 2024-04-13 a 2024-06-10 | 59 | 50 | 4.701 | 67.140 | 163.469 | 3 | 0 |
| 33 | 1601-1650 | 2024-02-21 a 2024-04-12 | 52 | 50 | 2.679 | 10.150 | 74.158 | 0 | 0 |
| 34 | 1651-1700 | 2023-12-22 a 2024-02-20 | 61 | 50 | 1.588 | 3.461 | 50.343 | 0 | 0 |
| 35 | 1701-1750 | 2023-09-20 a 2023-12-21 | 92 | 50 | 2.158 | 3.333 | 1.145.693 | 1 | 1 |
| 36 | 1751-1800 | 2023-06-12 a 2023-09-17 | 97 | 50 | 2.666 | 31.361 | 72.988 | 0 | 0 |
| 37 | 1801-1850 | 2023-01-12 a 2023-06-09 | 148 | 50 | 2.504 | 8.203 | 29.196 | 0 | 0 |
| 38 | 1851-1900 | 2022-04-17 a 2023-01-11 | 269 | 35 | 493 | 5.026 | 11.926 | 0 | 0 |
| 39 | 1901-1930 | 2017-09-27 a 2022-04-14 | 1660 | 11 | 739 | 3.226 | 5.122 | 0 | 0 |

- Tendência de longo prazo: Spearman entre a ordem do bloco (1 = mais novo) e a mediana = −0,68 (p<0,0001). Ou seja, quanto mais novo o bloco, maior a mediana: sobe de cerca de 2 mil (2023) para 10 a 17 mil (2025 e 2026).
- Pico: bloco 9 (27/02 a 23/03/2026), mediana 23.094,5. Depois disso o patamar fica entre 10 e 17 mil até julho de 2026.
- Queda recente: os blocos 3 (29/07 a 12/08/2026, mediana 5.602) e 1 (02 a 28/09/2026, mediana 7.142,5) são as duas menores medianas desde dez/2024 (bloco 28: 4.243). O bloco 2, entre eles, voltou a 14.952. Por mês, **agosto (8.330,5) e setembro de 2026 (7.184,5) são os dois piores meses dos últimos 12**. De out/2025 a jul/2026 a mediana mensal ficou entre 10.081 e 17.276. Agosto também teve 90 reels, contra cerca de 60 por mês antes.
- Parte da queda vem das colaborações em inglês com @inventormiguel.eu e @sofiya.vetryakova (28 no total, 10 delas em setembro de 2026). Nos 50 reels mais novos, as 9 colaborações têm mediana de 3.779 views; os outros 41, 7.637. Sem essas colaborações, a mediana mensal ainda cai: ago 10.284, set 8.753,5 (contra 15.323,5 em julho). A queda é real, não só efeito das colaborações.

## 2. Os 30 selecionados

CTA falado = primeira ocorrência na fala de comenta/comente/segue/siga/link/salva/compartilha/manda, mais as variantes "me seguir", "curtir" e "dois toques"; entre parênteses, a posição em % da duração. Perguntas = frases da transcrição terminadas em "?". Números = algarismos (inclui %, decimais e versões como 2.5) mais numerais por extenso de "dois" para cima; "um/uma" não contam.

| código | grupo | data | dur. (s) | views | × mediana | likes/views | coment./views | pal/min | cortes/min | tem fala? | idioma | palavras | perguntas | números | CTA falado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DY22ZGSkoRy | TOP#1 | 2026-05-27 | 90,1 | 13.211.376 | 1.485,5 | 3,22% | 0,008% | — | 0,7 | sim | en | 40 | 2 | 1 | — |
| DWzfD6WD29F | TOP#2 | 2026-04-06 | 7,6 | 5.547.762 | 623,8 | 1,28% | 0,013% | — | 0,0 | não | en (sem fala útil) | 0 | 0 | 0 | — |
| DQPuj3LErfh | TOP#3 | 2025-10-25 | 54,2 | 4.794.552 | 539,1 | 0,50% | 0,078% | 226 | 11,1 | sim | pt | 204 | 1 | 0 | 25,9 s (48%) "curtir" |
| DcRsSr7lx1q | TOP#4 | 2026-08-20 | 52,7 | 4.589.112 | 516,0 | 0,43% | 0,097% | 222 | 6,8 | sim | pt | 195 | 1 | 1 | 51,0 s (97%) "comenta" |
| Dbn5IcHDCGG | TOP#5 | 2026-08-04 | 93,7 | 3.861.355 | 434,2 | 0,32% | 0,014% | 167 | 1,9 | sim | pt | 260 | 0 | 3 | — |
| DTTii0Lkr9T | TOP#6 | 2026-01-09 | 44,1 | 3.425.825 | 385,2 | 1,68% | 0,013% | 231 | 23,1 | sim | pt | 169 | 1 | 0 | 40,3 s (91%) "segue" |
| DXkaaK7icEg | TOP#7 | 2026-04-25 | 7,6 | 3.248.317 | 365,2 | 2,98% | 0,013% | — | 0,0 | não (8 pal. em inglês, provável alucinação) | en | 8 | 0 | 0 | — |
| DRp5npNElkT | TOP#8 | 2025-11-29 | 14,7 | 3.202.650 | 360,1 | 0,55% | 0,007% | — | 8,2 | não | pt (sem fala útil) | 0 | 0 | 0 | — |
| DPruqH5ibBj | TOP#9 PROVÁVEL-ANÚNCIO | 2025-10-11 | 9,7 | 2.505.073 | 281,7 | 0,08% | 0,004% | 174 | 30,9 | sim | pt | 28 | 0 | 0 | — |
| DbRTrbElCGr | TOP#10 | 2026-07-26 | 67,6 | 2.110.052 | 237,3 | 3,67% | 2,534% | 235 | 2,7 | sim | pt | 265 | 1 | 0 | 64,9 s (96%) "segue" |
| DPyxGjagMYz | TOP#11 PROVÁVEL-ANÚNCIO | 2025-10-14 | 90,5 | 2.021.565 | 227,3 | 0,13% | 0,002% | 154 | 21,9 | sim | pt | 224 | 1 | 0 | — |
| DWuVtiKRMnS | TOP#12 | 2026-04-04 | 9,7 | 2.020.180 | 227,2 | 0,51% | 0,032% | 140 | 12,4 | sim | pt | 21 | 0 | 0 | — |
| DZ-6LBiEqbV | TOP#13 | 2026-06-24 | 100,1 | 1.762.527 | 198,2 | 5,46% | 0,442% | 155 | 1,2 | sim | pt | 259 | 4 | 6 | — |
| DKQIhiKvdZa | TOP#14 | 2025-05-29 | 82,5 | 1.195.877 | 134,5 | 5,46% | 0,334% | 201 | 5,1 | sim | pt | 257 | 1 | 1 | — |
| C0zQJfuMMgF | TOP#15 | 2023-12-13 | 42,1 | 1.145.693 | 128,8 | 2,24% | 0,031% | 225 | 17,1 | sim | pt | 157 | 1 | 4 | — |
| Dd19BTxofHd | RECENTE#1 | 2026-09-28 | 44,7 | 1.127 | 0,1 | 0,98% | 0,089% | — | 13,4 | sim | en | 120 | 2 | 0 | — |
| Dd1JMKIjBg6 | RECENTE#2 | 2026-09-28 | 70,4 | 146.291 | 16,4 | 6,12% | 1,420% | 199 | 11,9 | sim | pt | 234 | 0 | 2 | 68,6 s (97%) "comenta" |
| Ddzk06Jk3jV | RECENTE#3 | 2026-09-27 | 46,7 | 27.127 | 3,1 | 5,57% | 0,232% | 177 | 21,8 | sim | pt | 138 | 1 | 4 | 44,6 s (95%) "segue" |
| Ddys4HBjWBp | RECENTE#4 | 2026-09-27 | 34,1 | 3.229 | 0,4 | 0,59% | 0,031% | — | 3,5 | sim | en | 75 | 0 | 0 | — |
| Ddufa1LlSBq | RECENTE#5 | 2026-09-25 | 39,9 | 3.869 | 0,4 | 0,85% | 0,026% | — | 0,0 | sim | en | 85 | 1 | 0 | — |
| DdsDUnUEq-n | RECENTE#6 | 2026-09-24 | 136,4 | 4.675 | 0,5 | 2,80% | 0,128% | 181 | 8,8 | sim | pt | 411 | 2 | 2 | — |
| Ddq1kcZlTku | RECENTE#7 | 2026-09-24 | 93,3 | 2.815 | 0,3 | 1,81% | 0,107% | 170 | 30,9 | sim | pt | 220 | 1 | 0 | — |
| DdoQ4R7Ehp9 | RECENTE#8 | 2026-09-23 | 79,3 | 2.687 | 0,3 | 2,23% | 0,186% | 140 | 25,7 | sim | pt | 164 | 3 | 0 | — |
| DdmiydEAUad | RECENTE#9 | 2026-09-22 | 16,8 | 2.599 | 0,3 | 1,42% | 0,000% | — | 25,0 | sim | en | 44 | 0 | 0 | — |
| DdlsEHZlfgp | RECENTE#10 | 2026-09-22 | 61,5 | 6.916 | 0,8 | 1,55% | 0,000% | 87 | 32,2 | sim | pt | 71 | 2 | 1 | 45,6 s (74%) "siga" |
| DdfJXzgoKVW | RECENTE#11 | 2026-09-19 | 37,9 | 4.656 | 0,5 | 0,97% | 0,021% | — | 7,9 | sim | en | 90 | 1 | 0 | — |
| DdZH69ED9nw | RECENTE#12 | 2026-09-17 | 65,9 | 3.245 | 0,4 | 2,43% | 0,462% | 186 | 1,8 | sim | pt | 204 | 3 | 2 | 64,5 s (98%) "comenta" |
| DdXQeBBEx8D | RECENTE#13 | 2026-09-16 | 53,2 | 4.031 | 0,5 | 2,23% | 0,025% | 166 | 4,5 | sim | pt | 147 | 2 | 4 | 50,8 s (95%) "dois toques" |
| DdXEL72okat | RECENTE#14 | 2026-09-16 | 35,7 | 3.779 | 0,4 | 0,74% | 0,132% | — | 11,8 | sim | en | 85 | 0 | 0 | — |
| DdWjzGdE7SC | RECENTE#15 | 2026-09-16 | 43,9 | 3.639 | 0,4 | 2,25% | 0,055% | 210 | 6,8 | sim | pt | 152 | 1 | 0 | — |

**Medianas por grupo:**

| métrica | TOP (15) | RECENTE (15) | 30 |
|---|---|---|---|
| views | 3.202.650 | 3.779 | 645.992 |
| duração (s) | 52,7 | 46,7 | 49,7 |
| likes/views | 1,28% | 1,81% | 1,61% |
| comentários/views | 0,014% | 0,089% | 0,032% |
| palavras/min (pt ok) | 201 (n=11) | 177 (n=9) | 179 (n=20) |
| cortes/min | 6,8 | 11,8 | 8,5 |
| palavras faladas (vídeos com fala) | 199,5 | 138,0 | 157,0 |

- Com fala: 12 de 15 no TOP (TOP#2, #7 e #8 não têm fala útil) e 15 de 15 nos RECENTES. Em português com flag ok: 11 no TOP e 9 nos RECENTES (os outros 6 RECENTES são colaborações em inglês).
- Os 5 vídeos de até 15 s do TOP (TOP#2, #7, #8, #9, #12) são todos clipes gerados por IA sem fala do criador (4 com selo NEWS, 1 provável anúncio). Nenhum RECENTE tem menos de 16,8 s.
- Fala ou narração do próprio Miguel em português aparece em 8 do TOP (TOP#3, #4, #5, #6, #10, #13, #14, #15): 1.145.693 a 4.794.552 views, duração de 42,1 a 100,1 s (mediana 60,9 s).
- Números citados: TOP#5 (2.5; 2.5; 2.5), TOP#13 (120; 30; 100; 15; 30; 15), TOP#15 (25; três; duas; quatro), RECENTE#2 (29; 92%), RECENTE#3 (137; 600; duas; dois), RECENTE#6 (três; três), RECENTE#12 (20; 5), RECENTE#13 (19; 20; 25%; dois); com 1 número: TOP#1, TOP#4, TOP#14, RECENTE#10. Quantificadores vagos ("centenas", "milhares", "dezenas") aparecem em RECENTE#2, #3, #6 e #12. Resultado: 11 de 20 falas em pt citam pelo menos um número.
- CTA falado em 9 de 30 vídeos (TOP 4, RECENTE 5). Em 7 deles o CTA está nos últimos 10% do vídeo. RECENTE#10 (ficção) coloca o CTA na última fala, aos 74%, e depois vêm só imagens. A exceção real é TOP#3, com o CTA aos 48%, no meio de um loop aberto: segura o nome da ferramenta, pede curtida e seguir, depois revela o nome e pede comentário (aos 32,6 s).

## 3. Ganchos (0 a 5 s)

Paráfrase do que é dito até 5 s (no máximo 12 palavras). A coluna "pal. 0-5 s" conta as palavras faladas nesse intervalo, rateando o trecho que passa dos 5 s. O texto na tela vem do OCR em t=0, limpo à mão (tirei o ruído do OCR); até 12 palavras vai literal entre aspas, e acima disso vira paráfrase entre colchetes.

| código | grupo | fala 0-5 s (paráfrase) | pal. 0-5 s | 1ª palavra (s) | texto na tela no 1º frame | tipo |
|---|---|---|---|---|---|---|
| DY22ZGSkoRy | TOP#1 | Sem fala do criador: diálogo em inglês do próprio clipe | 1,1 | 0,00 | [manchete de 20 palavras: criador chinês fez vídeo cinematográfico de WoW em 3 dias com US$ 40] | manchete fixa |
| DWzfD6WD29F | TOP#2 | Sem fala: só uma interjeição de susto | 0 | — | NEWS + "HOMEM SE ASSUSTA COM AVE BICO DE SAPATO NO MEIO DO PÂNTANO" | selo NEWS + manchete fixa |
| DQPuj3LErfh | TOP#3 | Anuncia a melhor IA para usar com o filho | 20,5 | 0,00 | "A MELHOR IA PRA BRINCAR COM SEUS FILHOS" | manchete |
| DcRsSr7lx1q | TOP#4 | Contou só uma ideia à IA e virou história inteira | 19,1 | 0,00 | "UMA CONVERSA VIROU UMA HISTÓRIA COMPLETA EM VÍDEO" | manchete |
| Dbn5IcHDCGG | TOP#5 | Revela que o vídeo todo saiu de um modelo novo | 12,6 | 0,00 | "PRIMEIRA IMPRESSÃO SEEDANCE 2.5 / TESTEI DE GRAÇA NO DOLA" | manchete |
| DTTii0Lkr9T | TOP#6 | Personagem de IA mostra achado absurdo no açougue do mercado | 27,2 | 0,00 | NEWS + [manchete de 13 palavras: mercado vende urubu inteiro, com penas, na bandeja por R$ 70] | selo NEWS + manchete |
| DXkaaK7icEg | TOP#7 | Sem fala útil: frase curta em inglês (provável alucinação) | 0 | — | NEWS + "Homem leva susto de pássaro gigante no meio do pântano" | selo NEWS + manchete fixa |
| DRp5npNElkT | TOP#8 | Sem fala útil: só uma exclamação do personagem | 0 | — | NEWS + "Brasileiro testa Inteligência Artificial para cortar cabelos em Dubai" | selo NEWS + manchete fixa |
| DPruqH5ibBj | TOP#9 | Locutor fictício narra final olímpica de lavar louça | 10,6 | 0,00 | "Leia a legenda" + placar de TV "BRA 12" | chamada fixa + grafismo de TV |
| DbRTrbElCGr | TOP#10 | Pergunta o que acontece se o ChatGPT montar sua árvore genealógica | 20,8 | 0,00 | "DESCUBRA SEUS PARENTES DESCONHECIDOS COM A AJUDA DO CHATGPT" | manchete |
| DPyxGjagMYz | TOP#11 | Define o próprio livro como diário de bordo | 4,7 | 0,00 | (nenhum texto sobreposto; o OCR só lê o letreiro do local) | nenhum |
| DWuVtiKRMnS | TOP#12 | Personagem testa máquina que promete cabelo em segundos; reage espantado | 15,0 | 0,00 | NEWS + "Brasileiro testa máquina de criar cabelo em Dubai e resultado impressiona" | selo NEWS + manchete fixa |
| DZ-6LBiEqbV | TOP#13 | Apresenta prisão com IA que reabilita criminoso numa manhã | 11,5 | 0,00 | "A PRISÃO DO FUTURO SERÁ FEITA COM IA" | manchete |
| DKQIhiKvdZa | TOP#14 | Cita estudo do MIT com turma dividida em dois grupos | 15,1 | 0,00 | "Tem um estudo do MIT" | legenda da fala |
| C0zQJfuMMgF | TOP#15 | Mostra foto tirada hoje e pede ao ChatGPT tendências de moda | 19,2 | 0,00 | "Esse aqui foi hoje, tá?" (no frame de 0,4 s já não há texto) | legenda da fala |
| Dd19BTxofHd | RECENTE#1 | Em inglês: diz ter medo da próxima fase, excesso de conteúdo | 13,1 | 0,98 | "THIS DINNER PROVOCATION CAME TRUE." | manchete em inglês |
| Dd1JMKIjBg6 | RECENTE#2 | Brasileiro criou IA absurda de que ninguém fala; dá o nome | 16,4 | 0,00 | "BRASILEIRO CRIOU UMA IA ABSURDA" | manchete |
| Ddzk06Jk3jV | RECENTE#3 | Anuncia que saiu o primeiro longa feito com IA | 11,9 | 0,00 | "SAIU O 1º FILME FEITO 100% COM IA" + "Finalmente aconteceu" | manchete + legenda |
| Ddys4HBjWBp | RECENTE#4 | Em inglês: mandar foto ao chatbot para ler o humor alheio | 8,1 | 0,00 | "When is not the right moment to talk about AI" + legenda bilíngue | manchete em inglês + legenda |
| Ddufa1LlSBq | RECENTE#5 | Em inglês: esquete de casal; um diz que está editando vídeo | 2,2 | 0,00 | "Eu tentando ter uma relação saudável com a IA" (+ versão em inglês) | manchete-meme bilíngue |
| DdsDUnUEq-n | RECENTE#6 | Nova IA de que todos falam tem um detalhe: não fala | 20,0 | 0,00 | "Essa é a nova IA…" (legenda da fala, cortada em 5 palavras) | legenda da fala |
| Ddq1kcZlTku | RECENTE#7 | Ficção: inventor comemora robô funcionando, sua maior invenção | 18,0 | 0,42 | logo "DRAMA" + "ESTOU MUITO FELIZ" | logo da série + legenda |
| DdoQ4R7Ehp9 | RECENTE#8 | Ficção: robô ganha pizza por ajudar o vendedor de coco | 15,0 | 0,00 | logo "DRAMA" + "INVENTOR MIGUEL E SEU ROBÔ MISTERIOSO" + recapitulação | título da série |
| DdmiydEAUad | RECENTE#9 | Em inglês: gosta da adrenalina de quase perder o voo | 16,5 | 0,00 | "HOW EARLY IS 'ON TIME' FOR YOU?" | manchete em inglês |
| DdlsEHZlfgp | RECENTE#10 | Ficção: inventor manda robô ajudar vendedor de coco com turista | 13,3 | 0,00 | logo "DRAMA" + "INVENTOR MIGUEL E SEU ROBÔ MISTERIOSO" + legenda | título da série |
| DdfJXzgoKVW | RECENTE#11 | Em inglês: França é romântica, com clima interessante | 10,8 | 0,00 | "ROMANTIC... BUT NOT ABOUT LOVE?" | manchete em inglês |
| DdZH69ED9nw | RECENTE#12 | Empresas perdem dinheiro com IA por motivo que não é o modelo | 17,8 | 0,00 | "SUA EMPRESA PODE ESTAR AUTOMATIZANDO DECISÕES ERRADAS SEM PERCEBER" + infográfico "-$2,480,000" | manchete + número grande |
| DdXQeBBEx8D | RECENTE#13 | Empresas usam IA para acelerar e ficam mais lentas | 14,4 | 0,00 | "A ARMADILHA DA IA QUE MUITOS IGNORAM" + legenda | manchete + legenda |
| DdXEL72okat | RECENTE#14 | Em inglês: mostra romãs crescendo no jardim | 10,7 | 0,00 | legenda bilíngue (romãs) + crédito "Sofiya Vetryakova, DIRECTOR" | legenda |
| DdWjzGdE7SC | RECENTE#15 | Muita gente acha que existe o melhor modelo de IA | 17,0 | 0,00 | "A IMPORTÂNCIA DE DIVERSIFICAR MODELOS DE IA NA SUA OPERAÇÃO" | manchete |

- A fala começa em 0,0 s em 19 dos 20 vídeos em pt com fala (RECENTE#7 começa em 0,42 s). Não há respiro nem vinheta.
- Palavras nos primeiros 5 s (pt ok, n=20): mediana 15,8, média 16,0, de 4,7 a 27,2. São cerca de 3,2 palavras por segundo já no gancho. Nos 8 vídeos-núcleo do TOP a mediana é 19,1.
- Texto na tela no 1º frame: 29 de 30 (só TOP#11 não tem). Manchete ou título sobreposto (não só a legenda da fala): 24 de 30 (TOP 12, RECENTE 12). Selo "NEWS": 5 de 15 no TOP e 0 nos RECENTES. Número na manchete: 5 de 30 (TOP#1, #5, #6, RECENTE#3, #12).
- Tamanho da manchete (24 com manchete): mediana 8,5 palavras, de 3 a 20. 22 de 24 têm até 12 palavras; as exceções são TOP#1 (20) e TOP#6 (13). 16 de 24 estão em caixa alta. As 8 em caixa baixa são TOP#1, 4 dos 5 clipes NEWS (TOP#6, #7, #8 e #12, com cara de manchete de portal), TOP#9 e duas colaborações (RECENTE#4 e #5).
- Dentro do TOP, os 3 vídeos sem manchete no 1º frame (TOP#11 sem texto; TOP#14 e TOP#15 só com a legenda da fala) estão todos na parte de baixo do TOP (posições 11, 14 e 15). Os 10 primeiros do TOP têm manchete. Veja o rho na seção 6.
- Primeira frase dos 14 vídeos-núcleo (fala ou narração do próprio Miguel): abre com dêitico que aponta para o que está na tela ("isso é", "isso aqui", "esse vídeo", "essa é") em 5 de 14 (TOP 4 de 8: #3, #5, #13, #15; RECENTE 1 de 6: #6). Abre com generalização ou tese abstrata ("muita empresa", "muita gente", "existe um motivo") em 3 de 14, todos RECENTES (#12, #13, #15, com 3,2 mil a 4,0 mil views). Os outros 6 se dividem assim: fato de terceiro ("tem um estudo", "um brasileiro criou") em 2 (TOP#14, RECENTE#2), relato em 1ª pessoa em 1 (TOP#4), cena encenada em 1 (TOP#6), pergunta em 1 (TOP#10) e anúncio de novidade em 1 (RECENTE#3).

## 4. Linguagem (falas em português com flag ok)

Base: 20 vídeos, 3.780 palavras, 292 frases (divisão pela pontuação do Whisper). Coluna "núcleo" = 14 vídeos com fala ou narração do próprio Miguel. Ficam fora do núcleo a ficção DRAMA (RECENTE#7, #8 e #10), os personagens de clipes de IA (TOP#9 e #12) e o lançamento do livro com depoimento de terceiro (TOP#11).

**Top 30 expressões recorrentes de 2 a 4 palavras** (aparecem em pelo menos 2 vídeos). Critérios: não cruzam pontuação; não podem ser só stopwords; não começam nem terminam em artigo, preposição ou conjunção (exceto "a gente"). Um n-grama contido em outro maior com a mesma contagem nos mesmos vídeos foi descartado. Também saíram as falas repetidas só dentro da série DRAMA, porque o episódio seguinte reprisa o anterior (lista no fim).

| # | expressão | vídeos | ocorrências | onde |
|---|---|---|---|---|
| 1 | inteligência artificial | 9 | 24 | TOP#3, TOP#6, TOP#13, TOP#14, RECENTE#2, RECENTE#3, RECENTE#6, RECENTE#12, RECENTE#15 |
| 2 | a gente | 9 | 20 | TOP#3, TOP#6, TOP#11, TOP#13, TOP#14, RECENTE#6, RECENTE#8, RECENTE#10, RECENTE#15 |
| 3 | eu te mando | 5 | 5 | TOP#3, TOP#4, TOP#10, RECENTE#2, RECENTE#12 |
| 4 | você quer | 5 | 5 | TOP#4, TOP#6, RECENTE#2, RECENTE#6, RECENTE#10 |
| 5 | te mando o link | 4 | 4 | TOP#3, TOP#4, TOP#10, RECENTE#12 |
| 6 | sua empresa | 3 | 5 | TOP#6, RECENTE#2, RECENTE#12 |
| 7 | me segue aqui | 3 | 3 | TOP#6, TOP#10, RECENTE#3 |
| 8 | esse vídeo | 3 | 3 | TOP#3, TOP#4, TOP#5 |
| 9 | eu estou | 3 | 3 | RECENTE#2, RECENTE#12, RECENTE#15 |
| 10 | mais rápida | 3 | 3 | RECENTE#6, RECENTE#13, RECENTE#15 |
| 11 | mais rápido | 3 | 3 | TOP#14, RECENTE#6, RECENTE#13 |
| 12 | eu fui | 2 | 5 | TOP#3, TOP#11 |
| 13 | esse tipo | 2 | 4 | TOP#6, RECENTE#6 |
| 14 | ele gerou | 2 | 3 | TOP#3, TOP#15 |
| 15 | foi feito | 2 | 3 | TOP#5, RECENTE#6 |
| 16 | não existe | 2 | 3 | TOP#6, RECENTE#15 |
| 17 | não precisa | 2 | 3 | TOP#4, RECENTE#6 |
| 18 | precisa escrever | 2 | 3 | TOP#4, RECENTE#6 |
| 19 | você sabe | 2 | 3 | TOP#10, RECENTE#3 |
| 20 | será que a gente | 2 | 2 | RECENTE#6, RECENTE#8 |
| 21 | você não precisa escrever | 2 | 2 | TOP#4, RECENTE#6 |
| 22 | comenta a roi (grafia do Whisper para "comenta ROI") | 2 | 2 | RECENTE#2, RECENTE#12 |
| 23 | dá dois toques | 2 | 2 | RECENTE#3, RECENTE#13 |
| 24 | mensagens dos clientes | 2 | 2 | RECENTE#6, RECENTE#8 |
| 25 | milhares de vezes | 2 | 2 | RECENTE#6, RECENTE#12 |
| 26 | usando inteligência artificial | 2 | 2 | TOP#3, TOP#14 |
| 27 | acontece quando | 2 | 2 | TOP#10, RECENTE#2 |
| 28 | cidense 2.5 (grafia do Whisper para "Seedance 2.5") | 2 | 2 | TOP#4, TOP#5 |
| 29 | consegue criar | 2 | 2 | TOP#5, TOP#6 |
| 30 | eu quero | 2 | 2 | TOP#10, RECENTE#8 |

- Próximas da lista, também em 2 vídeos: "eu trabalho"; "gente consegue"; "mais tempo"; "mesmo tempo"; "meu deus"; "não ficou"; "olha isso"; "precisa entender"; "todo mundo"; "você precisa"; "você quiser".
- Só na série DRAMA (reprise entre episódios, fora do ranking), exemplos: "estou muito feliz"; "minha maior invenção"; "eu não lembrava"; "tinha paciente agora".

**Frases, pessoa e marcadores:**

| métrica | todas (20 vídeos) | núcleo (14) |
|---|---|---|
| palavras por frase, média | 12,9 | 13,7 |
| palavras por frase, mediana | 11,0 | 12,0 |
| palavras por frase, p90 | 24 | 24 |
| % de frases com "você" | 17,8% | 18,4% |
| "a gente": ocorrências (vídeos; por mil palavras) | 20 (9; 5,3) | 17 (6; 5,6) |
| "olha": ocorrências (vídeos; por mil palavras) | 5 (3; 1,3) | 3 (2; 1,0) |
| "gente" solto (fora "a gente" e "muita gente"): ocorrências (vídeos; por mil palavras) | 1 (1; 0,3) | 1 (1; 0,3) |
| "cara": ocorrências (vídeos; por mil palavras) | 0 (0; 0,0) | 0 (0; 0,0) |
| "tá": ocorrências (vídeos; por mil palavras) | 4 (3; 1,1) | 2 (2; 0,7) |
| "né": ocorrências (vídeos; por mil palavras) | 0 (0; 0,0) | 0 (0; 0,0) |
| "sabe": ocorrências (vídeos; por mil palavras) | 5 (4; 1,3) | 5 (4; 1,6) |
| "mano": ocorrências (vídeos; por mil palavras) | 2 (2; 0,5) | 2 (2; 0,7) |
| "galera": ocorrências (vídeos; por mil palavras) | 0 (0; 0,0) | 0 (0; 0,0) |
| "beleza": ocorrências (vídeos; por mil palavras) | 3 (3; 0,8) | 3 (3; 1,0) |
| "entendeu": ocorrências (vídeos; por mil palavras) | 1 (1; 0,3) | 1 (1; 0,3) |
| "ó": ocorrências (vídeos; por mil palavras) | 1 (1; 0,3) | 1 (1; 0,3) |
| "tipo": ocorrências (vídeos; por mil palavras) | 5 (2; 1,3) | 5 (2; 1,6) |
| "sinceramente": ocorrências (vídeos; por mil palavras) | 2 (1; 0,5) | 2 (1; 0,7) |
| "literalmente": ocorrências (vídeos; por mil palavras) | 1 (1; 0,3) | 1 (1; 0,3) |
| "aí (início de frase)": ocorrências (vídeos; por mil palavras) | 16 (5; 4,2) | 15 (4; 4,9) |
| palavras/min: mediana (mín. a máx.) | 179 (87 a 235) | 200 (155 a 235) |

- Marcadores de oralidade quase não aparecem: "né", "cara" e "galera" têm 0; "mano" só aparece 2 vezes, e sempre no fecho "beleza, mano?" (TOP#3 e RECENTE#13); "tá" tem 4; "olha" tem 5 (ex.: "olha isso", "olha só"). O "aí" no começo da frase (16 vezes) vem quase todo, 12 das 16 vezes, de duas narrações em sequência: TOP#15 (8 vezes, na cadeia "aí eu pedi…, aí ele gerou…") e TOP#3 (4 vezes).
- "sabe" aparece como verbo ("você sabe", "a gente só vai saber") e não como muleta.
- **Construção "não é X, é Y" e variantes**: 9 ocorrências na fala, em 5 de 20 vídeos (TOP#5, TOP#6, TOP#15, RECENTE#6, RECENTE#13), e 8 nas legendas, em 7 de 30 (TOP#1, TOP#2, TOP#6, TOP#7, TOP#12, RECENTE#7, RECENTE#13). Por variante:

| variante (molde) | na fala: ocorrências (vídeos) | na legenda: ocorrências (vídeos) |
|---|---|---|
| não é/são X, é/são Y | 2 (TOP#5, RECENTE#13) | 7 (TOP#1, TOP#2, TOP#6, TOP#7, TOP#12, RECENTE#7, RECENTE#13) |
| não é X, mas (sim) Y | 1 (TOP#6) | 0 (—) |
| não [verbo] X, [mesmo verbo] Y | 3 (TOP#15, RECENTE#6, RECENTE#13) | 1 (TOP#12) |
| não X, (ele/ela) só Y | 2 (RECENTE#6, RECENTE#13) | 0 (—) |
| não foram/é só X ... Y (sem repetir o verbo) | 1 (TOP#5) | 0 (—) |

  Na leitura manual achei mais 2 variantes na fala que o regex não pega: TOP#13 ("a parte difícil não é mais X; a pergunta é outra") e RECENTE#12 ("o motivo quase nunca é X; o problema está em Y"). Com elas, a construção aparece em 7 dos 14 vídeos-núcleo. Na legenda, o molde fixo é "O mais interessante não é [X]. É [Y]", com cada parte em seu próprio parágrafo (TOP#1, #2, #12). TOP#6 usa "a lição não é sobre [X]. É sobre [Y]" (a legenda escreve "E" sem acento, e o regex ajustado conta).

**Por vídeo:**

| grupo | código | palavras | frases | pal./frase | "você" | "a gente" | pal/min | núcleo | 2 primeiras palavras | motor |
|---|---|---|---|---|---|---|---|---|---|---|
| TOP#3 | DQPuj3LErfh | 204 | 20 | 10,2 | 2 | 5 | 226 | sim | isso é | large-v3-turbo |
| TOP#4 | DcRsSr7lx1q | 195 | 15 | 13,0 | 7 | 0 | 222 | sim | eu só | large-v3-turbo |
| TOP#5 | Dbn5IcHDCGG | 260 | 14 | 18,6 | 3 | 0 | 167 | sim | esse vídeo | large-v3-turbo |
| TOP#6 | DTTii0Lkr9T | 169 | 12 | 14,1 | 2 | 2 | 231 | sim | a novidade | large-v3-turbo |
| TOP#9 | DPruqH5ibBj | 28 | 3 | 9,3 | 0 | 0 | 174 | não | agora o | large-v3-turbo |
| TOP#10 | DbRTrbElCGr | 265 | 15 | 17,7 | 11 | 0 | 235 | sim | o que | large-v3-turbo |
| TOP#11 | DPyxGjagMYz | 224 | 10 | 22,4 | 0 | 1 | 154 | não | o livro | large-v3-turbo |
| TOP#12 | DWuVtiKRMnS | 21 | 4 | 5,2 | 0 | 0 | 140 | não | agora mas | large-v3-turbo |
| TOP#13 | DZ-6LBiEqbV | 259 | 20 | 12,9 | 1 | 3 | 155 | sim | essa é | large-v3-turbo |
| TOP#14 | DKQIhiKvdZa | 257 | 14 | 18,4 | 1 | 4 | 201 | sim | tem um | large-v3-turbo |
| TOP#15 | C0zQJfuMMgF | 157 | 16 | 9,8 | 0 | 0 | 225 | sim | isso aqui | large-v3-turbo |
| RECENTE#2 | Dd1JMKIjBg6 | 234 | 14 | 16,7 | 5 | 0 | 199 | sim | um brasileiro | small |
| RECENTE#3 | Ddzk06Jk3jV | 138 | 16 | 8,6 | 1 | 0 | 177 | sim | finalmente aconteceu | small |
| RECENTE#6 | DdsDUnUEq-n | 411 | 30 | 13,7 | 11 | 2 | 181 | sim | essa é | small |
| RECENTE#7 | Ddq1kcZlTku | 220 | 25 | 8,8 | 6 | 0 | 170 | não | estou muito | large-v3-turbo |
| RECENTE#8 | DdoQ4R7Ehp9 | 164 | 16 | 10,2 | 4 | 1 | 140 | não | você fez | large-v3-turbo |
| RECENTE#10 | DdlsEHZlfgp | 71 | 11 | 6,5 | 3 | 1 | 87 | não | vai lá | large-v3-turbo |
| RECENTE#12 | DdZH69ED9nw | 204 | 15 | 13,6 | 1 | 0 | 186 | sim | existe um | large-v3-turbo |
| RECENTE#13 | DdXQeBBEx8D | 147 | 13 | 11,3 | 0 | 0 | 166 | sim | muita empresa | large-v3-turbo |
| RECENTE#15 | DdWjzGdE7SC | 152 | 9 | 16,9 | 3 | 1 | 210 | sim | muita gente | large-v3-turbo |

- Palavras/min dos vídeos-núcleo: TOP mediana 223 (n=8), RECENTE mediana 184 (n=6). Os TOP falados são mais rápidos; lembre que 3 dos 6 RECENTES usaram o motor small.

## 5. Legenda (caption)

| grupo | código | idioma | caracteres | linhas (não vazias) | 1ª linha (caract.) | emojis | hashtags | "?" | menções @ | CTAs |
|---|---|---|---|---|---|---|---|---|---|---|
| TOP#1 | DY22ZGSkoRy | pt | 1.149 | 9 | 84 | 2 | 0 | 1 | 1 | opinião nos comentários; segue |
| TOP#2 | DWzfD6WD29F | pt | 850 | 12 | 104 | 2 | 0 | 1 | 1 | link na bio; segue |
| TOP#3 | DQPuj3LErfh | pt | 589 | 6 | 71 | 4 | 10 | 2 | 0 | comenta/marca p/ receber link; "te mando/te envio" |
| TOP#4 | DcRsSr7lx1q | pt | 496 | 5 | 70 | 0 | 5 | 1 | 2 | comenta PALAVRA; "te mando/te envio" |
| TOP#5 | Dbn5IcHDCGG | pt | 580 | 4 | 156 | 0 | 5 | 0 | 0 | — |
| TOP#6 | DTTii0Lkr9T | pt | 1.108 | 14 | 79 | 3 | 5 | 3 | 1 | link na bio; segue |
| TOP#7 | DXkaaK7icEg | pt | 952 | 15 | 48 | 1 | 0 | 1 | 0 | segue |
| TOP#8 | DRp5npNElkT | pt | 1.094 | 8 | 29 | 5 | 10 | 2 | 0 | segue |
| TOP#9 | DPruqH5ibBj | pt | 1.254 | 9 | 183 | 5 | 13 | 0 | 0 | — |
| TOP#10 | DbRTrbElCGr | pt | 417 | 4 | 182 | 0 | 0 | 1 | 0 | comenta PALAVRA; "te mando/te envio" |
| TOP#11 | DPyxGjagMYz | pt | 465 | 6 | 52 | 2 | 0 | 0 | 0 | evento presencial |
| TOP#12 | DWuVtiKRMnS | pt | 789 | 10 | 60 | 2 | 0 | 1 | 1 | link na bio; segue |
| TOP#13 | DZ-6LBiEqbV | pt | 829 | 12 | 43 | 2 | 0 | 5 | 1 | opinião nos comentários; segue |
| TOP#14 | DKQIhiKvdZa | pt | 491 | 4 | 49 | 1 | 6 | 0 | 0 | comenta/marca p/ receber link |
| TOP#15 | C0zQJfuMMgF | pt+en | 738 | 4 | 338 | 0 | 7 | 0 | 0 | — |
| RECENTE#1 | Dd19BTxofHd | en | 525 | 3 | 75 | 0 | 0 | 1 | 0 | opinião nos comentários |
| RECENTE#2 | Dd1JMKIjBg6 | pt | 147 | 1 | 147 | 0 | 0 | 0 | 0 | — |
| RECENTE#3 | Ddzk06Jk3jV | pt | 187 | 1 | 187 | 0 | 3 | 0 | 0 | — |
| RECENTE#4 | Ddys4HBjWBp | en | 45 | 1 | 45 | 0 | 0 | 0 | 0 | — |
| RECENTE#5 | Ddufa1LlSBq | en | 164 | 3 | 51 | 1 | 0 | 0 | 0 | — |
| RECENTE#6 | DdsDUnUEq-n | pt | 249 | 1 | 249 | 0 | 0 | 1 | 0 | — |
| RECENTE#7 | Ddq1kcZlTku | pt | 374 | 5 | 59 | 0 | 4 | 1 | 0 | — |
| RECENTE#8 | DdoQ4R7Ehp9 | pt | 592 | 7 | 69 | 3 | 3 | 1 | 1 | segue |
| RECENTE#9 | DdmiydEAUad | pt | 547 | 6 | 71 | 0 | 4 | 1 | 1 | segue |
| RECENTE#10 | DdlsEHZlfgp | pt | 517 | 6 | 70 | 3 | 3 | 2 | 1 | segue |
| RECENTE#11 | DdfJXzgoKVW | en | 113 | 1 | 113 | 0 | 0 | 0 | 0 | — |
| RECENTE#12 | DdZH69ED9nw | pt | 1.033 | 6 | 130 | 0 | 0 | 0 | 0 | comenta PALAVRA; "te mando/te envio" |
| RECENTE#13 | DdXQeBBEx8D | pt | 776 | 5 | 105 | 0 | 0 | 2 | 0 | dois toques |
| RECENTE#14 | DdXEL72okat | en | 187 | 2 | 90 | 0 | 0 | 0 | 0 | — |
| RECENTE#15 | DdWjzGdE7SC | pt | 679 | 5 | 103 | 0 | 0 | 1 | 0 | — |

| métrica | TOP (15) | RECENTE (15) | 30 |
|---|---|---|---|
| caracteres, mediana | 789,0 | 374,0 | 563,5 |
| linhas, mediana | 8,0 | 3,0 | 5,0 |
| 1ª linha em caracteres, mediana | 71,0 | 90,0 | 77,0 |
| emojis, mediana | 2,0 | 0,0 | 0,0 |
| hashtags, mediana | 5,0 | 0,0 | 0,0 |
| perguntas ("?"), mediana | 1,0 | 1,0 | 1,0 |
| menções @, mediana | 0,0 | 0,0 | 0,0 |
| emojis, média | 1,9 | 0,5 | 1,2 |
| hashtags, média | 4,1 | 1,1 | 2,6 |
| legendas com ≥1 hashtag | 8 | 5 | 13 |
| legendas com ≥1 emoji | 11 | 3 | 14 |
| legendas com pergunta | 10 | 8 | 18 |
| legendas com menção @ | 6 | 3 | 9 |
| legenda em inglês (total ou parcial) | 1 | 5 | 6 |

**Tipos de CTA na legenda** (um vídeo pode ter mais de um):

| tipo | TOP | RECENTE | 30 |
|---|---|---|---|
| comenta PALAVRA | 2 | 1 | 3 |
| comenta/marca p/ receber link | 2 | 0 | 2 |
| opinião nos comentários | 2 | 1 | 3 |
| link na bio | 3 | 0 | 3 |
| segue | 7 | 3 | 10 |
| salva | 0 | 0 | 0 |
| compartilha | 0 | 0 | 0 |
| direct | 0 | 0 | 0 |
| "te mando/te envio" | 3 | 1 | 4 |
| dois toques | 0 | 1 | 1 |
| evento presencial | 1 | 0 | 1 |
| nenhum CTA | 3 | 9 | 12 |

- A assinatura "Siga @inventormiguel para mais conteúdos" aparece em 5 legendas (TOP#1, #2, #6, #12 e #13). Com as variações ("siga @inventormiguel para acompanhar", "já segue aqui", "é só me seguir"), são 10 legendas com CTA de seguir, 7 delas no TOP.
- Molde de palavra-chave: 'Comenta "[PALAVRA]" que eu te [mando/envio] [o link/os prompts]' aparece em 3 legendas (TOP#4, TOP#10, RECENTE#12). A variante sem palavra-chave ("comenta/marca alguém para receber o link") aparece em 2 (TOP#3, TOP#14). Salvar, compartilhar e chamar no direct: 0 de 30.
- Molde de legenda longa do TOP (TOP#1, #2, #6, #7, #12, #13): de 9 a 15 linhas curtas. Abre com frase-gancho e revela o ponto (nos clipes, que é tudo IA). Em 5 delas (TOP#1, #2, #6, #7, #12) vem o parágrafo de contraste "não é X. É Y". Termina com a pergunta de opinião (TOP#1, #13) ou com o link na bio (TOP#2, #6, #12) e fecha com o CTA de seguir.
- As 6 colaborações em inglês (RECENTE#1, #4, #5, #9, #11, #14) têm legenda de 45 a 547 caracteres. Só 2 têm CTA: RECENTE#1 pede opinião e RECENTE#9 manda acompanhar @inventormiguel.eu. A legenda de RECENTE#9 é em português.

- Efeito do "comenta [PALAVRA/marca alguém] → te mando [o link]" (na fala ou na legenda; TOP#3, #4, #10, #14, RECENTE#2, #12): mediana de comentários/views de **0,398%**, contra 0,031% nos outros 15 vídeos em pt, cerca de 13 vezes mais. Só os 4 com palavra-chave (TOP#4, #10, RECENTE#2, #12): mediana de 0,941%. TOP#10 teve 53.466 comentários (2,534% das views) e RECENTE#2, 2.078 (1,420%). O efeito aparece nos comentários, não nas views (seção 6).

## 6. Correlações de Spearman com views

**Aviso:** com n=30 (e n=15 dentro de cada grupo), isto é indício, não prova. No conjunto dos 30, qualquer variável que separa TOP de RECENTE aparece "correlacionada", porque as views dos dois grupos diferem em cerca de 850 vezes (medianas de 3.202.650 e 3.779). A comparação dentro do TOP é a mais informativa. Para ser significativo a 5%, o |rho| precisa passar de cerca de 0,36 com n=30 e de cerca de 0,52 com n=15. p = bicaudal.

| variável | 30 | dentro do TOP (15) | TOP sem os 2 anúncios (13) | dentro dos RECENTES (15) |
|---|---|---|---|---|
| duração (s) | −0,02 (p=0,906; n=30) | −0,11 (p=0,694; n=15) | −0,02 (p=0,943; n=13) | 0,24 (p=0,390; n=15) |
| palavras/min (pt, flag ok) | 0,35 (p=0,130; n=20) | 0,30 (p=0,370; n=11) | 0,27 (p=0,488; n=9) | 0,20 (p=0,606; n=9) |
| cortes/min | −0,31 (p=0,098; n=30) | −0,36 (p=0,193; n=15) | −0,35 (p=0,234; n=13) | −0,08 (p=0,781; n=15) |
| tamanho da legenda (caracteres) | 0,44 (p=0,014; n=30) | 0,32 (p=0,248; n=15) | 0,33 (p=0,271; n=13) | −0,39 (p=0,151; n=15) |
| texto no 1º frame (0/1) | −0,10 (p=0,612; n=30) | 0,19 (p=0,508; n=15) | constante (n=13) | constante (n=15) |
| fala (0/1) | −0,38 (p=0,039; n=30) | −0,27 (p=0,330; n=15) | −0,20 (p=0,523; n=13) | constante (n=15) |
| pedido de comentário, fala ou legenda (0/1) | 0,20 (p=0,296; n=30) | 0,09 (p=0,738; n=15) | 0,08 (p=0,789; n=13) | −0,08 (p=0,785; n=15) |
| extra: manchete/título no 1º frame (0/1) | 0,15 (p=0,416; n=30) | 0,62 (p=0,014; n=15) | 0,63 (p=0,022; n=13) | 0,00 (p=1,000; n=15) |
| extra: "comenta [PALAVRA/marca alguém] → te mando [o link]" (0/1) | 0,20 (p=0,284; n=30) | 0,03 (p=0,902; n=15) | 0,00 (p=1,000; n=13) | 0,23 (p=0,416; n=15) |
| extra: selo NEWS sobre clipe gerado por IA (0/1) | 0,44 (p=0,015; n=30) | 0,16 (p=0,560; n=15) | 0,08 (p=0,784; n=13) | constante (n=15) |

Leitura:
- **Duração**: nada (rho −0,02 nos 30; −0,11 no TOP). No TOP há vídeos de 7,6 s e de 100 s.
- **Palavras/min**: positiva e fraca (+0,35 nos 30 com n=20; +0,30 no TOP com n=11), não significativa. É coerente com a mediana de 223 pal/min dos TOP falados contra 184 dos RECENTES falados.
- **Cortes/min**: negativa e fraca (−0,31 nos 30; −0,36 no TOP). Os maiores do TOP têm poucos cortes (TOP#1 0,7/min; TOP#2 e #7 0/min; TOP#5 1,9/min), e os mais picotados são anúncio ou ficção (TOP#9 30,9/min; RECENTE#7 30,9/min; RECENTE#10 32,2/min).
- **Tamanho da legenda**: +0,44 nos 30 (p=0,014), mas o sinal inverte nos RECENTES (−0,39). É efeito de grupo: o TOP tem legenda longa (mediana 789 caracteres) e os RECENTES, curta (374). Não trate isso como alavanca.
- **Texto no 1º frame**: quase constante (29 de 30), então não discrimina. A versão "manchete ou título sobreposto" discrimina **dentro do TOP: +0,62 (p=0,014)**. Os 3 TOP sem manchete ocupam as posições 11, 14 e 15, e os 10 primeiros têm manchete. É o indício mais forte da ficha, mas vem de 3 vídeos.
- **Fala**: −0,38 nos 30 (p=0,039). Os 3 vídeos sem fala são clipes NEWS do TOP (TOP#2, #7, #8), e todos os RECENTES têm fala. Dentro do TOP dá −0,27 (n.s.). Ter fala não é o que puxa o topo; o que puxa é a imagem impossível (clipe de IA) ou a manchete.
- **Pedido de comentário**: +0,20 nos 30 e +0,09 no TOP, sem efeito em views. O efeito está nos comentários (seção 5).

## 7. Os 7 achados quantitativos para o roteirista

1. **Viral é exceção rara, e o patamar recente caiu.** A mediana é 8.893,5 views, e só 15 de 1.896 reels (0,8%) passaram de 1 milhão. Esses 15 somam 52,7% de todas as views do perfil. No último ano saiu 1 reel acima de 1 milhão a cada 58 publicados, com cerca de 2 reels por dia. Agosto e setembro de 2026 têm as menores medianas mensais dos últimos 12 meses (8.330,5 e 7.184,5, contra 10.081 a 17.276 entre out/2025 e jul/2026). Parte disso vem das colaborações em inglês (mediana de 3.779 nos 50 mais novos). Imitar o Miguel é imitar volume mais uma fórmula que às vezes acerta, não um roteiro que viraliza sempre.
2. **Só 8 dos 15 do TOP servem para quem grava falando para a câmera, e duração não importa.** 5 dos 15 mais vistos são clipes gerados por IA com selo "NEWS" e manchete (TOP#2, #6, #7, #8, #12), 4 deles com até 15 s. Depois, a legenda ou a narração deixa claro que é IA. É um formato que o Adriel não usa, porque não publica notícia falsa. Já 8 dos 15 têm fala ou narração do próprio Miguel em português (TOP#3, #4, #5, #6, #10, #13, #14, #15): de 1,15 mi a 4,79 mi views, com 42 a 100 s (mediana 60,9 s). Duração e views não se correlacionam (rho −0,02 nos 30; −0,11 no TOP). O molde transponível é cerca de 1 minuto, falado do início ao fim.
3. **Ritmo de fala alto e sem respiro.** Nos vídeos falados em português, a fala começa em 0,0 s em 19 de 20 vídeos e coloca cerca de 16 palavras nos primeiros 5 s (mediana 15,8). O ritmo mediano é 200 palavras/min no núcleo, com os TOP falados a 223 e os RECENTES falados a 184. As frases são curtas: mediana de 11 a 12 palavras e média de 13 a 14. Palavras/min tem correlação positiva com views, mas fraca e não significativa (+0,35; n=20).
4. **O 1º frame sempre tem texto, e a manchete separa o topo do resto do TOP.** 29 de 30 vídeos têm texto em t=0, e 24 de 30 têm manchete ou título sobreposto (mediana de 8,5 palavras; 22 de 24 com até 12). Dentro do TOP, os 10 primeiros têm manchete, e os 3 sem manchete ocupam as posições 11, 14 e 15 (rho +0,62; p=0,014; n=15, indício). Nos TOP falados com manchete, 5 de 6 estão em caixa alta. Molde: manchete em caixa alta com a ferramenta ou o fato e uma promessa concreta, como "A MELHOR IA PRA [tarefa]" ou "DESCUBRA [algo] COM A AJUDA DO [ferramenta]".
5. **A primeira frase aponta para algo concreto; tese abstrata rende pouco.** Nos vídeos falados do TOP, 4 de 8 abrem com dêitico ("isso é…", "esse vídeo…", "essa é a…"). Os outros 4 abrem com relato em 1ª pessoa, cena, pergunta ("o que acontece quando você…") ou estudo citado. Nos RECENTES falados, 3 de 6 abrem com generalização ("muita empresa…", "muita gente…", "existe um motivo…"), e esses 3 ficaram entre 3,2 mil e 4,0 mil views.
6. **O CTA fica no fim, e a palavra-chave multiplica comentários, não views.** O CTA falado aparece em 9 de 30 vídeos, 7 deles nos últimos 10% da duração. A exceção útil é TOP#3, aos 48%: um loop aberto que segura o nome da ferramenta, pede curtida e seguir, e só depois revela. O pedido "comenta [PALAVRA ou marca alguém] que eu te mando [X]", na fala ou na legenda, aparece em 6 vídeos (4 com palavra-chave). Ele dá mediana de 0,398% de comentários/views, contra 0,031% nos outros vídeos em português: cerca de 13 vezes mais. Só com palavra-chave, a mediana sobe para 0,941%. TOP#10 chegou a 53.466 comentários. Sobre as views o efeito é nulo (rho +0,03 no TOP). Salvar, compartilhar e chamar no direct aparecem 0 vezes em 30.
7. **A voz é direta, sem gíria, e usa muito o contraste "não é X, é Y".** "Você" aparece em 17,8% das frases e "a gente", 20 vezes (5,3 por mil palavras). "Né", "cara" e "galera" têm 0 ocorrências, e "mano" só aparece no fecho "beleza, mano?". O contraste "não é X, é Y" e variantes aparece 9 vezes em 5 das 20 falas (7 dos 14 vídeos-núcleo, somando a leitura manual) e em 7 das 30 legendas. 11 de 20 falas citam números (TOP#13 cita 6), mas a manchete com número é minoria (5 de 30).

