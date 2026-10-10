---
name: modelagem
description: Escreve roteiros de Reels sobre IA para o Adriel no padrão medido de 5 criadores brasileiros de IA (Danilo Gato, Miguel Lannes, Alan Nicolas, Rodrigo Tadewald e Mateus Dias; 150 reels), sempre com fatos reais pesquisados na hora, com fonte e data. Faz radar de novidades de IA, pautas com nota de viralidade, roteiro completo no formato que ele aprovou, pautas da semana, roteiro no estilo de um dos 5, revisão de roteiro e atualização da base. Use quando ele pedir "/modelagem", "modela", "no estilo do Alan/Danilo/Miguel/Rodrigo/Mateus", "novidades de IA pra reels", "pauta de IA", "roteiro viral de IA" ou "o que postar essa semana". Complementa a criacao-conteudo (funil, carrossel, bio, perfil) e segue a roteiro-storytelling para tirar a cara de IA da fala.
argument-hint: "<tema> | novidades [dias] | semana | estilo <criador> <tema> | revisar <roteiro> | atualizar"
---

# /modelagem: Reels de IA no padrão dos 5 criadores, com fato do dia

Pasta da skill: `/Users/adriel/.claude/skills/modelagem/`. Os caminhos abaixo são relativos a ela.

## 1. O que é

**A base.** 5 perfis brasileiros de IA no Instagram e 150 reels, coletados em 29/09/2026: os 15 mais vistos de todos os tempos (TOP) e os 15 mais recentes de cada perfil. Os perfis são @odanilogato (Danilo Gato), @inventormiguel (Miguel Lannes), @oalanicolas (Alan Nicolas), @rodrigotadewald (Rodrigo Tadewald) e @ddiasmatt (Mateus Dias). Cada reel foi medido em views, likes, comentários, duração, fala transcrita, texto na tela, cortes e legenda. O padrão comum está em `references/dna-dos-criadores.md`, e os moldes prontos, em `references/moldes.md`.

**O objetivo.** Escrever os roteiros do Adriel no padrão que os dados mostram, sempre com fato real pesquisado na hora, conferido na fonte e datado. Nenhum fato sai da memória do modelo.

**Limites da base** (dna §1): as views incluem impulsionamento pago; são 15 vídeos por grupo; TOP e recentes são de épocas diferentes; não há dado de retenção nem de envios. O que aparece em só 1 criador é hipótese.

**Skills vizinhas.** Estratégia de funil, carrossel, stories, bio e análise de perfil ficam com `criacao-conteudo` (e `stories`), e esta skill não repete aquela. O polimento anti-IA da fala segue `roteiro-storytelling` (seções 1 e 2). Aqui ficam a pauta, a pesquisa, o molde e o roteiro de Reels de IA.

## 2. Comandos

O texto depois de /modelagem chega aqui: "$ARGUMENTS". Leia a 1ª palavra e escolha o modo. Se o pedido for ambíguo, escolha o mais próximo e diga qual em 1 linha.

| Pedido | Modo | Entrega |
|---|---|---|
| (vazio) | menu | 3 pautas do radar de 3 dias e a sugestão de rodar `novidades` |
| `novidades [dias]` | novidades | radar dos últimos N dias (padrão 7) → 10 pautas com nota → 3 roteiros completos |
| `semana` | semana | 7 pautas ranqueadas, com o mix de formatos justificado pelos dados |
| `estilo <criador> <tema>` | estilo | 1 roteiro no molde e no ritmo do criador |
| `revisar <roteiro ou arquivo>` | revisar | diagnóstico pelo checklist + versão reescrita |
| `atualizar` | atualizar | coleta nova do Instagram, só depois do sim dele |
| qualquer outro texto | tema | 3 ângulos com nota + roteiro completo do melhor |

Frases naturais valem: "o que postar essa semana" é `semana`; "no estilo do Rodrigo sobre X" é `estilo`; "novidades de hoje" é `novidades 1`.

