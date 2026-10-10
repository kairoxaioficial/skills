# Ficha quantitativa — @oalanicolas (Alan Nicolas)

Fundador e CEO da Academia Lendária · 261.650 seguidores · 1.843 posts · **1.032 reels** (lista completa) · coleta em 29/09/2026 com login. Fontes: `users/oalanicolas.json` (todos os reels), `dossie/oalanicolas.md`, `videos/oalanicolas/*.tr.json | *.ocr.json | *.vis.json`. Números calculados em Python a partir dos brutos; nenhum trecho de fala ou legenda com mais de 5 palavras foi copiado (manchetes de tela com até 12 palavras aparecem entre «»).

## 0. Como os números foram medidos

- **views** = `play_count`; os 4 IGTV antigos sem `play_count` usam `view_count`. Views, likes e comentários dos 30 vêm da mesma lista (`items`), igual ao dossiê.
- **Percentis**: interpolação linear sobre os 1.032 reels. O dossiê usa posto mais próximo sobre 1.028; a mediana é a mesma (14.043,5), p25/p75/p90 diferem até 1,6%. **Múltiplo** = views ÷ 14.043,5.
- **Tendência**: ordem da lista do Instagram (mais novo → mais velho) sem os 2 fixados (`DDkdUxoJTFo`, `DJxbN2lgd-j`); datas dos blocos tiradas do ID do post (erro de minutos).
- **Palavras/min** = palavras ÷ (fim do último trecho − início do 1º) × 60, como no dossiê; só fala em pt com flag ok (12 vídeos). Também mostro sobre a duração total (seção 4.6).
- **Cortes/min**: bruto = cortes do `vis.json` ÷ duração. Agrupado = cortes a menos de 1 s um do outro contam como 1 (zoom ou flash geram 2 a 4 detecções seguidas).
- **Tem fala**: flag ok do Whisper. RECENTE#4 foi marcado sem fala: a "letra" em inglês é alucinação sobre a trilha instrumental.
- **Números citados**: dígitos e numerais por extenso na fala, incluindo versões de modelo e códigos; sem "um/uma" e sem a expressão "do zero". **Perguntas**: quantidade de "?" na transcrição (o faster-whisper-small pontua menos). **CTA falado**: conferido à mão; o segundo é o início do trecho em que o verbo aparece.
- **Formato**: classificado por OCR, legenda e transcrição, conferido em 9 folhas de contato (TOP#3, 6, 9, 13, 14, 15, RECENTE#3, 4, 10) e 5 frames de gancho (TOP#7, 8, 10, 11, 12).
- **Limites**: nos cortes de podcast a transcrição mistura a voz do entrevistador (ex.: "Exato"); o faster-whisper-small (TOP#11, 12, 14, 15 e todos os recentes) erra nomes e às vezes a 1ª frase (TOP#12: o OCR mostra a frase certa). OCR a cada 2 s: uma cartela pode ter entrado até 2 s antes do segundo indicado.

## 1. Distribuição de views (1.032 reels) e tendência

| p10 | p25 | p50 (mediana) | p75 | p90 | p99 | máximo | média |
|---|---|---|---|---|---|---|---|
| 4.328 | 7.615 | 14.043,5 | 36.080 | 118.580 | 1.271.717 | 3.641.476 | 71.142 |

- Mediana = 5,4% dos seguidores. Média 5,1x a mediana: cauda longa. ≥ 50 mil: 203 reels (19,7%); ≥ 100 mil: 116 (11,2%); ≥ 500 mil: 30; ≥ 1 milhão: 16 (1,6%).
- Mediana de likes/views de todos os reels: 1,97%; comentários/views: 0,080%.
- Prováveis anúncios (likes/views < 0,3%): 88 de 1.032 (8,5%); 2 no TOP 15, 10 no TOP 50, 22 no TOP 100. 62 dos 88 caem entre ago/2024 e mai/2025 (blocos 9–13); só o bloco 13 (ago–set/2024) tem 20 de 50.

**Mediana por blocos de 50 reels (mais novo → mais velho, sem fixados)**

| bloco | reels | período (mais novo → mais velho) | dias | reels/semana | mediana | x mediana geral | p90 | máximo | prováveis anúncios |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 50 | 2026-09-27 → 2026-08-24 | 35 | 10,0 | 3.759 | 0,27x | 46.813 | 430.712 | 0 |
| 2 | 50 | 2026-08-22 → 2026-06-25 | 59 | 5,9 | 4.972 | 0,35x | 42.068 | 361.360 | 2 |
| 3 | 50 | 2026-06-21 → 2026-04-15 | 68 | 5,1 | 9.531 | 0,68x | 70.345 | 129.781 | 2 |
| 4 | 50 | 2026-04-14 → 2026-02-09 | 65 | 5,4 | 16.874 | 1,20x | 156.228 | 504.849 | 9 |
| 5 | 50 | 2026-02-06 → 2025-11-29 | 70 | 5,0 | 6.116 | 0,44x | 50.506 | 768.330 | 0 |
| 6 | 50 | 2025-11-28 → 2025-10-15 | 45 | 7,8 | 8.222 | 0,59x | 78.281 | 798.763 | 4 |
| 7 | 50 | 2025-10-14 → 2025-07-27 | 80 | 4,4 | 15.503 | 1,10x | 301.987 | 724.202 | 3 |
| 8 | 50 | 2025-07-26 → 2025-05-08 | 80 | 4,4 | 17.349 | 1,24x | 94.701 | 476.994 | 0 |
| 9 | 50 | 2025-05-07 → 2025-02-15 | 82 | 4,3 | 28.426 | 2,02x | 391.480 | 3.641.476 | 11 |
| 10 | 50 | 2025-02-15 → 2024-12-14 | 64 | 5,5 | 24.630 | 1,75x | 146.865 | 2.852.254 | 10 |
| 11 | 50 | 2024-12-13 → 2024-11-02 | 42 | 8,3 | 18.513 | 1,32x | 100.816 | 535.711 | 11 |
| 12 | 50 | 2024-11-01 → 2024-09-21 | 42 | 8,3 | 8.478 | 0,60x | 27.284 | 1.535.479 | 10 |
| 13 | 50 | 2024-09-20 → 2024-08-06 | 46 | 7,6 | 12.274 | 0,87x | 789.879 | 1.616.031 | 20 |
| 14 | 50 | 2024-08-03 → 2024-06-28 | 37 | 9,5 | 16.650 | 1,19x | 343.293 | 1.624.738 | 1 |
| 15 | 50 | 2024-06-27 → 2024-04-29 | 60 | 5,8 | 15.618 | 1,11x | 35.491 | 56.433 | 0 |
| 16 | 50 | 2024-04-26 → 2024-02-23 | 64 | 5,5 | 42.875 | 3,05x | 172.873 | 1.244.365 | 5 |
| 17 | 50 | 2024-02-23 → 2023-10-24 | 123 | 2,8 | 16.969 | 1,21x | 53.112 | 1.834.990 | 0 |
| 18 | 50 | 2023-10-23 → 2023-09-05 | 49 | 7,1 | 11.926 | 0,85x | 38.875 | 80.836 | 0 |
| 19 | 50 | 2023-09-03 → 2023-07-08 | 58 | 6,0 | 14.173 | 1,01x | 41.376 | 182.184 | 0 |
| 20 | 50 | 2023-07-07 → 2023-05-17 | 52 | 6,7 | 14.145 | 1,01x | 67.213 | 132.047 | 0 |
| 21 | 30 | 2023-05-17 → 2021-06-17 | 700 | 0,3 | 8.682 | 0,62x | 23.604 | 212.716 | 0 |

Leitura: dois picos de mediana (bloco 16, fev–abr/2024: 42.875; blocos 9–10, dez/2024–mai/2025: 28.426 e 24.630) e queda contínua desde abr/2026. O bloco mais novo (24/08 a 27/09/2026) tem a **menor mediana dos 21 blocos (3.759; 0,27x)** e o **maior ritmo de postagem (10 reels/semana)**; os blocos de pico saíram a 4,3–5,5 por semana.

## 2. Os 30 selecionados

| código | grupo | data | dur (s) | views | x mediana | likes/views | coment./views | pal/min | cortes/min bruto (agrupado) | tem fala? | idioma | nº palavras | nº perguntas | nº números | CTA falado (s) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DGohKSZOTWN | TOP#1 | 2025-02-28 | 69,8 | 3.641.476 | 259,3x | 1,79% | 0,022% | — | 0,0 (0,0) | sim | en | 65 | 2 | 0 | — |
| DG8hcKiOzDn | TOP#2 | 2025-03-08 | 19,0 | 2.892.711 | 206,0x | 0,68% | 0,003% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |
| DE2NREBONGY | TOP#3 | 2025-01-15 | 13,2 | 2.852.254 | 203,1x | 1,32% | 0,000% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |
| DGfjs33uvum | TOP#4 (anúncio?) | 2025-02-25 | 21,3 | 2.748.072 | 195,7x | 0,08% | 0,006% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |
| DFtjq1KNqB2 | TOP#5 | 2025-02-05 | 40,0 | 1.882.866 | 134,1x | 0,58% | 0,016% | — | 1,5 (1,5) | não | — | 0 | 0 | 0 | — |
| C3Yma6QiKyt | TOP#6 | 2024-02-15 | 49,6 | 1.834.990 | 130,7x | 1,38% | 0,113% | 295 | 9,7 (3,6) | sim | pt | 224 | 2 | 1 | — |
| C9LZM7kxbLT | TOP#7 | 2024-07-08 | 86,5 | 1.624.738 | 115,7x | 0,72% | 0,041% | 191 | 6,9 (4,9) | sim | pt | 259 | 2 | 3 | — |
| C-5jOGDu5tL | TOP#8 | 2024-08-20 | 72,8 | 1.616.031 | 115,1x | 0,81% | 0,016% | 244 | 9,1 (6,6) | sim | pt | 282 | 7 | 4 | — |
| C9I4T5IPENM | TOP#9 | 2024-07-07 | 77,2 | 1.600.912 | 114,0x | 0,73% | 0,020% | 211 | 3,1 (1,6) | sim | pt | 255 | 0 | 3 | — |
| DATfyhdO3te | TOP#10 | 2024-09-24 | 62,6 | 1.535.479 | 109,3x | 0,54% | 0,003% | 231 | 14,4 (7,7) | sim | pt | 233 | 1 | 5 | — |
| C9YKgiMPVnS | TOP#11 | 2024-07-13 | 55,2 | 1.284.005 | 91,4x | 0,67% | 0,004% | 218 | 3,3 (1,1) | sim | pt | 183 | 2 | 1 | — |
| C3vQkI-C-z7 | TOP#12 | 2024-02-24 | 84,6 | 1.244.365 | 88,6x | 1,97% | 0,352% | 238 | 3,5 (1,4) | sim | pt | 331 | 1 | 4 | 76,4 (90% do vídeo) |
| C_Y3-f0PG8T | TOP#13 (anúncio?) | 2024-09-01 | 52,7 | 1.209.509 | 86,1x | 0,21% | 0,002% | — | 17,1 (17,1) | não | — | 0 | 0 | 0 | — |
| C93E6wLvbju | TOP#14 | 2024-07-25 | 90,0 | 1.178.648 | 83,9x | 0,40% | 0,039% | 225 | 0,0 (0,0) | sim | pt | 328 | 7 | 1 | — |
| C_XCYhDtjeA | TOP#15 | 2024-09-01 | 43,6 | 1.164.167 | 82,9x | 0,46% | 0,009% | 176 | 1,4 (1,4) | sim | pt | 113 | 0 | 0 | — |
| Ddywg4_ivND | RECENTE#1 | 2026-09-27 | 46,3 | 27.831 | 2,0x | 2,26% | 0,122% | — | 1,3 (1,3) | sim | en | 31 | 3 | 0 | — |
| DdtmTcaiR7t | RECENTE#2 | 2026-09-25 | 11,3 | 430.712 | 30,7x | 4,57% | 0,278% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |
| DdmigcfKavn | RECENTE#3 | 2026-09-22 | 68,3 | 14.457 | 1,0x | 3,53% | 0,235% | 164 | 0,0 (0,0) | sim | pt | 186 | 0 | 10 | 64,8 (95% do vídeo) |
| Ddje6-ECHig | RECENTE#4 | 2026-09-21 | 16,1 | 42.262 | 3,0x | 1,40% | 0,083% | — | 26,1 (26,1) | não* | — | 0 | 0 | 0 | — |
| DdjMec3Ct4x | RECENTE#5 | 2026-09-21 | 8,5 | 3.656 | 0,3x | 0,71% | 0,027% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |
| DdhgFU4hRIP | RECENTE#6 | 2026-09-20 | 32,1 | 79.024 | 5,6x | 1,54% | 0,080% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |
| Ddgbeb1BHj5 | RECENTE#7 | 2026-09-20 | 7,0 | 5.086 | 0,4x | 0,87% | 0,000% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |
| Ddd38gaT51R | RECENTE#8 | 2026-09-19 | 7,0 | 1.771 | 0,1x | 1,41% | 0,000% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |
| DdcdXIrpkXT | RECENTE#9 | 2026-09-18 | 32,6 | 3.305 | 0,2x | 1,48% | 0,030% | 187 | 3,7 (3,7) | sim | pt | 93 | 0 | 0 | — |
| DdcJA40pEYF | RECENTE#10 | 2026-09-18 | 79,2 | 58.567 | 4,2x | 3,38% | 0,142% | 187 | 1,5 (1,5) | sim | pt | 244 | 1 | 5 | 68,7 (87% do vídeo) |
| Ddbdb1CqTYk | RECENTE#11 | 2026-09-18 | 8,5 | 2.848 | 0,2x | 0,42% | 0,000% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |
| DdbRy96BUyo | RECENTE#12 | 2026-09-18 | 7,0 | 2.643 | 0,2x | 0,95% | 0,038% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |
| DdYtAfAu9fO | RECENTE#13 | 2026-09-17 | 6,3 | 1.469 | 0,1x | 0,82% | 0,000% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |
| DdWHFCITfAq | RECENTE#14 | 2026-09-16 | 11,4 | 2.169 | 0,2x | 0,92% | 0,000% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |
| DdTjfRXuum_ | RECENTE#15 | 2026-09-15 | 7,3 | 2.445 | 0,2x | 0,98% | 0,041% | — | 0,0 (0,0) | não | — | 0 | 0 | 0 | — |

\* RECENTE#4: a transcrição achou 19 palavras em inglês sobre a trilha instrumental do Exterminador; é alucinação. TOP#1 e RECENTE#1 têm fala em inglês de terceiros (clipes legendados).

| grupo | mediana views | mediana x | mediana dur (s) | mediana likes/views | mediana coment./views | com fala dele em pt | prováveis anúncios |
|---|---|---|---|---|---|---|---|
| TOP 15 | 1.616.031 | 115,1x | 55,2 | 0,68% | 0,016% | 9 | 2 |
| RECENTES 15 | 3.656 | 0,3x | 11,3 | 1,40% | 0,038% | 3 | 0 |

**Views por formato (nos 30)**

| formato | grupo | n | mediana views | mínimo | máximo |
|---|---|---|---|---|---|
| corte de podcast (estúdio) | TOP | 7 | 1.600.912 | 1.244.365 | 1.834.990 |
| conversa em tela dividida | TOP | 2 | 1.171.408 | 1.164.167 | 1.178.648 |
| clipe de terceiros (curadoria) | TOP | 4 | 2.872.483 | 1.882.866 | 3.641.476 |
| clipe de terceiros (curadoria) | RECENTE | 4 | 60.643 | 27.831 | 430.712 |
| provável anúncio | TOP | 2 | 1.978.791 | 1.209.509 | 2.748.072 |
| selfie falando pra câmera | RECENTE | 2 | 36.512 | 14.457 | 58.567 |
| narração sobre imagens | RECENTE | 1 | 3.305 | 3.305 | 3.305 |
| texto na tela + música | RECENTE | 8 | 2.544 | 1.469 | 5.086 |

Os 9 do TOP com fala dele em pt são todos cortes de conversa de 2024 (7 de podcast, com microfone no quadro e olhar para o entrevistador; 2 em tela dividida). Nenhum vídeo do TOP é monólogo olhando para a câmera. Selfie falando para a câmera só aparece nos recentes (2 vídeos).

## 3. Ganchos: primeiros 5 s e texto na tela no 1º frame

| código | grupo | formato | o que é dito em 0–5 s (paráfrase) | texto na tela no 1º frame (OCR t=0, sem o selo nome/@) | tipo do texto |
|---|---|---|---|---|---|
| DGohKSZOTWN | TOP#1 | clipe de terceiros (curadoria) | (en, clipe de terceiros) Recepcionista de hotel atende; quem liga se apresenta como agente de IA | «Esse é o futuro?» + frase dizendo que dois agentes de IA trocam de linguagem ao se reconhecerem (14 palavras, parafraseada) + legenda em PT da conversa | manchete |
| DG8hcKiOzDn | TOP#2 | clipe de terceiros (curadoria) | sem fala | manchete de 19 palavras (parafraseada): estudante indiano criou máquina de IA que faz a lição com a letra dele + «Gênio?» | manchete |
| DE2NREBONGY | TOP#3 | clipe de terceiros (curadoria) | sem faixa de áudio | nenhum texto (OCR só ruído); imagem: cães-robô com cabeças humanas realistas numa exposição | nenhum |
| DGfjs33uvum | TOP#4 | provável anúncio | sem fala | «o3-mini / DeepSeek R1 / Grok 3 / Claude 3.7 Sonnet»: grade comparando 4 modelos no mesmo prompt (OCR leu "03-mini") | rótulos |
| DFtjq1KNqB2 | TOP#5 | clipe de terceiros (curadoria) | sem fala | «só precisa disso para ultrapassar na corrida da IA» + «chips de <= 5nm» (lacunas onde a legenda usa bandeiras 🇺🇸/🇨🇳) | manchete |
| C3Yma6QiKyt | TOP#6 | corte de podcast (estúdio) | Confessa um passatempo inusitado (hackear IAs) e emenda pergunta retórica | «Meu passatempo preferido é hackear IA's» + selo nome/@ | legenda da fala |
| C9LZM7kxbLT | TOP#7 | corte de podcast (estúdio) | Cita previsão do CEO da OpenAI: IA quase de graça até 2030 | «O ser humano não vai acompanhar a evolução da I.A» (caixa central) | manchete |
| C-5jOGDu5tL | TOP#8 | corte de podcast (estúdio) | No Brasil é fácil se destacar, porque a maioria se acomoda | «No Brasil é muito fácil» | legenda da fala |
| C9I4T5IPENM | TOP#9 | corte de podcast (estúdio) | Antes e agora: IA gratuita era fraca, agora qualquer um acessa | «Qualquer pessoa tem acesso a I.A multimodal de graça» (caixa central) | manchete |
| DATfyhdO3te | TOP#10 | corte de podcast (estúdio) | Abertura antecipada: IA muda tão rápido que nem dá pra escrever livro | «IA, muda toda» (legenda; a fala desse trecho se repete aos 30,0 s) | legenda da fala |
| C9YKgiMPVnS | TOP#11 | corte de podcast (estúdio) | Curiosidade de bastidor: foi Musk quem batizou a OpenAI | «I.A é a nova corrida espacial» (caixa central) | manchete |
| C3vQkI-C-z7 | TOP#12 | corte de podcast (estúdio) | Regra-ameaça: quem não usa IA a cada 15 minutos está atrasado | «Se tu não tá usando uma IA a cada 15 minutos,» (a fala se repete aos 65,7 s) | legenda da fala |
| C_Y3-f0PG8T | TOP#13 | provável anúncio | sem fala | nenhum texto (nome do criador entra aos 4 s); bastidores de evento com plateia | nenhum |
| C93E6wLvbju | TOP#14 | conversa em tela dividida | Pessoas não querem aprender a ferramenta; querem o problema resolvido | «IA para gestores de tráfego» (OCR leu "LA para") | manchete |
| C_XCYhDtjeA | TOP#15 | conversa em tela dividida | Anuncia virada: IA deixa de ser só texto e vira quase humana | «Aqui a IA vai sair» + letreiro neon "GRAVANDO" ao fundo (OCR parcial) | legenda da fala |
| Ddywg4_ivND | RECENTE#1 | clipe de terceiros (curadoria) | (en, clipe de terceiros) Criador do projeto diz ter dado um corpo a uma IA | manchete de 34 palavras (parafraseada): equipe de hackathon do MIT criou IA que move a mão da pessoa + legenda «Eu dei um corpo para uma IA» | manchete |
| DdtmTcaiR7t | RECENTE#2 | clipe de terceiros (curadoria) | sem fala | «Em 1991, isso era ficção. Em 2026, virou produto.» + rótulos filme × robô real | manchete |
| DdmigcfKavn | RECENTE#3 | selfie falando pra câmera | Notícia: novo modelo da Anthropic saiu e a empresa voltou à forma | «O Opus 5.5» (legenda em bloco curto) + estampa da camiseta lida pelo OCR | legenda da fala |
| Ddje6-ECHig | RECENTE#4 | clipe de terceiros (curadoria) | sem fala real (trilha do Exterminador; a "letra" transcrita é alucinação) | nenhum texto; robô humanoide pequeno chutando entre crianças + desenho do Exterminador | nenhum |
| DdjMec3Ct4x | RECENTE#5 | texto na tela + música | sem fala (música) | «A frase do JENSEN HUANG sobre IA e emprego.» + aviso de que os 5 hábitos estão na legenda | manchete |
| DdhgFU4hRIP | RECENTE#6 | clipe de terceiros (curadoria) | sem fala | «Os vídeos que a minha mãe me manda» + resto parafraseado: perguntando se é IA (13 palavras no total); imagem: Coca-Cola e Mentos | manchete |
| Ddgbeb1BHj5 | RECENTE#7 | texto na tela + música | sem fala | «A MUDANÇA É A ÚNICA CONSTANTE NA VIDA.» | manchete |
| Ddd38gaT51R | RECENTE#8 | texto na tela + música | sem fala | «SE FOR IMPORTANTE, VOCÊ ENCONTRARÁ UM CAMINHO» | manchete |
| DdcdXIrpkXT | RECENTE#9 | narração sobre imagens | (fala só a partir de 2,6 s) Define direto: segundo cérebro é lugar para guardar informação | «O que é Segundo Cérebro?» | manchete |
| DdcJA40pEYF | RECENTE#10 | selfie falando pra câmera | Promessa-tutorial: como liberar ~100 milhões de tokens de graça | «Como desbloquear quase 100 milhões de tokens no Astra» (continua: grátis, sem pagar) | legenda da fala |
| Ddbdb1CqTYk | RECENTE#11 | texto na tela + música | sem fala (música) | «5 perguntas pra saber se vale testar a IA nova» (continua: ou ignorar, "IGNORAR" em destaque) | manchete |
| DdbRy96BUyo | RECENTE#12 | texto na tela + música | sem fala | palavras soltas (OCR t=0: «VOCÊ / NÃO / VOCÊ / TEM / COMEÇAR»); ao longo do vídeo completam a ideia de não precisar ser perfeito para começar | manchete |
| DdYtAfAu9fO | RECENTE#13 | texto na tela + música | sem fala | «MOTIVAÇÃO / DISCIPLINA» | manchete |
| DdWHFCITfAq | RECENTE#14 | texto na tela + música | sem fala (música) | «ENERGIA / MULTITAREFAS / FOCO» | manchete |
| DdTjfRXuum_ | RECENTE#15 | texto na tela + música | sem fala | «REDEFINA, RECOMECE, RETOME O FOCO» | manchete |

Contagens do gancho:

- Início da fala: 11 de 12 vídeos com fala em pt falam em 0,0 s (RECENTE#9 em 2,6 s, depois de um título mudo). Nenhum dos 12 abre com saudação, "fala galera" ou apresentação.
- 1ª frase dos 9 do TOP com fala: afirmação provocativa 5 (TOP#8, 10, 12, 14, 15), citação de autoridade com data 1 (TOP#7), curiosidade/confissão 2 (TOP#6, 11), antes × agora 1 (TOP#9). Nenhuma abre com pergunta (TOP#14 só fecha a 1ª frase com "entendeu?"); pergunta retórica curta aparece antes de 5 s em 2 (2,4 s e 2,5 s).
- Texto no 1º frame: 27 de 30 (sem texto: TOP#3, TOP#13, RECENTE#4). Nos 9 do TOP com fala: 4 com manchete em caixa diferente da fala (TOP#7, 9, 11, 14) e 5 com a legenda da 1ª frase (TOP#6, 8, 10, 12, 15). Nos 15 recentes: 12 manchetes, 2 legendas, 1 sem texto.
- Manchete que só é paga no fim: em 3 dos 4 cortes com manchete, a frase da manchete só é dita por inteiro depois de 70% do vídeo (TOP#7 aos 67 s de 86; TOP#11 aos 42 s de 55; TOP#9 entre 54 e 69 s de 77). No 4º (TOP#14) é o tema, dito aos 16 s.
- Abertura antecipada: 2 dos 9 começam com a melhor fala tirada do meio ou do fim e depois voltam ao contexto (TOP#10: o trecho de 0–6,7 s reaparece aos 30,0 s; TOP#12: a frase de 0–3,8 s reaparece aos 65,7 s).
- Moldes (com lacunas): «[Tese curta sobre IA em até 10 palavras]» na tela + fala abrindo com "[Afirmação que contraria o senso comum sobre IA/mercado]"; ou "[Autoridade] disse que até [ano] [mudança grande]" + manchete com a consequência; ou "Antes [situação limitada]; agora [qualquer pessoa] tem [capacidade] de graça".

## 4. Linguagem (12 vídeos com fala em pt e flag ok; 2.731 palavras; 204 frases)

### 4.1 Top 30 expressões recorrentes de 2 a 4 palavras

Contadas dentro da frase, descartando combinações feitas só de palavras vazias (artigo, preposição, pronome, conjunção, formas de ser/estar/ter/ir) e as que só existem dentro de outra maior com a mesma contagem. Ordem: nº de vídeos, depois ocorrências.

| # | expressão | vídeos (de 12) | ocorrências | onde |
|---|---|---|---|---|
| 1 | a gente | 6 | 10 | TOP#7, TOP#10, TOP#11, TOP#15, RECENTE#3, RECENTE#9 |
| 2 | o cara | 4 | 8 | TOP#8, TOP#10, TOP#12, TOP#14 |
| 3 | as pessoas | 4 | 7 | TOP#7, TOP#9, TOP#10, TOP#14 |
| 4 | por exemplo | 4 | 7 | TOP#6, TOP#9, TOP#10, TOP#14 |
| 5 | o jogo | 4 | 5 | TOP#9, TOP#10, TOP#11, RECENTE#3 |
| 6 | pessoas que | 4 | 4 | TOP#10, TOP#14, RECENTE#9, RECENTE#10 |
| 7 | a ia | 3 | 6 | TOP#6, TOP#7, TOP#15 |
| 8 | eu vou | 3 | 5 | TOP#11, TOP#12, RECENTE#3 |
| 9 | capacidade cognitiva | 3 | 4 | TOP#7, TOP#9, TOP#12 |
| 10 | fazer isso | 3 | 4 | TOP#12, TOP#15, RECENTE#10 |
| 11 | que tá | 3 | 4 | TOP#6, TOP#9, TOP#14 |
| 12 | a gente tem | 3 | 3 | TOP#7, TOP#10, TOP#11 |
| 13 | que a gente | 3 | 3 | TOP#7, RECENTE#3, RECENTE#9 |
| 14 | e daí | 3 | 3 | TOP#9, TOP#12, TOP#14 |
| 15 | não quer | 3 | 3 | TOP#7, TOP#9, RECENTE#10 |
| 16 | open ai | 3 | 3 | TOP#7, TOP#10, TOP#11 |
| 17 | ou seja | 3 | 3 | TOP#9, TOP#11, RECENTE#3 |
| 18 | todo mundo | 3 | 3 | TOP#8, TOP#9, TOP#12 |
| 19 | eu quero | 2 | 8 | TOP#12, RECENTE#3 |
| 20 | eu quero que você | 2 | 6 | TOP#12, RECENTE#3 |
| 21 | não tá | 2 | 6 | TOP#10, TOP#14 |
| 22 | uma ia | 2 | 6 | TOP#9, TOP#12 |
| 23 | um monte de | 2 | 4 | TOP#8, TOP#10 |
| 24 | com base | 2 | 4 | TOP#12, TOP#14 |
| 25 | não sabem | 2 | 4 | TOP#6, TOP#9 |
| 26 | todas as | 2 | 4 | TOP#9, TOP#11 |
| 27 | o que tá acontecendo | 2 | 3 | TOP#6, TOP#9 |
| 28 | com base no | 2 | 3 | TOP#12, TOP#14 |
| 29 | escrever o | 2 | 3 | TOP#10, TOP#12 |
| 30 | inteligência artificial | 2 | 3 | TOP#7, TOP#15 |

Fora do top 30, com 2 vídeos cada: "muda completamente o jogo", "um monte de coisa", "tipo assim", "daí tu vai", "faz com que", "vai ter acesso". "eu quero que você" (6 vezes) vem de ditar um prompt para a IA em voz alta (TOP#12) e de um pedido de comentário (RECENTE#3).

### 4.2 Tamanho de frase

- Por pontuação do Whisper: média **13,4** palavras, mediana **9,0** (204 frases; 49 com até 5 palavras, 38 com 20 ou mais).
- Por trecho do Whisper (pausa de respiração): média 8,9, mediana 8,0 palavras (307 trechos). Vídeos com pouca pontuação (TOP#9, TOP#15, RECENTE#9) inflam a média por frase; a mediana por trecho é a medida mais estável.

### 4.3 Tratamento do espectador

| recorte | vídeos | frases | frases com "você" | frases com "tu" | frases com 2ª pessoa (você/tu/te/teu/ti) | "você(s)" | "tu" |
|---|---|---|---|---|---|---|---|
| TOP (2024) | 9 | 177 | 12 (6,8%) | 28 (15,8%) | 41 (23,2%) | 14 | 36 |
| RECENTES (2026) | 3 | 27 | 14 (51,9%) | 0 | 15 (55,6%) | 21 | 0 |
| total | 12 | 204 | 26 (12,7%) | 28 (13,7%) | 56 (27,5%) | 35 | 36 |

"a gente": 10 vezes (3,7 por mil palavras), em 6 de 12 vídeos. Em TOP#12, 8 dos 9 "você" estão no prompt ditado à IA (6) ou no CTA (2).

### 4.4 Marcadores de oralidade

| marcador | ocorrências | por mil palavras | vídeos (de 12) | observação |
|---|---|---|---|---|
| cara | 23 | 8,4 | 4 | só em cortes de conversa (TOP#8, 10, 12, 14); 14 das 23 são "o/um/esse cara", ~9 vocativo |
| tá | 19 | 7,0 | 5 | contração de "está" na maioria; em TOP#14 também como "ok" |
| né | 4 | 1,5 | 4 |  |
| olha | 2 | 0,7 | 2 | "olha só" |
| galera | 2 | 0,7 | 2 |  |
| sabe | 1 | 0,4 | 1 | verbo, não marcador |
| mano | 0 | 0,0 | 0 |  |
| gente (vocativo) | 0 | 0,0 | 0 | todas as 10 ocorrências de "gente" são "a gente" |

Outros marcadores que aparecem nos dados:

| palavra | ocorrências | por mil palavras | vídeos (de 12) |
|---|---|---|---|
| porque | 19 | 7,0 | 8 |
| então | 15 | 5,5 | 7 |
| tipo | 7 | 2,6 | 4 |
| por exemplo | 7 | 2,6 | 4 |
| exato / exatamente (muitas vezes do entrevistador) | 7 | 2,6 | 4 |
| daí | 6 | 2,2 | 6 |
| basicamente | 6 | 2,2 | 5 |
| imagina | 5 | 1,8 | 2 |
| tipo assim | 3 | 1,1 | 2 |
| ou seja | 3 | 1,1 | 3 |
| entendeu | 2 | 0,7 | 2 |

### 4.5 Construção "não é X, é Y"

- **Na fala (12 vídeos)**: 0 na forma exata. 5 variantes em 3 vídeos (1,8 por mil palavras): "não é só isso, [é]…" e "não é que [X]… [Y]" (TOP#9), "não é só [A], não é só [B]…" e "não é só [X]… [Y]" (TOP#11), "não [X], mas [Y]" (TOP#14).
- **Nas legendas (30)**: 11 legendas usam a construção. Exata ("não é X, é Y"): 2, ambas de 2024 (TOP#8, TOP#9). Variantes: 9 ("não é X mas sim Y", "não só X, já é Y", "não se trata de X, mas de Y", "não seja X, mas Y", "não é sobre X, só sobre Y", "não precisa X, só precisa Y", "não como X, mas como Y", "deixa de ser X, passa a ser Y", citação "não vai perder para X, vai perder para Y"), 6 delas em legendas de 2026. Mais 1 caso limítrofe (RECENTE#9).

### 4.6 Palavras por minuto e perfil de cada vídeo com fala em pt

| vídeo | formato | motor | palavras | fala (s) | pal/min (fala) | pal/min (duração total) | frases | média pal/frase | mediana | "tu" | "você" | "cara" | "tá" | números |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TOP#6 | corte de podcast (estúdio) | large-v3-turbo | 224 | 45,6 | 295 | 271 | 25 | 9,0 | 7,0 | 7 | 0 | 0 | 2 | 1 |
| TOP#7 | corte de podcast (estúdio) | large-v3-turbo | 259 | 81,3 | 191 | 180 | 26 | 10,0 | 8,5 | 12 | 0 | 0 | 0 | 3 |
| TOP#8 | corte de podcast (estúdio) | large-v3-turbo | 282 | 69,4 | 244 | 232 | 36 | 7,8 | 8,0 | 3 | 2 | 8 | 0 | 4 |
| TOP#9 | corte de podcast (estúdio) | large-v3-turbo | 255 | 72,5 | 211 | 198 | 5 | 51,0 | 20,0 | 2 | 0 | 0 | 2 | 3 |
| TOP#10 | corte de podcast (estúdio) | large-v3-turbo | 233 | 60,5 | 231 | 223 | 34 | 6,9 | 6,0 | 5 | 1 | 9 | 5 | 5 |
| TOP#11 | corte de podcast (estúdio) | small | 183 | 50,4 | 218 | 199 | 12 | 15,2 | 12,0 | 2 | 0 | 0 | 0 | 1 |
| TOP#12 | corte de podcast (estúdio) | small | 331 | 83,6 | 238 | 235 | 11 | 30,1 | 25,0 | 1 | 9 | 2 | 2 | 4 |
| TOP#14 | conversa em tela dividida | small | 328 | 87,3 | 225 | 219 | 24 | 13,7 | 11,0 | 4 | 1 | 4 | 8 | 1 |
| TOP#15 | conversa em tela dividida | small | 113 | 38,6 | 176 | 156 | 4 | 28,2 | 25,5 | 0 | 1 | 0 | 0 | 0 |
| RECENTE#3 | selfie falando pra câmera | small | 186 | 68,0 | 164 | 163 | 8 | 23,2 | 17,0 | 0 | 4 | 0 | 0 | 10 |
| RECENTE#9 | narração sobre imagens | small | 93 | 29,8 | 187 | 171 | 3 | 31,0 | 31,0 | 0 | 1 | 0 | 0 | 0 |
| RECENTE#10 | selfie falando pra câmera | small | 244 | 78,5 | 187 | 185 | 16 | 15,2 | 15,5 | 0 | 16 | 0 | 0 | 5 |

Mediana TOP (9): 225 pal/min (faixa 176–295), 255 palavras, 72,8 s. Recentes (3): 164, 187, 187 pal/min. Perguntas: 23 sinais de interrogação em 2.731 palavras (0,84 por 100 palavras; em TOP#8 e TOP#14 parte é do entrevistador). Números: 37 no total; mediana 3 por vídeo no TOP (0 a 5); RECENTE#3 (notícia de lançamento) tem 10 em 68 s.

## 5. Legenda (caption) dos 30

| código | grupo | caracteres | linhas | emojis | hashtags | CTA na legenda | "?" | menção @ |
|---|---|---|---|---|---|---|---|---|
| DGohKSZOTWN | TOP#1 | 117 | 2 | 0 | 0 | — | 1 | — |
| DG8hcKiOzDn | TOP#2 | 386 | 3 | 0 | 0 | — | 5 | — |
| DE2NREBONGY | TOP#3 | 225 | 2 | 0 | 0 | — | 1 | — |
| DGfjs33uvum | TOP#4 | 222 | 2 | 0 | 0 | — | 1 | — |
| DFtjq1KNqB2 | TOP#5 | 128 | 2 | 2 | 3 | — | 0 | — |
| C3Yma6QiKyt | TOP#6 | 477 | 5 | 0 | 0 | comenta PALAVRA (1ª linha) | 0 | — |
| C9LZM7kxbLT | TOP#7 | 453 | 5 | 0 | 10 | — | 1 | — |
| C-5jOGDu5tL | TOP#8 | 194 | 3 | 0 | 4 | comenta PALAVRA | 0 | — |
| C9I4T5IPENM | TOP#9 | 367 | 5 | 0 | 10 | — | 0 | — |
| DATfyhdO3te | TOP#10 | 545 | 4 | 0 | 0 | comenta PALAVRA | 0 | — |
| C9YKgiMPVnS | TOP#11 | 600 | 5 | 0 | 10 | — | 1 | — |
| C3vQkI-C-z7 | TOP#12 | 518 | 4 | 0 | 0 | comenta PALAVRA (1ª e última linha) | 0 | — |
| C_Y3-f0PG8T | TOP#13 | 450 | 5 | 0 | 0 | comenta opinião | 0 | — |
| C93E6wLvbju | TOP#14 | 396 | 5 | 0 | 8 | — | 1 | — |
| C_XCYhDtjeA | TOP#15 | 396 | 4 | 0 | 0 | comenta PALAVRA | 0 | @realcadufranco |
| Ddywg4_ivND | RECENTE#1 | 992 | 7 | 0 | 0 | me conta + me segue | 1 | — |
| DdtmTcaiR7t | RECENTE#2 | 647 | 10 | 0 | 0 | segue @ (2x) | 1 | @oalanicolas, @oalanicolas |
| DdmigcfKavn | RECENTE#3 | 434 | 4 | 0 | 0 | me conta (comentários) | 0 | — |
| Ddje6-ECHig | RECENTE#4 | 70 | 2 | 1 | 0 | — | 0 | — |
| DdjMec3Ct4x | RECENTE#5 | 1820 | 17 | 0 | 0 | salva + manda pra alguém + me segue | 0 | — |
| DdhgFU4hRIP | RECENTE#6 | 20 | 1 | 1 | 0 | — | 1 | — |
| Ddgbeb1BHj5 | RECENTE#7 | 542 | 7 | 0 | 0 | — | 1 | — |
| Ddd38gaT51R | RECENTE#8 | 370 | 4 | 0 | 0 | — | 0 | — |
| DdcdXIrpkXT | RECENTE#9 | 1226 | 7 | 0 | 0 | comenta opinião | 0 | — |
| DdcJA40pEYF | RECENTE#10 | 146 | 4 | 1 | 1 | me conta | 1 | — |
| Ddbdb1CqTYk | RECENTE#11 | 1765 | 12 | 0 | 0 | salva + manda pra alguém + segue o perfil | 10 | — |
| DdbRy96BUyo | RECENTE#12 | 513 | 7 | 0 | 0 | — | 0 | — |
| DdYtAfAu9fO | RECENTE#13 | 594 | 9 | 0 | 0 | — | 0 | — |
| DdWHFCITfAq | RECENTE#14 | 916 | 8 | 0 | 0 | — | 3 | — |
| DdTjfRXuum_ | RECENTE#15 | 567 | 7 | 0 | 0 | — | 0 | — |

| recorte | caracteres (média / mediana) | linhas (média / mediana) | emojis por legenda (média) | legendas com hashtag | hashtags (total) | legendas com "?" | "?" (total) | legendas com @ |
|---|---|---|---|---|---|---|---|---|
| TOP 15 | 365 / 396 | 3,7 / 4,0 | 0,13 | 6 | 45 | 7 | 11 | 1 |
| RECENTES 15 | 708 / 567 | 7,1 / 7,0 | 0,20 | 1 | 1 | 7 | 18 | 1 |
| 30 | 537 / 452 | 5,4 / 5,0 | 0,17 | 7 | 46 | 14 | 29 | 2 |

**Tipos de CTA (legendas com o tipo)**

| tipo | TOP 15 | RECENTES 15 | 30 |
|---|---|---|---|
| comenta PALAVRA-chave para receber algo | 5 | 0 | 5 |
| comenta opinião / "me conta" | 1 | 4 | 5 |
| segue (me segue, segue o perfil, segue @) | 0 | 4 | 4 |
| salva | 0 | 2 | 2 |
| compartilha ("manda pra alguém") | 0 | 2 | 2 |
| link na bio | 0 | 0 | 0 |
| direct | 0 | 0 | 0 |
| **qualquer CTA explícito** | 6 | 7 | 13 |

- Palavras-chave usadas na legenda do TOP: IA, Diamand, Infinito, 888, avatar (todas de 2024). Nos 15 recentes, nenhuma.
- CTA fora da legenda: cartela final na tela pedindo comentário em 7 cortes do TOP, entre 87% e 96% da duração (OCR: «Comente "SG"» em TOP#7 aos 82 s, #9 aos 72 s e #11 aos 50 s; «Comente INFINITO» em #10 aos 58 s; «Comente "AVATAR"» em #15 aos 38 s; «Comenta» em #8 aos 70 s; «PARA RECEBER O LINK» em #6 aos 46 s); falado em 3 vídeos (seção 2). Somando legenda, fala e cartela: 8 dos 9 cortes de conversa do TOP pedem comentário com palavra-chave; só TOP#14 não pede.
- Comentários/views: mediana do TOP 0,016%. Os 2 maiores do TOP (TOP#12 0,352% e TOP#6 0,113%; 22x e 7x a mediana) são os únicos com a palavra-chave na 1ª linha da legenda; TOP#12 também pede na fala. Sem contar anúncios e TOP#3 (0 comentários, provável comentário desativado), a mediana dos 4 sem palavra-chave é 0,019%, igual à dos 8 com palavra-chave (0,018%): o ganho aparece quando o pedido abre a legenda.
- Emojis: 5 em 30 legendas (4 legendas). Hashtags: 46, em 7 legendas; 38 delas em 4 legendas de 2024 (8 a 10 cada).

## 6. Correlações de Spearman entre views e cada variável

ρ de Spearman (empates com posto médio) e p bicaudal do scipy. Com n = 30, 15 ou 12 isto é **indício, não prova**: são 33 testes, e a p < 0,05 espera-se cerca de 1,6 "significância" só por acaso.

| variável | 30 (n; ρ; p) | dentro do TOP (n; ρ; p) | dentro dos recentes (n; ρ; p) |
|---|---|---|---|
| duração (s) | **30; 0,58; 0,001** | 15; −0,46; 0,084 | **15; 0,63; 0,012** |
| palavras/min (só fala em pt) | **12; 0,70; 0,011** | 9; 0,40; 0,286 | 3; −0,50; 0,667 |
| cortes/min bruto | 30; 0,31; 0,097 | 15; −0,41; 0,124 | 15; 0,37; 0,173 |
| cortes/min agrupado | 30; 0,29; 0,114 | 15; −0,37; 0,169 | 15; 0,37; 0,173 |
| tamanho da legenda (caracteres) | **30; −0,52; 0,003** | **15; −0,57; 0,025** | 15; −0,29; 0,296 |
| texto no 1º frame (0/1) | 30; −0,15; 0,436 | 15; 0,00; 1,000 | 15; −0,25; 0,374 |
| manchete diferente da fala no 1º frame (0/1) | 30; −0,33; 0,073 | 15; 0,22; 0,438 | 15; −0,42; 0,115 |
| fala em qualquer idioma (0/1) | 30; 0,32; 0,088 | 15; −0,43; 0,114 | 15; 0,31; 0,254 |
| fala do criador em pt (0/1) | 30; 0,24; 0,194 | **15; −0,63; 0,012** | 15; 0,23; 0,407 |
| pedido de comentário: legenda, fala ou cartela (0/1) | 30; 0,21; 0,257 | **15; −0,60; 0,018** | 15; 0,31; 0,254 |
| "comenta PALAVRA" em qualquer canal (0/1) | **30; 0,40; 0,028** | 15; −0,43; 0,107 | — |

Em negrito: p < 0,05. Palavras/min nos recentes tem n = 3 (sem valor). "Comenta PALAVRA" não varia nos recentes (0 de 15).

**Mediana de views com × sem (nos 30)**

| variável | com (n; mediana) | sem (n; mediana) | dentro dos recentes: com × sem |
|---|---|---|---|
| texto no 1º frame | 27; 430.712 | 3; 1.209.509 | 14: 3.481 × 1: 42.262 |
| manchete diferente da fala | 19; 27.831 | 11; 1.244.365 | 12: 3.077 × 3: 42.262 |
| fala (qualquer idioma) | 14; 1.264.185 | 16; 23.674 | 4: 21.144 × 11: 2.848 |
| fala do criador em pt | 12; 1.264.185 | 18; 35.047 | 3: 14.457 × 12: 3.252 |
| pedido de comentário | 13; 1.244.365 | 17; 42.262 | 4: 21.144 × 11: 2.848 |
| "comenta PALAVRA" | 8; 1.568.196 | 22; 35.047 | — |

Leitura:

- Só o **tamanho da legenda** mantém o sinal nos três recortes (negativo: −0,52; −0,57; −0,29). Legenda longa, que é o padrão de 2026, não trouxe alcance.
- Duração, fala e pedido de comentário são positivos nos 30 e negativos dentro do TOP. Nos 30 eles separam 2024–25 (vídeos longos, com fala e alcance alto) de 2026 (posts curtos de texto). Dentro do TOP, os 5 mais vistos (13 a 70 s) são 4 clipes de terceiros e 1 provável anúncio, sem fala dele e sem CTA. Medem formato e época, não uma alavanca que se possa puxar.
- Palavras/min: ρ 0,70 nos 12 com fala, mas separa 2024 (176–295) de 2026 (164–187); dentro do TOP cai para 0,40 (p 0,29).
- Dentro dos recentes, vídeo com fala dele em pt teve mediana 14.457 contra 3.252 sem fala (n = 3 × 12); os clipes de terceiros ficaram acima dos dois (mediana 60.643, n = 4).

## 7. Os 7 achados quantitativos para quem vai roteirizar

1. **O alcance está na cauda, e a fase atual é a pior da série.** Mediana de 14.043,5 views (5,4% dos 261.650 seguidores), p90 de 118.580, e só 16 de 1.032 reels (1,6%) passaram de 1 milhão. Os 50 reels mais novos (24/08 a 27/09/2026) têm mediana de 3.759 (0,27x), a menor dos 21 blocos, e saíram a 10 por semana. Os blocos de pico (42.875 em fev–abr/2024; 28.426 em fev–mai/2025) saíram a 4,3–5,5 por semana. Oito dos 15 recentes são texto na tela + música de 6 a 11 s, com mediana de 2.544 views (0,18x). O formato atual não é o que deu alcance.
2. **Os virais com a fala dele são cortes de conversa, não monólogo.** Dos 15 mais vistos, 9 têm a fala dele em pt, e os 9 são cortes de conversa de 2024: 7 de podcast em estúdio, com microfone no quadro, e 2 em tela dividida. Mediana de 1.535.479 views (109x), 72,8 s, 255 palavras, 225 palavras/min (176–295). Os outros 6 do TOP são 4 clipes de terceiros (1,88 a 3,64 milhões; 3 com manchete na tela) e 2 prováveis anúncios. Nos recentes, os 3 vídeos com a fala dele (2 selfies, 1 narração) têm mediana de 14.457, contra 60.643 dos clipes de terceiros. Para quem só grava falando para a câmera, o molde é o corte de conversa: cerca de 250 palavras em cerca de 70 s, fala contínua e tese única. A versão selfie ainda não provou alcance neste perfil (n = 3).
3. **O gancho é uma afirmação no segundo 0, sem saudação, com texto na tela desde o 1º frame.** 11 de 12 vídeos com fala em pt começam a falar em 0,0 s, e nenhum abre com saudação. Nos 9 do TOP, a 1ª frase é afirmação provocativa (5), autoridade + data (1), curiosidade (2) ou antes × agora (1), e nunca uma pergunta. Todos têm texto no 1º frame. Em 4 é uma manchete em caixa, diferente da fala; em 3 desses 4, a frase da manchete só é dita depois de 70% do vídeo: a tese é prometida no início e paga no fim. Em 2 dos 9, a melhor fala do meio é repetida na abertura (volta aos 30,0 s e aos 65,7 s).
4. **A retenção vem da densidade da fala, não da edição.** Os cortes do TOP com fala têm mediana de 3,5 cortes/min bruto e 1,6 agrupado (um a cada ~38 s); 1 deles fica 90 s sem corte. Os 12 vídeos com fala têm legenda embutida. A frase mediana tem 9 palavras (8 por pausa de respiração). Há 0,84 pergunta por 100 palavras, parte delas do entrevistador. 8 dos 9 citam números (mediana 3 por vídeo), e a notícia de lançamento recente cita 10 em 68 s.
5. **A linguagem é coloquial do Sul na conversa e passa para "você" na selfie.** Nos cortes de 2024: "tu" 36 vezes contra 14 de "você" (28 de 177 frases com "tu"). Nos vídeos de 2026: "você" 21 vezes e "tu" nenhuma (14 de 27 frases). Por mil palavras: "cara" 8,4 (em 4 cortes de conversa, nenhum de 2026), "tá" 7,0, "né" 1,5, "olha" 0,7, "galera" 0,7, "mano" 0 e "gente" como vocativo 0 ("a gente" 3,7, em 6 de 12 vídeos). O raciocínio anda com "porque" (7,0), "então" (5,5), "por exemplo" (2,6; 4 vídeos), "daí" (2,2; 6 vídeos) e "basicamente" (2,2; 5 vídeos). Expressões que voltam entre vídeos: "o jogo" (4 vídeos; "muda completamente o jogo" em 2), "capacidade cognitiva" (3), "todo mundo" (3) e "ou seja" (3).
6. **"Não é X, é Y" é recurso da legenda escrita, não da fala.** Na fala: 0 na forma exata e 5 variantes ("não é só isso", "não é que…", "não X, mas Y") em 3 de 12 vídeos, ou 1,8 por mil palavras. Nas legendas: 11 de 30 (2 exatas, de 2024; 9 variantes, 6 delas de 2026). A legenda mediana do TOP tem 396 caracteres e 4 linhas, com hashtags em 6 de 15; a dos recentes tem 567 caracteres e 7 linhas, com hashtag em 1 de 15. O tamanho da legenda tem correlação negativa com views nos três recortes (ρ −0,52 nos 30, −0,57 no TOP, −0,29 nos recentes).
7. **O CTA mudou de "comente PALAVRA" no fim (2024) para "segue/salva/manda" (2026).** 8 dos 9 cortes de conversa do TOP fecham pedindo comentário com palavra-chave: numa cartela na tela entre 87% e 96% da duração (7) ou falado aos 90% (1). Cinco repetem a palavra na legenda. Nenhum dos 15 recentes usa palavra-chave. As 2 maiores taxas de comentário do TOP (0,352% e 0,113%; 22x e 7x a mediana do TOP, de 0,016%) são os únicos vídeos com a palavra-chave na 1ª linha da legenda. Nos recentes: "segue" 4/15, "me conta"/comenta opinião 4/15, "salva" 2/15 e "manda pra alguém" 2/15. "Link na bio" e "direct" não aparecem em nenhuma das 30 legendas. O CTA falado aparece em só 3 de 12 vídeos com fala, sempre nos últimos 5–13%.
