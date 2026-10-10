---
name: viral
description: Narrativa viral e edição no padrão do criador americano Kallaway (@kallawaymarketing), medidas em 30 reels (15 mais vistos e 15 recentes) e no vídeo dele sobre neurociência do storytelling. Reestrutura roteiros no loop aposta, grande pergunta, virada e re-gancho, com gancho em 3 camadas, zona de lock-in, re-gancho de escalada e CTA de palavra-chave; cria ganchos; e edita o vídeo gravado do Adriel em tela dividida (gráfico em cima, rosto embaixo, legenda de 1 palavra, closes) com HTML/GSAP renderizado por quadros e ffmpeg. Funciona sozinha ou depois da /modelagem, que faz pauta e fatos com fonte; em choque de voz e marca, vale a /modelagem. Use quando ele pedir "/viral", "deixa viral", "estrutura viral", "roteiro no estilo Kallaway", "edita no padrão Kallaway" ou "edição viral".
argument-hint: "roteiro <tema> | revisar <roteiro> | edicao <video.mp4> | gancho <tema>"
---

# /viral: narrativa e edição no padrão Kallaway

Pasta da skill: `/Users/adriel/.claude/skills/viral/`. Caminhos abaixo são relativos a ela.

## 1. O que é

- **A base.** 30 reels de @kallawaymarketing (os 15 mais vistos e os 15 mais recentes, coletados em 30/09/2026) com views, transcrição com tempo, texto na tela, cortes e quadros. Também a transcrição do vídeo longo dele "The Neuroscience of Addictive Storytelling". Mídia em `~/.cache/viral/`. Os números estão em `references/analise-kallaway.md`.
- **O que a /viral faz.** Cuida da estrutura narrativa, da retenção e da edição. A pauta, a pesquisa de fatos e o padrão dos 5 criadores brasileiros ficam com a `/modelagem`.
- **Para quem.** O Adriel, criador brasileiro que fala de IA para quem quer ganhar dinheiro com IA e para donos de negócio, gravando para a câmera.
- **Limites da base.** Views incluem impulsionamento e vídeos fixados. São 15 por grupo, de épocas diferentes, e não há dado de retenção. Os números que o Kallaway diz de si mesmo são autodeclarados. O que aparece em 1 ou 2 vídeos é hipótese.

## 2. Comandos

O texto depois de /viral chega aqui: "$ARGUMENTS". Leia a 1ª palavra e escolha o modo; se for ambíguo, escolha o mais próximo e diga qual em 1 linha.

| Pedido | Modo | Entrega |
|---|---|---|
| (vazio) | menu | os 4 modos em 4 linhas e a pergunta: tem roteiro, tema ou vídeo? |
| `roteiro <tema>` | roteiro | roteiro no loop viral + mapa do loop + plano de edição |
| `revisar <roteiro ou arquivo>` | revisar | diagnóstico pelo checklist + versão reescrita + plano de edição |
| `gancho <tema>` | gancho | 10 ganchos em 5 tipos, cada um com lock-in, título da tela e visual do 1º quadro |
| `edicao <video.mp4>` | edicao | `final.mp4` editado no padrão, com a conferência |

Frases naturais valem: "deixa viral" com um roteiro colado é `revisar`; "edita no padrão Kallaway" com um vídeo é `edicao`; "roteiro no estilo Kallaway sobre X" é `roteiro`.

## 3. Junto com a /modelagem