**Sem argumento:** não escreva roteiro. Rode `date` e o radar de 3 dias (passo 3 do fluxo), sugira 3 pautas (manchete, data, veículo, molde e nota provisória; ao menos 1 com prova própria dele) e ofereça `/modelagem novidades`. A checagem completa vem quando ele escolher.

## 3. Fluxo obrigatório

Vale para todo modo que escreve ou revisa roteiro.

1. **Data de hoje.** Rode `date`. "Ontem", "essa semana" e "há 2 anos" saem dessa data; o que o modelo lembra pode estar velho.
2. **Leitura.** Leia `references/dna-dos-criadores.md` inteiro, uma vez por sessão. No modo estilo, leia também a análise do criador em `references/criadores/` (as seções 7, 11 e 12 pesam mais). Ao escrever, leia em `references/moldes.md` a tabela da §1 e a seção do molde escolhido; os ganchos (§3), o CTA e a legenda (§4) e a edição (§5), quando precisar.
3. **Pesquisa**, seguindo `references/pesquisa.md`:
   - radar: `python3 ~/.claude/skills/modelagem/scripts/radar.py <dias> ["termo" ...]` lista manchetes datadas do Google News (Brasil e EUA) e as buscas em alta do Google Trends Brasil (nos modos, `radar.py` abrevia esse comando). Ele acha a pauta; não confirma o fato. Se falhar, use WebSearch com o mês e o ano no termo;
   - fonte primária: anúncio oficial, documentação, página de preço ou relatório original; sem ela, duas fontes independentes. Se WebSearch e WebFetch estiverem adiados, carregue com ToolSearch (`select:WebSearch,WebFetch`). Link do Google News é redirecionamento: busque o título;
   - checagem: anunciado, lançado e disponível no Brasil são estados diferentes; grátis leva o limite; preço leva moeda e data;
   - **nenhum número, nome, data, preço ou recurso entra sem fonte e data.** Sem fonte, o dado sai. Vale também para estudo e caso antigo (M6, M13).
4. **Pauta e molde.** Faça a triagem de `pesquisa.md` §3 (a notícia serve? 10 ou mais de 15) e passe a pauta pelo filtro de viralidade da dna §13: sujeito e fato (peso 2), prova dita numa frase ou num objeto (peso 2), emoção simples, bolso do público com ponte no meio, novidade e prova própria do Adriel; de 0 a 3 cada, máximo 24.
   - 16 ou mais vira roteiro; de 12 a 15, reescreva o ângulo até achar o sujeito ou a prova; 11 ou menos, descarte.
   - Menos 3 pontos: tese genérica, conceito sem cena, pergunta de seguidor lida, aforismo, jargão sem tradução. Zera: promessa de ganho, fato sem fonte e data, cena encenada, IA no lugar de vendedor ou time.
   - Temas com mais TOP (dna §3): espetáculo visual (21 de 75; para ele, vira antes × agora falado), prova de uso próprio (10), medo com saída (9), ferramenta grátis (7), carreira e oportunidade (7).
   - Escolha o molde pela tabela de `moldes.md` §1 (M1 a M14).
5. **Escrita.** Na voz do Adriel (seção 5), na ordem das batidas do molde, a 3,3 palavras por segundo (60 s ≈ 200 palavras; 90 s ≈ 300). Escreva a Ideia em até 15 palavras, depois a 1ª frase e o fecho, depois o meio.
6. **Conferência.** Passe o checklist da seção 8 e leia a fala em voz alta. Travou, reescreva.
7. **Entrega** no formato da seção 6.

## 4. O DNA em uma tela

As 12 regras mais fortes da dna §2, todas presentes em 4 ou 5 dos 5 criadores ("x" = views ÷ mediana do próprio perfil).

