# Ficha quantitativa — @ddiasmatt (Mateus Dias)

Fundador do app ChatFunnel · 46.936 seguidores · 185 posts · **92 reels** (lista completa) · coleta em 29/09/2026 com login. Fontes: `users/ddiasmatt.json` (todos os reels), `dossie/ddiasmatt.md`, `videos/ddiasmatt/*.tr.json | *.ocr.json | *.vis.json`, as 30 folhas de contato (`*.sheet.jpg`) e os 30 frames de gancho (`*.hook.jpg`). Números calculados em Python a partir dos brutos. Nenhum trecho de fala ou legenda com mais de 5 palavras seguidas foi copiado; manchetes de tela com até 12 palavras aparecem entre «».

## 0. Como os números foram medidos

- **views** = `play_count` (todos os 92 têm). Views, likes e comentários dos 30 vêm da lista `items`, igual ao dossiê.
- **Percentis**: interpolação linear sobre os 92 reels. A mediana é a mesma do dossiê (1.586,5); p25, p75 e p90 do dossiê (801 / 7.382 / 21.899) usam outro método e diferem até 1,7%. **Múltiplo** = views ÷ 1.586,5.
- **Tendência**: ordem da lista do Instagram (mais novo → mais velho) sem o único fixado (`DMdKmfEMdTl`, TOP#14). Datas tiradas do ID do post, no horário de Brasília (UTC−3).
- **Palavras/min** = palavras ÷ (fim do último trecho − início do 1º) × 60, como no dossiê, só com fala em pt e flag ok (26 vídeos). Antes de contar, tirei alucinações do Whisper que passam do fim do vídeo ou ficam sobre a cartela final ("Legenda Adriana Zanotto" em RECENTE#5 e #6; "E aí" em RECENTE#8 e #15) e vozes de terceiros (RECENTE#15, 0–17,5 s: clipe deepfake; TOP#12: 2 respostas de entrevistados). Por isso RECENTE#5, #6, #8 e #15 ficam diferentes do dossiê (165→232, 138→237, 219→238, 153→233 pal/min). Também mostro o ritmo sobre a duração total (seção 4.6).
- **Cortes/min**: bruto = cortes do `vis.json` ÷ duração. Agrupado = cortes a menos de 1 s um do outro contam como 1.
- **Tem fala**: fala em pt com flag ok. TOP#1 e TOP#10 saíram como "en, ok", mas o texto é letra de música; contam como sem fala. TOP#8 e TOP#13 não têm fala.
- **Números citados**: dígitos e numerais por extenso na fala, sem "um/uma"; uma sequência como "60 mil" ou "vinte e cinco" conta 1; entram datas, porcentagens, preços, versões de modelo e códigos. **Perguntas**: quantidade de "?" na transcrição (RECENTE#1–4 foram transcritos pelo faster-whisper-small). **CTA falado**: conferido à mão; o segundo é o início do trecho em que o verbo aparece.
- **Formato** e **tipo do texto no 1º frame**: classificados olhando as 30 folhas de contato e os 30 frames de gancho, junto com OCR, legenda e transcrição.
- **Linguagem**: nomes de marca que o Whisper escreve de vários jeitos foram unificados antes de contar ("chat EPT/EPP/de PT" → ChatGPT; "chat funny/chatfone" → ChatFunnel; "Cloud Code" → Claude Code).
- **Limites**: em TOP#6 o 1º trecho do Whisper cobre 0–17 s, onde há uma montagem com trilha (sem esse trecho o ritmo seria 232 pal/min); TOP#9 é narração em off sobre imagens; o faster-whisper-small (RECENTE#1–4) erra nomes. OCR a cada 2 s: uma cartela pode ter entrado até 2 s antes do segundo indicado.

## 1. Distribuição de views (92 reels) e tendência

| p10 | p25 | p50 (mediana) | p75 | p90 | p99 | máximo | média |
|---|---|---|---|---|---|---|---|
| 619,3 | 796,5 | 1.586,5 | 7.260,5 | 21.625,2 | 1.766.377,7 | 18.325.149 | 207.789 |

- Mediana = 3,4% dos seguidores. Um único reel (TOP#1, comparação visual de 8,8 s) tem 18.325.149 views, **95,9% de todas as views** dos 92 (19.116.592). Sem ele, a média cai de 207.789 para 8.697.
- ≥ 10 mil: 17 reels (18,5%); ≥ 50 mil: 4; ≥ 100 mil: 3; ≥ 1 milhão: 1.
- Mediana de likes/views de todos os reels: 1,40%; comentários/views: 0,054%. 36 dos 92 reels (39%) têm zero comentários.
- Prováveis anúncios (likes/views < 0,3%): 4 de 92, todos entre jul/2024 e abr/2026: TOP#7 (`DXc3jcXgoM9`, 0,15%), TOP#8 (`C9LgYAFvCbl`, 0,29%, cartaz de evento em collab), `DCrQhwlNjnW` (8.571 views, 0,04%) e `DAHUaoNOJIE` (9.490 views, 0,03%). Nenhum entre os 50 mais novos.

**Mediana por blocos de 50 reels (mais novo → mais velho, sem o fixado)**

| bloco | reels | período (mais novo → mais velho) | dias | reels/semana | mediana | x mediana geral | p90 | máximo | prováveis anúncios | reels com 0 comentário | mediana likes/views |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 50 | 2026-09-28 → 2026-06-20 | 101 | 3,5 | 827,0 | 0,52x | 2.656 | 62.690 | 0 | 31 | 1,32% |
| 2 | 41 | 2026-06-17 → 2022-06-13 | 1.466 | 0,2 | 7.382,0 | 4,65x | 42.695 | 18.325.149 | 4 | 5 | 1,61% |

Com só 91 reels não fixados, dois blocos escondem a curva. Complemento com blocos de 10:

| bloco de 10 | período | reels/semana | mediana | x mediana geral | máximo | reels com 0 comentário |
|---|---|---|---|---|---|---|
| 1 (10) | 2026-09-28 → 2026-09-14 | 4,7 | 856,0 | 0,54x | 3.288 | 5 |
| 2 (10) | 2026-09-11 → 2026-08-25 | 3,9 | 771,5 | 0,49x | 1.504 | 7 |
| 3 (10) | 2026-08-24 → 2026-08-12 | 5,4 | 665,0 | 0,42x | 1.338 | 9 |
| 4 (10) | 2026-08-11 → 2026-07-22 | 3,3 | 827,5 | 0,52x | 7.220 | 6 |
| 5 (10) | 2026-07-15 → 2026-06-20 | 2,7 | 1.075,0 | 0,68x | 62.690 | 4 |
| 6 (10) | 2026-06-17 → 2026-04-17 | 1,1 | 2.147,5 | 1,35x | 43.656 | 3 |
| 7 (10) | 2026-04-15 → 2025-10-19 | 0,4 | 5.587,0 | 3,52x | 42.695 | 0 |
| 8 (10) | 2025-09-11 → 2024-09-19 | 0,2 | 10.540,5 | 6,64x | 18.325.149 | 2 |
| 9 (10) | 2024-09-01 → 2022-07-23 | 0,1 | 13.483,0 | 8,50x | 128.697 | 0 |
| 10 (1) | 2022-06-13 → 2022-06-13 | 7,0 | 21.899,0 | 13,80x | 21.899 | 0 |

**2026 mês a mês** (66 dos 92 reels são de 2026)

| mês | reels | mediana | máximo | reels com 0 comentário |
|---|---|---|---|---|
| mar/2026 | 2 | 4.401,0 | 6.879 | 0 |
| abr/2026 | 8 | 5.172,5 | 41.766 | 1 |
| mai/2026 | 1 | 1.267,0 | 1.267 | 0 |
| jun/2026 | 10 | 1.190,0 | 62.690 | 3 |
| jul/2026 | 6 | 1.121,5 | 2.599 | 4 |
| ago/2026 | 25 | 714,0 | 7.220 | 19 |
| set/2026 | 14 | 813,5 | 3.288 | 7 |

Leitura: a mediana cai em quase todos os blocos de 10, do mais velho para o mais novo (13.483 em 2022–2024 → 10.540,5 → 5.587 → 2.147,5 → 1.075 → 827,5 → 665 → 771,5 → 856), enquanto o ritmo subiu de 0,1–0,4 reel por semana (até abr/2026) para 2,7–5,4 por semana (jun–set/2026). Os 50 mais novos têm mediana 0,52x a geral e 31 deles têm zero comentário; o bloco anterior tem 4,65x e 5 sem comentário. Ago/2026 teve 25 reels, 19 sem nenhum comentário. Dos 15 mais vistos de todos os tempos, só 1 (TOP#4, 23/06/2026) está entre os 50 mais novos.

## 2. Os 30 selecionados

| código | grupo | data | dur (s) | views | x mediana | likes/views | coment./views | pal/min | cortes/min bruto (agrupado) | tem fala? | idioma | nº palavras | nº perguntas | nº números | CTA falado (s; % do vídeo) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DF8fxOLPsqu | TOP#1 | 2025-02-11 | 8,8 | 18.325.149 | 11.550,7x | 2,95% | 0,007% | — | 0,0 (0,0) | não | — (letra de música em en) | 0 | 0 | 0 | — |
| CrYyOTttWUd | TOP#2 | 2023-04-23 | 69,4 | 128.697 | 81,1x | 1,40% | 0,172% | 247 | 5,2 (4,3) | sim | pt | 273 | 3 | 6 | — |
| CpL6jsQLpmx | TOP#3 | 2023-02-27 | 32,2 | 105.303 | 66,4x | 0,97% | 1,761% | 213 | 0,0 (0,0) | sim | pt | 113 | 1 | 2 | 17,9 (56%; comenta PALAVRA) |
| DZ8fXciiaig | TOP#4 | 2026-06-23 | 87,7 | 62.690 | 39,5x | 2,57% | 0,225% | 247 | 0,0 (0,0) | sim | pt | 360 | 1 | 0 | — |
| DZdlhdYiRQQ | TOP#5 | 2026-06-11 | 86,9 | 43.656 | 27,5x | 2,33% | 0,085% | 237 | 1,4 (0,7) | sim | pt | 342 | 6 | 5 | 80,6 (93%; comenta NÚMERO + link na bio) |
| DQcJ5RIDrNl | TOP#6 | 2025-10-30 | 180,0 | 42.695 | 26,9x | 0,68% | 0,108% | 216 | 14,3 (11,7) | sim | pt | 640 | 1 | 7 | 174,2 (97%; comenta PALAVRA) |
| DXc3jcXgoM9 | TOP#7 (anúncio?) | 2026-04-22 | 82,9 | 41.766 | 26,3x | 0,15% | 0,007% | 196 | 0,0 (0,0) | sim | pt | 270 | 5 | 9 | — |
| C9LgYAFvCbl | TOP#8 (anúncio?) | 2024-07-08 | 19,7 | 32.176 | 20,3x | 0,29% | 0,056% | — | 3,0 (3,0) | não | — | 0 | 0 | 0 | — |
| C_YaWJOu0Az | TOP#9 | 2024-09-01 | 90,0 | 28.389 | 17,9x | 1,04% | 0,053% | 161 | 8,7 (6,7) | sim | pt | 230 | 2 | 0 | — |
| CewUQzBpsE_ | TOP#10 | 2022-06-13 | 75,9 | 21.899 | 13,8x | 4,97% | 0,269% | — | 6,3 (4,0) | não | — (letra de música em en) | 0 | 0 | 0 | — |
| DWpV8sRgumA | TOP#11 | 2026-04-02 | 83,5 | 19.161 | 12,1x | 1,34% | 1,461% | 185 | 2,2 (1,4) | sim | pt | 257 | 2 | 4 | — |
| C-5h7UOOlKM | TOP#12 | 2024-08-20 | 37,0 | 16.970 | 10,7x | 1,90% | 0,265% | 253 | 21,1 (13,0) | sim | pt | 131 | 7 | 0 | — |
| DAiwAizuTUg | TOP#13 | 2024-09-30 | 23,2 | 16.765 | 10,6x | 1,83% | 0,078% | — | 80,1 (20,7) | não | — | 0 | 0 | 0 | — |
| DMdKmfEMdTl | TOP#14 (fixado) | 2025-07-23 | 71,0 | 13.162 | 8,3x | 4,49% | 0,745% | 231 | 21,1 (19,4) | sim | pt | 272 | 0 | 2 | 37,0 (52%; comenta PALAVRA) + 65,9 (93%; me segue) |
| DIxHPh1tKGi | TOP#15 | 2025-04-22 | 124,7 | 12.831 | 8,1x | 1,40% | 0,359% | 204 | 13,5 (6,3) | sim | pt | 424 | 5 | 2 | 121,4 (97%; comenta PALAVRA) |
| Dd2OUbvRGSM | RECENTE#1 | 2026-09-28 | 123,2 | 425 | 0,3x | 1,18% | 0,000% | 252 | 1,0 (1,0) | sim | pt | 476 | 4 | 3 | — |
| DdxK3HJx9ss | RECENTE#2 | 2026-09-26 | 64,9 | 868 | 0,5x | 1,27% | 0,000% | 266 | 1,8 (0,9) | sim | pt | 243 | 0 | 0 | — |
| Ddr6ek-RpDB | RECENTE#3 | 2026-09-24 | 100,9 | 704 | 0,4x | 0,85% | 0,000% | 239 | 2,4 (2,4) | sim | pt | 362 | 1 | 5 | — |
| Ddmttb6RpJf | RECENTE#4 | 2026-09-22 | 116,0 | 551 | 0,3x | 1,45% | 0,181% | 266 | 4,7 (3,1) | sim | pt | 471 | 3 | 0 | — |
| DdfGIizCcTy | RECENTE#5 | 2026-09-19 | 94,3 | 844 | 0,5x | 1,30% | 0,000% | 232 | 2,5 (1,9) | sim | pt | 325 | 1 | 5 | — |
| Ddcddm_CZO4 | RECENTE#6 | 2026-09-18 | 61,5 | 3.173 | 2,0x | 2,90% | 0,284% | 237 | 22,4 (18,5) | sim | pt | 204 | 8 | 12 | — |
| DdZ5-xaiEPx | RECENTE#7 | 2026-09-17 | 71,9 | 572 | 0,4x | 1,22% | 0,175% | 233 | 2,5 (1,7) | sim | pt | 240 | 2 | 0 | — |
| DdXUmI0C0QG | RECENTE#8 | 2026-09-16 | 117,5 | 1.869 | 1,2x | 1,93% | 0,054% | 238 | 2,0 (1,5) | sim | pt | 425 | 2 | 9 | — |
| DdUwYbhiIK3 | RECENTE#9 | 2026-09-15 | 137,3 | 3.288 | 2,1x | 2,40% | 0,000% | 231 | 1,3 (0,9) | sim | pt | 490 | 4 | 8 | — |
| DdSKOZmSeBQ | RECENTE#10 | 2026-09-14 | 85,9 | 1.197 | 0,8x | 2,17% | 1,420% | 250 | 4,2 (2,8) | sim | pt | 316 | 7 | 0 | — |
| DdKgaOaCVjD | RECENTE#11 | 2026-09-11 | 196,7 | 707 | 0,4x | 0,99% | 0,000% | 247 | 1,2 (0,6) | sim | pt | 768 | 13 | 3 | — |
| Dc7DZ2MC6dI | RECENTE#12 | 2026-09-05 | 155,8 | 1.504 | 0,9x | 1,80% | 0,066% | 262 | 1,5 (0,8) | sim | pt | 647 | 8 | 9 | — |
| Dc1974Li3eN | RECENTE#13 | 2026-09-03 | 78,8 | 618 | 0,4x | 0,81% | 0,162% | 239 | 4,6 (3,8) | sim | pt | 274 | 0 | 7 | — |
| DczW37aClod | RECENTE#14 | 2026-09-02 | 114,0 | 783 | 0,5x | 1,02% | 0,000% | 262 | 2,6 (2,1) | sim | pt | 455 | 5 | 5 | — |
| DcuKBXdi9s7 | RECENTE#15 | 2026-08-31 | 116,5 | 1.452 | 0,9x | 1,31% | 0,000% | 233 | 3,1 (3,1) | sim | pt | 345 | 11 | 4 | — |

TOP#1 e TOP#10: a "fala" em inglês é letra de música. RECENTE#15: contagens só da fala dele (a partir de 17,6 s). CTA falado aparece em só 5 dos 26 vídeos com fala, todos do TOP; nos 15 recentes o CTA nunca é falado (fica numa cartela final muda, seção 5).

| grupo | mediana views | mediana x | mediana dur (s) | mediana likes/views | mediana coment./views | com fala dele em pt | prováveis anúncios | comentários (soma) | vídeos com 0 comentário |
|---|---|---|---|---|---|---|---|---|---|
| TOP 15 | 32.176 | 20,3x | 75,9 | 1,40% | 0,172% | 11 | 2 | 4.189 | 0 |
| RECENTES 15 | 844 | 0,5x | 114,0 | 1,30% | 0,000% | 15 | 0 | 31 | 8 |

**Views por formato (nos 30)**

| formato | grupo | n | vídeos | mediana views | mínimo | máximo |
|---|---|---|---|---|---|---|
| A. tela dividida (rosto em cima + tela embaixo) | TOP | 4 | T#4, T#5, T#7, T#11 | 42.711,0 | 19.161 | 62.690 |
| A. tela dividida (rosto em cima + tela embaixo) | RECENTE | 13 | R#2, R#3, R#4, R#5, R#7, R#8, R#9, R#10, R#11, R#12, R#13, R#14, R#15 | 844,0 | 551 | 3.288 |
| B. falando pra câmera em tela cheia | TOP | 4 | T#2, T#3, T#6, T#15 | 73.999,0 | 12.831 | 128.697 |
| B. falando pra câmera em tela cheia | RECENTE | 2 | R#1, R#6 | 1.799,0 | 425 | 3.173 |
| C. narração/entrevista/vlog | TOP | 3 | T#9, T#12, T#14 | 16.970,0 | 13.162 | 28.389 |
| D. sem fala dele | TOP | 4 | T#1, T#8, T#10, T#13 | 27.037,5 | 16.765 | 18.325.149 |

T#n = TOP#n; R#n = RECENTE#n.

O TOP cobre jun/2022 a jun/2026; os 15 recentes saíram em 29 dias (31/08 a 28/09/2026). Formatos só se comparam dentro do mesmo grupo. Os 3 vídeos orgânicos de 2026 no TOP (TOP#4, #5 e #11; o 4º, TOP#7, é provável anúncio) são **tela dividida, com 83–88 s, 257–360 palavras e "comenta PALAVRA" na legenda**. Nos recentes, 13 de 15 usam o mesmo formato de tela dividida, só que com 65–197 s (mediana 114) e, em 12 deles, "link na bio". Falando pra câmera em tela cheia: os 2 vídeos com fala dele mais vistos de todos (TOP#2, 128.697, e TOP#3, 105.303, ambos de 2023) são desse formato; nos recentes, os 2 desse formato ficaram em 2º (RECENTE#6, 3.173) e em último (RECENTE#1, 425).

## 3. Ganchos: primeiros 5 s e texto na tela no 1º frame

| código | grupo | formato | o que é dito em 0–5 s (paráfrase) | texto na tela no 1º frame (OCR t=0, limpo) | tipo do texto |
|---|---|---|---|---|---|
| DF8fxOLPsqu | TOP#1 | comparação feita com IA + música | sem fala (música com letra em inglês) | «A evolução da IA» + rótulos «2 anos atrás» × «Agora» | manchete |
| CrYyOTttWUd | TOP#2 | falando pra câmera (estúdio) + prints | Diz que a copy feita pelo ChatGPT ficou ótima e promete provar | «COPY,» (legenda palavra a palavra) | legenda da fala |
| CpL6jsQLpmx | TOP#3 | selfie falando pra câmera | Pergunta se a pessoa produz conteúdo e propõe um desafio | «cê cria conteúdo no Instagram» | legenda da fala |
| DZ8fXciiaig | TOP#4 | tela dividida (rosto + tela) | Revela uma regra que impôs à IA: registrar tudo que fizer | «Eu criei uma» sobre o grafo do Obsidian | legenda da fala |
| DZdlhdYiRQQ | TOP#5 | tela dividida (rosto + tela) | Anuncia que a OpenAI decretou o fim do ChatGPT; encena espanto | print da newsletter: «#012 - Os Chats Morreram! O Que Vem Depois?» + legenda «A OpenAI» | print com título |
| DQcJ5RIDrNl | TOP#6 | manifesto falando pra câmera (estúdio) | Após montagem com trilha, denuncia mercado digital reduzido a números | «POV: Você não desistiu» (cartela sobre montagem 2021–2024) | manchete |
| DXc3jcXgoM9 | TOP#7 | tela dividida (rosto + tela) | Diz que sites gerados por IA em geral carregam rápido | «Páginas feitas com» + fluxograma «Performance» | legenda da fala |
| C9LgYAFvCbl | TOP#8 | cartaz de evento (collab) | sem fala (música) | «PALESTRANTE CONFIRMADO» + nome do evento | cartaz |
| C_YaWJOu0Az | TOP#9 | manifesto narrado sobre imagens | Pergunta quantos sonhos o espectador abandonou por medo | «GIRE O SEU TELEFONE» | instrução |
| CewUQzBpsE_ | TOP#10 | vida pessoal + música | sem fala (música de Ed Sheeran) | nenhum | nenhum |
| DWpV8sRgumA | TOP#11 | tela dividida (rosto + tela) | Mostra o sistema com 22 agentes de IA trabalhando na empresa | «Eu criei um sistema» + slide «E ele continua sendo um dos mais produtivos da empresa» | legenda da fala |
| C-5h7UOOlKM | TOP#12 | entrevista de rua | Avisa que saiu na rua perguntando quem já comprou curso | «EU VIM PRA» | legenda da fala |
| DAiwAizuTUg | TOP#13 | bastidor de palestra | sem fala | nenhum | nenhum |
| DMdKmfEMdTl | TOP#14 | vlog narrado (série) | Declara que abandonou tudo, trocou de estado e mira ser bilionário | «LARGUEI TUDO» | legenda da fala |
| DIxHPh1tKGi | TOP#15 | falando pra câmera (estúdio) | Pergunta o que faria ao flagrar "ela" flertando; diz que apagou | «faria» | legenda da fala |
| Dd2OUbvRGSM | RECENTE#1 | falando pra câmera (estúdio) | Avisa que a maior parte do público ainda não está pronta | «SE VOCÊ ESTÁ TENTANDO VENDER NO INSTAGRAM, VEJA ISSO» | manchete |
| DdxK3HJx9ss | RECENTE#2 | tela dividida (rosto + tela) | Entra no meio da demonstração, explicando a base de conhecimento | «DÊ À IA ACESSO AO CONHECIMENTO DO SEU E-COMMERCE» | manchete |
| Ddr6ek-RpDB | RECENTE#3 | tela dividida (rosto + tela) | Pergunta, sem saudação, se a loja do espectador roda tráfego pago | «FAÇA ISSO PARA ACOMPANHAR SEUS ANÚNCIOS PELO CHATGPT» | manchete |
| Ddmttb6RpJf | RECENTE#4 | tela dividida (rosto + tela) | Entra no meio: descreve a mecânica comentar-e-receber-link | «FAÇA ISSO NO INSTAGRAM PARA CONVERTER COMENTÁRIOS EM CLIENTES» | manchete |
| DdfGIizCcTy | RECENTE#5 | tela dividida (rosto + tela) | Abre como continuação: mais um teste, criar pautas com IA | «Se você está sem ideias de conteúdo, faça isso no GPT Astra» | manchete |
| Ddcddm_CZO4 | RECENTE#6 | falando pra câmera (estúdio) | Manda abrir o GPT por voz e pedir um número aleatório | «SEU GPT TAMBÉM VAI ESCOLHER 17? FAÇA ESSE TESTE» | manchete |
| DdZ5-xaiEPx | RECENTE#7 | tela dividida (rosto + tela) | Afirma que cada tarefa dada à IA é um contrato de trabalho | «FAÇA ISSO ANTES DE ENVIAR QUALQUER PROMPT PARA A IA» | manchete |
| DdXUmI0C0QG | RECENTE#8 | tela dividida (rosto + tela) | Anuncia que vai mostrar como organiza as empresas com IA | «USE O OBSIDIAN DESSE JEITO PARA ORGANIZAR SUA EMPRESA COM IA» | manchete |
| DdUwYbhiIK3 | RECENTE#9 | tela dividida (rosto + tela) | Entra no meio: fotografou um controle e mandou as fotos ao GPT | «3 prompts foram suficientes para fazer isso aqui com o GPT-6 Astra» | manchete |
| DdSKOZmSeBQ | RECENTE#10 | tela dividida (rosto + tela) | Reage espantado à qualidade do resultado e pergunta como foi feito | «ESSE É O JEITO CERTO DE USAR MÚLTIPLOS AGENTES DE IA» | manchete |
| DdKgaOaCVjD | RECENTE#11 | tela dividida (rosto + tela) | Duas perguntas: como e por que usar IA "com essa plataforma" | «ESSA É UMA DAS MELHORES FORMAS DE USAR IA COM OBSIDIAN» | manchete |
| Dc7DZ2MC6dI | RECENTE#12 | tela dividida (rosto + tela) | Provoca: no Instagram a vida alheia parece perfeita, a sua péssima | «ISSO AQUI VAI MUDAR A FORMA COMO VOCÊ CRIA CONTEÚDO» | manchete |
| Dc1974Li3eN | RECENTE#13 | tela dividida (rosto + tela) | Ataca a prestação de serviço como modelo de negócio (com palavrão) | «Se você já presta serviço, precisa ver isso» | manchete |
| DczW37aClod | RECENTE#14 | tela dividida (rosto + tela) | Começa em história: cansou de pagar editor de thumbnail | «Se eu fosse começar um software hoje, faria exatamente isso» | manchete |
| DcuKBXdi9s7 | RECENTE#15 | tela dividida (rosto + tela) | Clipe deepfake de terceiros (chefe acorda funcionário); ele fala aos 17,6 s | «Você ainda vai saber o que é real na internet?» | manchete |

Contagens do gancho:

- **Início da fala**: 25 dos 26 vídeos com fala em pt começam a falar em 0,0 s (exceção: RECENTE#15, em que a voz dele entra aos 17,6 s, depois de um clipe de terceiros). Nenhum dos 26 abre com saudação, nome ou apresentação.
- **1ª frase dele, TOP (11 com fala)**: "eu fiz/eu criei" em 1ª pessoa 4 (TOP#4, #11, #12, #14); pergunta 3 (ao espectador TOP#3, retórica TOP#9, isca de duplo sentido TOP#15); notícia chocante 1 (TOP#5); afirmação provocativa 1 (TOP#6); afirmação com promessa de prova 1 (TOP#2); afirmação técnica 1 (TOP#7, anúncio).
- **1ª frase dele, RECENTES (15)**: começa no meio de um raciocínio 5 (RECENTE#2, #4, #5, #9, #11: abre com "E…", "Então…", "Uma outra coisa…" ou cita "essa plataforma" sem apresentar, sinal de corte de vídeo longo); afirmação provocativa 4 (#1, #7, #12, #13; 2 delas com palavrão); pergunta 2 (#3, #8); teste ao vivo 1 (#6); reação ao resultado 1 (#10); "eu fiz" 1 (#14); clipe de terceiros 1 (#15).
- **Texto no 1º frame**: 28 de 30 (sem texto: TOP#10 e TOP#13). No TOP: legenda da própria fala 8, manchete 2 (TOP#1, TOP#6), print com título 1 (TOP#5), cartaz 1 (TOP#8), instrução 1 (TOP#9). Nos recentes: **15 de 15 com manchete** numa caixa escura no meio da tela, com palavras-chave em cor.
- **Manchetes dos recentes** (15): 8 a 12 palavras, mediana 10. "isso/ISSO" em 9 (a manchete aponta para o vídeo sem dizer o quê); imperativo ("FAÇA ISSO", "FAÇA ESSE TESTE", "USE", "DÊ") em 7; "você/seu/sua" em 9; nome de ferramenta (GPT, ChatGPT, Obsidian, GPT Astra) em 6; "IA" em 5; "Se você…/Se eu…" em 4; pergunta em 2. Só 2 têm número (RECENTE#9 «3 prompts foram suficientes…» e RECENTE#6 «…ESCOLHER 17? FAÇA ESSE TESTE»), e são os 2 recentes mais vistos (3.288 e 3.173; os outros 13 têm mediana 783). Com n = 2, é indício.
- **No TOP o gancho é falado**: em 8 dos 15 o texto do 1º frame é a legenda da própria fala, sem manchete. As frases que abriram os mais vistos com fala: resultado com prova (TOP#2), desafio com pergunta direta (TOP#3), regra que ele criou para a IA (TOP#4), notícia de impacto com objeções encenadas logo em seguida (TOP#5: quatro perguntas na voz do público entre 2,6 e 7,6 s).
- **Moldes (com lacunas)**: "Eu criei [regra/sistema] para [a minha IA/a minha empresa] que [faz algo visível]" + mostrar o resultado; "[Empresa] anunciou [mudança grande em ferramenta famosa]" + 2 ou 3 objeções curtas na voz do público ("Como assim? Vou perder [X]?") + "Calma, a questão é [explicação]"; "Você [faz tarefa comum]? Tenho um desafio pra você: [entrega concreta, com número]"; manchete «[Número] [recurso] foram suficientes para [resultado]» ou «[Ferramenta] também vai [comportamento]? Faça esse teste».

## 4. Linguagem (26 vídeos com fala em pt e flag ok; 9.353 palavras; 482 frases)

### 4.1 Top 30 expressões recorrentes de 2 a 4 palavras

Contadas dentro da frase, descartando combinações feitas só de palavras vazias (artigo, preposição, pronome, conjunção, formas de ser/estar/ter/ir, quantificadores como "todo/tudo") e os pedaços que só existem dentro de uma expressão maior (ex.: "fazendo um" dentro de "fazendo um favor"); variações do tipo "a/para a/com inteligência artificial" foram somadas à forma base. Ordem: nº de vídeos, depois ocorrências.

| # | expressão | vídeos (de 26) | ocorrências | onde |
|---|---|---|---|---|
| 1 | a gente | 18 | 60 | TOP#2, TOP#4, TOP#5, TOP#7, TOP#12, TOP#14, TOP#15, RECENTE#1, RECENTE#2, RECENTE#3, RECENTE#4, RECENTE#5, RECENTE#6, RECENTE#10, RECENTE#11, RECENTE#12, RECENTE#13, RECENTE#15 |
| 2 | inteligência artificial | 15 | 63 | TOP#4, TOP#5, TOP#6, TOP#7, TOP#11, TOP#15, RECENTE#1, RECENTE#3, RECENTE#6, RECENTE#7, RECENTE#8, RECENTE#11, RECENTE#12, RECENTE#13, RECENTE#15 |
| 3 | as pessoas | 11 | 35 | TOP#6, TOP#12, TOP#15, RECENTE#1, RECENTE#2, RECENTE#4, RECENTE#6, RECENTE#12, RECENTE#13, RECENTE#14, RECENTE#15 |
| 4 | de conteúdo | 7 | 16 | TOP#3, TOP#11, RECENTE#1, RECENTE#5, RECENTE#11, RECENTE#12, RECENTE#15 |
| 5 | você pode | 7 | 13 | RECENTE#1, RECENTE#2, RECENTE#3, RECENTE#4, RECENTE#8, RECENTE#12, RECENTE#14 |
| 6 | dentro do | 7 | 12 | TOP#2, TOP#4, RECENTE#1, RECENTE#3, RECENTE#5, RECENTE#8, RECENTE#11 |
| 7 | ou seja | 7 | 12 | TOP#2, TOP#4, TOP#5, TOP#11, TOP#15, RECENTE#1, RECENTE#8 |
| 8 | todo mundo | 7 | 9 | TOP#6, TOP#11, TOP#15, RECENTE#1, RECENTE#12, RECENTE#13, RECENTE#15 |
| 9 | aqui dentro | 6 | 15 | RECENTE#2, RECENTE#3, RECENTE#4, RECENTE#8, RECENTE#10, RECENTE#11 |
| 10 | eu quero | 6 | 11 | TOP#14, RECENTE#4, RECENTE#5, RECENTE#9, RECENTE#11, RECENTE#14 |
| 11 | por exemplo | 6 | 11 | TOP#4, RECENTE#1, RECENTE#3, RECENTE#4, RECENTE#8, RECENTE#10 |
| 12 | criar uma | 6 | 9 | TOP#2, TOP#4, TOP#14, RECENTE#4, RECENTE#8, RECENTE#11 |
| 13 | eu posso | 6 | 8 | TOP#2, TOP#4, RECENTE#3, RECENTE#4, RECENTE#5, RECENTE#11 |
| 14 | dentro da | 6 | 6 | TOP#11, TOP#15, RECENTE#1, RECENTE#2, RECENTE#3, RECENTE#11 |
| 15 | tipo de | 5 | 10 | TOP#3, TOP#15, RECENTE#5, RECENTE#6, RECENTE#12 |
| 16 | o ChatFunnel | 5 | 8 | RECENTE#1, RECENTE#2, RECENTE#3, RECENTE#4, RECENTE#12 |
| 17 | a gente faz | 5 | 6 | TOP#4, TOP#7, TOP#15, RECENTE#4, RECENTE#10 |
| 18 | uma pessoa | 5 | 6 | RECENTE#1, RECENTE#3, RECENTE#6, RECENTE#12, RECENTE#14 |
| 19 | você faz | 5 | 6 | TOP#5, RECENTE#1, RECENTE#3, RECENTE#4, RECENTE#7 |
| 20 | coisa que | 5 | 5 | TOP#4, RECENTE#5, RECENTE#7, RECENTE#11, RECENTE#14 |
| 21 | deixa eu | 5 | 5 | TOP#2, TOP#3, TOP#5, TOP#14, RECENTE#11 |
| 22 | conteúdo que | 4 | 7 | TOP#4, TOP#11, RECENTE#1, RECENTE#12 |
| 23 | o link | 4 | 7 | TOP#5, TOP#14, RECENTE#4, RECENTE#14 |
| 24 | as coisas | 4 | 6 | TOP#11, RECENTE#1, RECENTE#3, RECENTE#12 |
| 25 | eu venho aqui | 4 | 6 | TOP#6, RECENTE#8, RECENTE#10, RECENTE#11 |
| 26 | você consegue | 4 | 6 | RECENTE#3, RECENTE#11, RECENTE#13, RECENTE#14 |
| 27 | você precisa | 4 | 6 | TOP#4, RECENTE#1, RECENTE#7, RECENTE#11 |
| 28 | Claude Code | 4 | 5 | TOP#4, TOP#5, TOP#11, RECENTE#14 |
| 29 | está fazendo | 4 | 5 | RECENTE#3, RECENTE#7, RECENTE#11, RECENTE#12 |
| 30 | eu criei | 4 | 5 | TOP#4, TOP#11, RECENTE#8, RECENTE#10 |

Fora do top 30, em 4 vídeos cada: "fazendo um favor" (5 vezes, sempre ao ditar um pedido para a IA; mais 1 "faz um favor"), "olha só" (5), "o resultado" (5), "precisa ter" (5), "uma mensagem" (5), "vai fazer" (5), "o GPT" (5), "como eu disse" (4, só no TOP). Variantes de "a gente" que também se repetem: "que a gente" (10 vídeos, 18 vezes) e "a gente tem" (8 vídeos). "você pode" (7 vídeos), "aqui dentro" (6) e "o ChatFunnel" (5) só aparecem nos recentes.

### 4.2 Tamanho de frase

- Por pontuação do Whisper: média **19,4** palavras, mediana **13,5** (482 frases; 59 com até 5 palavras, 150 com 20 ou mais). TOP: média 19,0, mediana 13,0 (175 frases); recentes: 19,6 e 14,0 (307 frases).
- Por trecho do Whisper (pausa de respiração): média 9,1, mediana 8,0 palavras (1.023 trechos). TOP: mediana 10,0 (306 trechos); recentes: 7,0 (717 trechos). Em fala rápida o Whisper deixa de pôr ponto final (TOP#4, RECENTE#2, #5, #13, #14 têm mediana de 17 a 36 palavras por frase); a mediana por trecho é a medida mais estável.

### 4.3 Tratamento do espectador

| recorte | vídeos | frases | frases com "você(s)" | frases com "tu" | frases com 2ª pessoa (você/tu/te/teu/ti) | frases com 1ª pessoa do singular (eu/me/mim/meu/minha) | frases com "a gente"/nós | "você(s)" por mil palavras | "eu" por mil palavras |
|---|---|---|---|---|---|---|---|---|---|
| TOP | 11 | 175 | 45 (25,7%) | 1 | 58 (33,1%) | 59 (33,7%) | 21 (12,0%) | 21,7 | 22,6 |
| RECENTES | 15 | 307 | 81 (26,4%) | 1 | 84 (27,4%) | 115 (37,5%) | 34 (11,1%) | 22,8 | 30,0 |
| total | 26 | 482 | 126 (26,1%) | 2 | 142 (29,5%) | 174 (36,1%) | 55 (11,4%) | 22,5 | 27,4 |

"a gente": 60 vezes (6,4 por mil palavras), em 18 de 26 vídeos; "tu" só 2 vezes (TOP#4 e RECENTE#14) e "cê" nenhuma. Ele fala mais de si ("eu") do que do espectador ("você"): o vídeo típico é "eu fiz / eu uso / eu criei" mostrado na tela, com "você" nas instruções ("você pode", "você precisa", "você consegue").

### 4.4 Marcadores de oralidade

| marcador | ocorrências | por mil palavras | vídeos (de 26) | observação |
|---|---|---|---|---|
| né | 31 | 3,3 | 17 | 30 das 31 são "né?" no fim da frase |
| tá | 26 | 2,8 | 10 | 21 como "está"; 4 como "tá?" no fim da frase; 1 como "Tá, Mateus" na voz do público |
| olha | 7 | 0,7 | 6 | 5 como "olha só", sempre apontando para a tela; os 2 "olha essencial" de RECENTE#1 são erro do Whisper ("óleo essencial") e foram descontados |
| sabe | 7 | 0,7 | 5 | só 1 como marcador ("sabe?", TOP#2); 6 são o verbo |
| cara | 4 | 0,4 | 4 | vocativo só 1 (RECENTE#14); 2 "o cara", 1 "de cara" |
| gente (vocativo) | 1 | 0,1 | 1 | "né gente?" (RECENTE#15); outras 3 são "muita/só gente"; 60 são "a gente" |
| galera | 2 | 0,2 | 1 | "a galera" = a equipe dele (TOP#11); nunca chama o público de galera |
| mano | 0 | 0,0 | 0 |  |

Outros marcadores que aparecem nos dados:

| palavra | ocorrências | por mil palavras | vídeos (de 26) | TOP (por mil) | recentes (por mil) |
|---|---|---|---|---|---|
| aqui | 176 | 18,8 | 25 | 11,2 | 23,0 |
| então | 83 | 8,9 | 21 | 4,2 | 11,4 |
| inteligência artificial | 63 | 6,7 | 15 | 6,6 | 6,8 |
| pra mim / para mim | 32 | 3,4 | 12 | 1,2 | 4,6 |
| porque | 29 | 3,1 | 16 | 3,9 | 2,6 |
| pra você / para você | 28 | 3,0 | 16 | 3,0 | 3,0 |
| isso aqui | 27 | 2,9 | 11 | 0,6 | 4,1 |
| aqui dentro | 15 | 1,6 | 6 | 0,0 | 2,5 |
| ou seja | 12 | 1,3 | 7 | 3,0 | 0,3 |
| IA / AI (sigla) | 11 | 1,2 | 6 | 1,8 | 0,8 |
| por exemplo | 11 | 1,2 | 6 | 0,3 | 1,7 |
| ó (apontando) | 9 | 1,0 | 6 | 1,5 | 0,7 |
| "Bom," abrindo frase | 8 | 0,9 | 6 | 1,5 | 0,5 |
| simplesmente | 7 | 0,7 | 7 | 0,6 | 0,8 |
| é só | 6 | 0,6 | 4 | 1,2 | 0,3 |
| deixa eu | 5 | 0,5 | 5 | 1,2 | 0,2 |
| fazendo um favor (à IA) | 5 | 0,5 | 4 | 0,0 | 0,8 |
| ok | 5 | 0,5 | 3 | 0,9 | 0,3 |
| inclusive | 5 | 0,5 | 4 | 0,3 | 0,7 |
| como eu disse | 4 | 0,4 | 4 | 1,2 | 0,0 |
| simples assim | 3 | 0,3 | 2 | 0,0 | 0,5 |
| tipo (marcador; fora "tipo de") | 1 | 0,1 | 1 | 0,0 | 0,2 |

"inteligência artificial" por extenso sai 63 vezes contra 11 da sigla (85% das menções). "aqui" dobra nos recentes (11,2 → 23,0 por mil), com "isso aqui" (0,6 → 4,1) e "aqui dentro" (0 → 2,5), porque ele narra o que aparece na metade de baixo da tela; "então" quase triplica (4,2 → 11,4 por mil) e vira o conector entre um passo e outro da demonstração.

### 4.5 Construção "não é X, é Y"

- **Na fala (26 vídeos)**: 22 ocorrências em 10 vídeos (2,4 por mil palavras). Forma exata: 4 ("não é X, é Y", "não é sobre X, é sobre Y", "não sou eu que X, é Y"), em TOP#6, TOP#9, RECENTE#8 e RECENTE#14. Variantes: 18 ("não X, mas Y", "não porque X, mas porque Y", "não só X, mas também Y", "não está em X… está em Y", "ninguém quer X, mas querem Y", "X, mas não Y").
- **Concentração**: 13 das 22 estão nos 2 manifestos (TOP#9: 8; TOP#6: 5). Nos 15 recentes são 4 (0,7 por mil palavras), em RECENTE#8, #11, #13 e #14.
- **Nas legendas (30)**: nenhuma na forma exata; 7 variantes em 6 legendas, todas dos recentes (RECENTE#1, #2 com 2, #5, #12, #13, #14): "não só X, mas Y", "deixa de X e começa a Y", "em vez de X, Y", "não precisa X, mas sim Y".

### 4.6 Palavras por minuto e perfil de cada vídeo com fala em pt

| vídeo | formato | motor | palavras | fala (s) | pal/min (fala) | pal/min (duração total) | frases | média pal/frase | mediana | "você(s)" | "a gente" | "né" | "então" | "aqui" | "?" | números |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TOP#2 | falando pra câmera (estúdio) + prints | large-v3-turbo | 273 | 66,4 | 247 | 236 | 14 | 20,1 | 17,0 | 4 | 1 | 1 | 1 | 6 | 3 | 6 |
| TOP#3 | selfie falando pra câmera | large-v3-turbo | 113 | 31,8 | 213 | 210 | 11 | 10,3 | 10,0 | 4 | 0 | 0 | 0 | 2 | 1 | 2 |
| TOP#4 | tela dividida (rosto + tela) | large-v3-turbo | 360 | 87,5 | 247 | 246 | 9 | 40,0 | 33,0 | 4 | 6 | 1 | 2 | 10 | 1 | 0 |
| TOP#5 | tela dividida (rosto + tela) | large-v3-turbo | 342 | 86,5 | 237 | 236 | 12 | 28,0 | 8,0 | 16 | 1 | 1 | 2 | 1 | 6 | 5 |
| TOP#6 | manifesto falando pra câmera (estúdio) | large-v3-turbo | 640 | 178,2 | 216 | 213 | 38 | 16,9 | 14,0 | 10 | 0 | 0 | 0 | 1 | 1 | 7 |
| TOP#7 | tela dividida (rosto + tela) | large-v3-turbo | 270 | 82,7 | 196 | 195 | 15 | 18,2 | 16,0 | 6 | 3 | 3 | 5 | 3 | 5 | 9 |
| TOP#9 | manifesto narrado sobre imagens | large-v3-turbo | 230 | 85,7 | 161 | 153 | 11 | 20,9 | 16,0 | 12 | 0 | 0 | 0 | 0 | 2 | 0 |
| TOP#11 | tela dividida (rosto + tela) | large-v3-turbo | 257 | 83,4 | 185 | 185 | 11 | 23,4 | 16,0 | 2 | 0 | 1 | 2 | 6 | 2 | 4 |
| TOP#12 | entrevista de rua | large-v3-turbo | 131 | 31,0 | 253 | 212 | 16 | 8,2 | 8,0 | 5 | 1 | 0 | 0 | 1 | 7 | 0 |
| TOP#14 | vlog narrado (série) | large-v3-turbo | 272 | 70,5 | 231 | 230 | 13 | 20,9 | 13,0 | 2 | 1 | 0 | 2 | 3 | 0 | 2 |
| TOP#15 | falando pra câmera (estúdio) | large-v3-turbo | 424 | 124,5 | 204 | 204 | 25 | 17,0 | 13,0 | 7 | 13 | 0 | 0 | 4 | 5 | 2 |
| RECENTE#1 | falando pra câmera (estúdio) | small | 476 | 113,2 | 252 | 232 | 22 | 21,5 | 16,5 | 13 | 2 | 2 | 7 | 2 | 4 | 3 |
| RECENTE#2 | tela dividida (rosto + tela) | small | 243 | 54,8 | 266 | 225 | 7 | 34,4 | 36,0 | 9 | 3 | 0 | 3 | 7 | 0 | 0 |
| RECENTE#3 | tela dividida (rosto + tela) | small | 362 | 90,9 | 239 | 215 | 19 | 18,7 | 21,0 | 15 | 3 | 1 | 4 | 3 | 1 | 5 |
| RECENTE#4 | tela dividida (rosto + tela) | small | 471 | 106,1 | 266 | 244 | 29 | 16,1 | 13,0 | 14 | 3 | 2 | 8 | 21 | 3 | 0 |
| RECENTE#5 | tela dividida (rosto + tela) | large-v3-turbo | 325 | 84,1 | 232 | 207 | 7 | 46,0 | 24,0 | 0 | 3 | 1 | 5 | 9 | 1 | 5 |
| RECENTE#6 | falando pra câmera (estúdio) | large-v3-turbo | 204 | 51,6 | 237 | 199 | 18 | 11,3 | 7,0 | 4 | 2 | 1 | 2 | 2 | 8 | 12 |
| RECENTE#7 | tela dividida (rosto + tela) | large-v3-turbo | 240 | 61,8 | 233 | 200 | 15 | 16,0 | 16,0 | 19 | 0 | 0 | 3 | 1 | 2 | 0 |
| RECENTE#8 | tela dividida (rosto + tela) | large-v3-turbo | 425 | 107,3 | 238 | 217 | 18 | 23,6 | 20,0 | 6 | 0 | 1 | 5 | 8 | 2 | 9 |
| RECENTE#9 | tela dividida (rosto + tela) | large-v3-turbo | 490 | 127,3 | 231 | 214 | 24 | 20,3 | 14,0 | 2 | 0 | 3 | 7 | 13 | 4 | 8 |
| RECENTE#10 | tela dividida (rosto + tela) | large-v3-turbo | 316 | 75,8 | 250 | 221 | 26 | 12,1 | 10,0 | 4 | 1 | 2 | 4 | 8 | 7 | 0 |
| RECENTE#11 | tela dividida (rosto + tela) | large-v3-turbo | 768 | 186,7 | 247 | 234 | 52 | 14,8 | 10,0 | 10 | 2 | 1 | 8 | 36 | 13 | 3 |
| RECENTE#12 | tela dividida (rosto + tela) | large-v3-turbo | 647 | 148,1 | 262 | 249 | 35 | 18,5 | 13,0 | 22 | 7 | 3 | 6 | 4 | 8 | 9 |
| RECENTE#13 | tela dividida (rosto + tela) | large-v3-turbo | 274 | 68,7 | 239 | 209 | 8 | 34,2 | 17,0 | 8 | 1 | 0 | 3 | 4 | 0 | 7 |
| RECENTE#14 | tela dividida (rosto + tela) | large-v3-turbo | 455 | 104,0 | 262 | 240 | 11 | 41,4 | 24,0 | 10 | 0 | 2 | 3 | 13 | 5 | 5 |
| RECENTE#15 | tela dividida (rosto + tela) | large-v3-turbo | 345 | 88,8 | 233 | 178 | 16 | 21,6 | 17,0 | 2 | 7 | 5 | 1 | 8 | 11 | 4 |

Mediana TOP (11): 216 pal/min (faixa 161–253), 272 palavras, 83,5 s. Recentes (15): 239 pal/min (faixa 231–266), 362 palavras, 114,0 s. Sobre a duração total: TOP 212 e recentes 217 pal/min (a cartela final muda de ~9,5 s puxa os recentes para baixo). Perguntas: 102 sinais de interrogação em 9.353 palavras (1,09 por 100 palavras; TOP 33, recentes 69). Números: 107 no total, em 19 dos 26 vídeos; mediana 2 por vídeo no TOP e 5 nos recentes. Só 20 dos 107 são dinheiro (R$, reais, dólares, faturamento), em 7 vídeos (TOP#2, TOP#6, RECENTE#3, #12, #13, #14, #15); os outros 87 são tempo, quantidade, porcentagem, data, versão de modelo ou código.

## 5. Legenda (caption) dos 30

| código | grupo | caracteres | linhas | emojis | hashtags | CTA na legenda | "?" | menção @ |
|---|---|---|---|---|---|---|---|---|
| DF8fxOLPsqu | TOP#1 | 362 | 4 | 0 | 0 | — | 2 | — |
| CrYyOTttWUd | TOP#2 | 131 | 2 | 0 | 4 | — | 0 | — |
| CpL6jsQLpmx | TOP#3 | 75 | 1 | 0 | 0 | comenta PALAVRA ("Conteúdo") | 0 | — |
| DZ8fXciiaig | TOP#4 | 454 | 4 | 0 | 0 | comenta PALAVRA ("CAIA") | 1 | — |
| DZdlhdYiRQQ | TOP#5 | 300 | 4 | 0 | 3 | comenta PALAVRA ("1306") | 1 | — |
| DQcJ5RIDrNl | TOP#6 | 84 | 1 | 0 | 0 | comenta PALAVRA ("LTV") | 0 | — |
| DXc3jcXgoM9 | TOP#7 | 272 | 2 | 1 | 0 | comenta PALAVRA ("Claude") | 1 | — |
| C9LgYAFvCbl | TOP#8 | 518 | 3 | 0 | 0 | direct | 1 | @ddiasmatt, @appchatfunnel |
| C_YaWJOu0Az | TOP#9 | 259 | 4 | 1 | 1 | comenta PALAVRA ("#desperta") | 0 | — |
| CewUQzBpsE_ | TOP#10 | 122 | 3 | 2 | 0 | — | 0 | — |
| DWpV8sRgumA | TOP#11 | 496 | 4 | 0 | 0 | comenta PALAVRA ("Agência") | 2 | — |
| C-5h7UOOlKM | TOP#12 | 371 | 4 | 4 | 0 | comenta PALAVRA ("LTV") | 3 | — |
| DAiwAizuTUg | TOP#13 | 1 | 1 | 1 | 0 | — | 0 | — |
| DMdKmfEMdTl | TOP#14 | 132 | 2 | 0 | 8 | — | 0 | — |
| DIxHPh1tKGi | TOP#15 | 52 | 2 | 0 | 1 | — | 0 | — |
| Dd2OUbvRGSM | RECENTE#1 | 848 | 9 | 0 | 0 | link na bio | 1 | — |
| DdxK3HJx9ss | RECENTE#2 | 476 | 5 | 0 | 0 | link na bio | 1 | — |
| Ddr6ek-RpDB | RECENTE#3 | 595 | 5 | 0 | 0 | link na bio | 2 | — |
| Ddmttb6RpJf | RECENTE#4 | 362 | 4 | 0 | 0 | link na bio | 2 | — |
| DdfGIizCcTy | RECENTE#5 | 654 | 6 | 0 | 0 | link na bio | 1 | — |
| Ddcddm_CZO4 | RECENTE#6 | 53 | 1 | 0 | 0 | comenta opinião ("me conta") | 0 | — |
| DdZ5-xaiEPx | RECENTE#7 | 514 | 8 | 0 | 0 | link na bio | 1 | — |
| DdXUmI0C0QG | RECENTE#8 | 469 | 6 | 0 | 0 | link na bio | 1 | — |
| DdUwYbhiIK3 | RECENTE#9 | 501 | 5 | 0 | 0 | link na bio | 1 | — |
| DdSKOZmSeBQ | RECENTE#10 | 424 | 5 | 0 | 0 | comenta PALAVRA ("LOOP") | 0 | — |
| DdKgaOaCVjD | RECENTE#11 | 406 | 4 | 0 | 0 | link na bio | 2 | — |
| Dc7DZ2MC6dI | RECENTE#12 | 792 | 6 | 0 | 0 | link na bio | 1 | — |
| Dc1974Li3eN | RECENTE#13 | 555 | 5 | 0 | 0 | link na bio | 0 | — |
| DczW37aClod | RECENTE#14 | 515 | 4 | 0 | 0 | link na bio | 1 | — |
| DcuKBXdi9s7 | RECENTE#15 | 547 | 5 | 0 | 0 | link na bio | 2 | — |

| recorte | caracteres (média / mediana) | linhas (média / mediana) | emojis por legenda (média) | legendas com emoji | legendas com hashtag | hashtags (total) | legendas com "?" | "?" (total) | legendas com @ |
|---|---|---|---|---|---|---|---|---|---|
| TOP 15 | 242 / 259 | 2,7 / 3,0 | 0,60 | 5 | 5 | 17 | 7 | 11 | 1 |
| RECENTES 15 | 514 / 514 | 5,2 / 5,0 | 0,00 | 0 | 0 | 0 | 12 | 16 | 0 |
| 30 | 378 / 415 | 4,0 / 4,0 | 0,30 | 5 | 5 | 17 | 19 | 27 | 1 |

**Tipos de CTA (legendas com o tipo)**

| tipo | TOP 15 | RECENTES 15 | 30 |
|---|---|---|---|
| comenta PALAVRA-chave para receber algo | 8 | 1 | 9 |
| comenta opinião ("me conta") | 0 | 1 | 1 |
| link na bio | 0 | 13 | 13 |
| segue | 0 | 0 | 0 |
| salva | 0 | 0 | 0 |
| compartilha / manda pra alguém | 0 | 0 | 0 |
| direct | 1 | 0 | 1 |
| **qualquer CTA explícito** | 9 | 15 | 24 |

- **Estrutura fixa nos recentes**: 13 de 15 legendas terminam com uma pergunta "Quer [resultado]?" (ou "Se você quer…") + "Clica no link da bio". São 7 perguntas diferentes para 13 legendas; a mais usada (a de "automatizar seu trabalho") aparece em 4. Os 15 recentes fecham com uma cartela final muda (pergunta do mesmo tipo + "Clica no link" ou, em RECENTE#10, "Comenta aqui") de 7,8 a 10,5 s (mediana 9,5 s), que começa entre 85% e 96% do vídeo, depois que ele para de falar; em RECENTE#14 e #15 a cartela diz "link nos comentários" enquanto a legenda diz "link da bio".
- **Comentários por tipo de CTA**: os 11 vídeos que pedem "comenta PALAVRA" (na legenda, na fala ou na tela) têm mediana de 0,265% comentários/views; as 13 legendas com "link na bio" somam 5 comentários (mediana 0; 8 com zero). Nos recentes, os 2 que pedem comentário (RECENTE#10 "LOOP" e RECENTE#6 "me conta") têm 26 dos 31 comentários do grupo (84%).
- **Palavras-chave do TOP**: Conteúdo, CAIA, 1306, LTV (2x), Claude, #desperta e Agência na legenda; "ativo" e "imersão" só faladas; "LTV" pedida por direct na cartela de TOP#2. As 3 maiores taxas de comentário dos 30 são de vídeos com palavra-chave: TOP#3 (1,761%, pedida em fala aos 56% do vídeo, em formato de desafio), TOP#11 (1,461%) e RECENTE#10 (1,420%).
- **Emojis e hashtags**: 9 emojis em 5 legendas e 17 hashtags em 5 legendas, todas do TOP (2022–2025). Nos 15 recentes: 0 emoji, 0 hashtag, 0 menção.
- **Tamanho**: a legenda dobrou. Recentes: mediana 514 caracteres e 5 linhas (um mini-artigo que repete a tese do vídeo); TOP: mediana 259 caracteres e 3 linhas; 4 legendas do TOP têm até 84 caracteres.

## 6. Correlações de Spearman entre views e cada variável

ρ de Spearman (empates com posto médio) e p bicaudal do scipy. **Com n = 30 (15 por grupo) isto é indício, não prova**: são 32 testes válidos, e a p < 0,05 espera-se cerca de 1,6 "significância" só por acaso. Nos 30, quase toda variável separa o TOP (2022–2026, os mais vistos da história) dos recentes (o último mês), então mede época e formato juntos.

| variável | 30 (n; ρ; p) | dentro do TOP (n; ρ; p) | dentro dos recentes (n; ρ; p) |
|---|---|---|---|
| duração (s) | **30; −0,41; 0,024** | 15; −0,18; 0,516 | 15; +0,08; 0,781 |
| palavras/min (fala em pt) | **26; −0,50; 0,009** | 11; +0,28; 0,401 | 15; −0,40; 0,136 |
| cortes/min bruto | 30; −0,06; 0,768 | **15; −0,74; 0,002** | 15; 0,00; 0,990 |
| cortes/min agrupado | 30; −0,08; 0,684 | **15; −0,69; 0,005** | 15; −0,12; 0,666 |
| tamanho da legenda (caracteres) | **30; −0,58; < 0,001** | 15; +0,21; 0,459 | 15; −0,26; 0,355 |
| texto no 1º frame (0/1) | 30; −0,12; 0,516 | 15; +0,32; 0,248 | 15; — |
| manchete no 1º frame (0/1) | **30; −0,69; < 0,001** | 15; +0,41; 0,131 | 15; — |
| fala dele em pt (0/1) | 30; −0,34; 0,066 | 15; 0,00; 1,000 | 15; — |
| pedido de comentário, qualquer canal (0/1) | **30; +0,49; 0,006** | 15; −0,20; 0,483 | 15; +0,36; 0,183 |
| pedido de comentário na legenda (0/1) | **30; +0,49; 0,006** | 15; +0,22; 0,438 | 15; +0,36; 0,183 |
| "link na bio" na legenda (0/1) | **30; −0,82; < 0,001** | 15; — | 15; −0,36; 0,183 |
| tela dividida (0/1) | **30; −0,48; 0,008** | 15; +0,17; 0,534 | 15; +0,05; 0,872 |

Em negrito: p < 0,05. "—": a variável não varia no recorte (ex.: todos os 15 recentes têm fala, texto e manchete no 1º frame).

**Mediana de views com × sem**

| variável | 30: com (n; mediana) | 30: sem (n; mediana) | TOP: com × sem | recentes: com × sem |
|---|---|---|---|---|
| texto no 1º frame (0/1) | 28; 3.230,5 | 2; 19.332,0 | 13: 41.766,0 × 2: 19.332,0 | 15: 844,0 × 0: — |
| manchete no 1º frame (0/1) | 17; 868,0 | 13; 28.389,0 | 2: 9.183.922,0 × 13: 28.389,0 | 15: 844,0 × 0: — |
| fala dele em pt (0/1) | 26; 2.521,0 | 4; 27.037,5 | 11: 41.766,0 × 4: 27.037,5 | 15: 844,0 × 0: — |
| pedido de comentário, qualquer canal (0/1) | 12; 23.775,0 | 18; 1.160,0 | 10: 35.077,5 × 5: 32.176,0 | 2: 2.185,0 × 13: 783,0 |
| "link na bio" na legenda (0/1) | 13; 783,0 | 17; 28.389,0 | 0: — × 15: 32.176,0 | 13: 783,0 × 2: 2.185,0 |
| tela dividida (0/1) | 17; 1.197,0 | 13; 21.899,0 | 4: 42.711,0 × 11: 28.389,0 | 13: 844,0 × 2: 1.799,0 |

Leitura:

- **Nos 30**, o pacote de set/2026 inteiro aparece como negativo: "link na bio" na legenda (ρ −0,82), manchete no 1º frame (−0,69), legenda longa (−0,58), fala mais rápida (−0,50), tela dividida (−0,48) e duração (−0,41). Pedir comentário é positivo (+0,49). São traços do formato do último mês, que coincide com as menores views do perfil; não dá para separar o efeito de cada um.
- **Dentro do TOP**, o único sinal forte é **cortes/min: ρ −0,74 (p 0,002)**. Os 5 mais vistos têm de 0 a 5,2 cortes/min (TOP#1 a #5), e os 4 menos vistos do TOP têm de 13,5 a 80,1 (TOP#12 a #15). Ter fala dele (ρ 0,00) e pedir comentário (−0,20) não separam os vídeos do TOP.
- **Dentro dos recentes** nada chega a p < 0,05 contra views. Palavras/min: ρ −0,40 (p 0,14): os 2 mais vistos falam a 231 e 237 pal/min; os 2 mais rápidos (266) tiveram 551 e 868 views.
- **Contra comentários/views** (não views), pedir comentário tem ρ +0,62 nos 30 (p < 0,001) e +0,64 dentro dos recentes (p 0,010); "link na bio" tem −0,64 dentro dos recentes (p 0,010). É o resultado mais consistente da ficha: o CTA escolhido decide se o vídeo recebe comentário.

## 7. Os 7 achados quantitativos para quem vai roteirizar

1. **O alcance caiu enquanto a frequência subiu de 0,2 para 3,5 reels por semana.** Mediana de 1.586,5 views (3,4% dos 46.936 seguidores), e um único meme visual de 8,8 s (TOP#1) tem 95,9% de todas as views dos 92 reels. Os 50 mais novos (20/06 a 28/09/2026) têm mediana de 827 (0,52x), a 3,5 reels por semana; os 41 anteriores (jun/2022 a jun/2026), 7.382 (4,65x), a 0,2 por semana. Em blocos de 10, a mediana desce de 13.483 (2022–2024) para 665–856 (ago–set/2026). 31 dos 50 mais novos não têm nenhum comentário, contra 5 dos 41 anteriores. Só 1 dos 15 mais vistos da história está entre os 50 mais novos.
2. **O que deu alcance em 2026 e o que não deu usam o mesmo formato. Mudam o tamanho e o CTA.** Os 3 orgânicos de 2026 no TOP (TOP#4 62.690, TOP#5 43.656, TOP#11 19.161) são tela dividida (rosto em cima, tela embaixo), com 83–88 s, 257–360 palavras e "comenta PALAVRA" na legenda (CAIA, 1306, Agência). Os 15 recentes (mediana de 844 views, 0,53x) têm 13 em tela dividida, mediana de 114 s e 362 palavras, 9 acima de 100 s e 13 com "link na bio". Para quem só grava falando para a câmera: os 2 vídeos com fala dele mais vistos de todos (TOP#2, 128.697, e TOP#3, 105.303, ambos de 2023) são falando para a câmera em tela cheia, com 69 e 32 s.
3. **O gancho começa a falar no segundo 0, sem saudação, e a manchete de tela carrega a promessa.** 25 dos 26 vídeos com fala começam em 0,0 s, e nenhum cumprimenta. No TOP, a 1ª frase é "eu fiz/eu criei" em 4 de 11, pergunta em 3 e notícia de impacto em 1. Em 8 dos 15 do TOP o texto do 1º frame é só a legenda da fala, sem manchete. Nos recentes, 15 de 15 abrem com manchete em caixa (8–12 palavras, mediana 10; "isso" em 9, imperativo em 7), e 5 de 15 começam no meio de um raciocínio, como corte de vídeo longo. Os 2 recentes mais vistos (3.288 e 3.173, contra mediana de 783 dos outros 13) são os únicos com número na manchete: «3 prompts foram suficientes…» e «…ESCOLHER 17? FAÇA ESSE TESTE». Com n = 2, é indício.
4. **O ritmo vem da fala contínua e rápida, com pouca edição.** Mediana de 239 pal/min nos recentes (231–266) e 216 no TOP (161–253). A frase mediana tem 13,5 palavras (7 a 10 por pausa de respiração). Os recentes têm 1,0 a 4,7 cortes/min, fora RECENTE#6 com 22,4. Dentro do TOP, menos cortes andam com mais views (ρ −0,74; p 0,002): os 5 mais vistos têm 0–5,2 cortes/min, e os 4 menos vistos, 13,5–80,1. Há 1,09 pergunta por 100 palavras. 19 dos 26 vídeos citam números (107 no total; mediana de 5 por vídeo nos recentes), e só 20 dos 107 são dinheiro. Dá para imitar essa densidade com tempo, quantidade, porcentagem e versão de ferramenta.
5. **Na linguagem, "eu" mostra, "você" executa e "a gente" inclui.** "eu": 27,4 por mil palavras, e 36,1% das frases estão em 1ª pessoa do singular. "você(s)": 22,5 por mil, em 26,1% das frases. "a gente": 60 vezes, em 18 de 26 vídeos. "tu" aparece 2 vezes e "cê", nenhuma. Ele diz "inteligência artificial" por extenso 63 vezes, contra 11 da sigla "IA". Marcadores: "né?" no fim da frase 30 vezes (17 vídeos); "então" 83 (11,4 por mil nos recentes, 4,2 no TOP); "aqui" 176 (aponta para a tela); "tá" 26. Como vocativo, "mano" e "galera" aparecem 0 vezes, "gente" 1 e "cara" 1. Expressões que voltam entre vídeos: "ou seja" (7), "todo mundo" (7), "você pode" (7, só nos recentes), "por exemplo" (6), "eu quero" (6), "deixa eu" (5) e "fazendo um favor" (4, ao ditar um pedido para a IA).
6. **"Não é X, é Y" é recurso de manifesto e raro no dia a dia.** Na fala há 22 ocorrências (4 exatas, 18 variantes) em 10 de 26 vídeos, mas 13 delas estão nos 2 manifestos (TOP#9: 8; TOP#6: 5). Nos 15 recentes são 4 (0,7 por mil palavras). Nas legendas há 0 exatas e 7 variantes, todas nos recentes ("não só X, mas Y", "em vez de X", "deixa de X e começa a Y").
7. **O CTA decide o comentário: "comenta PALAVRA" gera comentário e "link na bio" zera.** Os 11 vídeos com "comenta PALAVRA" (na legenda, na fala ou na tela) têm mediana de 0,265% de comentários/views. As 13 legendas com "link na bio" somam 5 comentários, e 8 delas têm zero. Nos recentes, os 2 que pedem comentário têm 26 dos 31 comentários (84%); dentro desse grupo, pedir comentário tem ρ +0,64 com comentários/views (p 0,010). No TOP, 10 de 15 pedem comentário, e o CTA falado aparece em 5 vídeos, entre 52% e 97% da duração. Os recentes nunca falam o CTA e fecham com uma cartela muda de ~9,5 s (a partir de 85–96% do vídeo). As 3 maiores taxas de comentário dos 30 (1,761%, 1,461% e 1,420%) são de vídeos com palavra-chave.