- **Divisão do trabalho.** A `/modelagem` faz a pauta, os fatos com fonte e data, o molde (M1 a M14) e o roteiro base no formato aprovado (`/modelagem` §6). A `/viral` reorganiza a narrativa no loop, reforça gancho, lock-in, re-ganchos e CTA, e gera o plano de edição. Fluxo típico: `/modelagem <tema>` e depois `/viral revisar <roteiro>`; ou `/viral roteiro <tema>`, que chama o fluxo de fatos da `/modelagem`.
- **Fatos.** Todo número, nome, data, preço ou recurso segue a `/modelagem` §3 (rodar `date`, fonte primária, data dita na fala, bloco Fontes). A `/viral` nunca acrescenta fato sem fonte.
- **Choque de regras.** Em voz e marca do Adriel vale a `/modelagem` §5, sempre. Nas outras regras de padrão (pedido único no fim, imagem estática opcional etc.), com as duas skills na mesma entrega vence a `/modelagem`; o que a `/viral` sugerir de diferente vira teste opcional, marcado "teste" e medido em envios por alcance e seguidores ganhos.
- **Já resolvido aqui** (detalhe em `references/narrativa.md` §5):
  - o exagero do Kallaway ("segredo", "hack", "impossível de pular") sai;
  - desejo vira tempo poupado ou tarefa resolvida, nunca ganho em dinheiro;
  - nada de "não é X, é Y" (use "normalmente X; o que funciona é Y");
  - a grande pergunta vira situação real, nunca pergunta que ele mesmo responde;
  - nada de gravação de tela, vídeo de terceiros, brilho neon, roxo ou degradê;
  - imagem estática no máximo 1 por vídeo, opcional.

## 4. Princípios narrativos (com evidência)

Detalhe e moldes em `references/narrativa.md`.