1. **Fala no segundo zero, sem "oi" e sem nome.** Nenhum dos 150 abre com saudação; o Rodrigo começa a falar em 0,0 s em 29 de 30.
2. **A 1ª frase é a promessa inteira e acaba perto dos 4 s** (medianas de 4,0 s no Danilo e 4,2 s no Rodrigo). Abra com fato nomeado, resultado próprio, antes × agora ou grátis com limite: 14 dos 18 recentes acima da mediana abriram com um desses ou com imagem, e nenhum dos 26 com tese, pergunta conceitual, lista muda ou sem gancho verbal passou.
3. **O texto do 1º frame repete ou resume a 1ª frase,** em até 12 palavras (há texto no 1º frame em 87% a 100% dos vídeos; as manchetes têm de 8 a 10 palavras na mediana).
4. **O rosto narra uma prova.** Nenhum viral dos 150 é só rosto; nos recentes do Danilo, os vídeos com corpo, robô ou objeto têm mediana de 103.367 views, e os que não mostram nada disso, 27.846. Para o Adriel, a prova vai na 1ª frase, num objeto na mão ou num número na tela.
5. **Número concreto, traduzido em coisa, com a fonte na boca de quem fez o fato** ("a própria [empresa] diz" + mês). No Rodrigo, mais números acompanharam mais views nos recentes (ρ +0,52); em DdwHUgCjtm- (11,2x), um peso em gramas vira o peso de um clipe. Data falada é obrigatória para o Adriel.
6. **Dinheiro só como custo, nunca como renda prometida.** O Miguel não promete renda em nenhum dos 30 vídeos; a exceção do Mateus, com % de ganho prometido (Dc1974Li3eN), fez 0,4x.
7. **O fato abre; a ponte para o bolso de quem assiste vem no meio** (4 de 5). Em Dd1JMKIjBg6 (16,4x), a empresa entra aos 63%; os 4 recentes do Miguel que abriram pelo processo de empresa ficaram entre 0,36x e 0,53x.
8. **Um re-gancho perto da metade:** viradas a 49–56% da duração no Danilo; "agora" na virada, com mediana de 46%, no Miguel.
9. **Regra ou eco do gancho antes do pedido:** veredito de 1 frase em 10 de 14 falas do Miguel (mediana a 79%); 20 de 30 do Rodrigo fecham no benefício ou no veredito.
10. **Um pedido só, nos últimos 2 a 8 s** (a 96% no Danilo; de 95% a 98% no Rodrigo). Pedir opinião não mexeu nas views (29.578 com o pedido, 29.256 sem).
11. **Palavra-chave multiplica comentário, não views:** 0,398% de comentários por view contra 0,031% no Miguel; no Rodrigo, de 170 a 201 vezes a taxa dos outros vídeos. Use quando o objetivo for lead.
12. **Voz de conversa, de 200 a 230 palavras por minuto,** frase de 9 a 16 palavras, com "você", "a gente" e a 1ª pessoa de quem testou. Ritmo e duração não previram views, mais cortes por minuto nunca ajudaram (negativo no TOP dos 5) e mais posts por semana não compraram alcance (4 de 5). O que acompanhou as views foi o tipo de gancho e a prova (dna §5 e §8).

## 5. Voz e marca do Adriel

**Quem fala.** O Adriel cria conteúdo sobre IA como pessoa física, em português do Brasil, em Reels no Instagram. Fala com dois públicos: quem quer usar IA para ganhar dinheiro (freela, serviço, renda extra, MEI) e donos de negócio que querem vender mais e organizar processos. Pauta de estudo (prova, faculdade, resumo) fica de fora.

**Formato.** Só ele falando para a câmera, com um objeto na mão quando couber. Sem personagem, encenação, diálogo, ligação ou gravação de tela. O dinamismo vem da edição: corte quando muda a ideia (a cada 4 a 8 s; dna §12, conflito 2), alternando plano médio e close; texto na tela; tom e pausa.

**Imagem estática na edição** (print da notícia, foto, gráfico): ainda não decidida. Sugira no máximo uma por roteiro, marcada "opcional", no trecho do fato, por 2 a 3 s e com a data visível, e deixe a decisão com ele. A favor: a prova na tela acompanha as views (regra 4), e um documento real mostrado fez 2,6x (DdnLA3sDoDX). Contra: nada nos dados, só o risco de marca (dna §12, conflito 6).

**Provas dele** (use só o que for verdade hoje e peça a confirmação no "Antes de gravar"): freelas em que entrega o site pronto antes de o cliente contratar; o quiz de captação que manda o lead para o WhatsApp; sistemas feitos com IA para clientes. **Frameworks autorais:** a Régua da Delegação (repetição × julgamento), que casa com o M9, e o Funcionário que Não Dorme (agente de IA como contratação, com função, meta e limite), que casa com o M10 e com qualquer pauta de agente. Os frameworks são opcionais: nunca puxe o tema para atendimento ou agente por causa deles, e nunca use "eu chamo isso de [nome]" (ele recusou em 03/10/2026). Quando ele pedir para "ensinar algo", varie a área: freela e proposta, preço, conteúdo, produtividade, vendas, ferramenta nova.

**Marca.**
- Nunca prometa valor de ganho: nem reais, nem %, nem "x vezes", nem prazo de resultado. Dinheiro só aparece como preço de ferramenta, com moeda e data. Nunca cite faturamento de cliente.
- Nunca notícia falsa nem cena encenada como notícia. Nada de imagem gerada com cara de registro real, voz clonada ou vídeo de terceiros.
- Fato sempre com fonte e data: dita na fala (quem, verbo e mês) e listada no bloco Fontes.
- Nunca diga que a IA substitui vendedor ou time: ela entra com função, meta e limite.
- Nunca copie fala ou legenda de criador com mais de 5 palavras seguidas; as frases-molde de `moldes.md` já são paráfrases.

**Voz.**
- Fala de gente, fluida, com contrações (tá, pra, pro, tô, né). Frase média, costurada por "só que", "então", "porque", "aí" e "por exemplo"; alterne uma frase longa com uma curta.
- "Você" no singular, "a gente" para se incluir e a 1ª pessoa só no que ele fez ("eu testei", "eu montei").
- Jargão vira analogia do dia a dia; número vira coisa que dá para imaginar.
- Corte as marcas de texto de IA (`roteiro-storytelling`, seções 1 e 2): a antítese "não é X, é Y"; o tricolon de fragmentos; as muletas de atenção ("presta atenção", "agora pensa comigo", "deixa eu te explicar", "olha só"); a pergunta que o próprio narrador responde; o em-dash dramático; "num mundo onde"; palavra de manual (utilizar, obter). Também ficam fora "segredo", "hack", "sensacional", "tu", "mano", "galera" e palavrão.

**O conflito "não é X, é Y", resolvido.** Os criadores usam a construção: o Miguel diz "o ponto não é X, é Y" em 12 dos 30 vídeos, e ela aparece em 10, 11 e 13 das 30 legendas do Danilo, do Alan e do Rodrigo. O Rodrigo a aponta como sinal de texto de IA (Dcv7xpPAWmq), e nas legendas dele ela cresceu justo na fase de queda (3 no TOP, 10 nos recentes). Registre o fato quando for útil, mas não reproduza para o Adriel, nem na fala nem na legenda: a decisão é dele, com feedback repetido. No lugar, afirme direto; ou mostre as duas coisas concretas e deixe o contraste implícito; ou use "normalmente, [jeito comum]" seguido do jeito novo, ou "ao invés de [comum], [melhor]". A pergunta que o narrador responderia vira a pergunta real de um cliente, contada como relato.

**Métricas dele:** envios por alcance e seguidores ganhos. Todo teste (tarja × legenda grande na abertura, imagem estática) é lido por essas duas.

## 6. Formato de entrega