1. **Atenção é previsão.** Dopamina sobe enquanto o espectador tenta adivinhar o que vem, e o maior pico vem quando o palpite quebra (NEURO 01:08 e 04:20). Vídeo previsível é máquina de salgadinho.
2. **O loop em 4 passos:**
   - aposta: personagem, risco e prazo;
   - grande pergunta: específica a ponto de o espectador chutar a resposta;
   - virada: contraria o chute e é lógica na hora;
   - re-gancho: fecha uma ideia e abre outra na mesma frase, sem ar morto.

   Boas histórias têm 1 loop; as ótimas, vários em cascata (TOP#1, 36,9x, ensina isso).
3. **Fala no 0,0 s, 1ª frase de ~3,3 s.** Nos 30 vídeos a fala começa no 0,0 s, e nos TOP a 1ª frase acaba entre 2,7 s e 4,7 s.
4. **Gancho em 3 camadas.** Fala, título na tela e visual sobre o mesmo assunto ao mesmo tempo (o gancho triplo, TOP#3). O título é a embalagem, não a legenda da fala: 3 a 8 palavras, em 2 linhas, com 1 palavra de destaque.
5. **"Como fazer [desejo]" vence lista.** São 9 dos 15 TOP; nos recentes a lista domina (6 de 15) e tem a pior mediana (0,8x). 7 TOP prometem um estado intenso no espectador; nenhum recente promete.
6. **Nome próprio do método até 5 s** (a "caixa mágica"): 10 de 15 TOP contra 6 de 15 recentes. Para o Adriel, nunca falado como "eu chamo isso de [nome]" (ele recusou, 03/10/2026): o lock-in vem do contraste ("são só 3 passos, e o terceiro quase todo mundo pula") ou da prova, e o nome fica no título da tela.
7. **Zona de lock-in** nas 2 ou 3 frases depois do gancho, até ~10 s. Os 6 jeitos: prova, transformação, contraste, nome, objeção e dobrar a aposta (REC#11, TOP#4).
8. **Passos numerados com analogia.** 11 de 15 TOP são métodos em passos. Cada passo tem nome, definição, exemplo concreto e porquê. Analogia com algo conhecido (cassino, pescaria, falcão) e contraste velho × novo (TOP#6, #7, #11, #14).
9. **Re-gancho de escalada entre 40% e 65%**: o passo seguinte é "o mais importante" ou "onde se ganha o jogo" (TOP#1 49%, TOP#3 65%, TOP#13 59%, TOP#14 53%).
10. **"Agora" abre cada passo** (1,8 por minuto nos TOP, 0,6 nos recentes); "mas" vira a frase; "então, em vez disso" leva à solução.
11. **Fecho:** recap dos nomes e um pedido de palavra-chave com isca usável. A isca é doc, modelo ou material que dá para colar na IA, nunca promessa de resultado. O pedido vem a 94% da duração, mediana TOP. Citar a palavra cedo multiplica comentário, não views: REC#10 e REC#12 têm 5,69% e 3,23% de comentários, com 1,3x de views.
12. **Assunto e gancho fazem o pico; edição faz o piso.** A edição é a mesma em 0,4x e em 36,9x (`analise-kallaway.md` §4).

## 5. Princípios de edição (com evidência)

Detalhe, medidas e código em `references/edicao.md`.

1. **Tela dividida em ~70% do tempo.** Título no topo (y 128–255), painel de gráfico (y 290–1170), legenda de 1 palavra (centro em y 1242) e cartão do rosto com cantos arredondados (x 67–1013, a partir de y 1405).
2. **Close do rosto em tela cheia** cerca de 5 vezes por minuto, com ~3 s cada, nas frases de opinião, no nome do método, na virada e no re-gancho. O 1º close vem entre 2,0 s e 3,5 s (7 de 11 TOP).
3. **Gancho visual:** um visual novo por segundo nos 4 primeiros segundos. Texto já no quadro 0 (30 de 30). O título entra palavra a palavra com desfoque.
4. **Painel muda a cada ideia** (bloco dividido de ~6 s). Cada imagem casa com a palavra dita (TOP#12). A lista-mapa numerada volta a cada passo como marcador de progresso, com o item atual nítido e o resto desfocado (TOP#3, #13).
5. **Legenda:** 1 palavra por bloco (as curtas se juntam), grotesca pesada, troca seca, sem caixa nem karaokê. O termo-chave sai em serifa itálica.
6. **Paleta:** fundo quase preto ou cinza-claro com quadriculado discreto; 1 cor de acento. Para o Adriel, o acento é a cor da marca dele (sugestão: verde, a confirmar).
7. **Som:** voz na frente e trilha baixa e contínua por baixo.
8. **Cortes:** ~9,6 por minuto, intervalo de 4,4 s (TOP). Pausas cortadas e fala de 200 a 230 palavras por minuto.

## 6. Molde de roteiro viral (o loop numa página)

Ritmo do Adriel: 3,3 palavras por segundo (60 s ≈ 200 palavras; 90 s ≈ 300). Duração alvo de 60 a 90 s (mediana do Kallaway: 90 s).

| % do vídeo | Batida | O que dizer | Na tela |
|---|---|---|---|
| 0–5% | **Gancho** | sujeito + ação + objetivo + contraste numa frase, com promessa concreta | título de 2 linhas entrando; visual de prova trocando a cada ~1 s |
| 5–12% | **Lock-in** | nome do método + 1 dos 6 jeitos (prova, transformação, contraste, objeção, dobrar a aposta) | 1º close no nome; serifa no nome |
| 12–25% | **Aposta** | personagem, risco e prazo (ou o custo de não fazer) | painel: número ou lista-mapa |
| 25–45% | **Passo 1 + grande pergunta** | contexto que deixa o espectador chutar | lista-mapa com o item 1 aceso |
| 40–65% | **Re-gancho de escalada** | "e o passo [n] é onde [o jogo vira]" | close |
| 50–80% | **Virada** | "normalmente [comum]; o que funciona é [novo]", com a pista plantada antes | painel novo + seta |
| 80–92% | **Recap** | os nomes em sequência | lista-mapa completa |
| 92–100% | **CTA** | "comenta [PALAVRA] que eu te mando [material]" | cartão do CTA |

Escolha a variação em `references/narrativa.md` §6:
- V1, método com nome: casa com os moldes M5, M9 e M10 da `/modelagem`;
- V2, velho × novo: com M8 e M13;
- V3, ferramenta com prova: com M2 e M4;
- V4, diagnóstico: com M12;
- V5, história com loop: com M3 e M4.

## 7. Formato de entrega

O roteiro usa o formato da `/modelagem` §6 (Ideia, Etapa, Para quem, Mecanismo, Prova, Molde, a fala entre aspas, Texto na tela, Legenda, Fontes e Antes de gravar). Na linha **Molde**, acrescente a variação viral (ex.: "M9 Três níveis + V1"). Depois do roteiro vêm dois blocos:

```markdown
**Mapa do loop:** Aposta: [quem, o que está em risco, prazo] · Grande pergunta: [a dúvida] · Virada: [o que contraria o palpite] · Re-gancho: [frase-ponte, em ~%] · Isca do CTA: [material]

**Plano de edição** (padrão Kallaway · tema [escuro|claro] · acento [#hex] · trilha [sim|não])
| Tempo (estimado) | Fala (começo do trecho) | Tela | Painel | Legenda |
|---|---|---|---|---|
| 0,0–3,0 | "[...]" | dividida | título entrando; [visual de prova 1 → 2 → 3] | 1 palavra |
| 3,0–5,5 | "[...]" | close | — | *[nome do método]* em serifa |
| ... | ... | ... | ... | ... |
| [fim-6]–[fim] | "comenta..." | dividida | cartão: Comenta "[PALAVRA]" + [subtítulo] | 1 palavra |
**Título (abertura):** linha 1 "[...]" / linha 2 "[... *destaque* ...]"
**Imagem opcional** (decisão sua): [qual print, com data, em que segundo] ou "nenhuma"
```

- Os tempos do plano são estimados a 3,3 palavras por segundo. No modo `edicao` saem da transcrição real.
- Sem tabela de tempos dentro da fala (regra da `/modelagem`): os tempos só aparecem no plano de edição.

## 8. Modos

### roteiro <tema>
1. Rode `date`. Se o tema tem fato (lançamento, número, estudo, preço), siga a `/modelagem` §3 inteira para a pesquisa e a nota do filtro. Se for método próprio do Adriel, sem fato externo, pule a pesquisa, mas toda prova dele vai para o "Antes de gravar".
2. Leia `references/narrativa.md` (uma vez por sessão) e escolha a variação V1 a V5.
3. Escreva primeiro o Mapa do loop, depois a 1ª frase, o lock-in, a virada e o CTA, e por último o meio.
4. Passe o checklist (§9), monte o plano de edição e entregue no formato da §7.

### revisar <roteiro>
1. Leia o roteiro (colado ou arquivo). Se ele veio da `/modelagem`, preserve fatos, fontes, molde e voz.
2. Diagnóstico só com o que falhou no checklist, em 3 grupos (gancho e lock-in, loop e re-ganchos, fecho), cada item com a correção em 1 linha.
3. Reescreva no formato da §7, mudando só ordem, ganchos e pontes. Não invente prova nem fato.

### gancho <tema>
1. Se o tema envolve fato, confira a fonte primeiro (`/modelagem` §3).
2. Entregue 10 ganchos, 2 de cada tipo: C, D, N ou S, H e K (`references/narrativa.md` §7). Cada um vem com a frase falada (até ~4 s), o lock-in de 1 frase, o título de 2 linhas com o destaque marcado e o visual do 1º quadro.
3. Indique os 3 melhores pela evidência (tipo C com desejo concreto e nome de método primeiro) e diga em 1 linha por quê.

### edicao <video.mp4>
Executa a receita de `references/edicao.md` §10. Leia o arquivo inteiro antes de começar.

1. **Perguntas, numa mensagem só e só o que faltar.** Use o padrão quando ele não responder:
   - roteiro ou plano de edição (padrão: monto a partir da transcrição);
   - tema: escuro ou claro (padrão: escuro);
   - cor de acento (padrão: #1DB954 no escuro, #0B7A35 no claro);
   - trilha: arquivo dele ou nenhuma;
   - imagem opcional: qual, ou nenhuma.
2. **Pasta:** `~/Movies/viral/<AAAA-MM-DD>-<slug>/`. Copie o vídeo como `gravacao.mp4`, rode o `npm i` da §10.3 e crie os 6 arquivos das §10.4 a §10.9 com Write, exatamente como estão.
3. **Rode:** `cortar.py`, depois `transcrever.py`. Confira a transcrição: corrija nomes de ferramenta e marca no `palavras.json`. Nunca rode o whisper e o Chrome ao mesmo tempo (Mac de 8 GB).
4. **Plano em dados.** Monte o `timeline.json` (§10.6) a partir do plano de edição, com os tempos tirados do `acha.py`:
   - close de 2 a 4 s, umas 5 por minuto, o 1º entre 2 e 3,5 s;
   - um gráfico novo a cada ideia;
   - lista-mapa nos passos e cartão de CTA nos últimos segundos;
   - nome do método em `serifadas`.
5. **Render e montagem:** `node render.mjs .` e `python3 montar.py .`.
6. **Conferência** (§10.10): folhas de quadros abertas com Read. No máximo 3 rodadas de ajuste.
7. **Entrega:** caminho do `final.mp4`, duração, e o que conferir antes de postar (transcrição de nomes, enquadramento, a imagem opcional). Se ficou algo pendente, diga.

Proibido na edição: gravação de tela, vídeo ou foto de terceiros, voz clonada, imagem gerada com cara de registro real (`/modelagem` §5). Para reel 100% animado sem o Adriel na câmera, indique a skill `conteudo-motion`.

## 9. Checklist final

É interno. Na entrega, o que ficou pendente vai para o "Antes de gravar" ou para a lista da edição.

**Gancho e lock-in**
- [ ] Fala no 0,0 s; a 1ª frase tem sujeito, ação, objetivo e contraste e acaba perto de 3–4 s.
- [ ] Título de 3 a 8 palavras, mesmo assunto da fala, com 1 destaque; texto já no quadro 0.
- [ ] Nome do método até ~5 s, ou outro dos 6 jeitos de lock-in até ~10 s.

**Loop**
- [ ] Aposta (personagem, risco, prazo), grande pergunta específica e virada lógica com pista plantada.
- [ ] Re-gancho em cada emenda e um de escalada entre 40% e 65%; "agora" abrindo os passos.
- [ ] Pelo menos 1 analogia do dia a dia do público; contraste velho × novo quando couber.

**Fecho**
- [ ] Recap dos nomes; um pedido de palavra-chave com isca que ele consegue mandar.

**Edição** (no plano ou no vídeo)
- [ ] ~70% dividido; close no nome, na virada e no re-gancho; 1º close entre 2 e 3,5 s.
- [ ] Visual novo a cada ~1 s no gancho e a cada ideia depois; legenda de 1 palavra sincronizada.
- [ ] Nada do painel abaixo de y 1180; título inteiro; CTA visível no fim.

**Voz e marca** (`/modelagem` §5)
- [ ] Sem "segredo", "hack", exagero, "não é X, é Y", pergunta auto-respondida e promessa de ganho.
- [ ] Fato com fonte e data; prova do Adriel só se for verdade (confirmar).
- [ ] Nenhuma fala ou legenda do Kallaway com mais de 5 palavras seguidas.
- [ ] Sem gravação de tela, vídeo de terceiros, brilho neon, roxo ou degradê; no máximo 1 imagem estática, opcional.

## 10. Mapa dos arquivos

```
viral/
├── SKILL.md                      este manual
└── references/
    ├── narrativa.md              ciência do loop, anatomia do Reel, métodos dele, adaptação, moldes V1–V5, banco de ganchos
    ├── edicao.md                 padrão de edição medido + receita técnica com o código completo (testado)
    └── analise-kallaway.md       números, tabela dos 30 vídeos, o que separa o viral do resto, método
~/.cache/viral/                   dados brutos (dossiê, vídeos, quadros, transcrições, OCR, cortes)
```