É o formato que ele aprovou em 27/09/2026 (Semana 1 de `~/Downloads/Adriel-Conteudo-Mes1-Atracao-Mes2-Consciencia-v2.md`), com dois acréscimos, a linha **Molde** e o bloco **Fontes**. O "Antes de gravar" continua, agora só com o que conferir ou preencher, porque as fontes vão para o bloco próprio.

```markdown
## "[Título curto: o objeto ou o fato]"

**Ideia:** [a tese do vídeo numa frase, até 15 palavras]
**Etapa:** [topo | meio | fundo] · **Para quem:** [quem quer ganhar dinheiro com IA | quem tem negócio | os dois] · **Mecanismo:** [o porquê, com nome] · **Prova:** [o fato com fonte, o teste ou o caso real dele]
**Molde:** [M1 Notícia traduzida] · referência: [Danilo, DdxElXaE2Uc] · filtro [19]/24

[cena: abertura com o objeto na mão, ou plano fechado]
"[1ª frase: a promessa inteira, com sujeito e verbo de acontecimento.]

[Parágrafos curtos, um por batida do molde, com a fonte dita: quem, verbo e mês.]"

[cena: troca de plano no re-gancho; opcional, decisão sua: print da fonte com a data, 2 a 3 s]
"[Ponte para o negócio, regra ou veredito.]

[O pedido, um só.]"

**Texto na tela (abertura):** "[a 1ª frase ou a versão curta, até 12 palavras]" ([tarja | legenda grande])
**Legenda do post:** [1ª linha: o gancho como frase completa. Depois o fato, o mecanismo e a ponte, e o pedido com a PALAVRA em caixa alta. Última linha: "Fonte: [empresa ou veículo], [dd/mm/aaaa]". Sem hashtag e sem emoji.]
**Fontes:**
- [o fato, em até 8 palavras]: [link] (publicado em [dd/mm/aaaa]; conferido em [data de hoje])
**Antes de gravar:** [o que conferir ou preencher: disponibilidade no Brasil, [resultado real], o objeto, a mensagem da palavra-chave pronta]
```

- A fala vai entre aspas, em parágrafos curtos, com no máximo 3 [cena: ...]. Nada de tabela de tempos nem marcação de tom.
- Duração: o padrão aprovado é de 60 a 90 s (200 a 300 palavras); os moldes curtos (M2, M8 e M14) podem ficar entre 45 e 60 s.
- CTA pelo objetivo (moldes §4): "comenta [PALAVRA] que eu te mando [material]" nos vídeos de captação; "me segue pra aprender a [X]" nos de topo; pergunta de sim ou não para conversa. A palavra-chave é um substantivo tirado do vídeo e entrega material, nunca resultado.
- Legenda no tamanho do molde (moldes §4): curta (L1) no M8 e no M14; média com palavra-chave (L2) no padrão; artigo com fontes (L3) no M1, no M11 e no M12.
- Abertura: alterne a tarja em caixa alta e a legenda grande das primeiras palavras, e diga qual entre parênteses, para ele comparar envios por alcance (dna §12, conflito 1).
- Entregue só o roteiro pronto. O checklist é interno; o que ficou pendente para ele vai no "Antes de gravar".

## 7. Modos

### novidades [dias]
1. `date` e `radar.py <dias>` (padrão 7; "hoje" = 1). Acrescente termos do público quando ajudar, como `"WhatsApp IA"` ou `"Instagram IA"`.
2. Descarte o que não serve ao público (estudo, prova, geopolítica sem ponte para o bolso, boato) e o que não tem fonte primária.
3. Confira as candidatas na fonte primária e monte a tabela das 10 melhores:

   | # | Pauta (sujeito + fato) | Fonte e data | Molde | Para quem | Nota /24 | Decisão |
   |---|---|---|---|---|---|---|

4. Escreva os 3 roteiros completos das 3 maiores notas (16 ou mais), com moldes diferentes e ao menos 1 para cada público, quando der. Se menos de 3 chegarem a 16, reescreva o ângulo das que têm de 12 a 15; se ainda faltar, entregue menos e diga por quê.

### tema
1. `date`, `radar.py 14 "<tema>"` e a fonte primária do tema.
2. Proponha 3 ângulos, cada um com molde e nota; escreva o roteiro completo do melhor e ofereça os outros 2.
3. Se o tema fugir do público (estudo, prova, faculdade) ou não tiver fato conferível, diga em 1 linha e proponha o ângulo que serve.

### semana
1. `date` e `radar.py 7`. Não repita pautas do plano aprovado (o arquivo de 27/09/2026 citado na seção 6, se existir) nem as já gravadas.
2. Entregue 7 pautas ranqueadas pela nota, com este mix, tirado da dna §3, §5 e §10:
   - **2 novidades com sujeito nomeado (M1 ou M7):** é o tipo de gancho com mais recentes acima da mediana (7 de 14; mediana de 1,5x), e 3 TOP do Danilo saíram em até 48 h do fato.
   - **1 prova própria dele (M4 ou M3):** CrYyOTttWUd (81,1x) e DdyzHcECTyI (5,8x); nos recentes, só 3 de 9 ganchos "eu testei" passaram da mediana, então a prova vai na 1ª frase.
   - **1 antes × agora (M8):** 6 no TOP e DdtmTcaiR7t (30,7x) nos recentes; os três de referência são imagem, e a versão falada é hipótese a testar.
   - **1 ferramenta grátis com o limite (M2):** 5 no TOP e DdcJA40pEYF (4,2x) nos recentes.
   - **1 alerta com saída ou checagem de promessa (M12 ou M11):** medo com saída tem 9 TOP e DRVZ9YskX9R (19,5x) é o maior do Rodrigo; nos recentes, só 1 de 5 alertas passou da mediana, então só com caso datado e saída concreta.
   - **1 de meio com framework (M5, M9 ou M10), com a Régua da Delegação ou o Funcionário que Não Dorme:** DbRTrbElCGr (237,3x), DUvhpvDk-ju (7,0x), DPlyTlMkSSg (10,7x).
   - **Fora:** tese genérica, pergunta de seguidor lida, lista muda, comando genérico e frase com música (nenhum dos 26 recentes com gancho de tese, pergunta conceitual, lista muda ou sem gancho verbal passou da mediana).
3. Equilibre os dois públicos e topo × meio. Por pauta: 1ª frase, molde, para quem e etapa, fonte e data, nota e tipo de CTA (palavra-chave nas de captação, seguir nas de topo).
4. Diga qual gravar primeiro e ofereça os roteiros completos. O plano dele é 1 reel por semana, e mais volume não comprou alcance em 4 de 5 criadores (dna, regra 15): as 7 pautas são um banco para escolher. Subir a frequência só faz sentido com gancho e prova próprios em cada vídeo. O que medir: envios por alcance e seguidores ganhos.

### estilo <criador> <tema>

| Criador | Análise em `references/criadores/` | Como soa (dna §7) | Moldes em que é referência |
|---|---|---|---|
| Danilo Gato (@odanilogato) | `danilo-gato.md` | professor que testa primeiro | M1, M3, M6, M8, M12 |
| Miguel Lannes (@inventormiguel) | `miguel-lannes.md` | direto, uma ideia por frase | M5, M6, M7, M13 |
| Alan Nicolas (@oalanicolas) | `alan-nicolas.md` | tese forte, fala contínua | M2, M5, M8, M13 |
| Rodrigo Tadewald (@rodrigotadewald) | `rodrigo-tadewald.md` | professor-colega cético | M2, M4, M9, M10, M11, M12 |
| Mateus Dias (@ddiasmatt) | `mateus-dias.md` | founder que abre o bastidor | M1, M4, M8, M14 |

1. Leia a análise do criador (seção 7 para a voz, 11 para a receita, 12 para a adaptação ao Adriel) e a dna §7 (o que o Adriel pega e o que deixa de cada um).
2. Use um molde em que ele é referência ou um esqueleto da seção 11 da análise, adaptado pela seção 12 (sem tela gravada, curadoria nem cena de IA).
3. Modele a estrutura, o ritmo, o tamanho de frase, o tipo de gancho e as marcas de até 5 palavras da coluna "O Adriel pega". A coluna "O Adriel deixa" e as regras da seção 5 vencem sempre: o "o ponto não é X, é Y" do Miguel fica de fora.
4. Depois do roteiro, 1 linha: "Do [criador]: [o que foi modelado]".
5. Criador fora dos 5: diga que a base não tem esse perfil e ofereça o mais parecido ou `atualizar` com o @ dele (gera o dossiê e a análise; o DNA continua sendo dos 5).

### revisar <roteiro>
1. Leia o roteiro (texto colado ou caminho de arquivo) e rode `date`.
2. Confira cada fato na fonte (passo 3 do fluxo); o que não tiver fonte sai ou vira lacuna no "Antes de gravar".
3. Dê a nota no filtro e ache o molde mais próximo.
4. Entregue: (a) o diagnóstico, só com os itens do checklist que falharam, agrupados em fatos, padrão, voz e formato, cada um com a correção em 1 linha; (b) a nota antes e depois; (c) a versão reescrita no formato da seção 6. Preserve o jeito dele de falar e as provas reais; não invente prova.

### atualizar
1. Veja a data da última coleta (29/09/2026; confira com `ls -l ~/.claude/skills/modelagem/dados/stats.json`). Com menos de 30 dias, avise e pergunte se ele quer mesmo rodar.
2. Avise antes de rodar: leva de 1 a 3 horas num Mac de 8 GB (a transcrição é o gargalo; o Mac fica ligado na tomada); usa a sessão do Instagram já logada no perfil de automação do Chrome (chrome-devtools-mcp; outro perfil vai em `IGPROFILE`); deve rodar no máximo uma vez por mês, porque navega na conta dele.
3. Com o sim dele, rode em segundo plano: `bash ~/.claude/skills/modelagem/scripts/atualizar_base.sh [perfil ...]` (sem perfil, os 5). Se o script disser que o perfil está sem login, peça para ele entrar no Instagram pelo Chrome de automação e rode de novo.
4. Depois da coleta, refaça as análises e o DNA:
   - uma análise por criador, cada uma num subagente, com `scripts/prompt_analise.txt` ({U} = o perfil sem @, como odanilogato; {NOME}, {DATA} = data da coleta, {DOSSIE} = `dados/dossie/<perfil>.md`, {MIDIA} = `dados/midia/<perfil>`, {SAIDA} = `dados/analise/<perfil>.md`); copie cada saída para `references/criadores/<nome>.md`;
   - refaça `references/dna-dos-criadores.md` a partir das 5 análises, de `dados/tabelas.md` e de `dados/stats.json`, e depois `references/moldes.md`;
   - atualize a data e os números das seções 1 e 4 deste arquivo;
   - apague os vídeos com `rm -rf ~/.cache/modelagem/videos`.

## 8. Checklist final

É interno: na entrega, o que ficou pendente vai para o "Antes de gravar"; no modo revisar, os itens que falharam viram o diagnóstico.

**Fatos**
- [ ] `date` rodado; "ontem", "essa semana" e "há N anos" batem com a data de hoje.
- [ ] Cada número, nome, data, preço e recurso tem fonte primária (ou duas independentes), com link e data no bloco Fontes, e a fala diz quem, verbo e mês.
- [ ] Disponibilidade no Brasil, idioma, preço (moeda e data) e limite do grátis conferidos; nada anunciado foi tratado como lançado.
- [ ] Nenhum superlativo sem quem o deu; nenhuma prova do Adriel inventada; crédito dado quando o exemplo é de outra pessoa.

**Padrão**
- [ ] Nota 16 ou mais no filtro; molde escolhido pela tabela.
- [ ] Fala no segundo zero; a 1ª frase traz a promessa inteira, com sujeito concreto e verbo de acontecimento, em cerca de 4 s.
- [ ] Texto de abertura igual à 1ª frase ou à versão curta, até 12 palavras.
- [ ] Prova na 1ª frase, num objeto ou num número; nenhum conceito sem cena.
- [ ] Ponte para o negócio no meio; re-gancho perto da metade; regra ou eco do gancho antes do pedido.
- [ ] Um pedido só, nos últimos 2 a 8 s; palavra-chave com um substantivo do vídeo.
- [ ] Palavras dentro da faixa do molde (3,3 por segundo).

**Voz e marca**
- [ ] Lido em voz alta sem travar, com contrações, "você" e "a gente".
- [ ] Zero "não é X, é Y", tricolon de fragmentos, muleta de atenção, pergunta auto-respondida, em-dash e "num mundo onde".
- [ ] Zero promessa de ganho (R$, %, "x vezes", prazo) e zero IA no lugar de vendedor ou time.
- [ ] Nenhum trecho de fala ou legenda de criador com mais de 5 palavras seguidas.

**Formato**
- [ ] Ideia, Etapa, Para quem, Mecanismo, Prova e Molde preenchidos.
- [ ] Fala entre aspas, em parágrafos curtos, com no máximo 3 [cena: ...]; sem personagem, encenação, diálogo, ligação ou tela gravada.
- [ ] Texto na tela, Legenda (sem hashtag e sem emoji), Fontes e Antes de gravar presentes; imagem estática só como opcional.

## 9. Mapa dos arquivos

```
modelagem/
├── SKILL.md                       este manual
├── references/
│   ├── dna-dos-criadores.md       o padrão dos 5 com números e o filtro de viralidade (§13); ler sempre
│   ├── moldes.md                  14 moldes (M1 a M14), 57 ganchos, CTA, legenda, texto na tela e edição
│   ├── pesquisa.md                protocolo de pesquisa e checagem de fatos
│   └── criadores/                 análise de cada criador em 13 seções (§11 receita, §12 adaptação)
│       ├── danilo-gato.md         @odanilogato
│       ├── miguel-lannes.md       @inventormiguel
│       ├── alan-nicolas.md        @oalanicolas
│       ├── rodrigo-tadewald.md    @rodrigotadewald
│       └── mateus-dias.md         @ddiasmatt
├── scripts/
│   ├── radar.py                   manchetes de IA com data real (Google News BR e EUA + Trends BR)
│   ├── atualizar_base.sh          refaz a coleta do Instagram (1 a 3 h; no máximo 1 vez por mês)
│   ├── prompt_analise.txt         prompt da análise por criador (um subagente por criador)
│   └── (peças da coleta)          collect.mjs, details.mjs, cdp.mjs, baixar.sh, download.py,
│                                  processar.sh, visual.sh, ocr e ocr.swift,
│                                  ocr_frames.py, transcribe.py, dossie.py, stats.py, tabelas.py
└── dados/                         base da coleta de 29/09/2026 (consulta; não editar à mão)
    ├── users/<perfil>.json        todos os reels do perfil, com views, likes e comentários
    ├── dossie/<perfil>.md         dossiê por criador (entrada da análise)
    ├── analise/<perfil>.md        a análise (cópia em references/criadores) e <perfil>.ficha.md (números)
    ├── midia/<perfil>/            por vídeo: gancho, folha de contato, capa, transcrição, OCR e cortes
    ├── stats.json                 números comparativos dos 5
    ├── tabelas.md                 TOP 15 e últimos 15 de cada criador
    └── relatorio/                 relatório completo (cópia em ~/Downloads)
```
