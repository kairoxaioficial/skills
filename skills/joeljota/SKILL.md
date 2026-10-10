---
name: joeljota
description: Escreve roteiros de Reels no estilo do Joel Jota (@joeljota), com uma mensagem de impacto, a partir da análise medida de 70 reels dele coletados em 03/10/2026 (os 30 mais vistos de todos os tempos, os 20 mais recentes e os 20 motivacionais mais vistos): gancho no segundo zero, frase curta com cabeça repetida, voz encenada, virada perto da metade, fecho curto sem pedido e direção de gravação. Faz roteiro a partir de um tema (ou escolhe o tema), versão curta, banco de ganchos, revisão de roteiro no estilo dele e atualização da base. Use quando o Adriel pedir "/joeljota", "estilo Joel Jota", "no estilo do Joel", "roteiro motivacional", "mensagem impactante", "vídeo de mensagem" ou "reels de alta performance". Complementa a modelagem (IA com fato do dia), a viral (narrativa Kallaway) e a roteiro-storytelling (fala sem cara de IA).
argument-hint: "<tema> | curto <tema> | ganchos <tema> | revisar <roteiro> | atualizar"
---

# /joeljota: roteiro de Reels no estilo do Joel Jota, com mensagem de impacto

Pasta da skill: `/Users/adriel/.claude/skills/joeljota/`. Os caminhos abaixo são relativos a ela.

## 1. O que é

**A base.** O perfil @joeljota (6,55 mi de seguidores, 2.539 reels, mediana de 528.783 views) foi coletado inteiro em 03/10/2026. Foram analisados 70 reels: os 30 mais vistos de todos os tempos (5,6 a 24,3 mi), os 20 mais recentes e os 20 motivacionais mais vistos fora desses dois grupos (4,1 a 5,6 mi). Cada um foi transcrito com tempo por palavra e medido em ritmo, pausas, volume, texto na tela, cortes e legenda; depois, oito analistas cruzaram os vídeos (ganchos, estrutura, linguagem, retórica, crenças, anatomia motivacional, visual e o que separa o viral) e um verificador cético por frente conferiu cada afirmação nos dados. O padrão está em `references/dna-joeljota.md`; o kit de escrita, em `references/moldes.md`.

**O objetivo.** Um roteiro original que soa como o Joel na forma (o jeito de abrir, de repetir, de encenar, de virar e de fechar) e que é verdadeiro no conteúdo: as histórias, as provas e os números são de quem grava, nunca do Joel. **Quem grava** é o Adriel, falando para a câmera, salvo se o pedido disser outra pessoa; nesse caso, troque só o "quem fala" e mantenha as regras de cópia e de fatos.

**Limites da base** (dna §1). Os grupos foram escolhidos por views: comparar grupos mostra composição, não causa. Os recentes têm de 0 a 16 dias e ainda crescem. Não há dado de retenção nem de envios. São 70 de 2.539 reels. Em 4 rodadas de teste cego em 03 e 04/10/2026 (17 roteiros, cada um ao lado de 3 transcrições reais), o juiz identificou o texto da IA em todos, com 78% a 96% de confiança; a rubrica deu 6 a 8 em impacto e em fidelidade e passou todos em verdade, cópia e formato. A detecção vem em boa parte de que as amostras reais têm ruído de transcrição e os vocativos e a aspereza do Joel que a voz do Adriel deixa de fora. O roteiro ganha naturalidade quando o Adriel grava com as palavras dele; a leitura em voz alta e o modo revisar são o filtro final.

**Skills vizinhas.** Notícia de IA com fonte e data é da `modelagem`; narrativa no loop do Kallaway e edição em tela dividida, da `viral`; funil, carrossel e perfil, da `criacao-conteudo`. As regras de voz sem cara de IA da `roteiro-storytelling` (seções 1 e 2) valem aqui também. Em choque de estilo com o Joel, as regras de voz e de marca do Adriel (seção 5) vencem.

## 2. Comandos

O texto depois de /joeljota chega aqui: "$ARGUMENTS". Leia a 1ª palavra e escolha o modo. Se o pedido for ambíguo, escolha o mais próximo e diga qual em 1 linha.

| Pedido | Modo | Entrega |
|---|---|---|
| (vazio) | escolha | 3 mensagens de vida com nota no filtro e o roteiro completo da melhor |
| `<tema ou situação>` | tema | 1 roteiro completo + 3 ganchos alternativos |
| `curto <tema>` | curto | 1 roteiro de 15 a 24 s (40 a 70 palavras) |
| `ganchos <tema>` | ganchos | 10 ganchos de tipos diferentes, com o melhor marcado |
| `revisar <roteiro ou arquivo>` | revisar | diagnóstico pelo checklist + versão reescrita |
| `atualizar` | atualizar | coleta nova do Instagram, só depois do sim dele |

Frases naturais valem: "um vídeo sobre disciplina no estilo do Joel" é `tema`; "uma frase de impacto pra postar hoje" é `curto`; "melhora esse roteiro" é `revisar`.

## 3. Fluxo obrigatório (todo modo que escreve ou revisa roteiro)

1. **Data de hoje.** Rode `date`. Data real da semana (segunda-feira, fim de mês) ou campanha e data comemorativa do mês (Janeiro Branco, Outubro Rosa, Dia das Crianças, Dia dos Pais) entra só quando a mensagem é sobre o assunto dela (Outubro Rosa: câncer de mama), dita uma vez como moldura, na abertura ou na legenda, como o Joel faz com o ano que chega (CmrRO80B1CJ) e com a segunda-feira (DdgtugiR8-S); nunca como detalhe dentro de uma cena. Data de assunto vizinho fica fora.
2. **Leitura**, uma vez por sessão: `references/moldes.md` inteiro e, no `references/dna-joeljota.md`, as seções §3 (regras), §4 (ganchos), §9 (anatomia motivacional) e §12 (conflitos). As outras seções do dna, quando precisar de número ou de exceção.
3. **A mensagem.** Escreva a tese numa frase de até 12 palavras, dita para um "você" sobre algo concreto da vida (filho, corpo, sono, casa, dinheiro, palavra, cansaço, trabalho que pesa na vida). Tema de negócio ou IA tem de pousar na vida, com o negócio como exemplo de passagem (dna §12.11): só 1 dos 30 virais é de negócio.
4. **O ângulo.** Procure a virada de lente que os maiores vídeos têm (dna §9): o problema visto de outro lugar, não só a cobrança. Ex. de forma: o cansaço visto como a vida que você pediu; o sucesso medido em outra coisa. Esses dois ângulos são do Joel; crie o seu. Escreva o ângulo como a frase que só este roteiro diz, com um objeto ou uma pessoa que o pedido não nomeia (quem paga a conta, quem lê o resultado, o que muda no dia seguinte). A Mensagem é essa frase; a metade de cartaz, que qualquer post sobre o tema diria, fica fora dela.
5. **Filtro da mensagem** (seção 4). 16 ou mais vira roteiro; de 12 a 15, reescreva o ângulo ou troque a prova; 11 ou menos, descarte e proponha outra mensagem.
6. **Molde.** Escolha pela tabela e pela lista "Qual escolher" de `moldes.md` §1 (J1 a J9). As batidas do molde contam o que costuma aparecer no Joel, não uma lista a cumprir: junte, pule ou troque. Os roteiros de `moldes.md` §8 mostram quanto a forma varia de um vídeo para outro; nenhum é esqueleto, e nenhuma frase deles entra no roteiro.
7. **Prova.** Na ordem de preferência: (a) fato real do Adriel, em uma linha, com número e unidade; se você não souber, a lacuna (abaixo); (b) cena em 2ª pessoa, junto da lacuna ou das frases em "eu", nunca no lugar delas ("Você [ação concreta] às [hora]..."); (c) caso real de terceiro, com fonte e crédito; (d) fábula tradicional de domínio público, com a origem dita, recontada com palavras próprias. Dado do mundo (estatística, estudo, fato histórico) só com fonte primária e data, conferido na hora com WebSearch (carregue com ToolSearch `select:WebSearch,WebFetch` se estiver adiado) e dito na fala; sem fonte, o dado sai. Número hipotético é anunciado como hipótese ("imagina dez pessoas...").
   - **Lacuna.** Sem a história real, deixe "[sua história real, em 1ª pessoa: ...]" onde ela servir e diga no "Antes de gravar" o tipo de história que prova a tese: o dano que o Adriel pagou por não seguir a ordem ou o que mudou quando seguiu (o "eu adoeci" de DW6yafsgCVe). A fala tem de fazer sentido sem a lacuna, e a frase logo depois dela repete o substantivo, não o pronome ("o seu filho", não "ele").
   - **"Eu".** Entra onde for verdade, na prova ou na opinião, sem posição fixa e sem número mínimo; "eu acredito", no máximo 1 vez. Toda frase em "eu" que afirma fato ou hábito vai para o "Antes de gravar". Fora: o conselho a si mesmo pelo nome ("[A ordem], Adriel."), que é a batida de DW6yafsgCVe, e "eu não tô dizendo [X], tô dizendo [Y]", que é "não é X, é Y".
8. **Ouvido.** Antes de escrever, leia inteira a seção Transcrição de 2 ou 3 fichas do Joel em `dados/fichas/<código>.md`: uma do molde escolhido e pelo menos uma de corte improvisado (CgPSTknA2SC, CymNEmcJKCh, C25NpotAcrA, CY1j1c9pRgQ, DW6yafsgCVe). Serve para pegar o ritmo, a aspereza e o jeito de emendar e repetir; nenhuma frase delas entra no roteiro (o `checar_copia.py` confere). Os monólogos roteirizados de 2025 e 2026 (DQF9FQKgEMw, DOMoAzKgAbX) servem só para a ordem das batidas: lidos como texto, soam polidos demais.
9. **Escrita.** O gancho sai da Mensagem, nunca do pedido: traz o objeto ou a pessoa do ângulo. Se ele for o pedido virado em ordem ("cuidar da saúde" vira "Faz o seu exame"; "culpa por trabalhar fora" vira "Não pede desculpa por trabalhar") ou couber no cartaz da campanha do mês, reescreva; se um gancho alternativo abre pelo ângulo e o principal não, troque os dois. O resto segue a ordem que a fala pedir e para quando a ideia acaba. Duração = (palavras da fala + 20 por lacuna) ÷ velocidade do molde (mensagem 175/min, bronca 230, leitura 150) × 60, mais 1 s por [pausa]; passou do teto do molde, corte.
10. **Conferência.** Passe o checklist da seção 8. Rode o `checar_copia.py` pela entrada padrão, sem criar arquivo (ele marca "COPIADO" quando acha 6 palavras seguidas do Joel e sai com código 1; marca "DO MOLDE", só como aviso, quando acha 4 palavras iguais aos exemplos dos moldes). O `sed` tira tudo entre colchetes (lacuna, [pausa], [cena]), que gera "DO MOLDE" falso:
   ```bash
   sed 's/\[[^]]*\]//g' <<'EOF' | python3 ~/.claude/skills/joeljota/scripts/checar_copia.py -
   [a fala, a capa, a legenda e os ganchos alternativos; nenhum campo do formato]
   EOF
   ```
   "COPIADO" é reescrito sempre; "DO MOLDE" é reescrito quando veio de um exemplo dos moldes (marcador genérico de até 5 palavras pode ficar). Leia a fala em voz alta; travou ou soou como texto escrito, reescreva.
11. **Entrega** no formato da seção 6. Antes, releia a fala inteira: nenhuma frase contradiz outra. Se o Adriel pedir para salvar num caminho, salve lá e confira com `ls`; se a gravação for negada, diga isso em 1 linha e traga a entrega inteira na resposta.

## 4. O estilo em uma tela

As regras descrevem tendências do Joel, não um formulário. Um roteiro bom usa bem 4 ou 5 delas, não todas. Nenhuma frase-modelo desta skill ou dos moldes entra no roteiro. A prova de cada regra vem entre parênteses (dna §3 e §9; "x" = views ÷ mediana do perfil).

1. **Fala no segundo 0, sem saudação.** A 1ª palavra sai em 0,0 s em 54 de 59 vídeos dele.
2. **Tema claro até 3 s.** A 1ª frase diz o tema: tese de cara ou moldura que nomeia o tema abrem 22 de 30 virais, e o assunto fica claro em 2,0 s (mediana), nunca depois de 5 s no topo. Os tipos fortes são ordem, sentença, meta ("Esse vídeo é pra quem..."), espelho (a queixa de quem assiste, em 1ª pessoa) e profecia. Pergunta e condicional são as aberturas mais fracas do topo (11,1x e 11,3x; nenhuma no top 10).
3. **"Você" e uma coisa concreta logo no começo.** Os 3 mais vistos falam de filho, cansaço e saúde. A 1ª frase traz o objeto do tema (o exame, o filho, a conta), não só o rótulo ("empreender", "disciplina") nem só a ferramenta (agenda, IA, celular).
4. **Tema de vida.** 29 dos 30 virais. Negócio fica abaixo da mediana nos recentes.
5. **Repetição em rajada, curta, sem frase-título.** 29 de 43 gravações repetem a mesma abertura de oração 3 vezes ou mais, cada vez com uma continuação nova ("pra quem" em CmrRO80B1CJ, "eu pedi" em CymNEmcJKCh; dna §3.6). A cabeça é curta (1 a 4 palavras), vem em frases coladas, com itens de tamanhos diferentes, e sai de cena quando a ideia anda. A frase inteira do gancho não vira refrão: no 1º teste cego, o sinal de IA mais citado foi a série simétrica; no 2º e no 3º, a frase do gancho repetida 4 a 8 vezes, abrindo e fechando o roteiro.
6. **Frase curta, com uma longa emendada de vez em quando.** Mediana de 8 palavras por frase; 21 de 28 vídeos dele de 28 a 65 s têm pelo menos uma frase de 20 palavras ou mais, emendada como fala, com "e", "aí" e "porque", sem oração subordinada de texto escrito. No 2º teste cego, "frases curtas sempre do mesmo tamanho" denunciou 2 dos 5 roteiros. Frase de efeito é rara; o resto é frase simples, com a palavra da tese repetida em vez de sinônimo. Fora: antítese que redefine a mesma palavra em dois tempos ou lugares, que soa como "não é X, é Y", e quiasmo ("Faz o seu exame. Ou o seu corpo faz por você.").
7. **Voz encenada, no máximo 2 rodadas, sem esquema de objeção e resposta.** A desculpa de quem assiste, a frase que a pessoa vai repetir, a voz de outra pessoa: 21 de 43 gravações. Entra crua, sem moldura nova a cada rodada, e não vira uma objeção que o roteiro rebate ponto por ponto (réplica a cada desculpa, a 2ª desculpa igual à 1ª com um pedaço a mais, resposta que concorda e explica). No 2º teste cego, esse esquema leu como quebra de objeção de copy nos 5 roteiros.
8. **Concreto, nenhum estudo.** Nenhuma fala dele cita pesquisa; a força vem do objeto do dia a dia, dito seco (a comida, a conta, o celular, o exame). Detalhe escolhido para parecer real (preço exato, dia da semana, marca, gesto de cena) só vem de fato real, do Adriel ou de fonte; os do Joel (roupão, 22 kg, 2h25 da madrugada) são biografia dele. Ele não diz "mindset", "motivação", "inspiração", "resiliência", "felicidade" nem "eu acho"; para opinião, "eu acredito", no máximo 1 vez.
9. **Virada perto do meio** (26 de 45 roteiros, mediana em 45%): um fato ou uma cena que muda o peso do que veio antes.
10. **Fecho curto, sem pedido falado.** O último trecho dele tem mediana de 5 palavras, sai mais grave e mais lento e varia: máxima ou sentença em 15 a 19 de 45 roteiros, ordem em cerca de 10, frase em "eu" em 6, eco da 1ª frase em só 5 (dna §5). Varie também: uma ordem seca, a ordem do gancho, uma frase dura ou simplesmente parar quando a ideia acaba. Nunca uma frase-slogan nova na última linha nem o círculo perfeito, com a frase-título abrindo e fechando (no 3º teste cego, "Eu [verbo do gancho]" fechou os 7 roteiros e foi lido como círculo ou assinatura). Nenhum dos 31 vídeos únicos do topo e do grupo motivacional pede comentário na fala.
11. **Fala contínua, uma pausa que pesa.** Cerca de 175 palavras/min, fala em 99% do vídeo; quando há palavra-recompensa, uma pausa de cerca de 1 s antes dela. O volume quase não varia: a força vem da frase curta e do freio no fecho, não de grito.
12. **Plano único nos 3 s iniciais, legenda desde o quadro 0** (25 de 30 virais). Corte depois disso: efeito inconclusivo; quando houver, que mostre a prova.

**Filtro da mensagem** (heurística tirada dos números acima; 0 a 3 cada, máximo 24): tema de vida que serve a qualquer adulto (peso 2); tese dita no 1º segundo, em ordem, sentença, meta, espelho ou profecia (peso 2); ângulo virado, que vê o problema de outro lugar e não só cobra; concreto (objeto, número com unidade ou cena do dia a dia); voz encenada ou espelho de quem assiste; âncora real (prova do Adriel, caso com fonte ou data verdadeira; 9 dos 11 vídeos de 10 mi ou mais com ele falando têm imagem real, data do calendário ou nome próprio).
Réguas: lacuna "[sua história real]" vazia vale 0 em âncora; data real do mês vale 2 só quando a mensagem é sobre o assunto dela. Detalhe de enfeite não soma em "concreto". Tema de negócio, IA ou trabalho vale no máximo 2 em "tema de vida" (1 se o negócio é o assunto central). "Tese no 1º segundo" só leva 3 se a 1ª frase traz a tese, e não só o nome do tema. "Ângulo virado" vale no máximo 2 se for lugar-comum conhecido (cumprir com os outros e falhar consigo). O corte de 16 do passo 5 vale para a nota sem a história. Menos 3 pontos: lista de virtudes sem objeto, tese genérica, pergunta na abertura, anúncio ou saudação. Zera: fato inventado, história do Joel, bordão de marca dele.

## 5. Quem grava e o que fica de fora

**Do Joel, fica de fora** (dna §12; lista completa em `moldes.md` §5):
- a biografia e as histórias pessoais dele (natação, 2011, a mãe na porta, os filhos pelo nome, a arena, a fila de autógrafos), as credenciais e os números públicos dele;
- a cena dele remontada pelos objetos, também na lacuna e no "Antes de gravar": mãe, porta, hora e ida ao trabalho (C5wH0MUAoG7); 2011, os 22 kg e o nódulo; o roupão; a fila de autógrafos; a arena. O pedido da lacuna diz qual lado da tese a história prova e não sugere esses objetos;
- o esqueleto do vídeo dele de tema vizinho. Dizer não e limites: DW6yafsgCVe, COQVncuHVnK, CeeACBWl5vT; cansaço e custo do que pediu: CymNEmcJKCh, DdeyF9BMO9v; reclamar e escolha: C25NpotAcrA; filhos como medida de sucesso: CgPSTknA2SC; a palavra e a boca: C4eRAX6RnFR; encerrar ciclo: C4CAfFdgCtn; não desistir: DQF9FQKgEMw; pagar o preço: DUWtkSmAJI9. Nesses temas, o roteiro não usa as batidas próprias do vídeo (no DW6yafsgCVe, "Você vai [doença]" como dano e a ordem dita a si mesmo pelo nome) e, se ele é a referência de textura do molde, troque a referência;
- os bordões de marca, nem em paráfrase próxima: "o trabalho devolve", "o sucesso é treinável", a chuva e a lama, o "dia 1", saúde, família e trabalho com o "não inverta", "o ambiente treina", "não enche o saco", "não engula sapo", "o campeão não se surpreende", "quem decide até pode errar", "VALENDO", "EU VOU", "alta performance", os nomes de produto;
- trechos dele com mais de 5 palavras seguidas (o `checar_copia.py` confere);
- react de vídeo de terceiros e texto com direito autoral na legenda.

**Do Joel, fica a mecânica:** abrir com a tese, repetir uma cabeça, encenar a voz do outro, virar a lente, fechar curto e grave. Admitir o custo de seguir a ordem é opcional; quando houver, vai numa frase própria e natural, sem o par "Eu sei que... assim mesmo" ou "ainda assim" (nas 70 transcrições dele, "eu sei que", "assim mesmo" e "mesmo assim" não aparecem, e "ainda assim" sai só numa leitura, CrgWhAFA_KG). Crie 1 ou 2 máximas do Adriel e recicle entre vídeos, como o Joel faz com as dele.

**Voz e marca do Adriel** (iguais às da `modelagem`, seção 5):
- Nunca "não é X, é Y" nem as variações ("não é sobre X, é sobre Y", "parece X, mas não é"). No Joel, a forma aparece em 11 de 61 vídeos e nunca nos dois mais vistos. No lugar: "Quem [A], [B]. Quem [C], [D]."; a concessiva que admite o limite e afirma; duas cenas lado a lado; a definição direta; "em vez de [comum], [melhor]".
- Sem pergunta que o próprio narrador responde ("Por quê? Porque..."): deixe só o "porque" depois da ordem. Sem três fragmentos seguidos. Sem muleta de atenção ("se liga", "olha só", "presta atenção", "deixa eu te contar"). Sem "segredo", "tem nome", "a verdade é que", travessão, "num mundo onde", palavra de manual.
- "Você" no singular; nada de "gente", "pessoal", "galera", "tu", "mano" nem palavrão. Vocativo no máximo "cara", 1 ou 2 vezes. A aspereza vem da verdade dura em frase curta, sem rótulo pessoal.
- Contrações (tá, pra, pro, tô, né) e costura com "porque", "então", "aí", "só que". As marcas de fala que o Joel tem e a voz do Adriel aceita (o sujeito repetido com pronome, "o seu corpo, ele", dna §6; a mesma frase dita duas vezes seguidas; o recomeço, "Você vai... você vai pagar isso no corpo."; a ordem refeita com a mesma palavra e outro verbo) entram onde sairiam sem querer, nunca por cota: no 3º teste cego, as marcas plantadas foram lidas como figurino. O imperativo sai na forma coloquial (faz, compara, larga) do começo ao fim, sem misturar com "faça, compare" no mesmo roteiro (no 3º teste, o mesmo verbo nas duas formas denunciou 4 de 5 roteiros). Os vocativos de camarada (velho, irmão, mano) e as muletas (se liga, olha só, repara), cuja falta o juiz cego notou, seguem fora. "Pô" ou "ó", no máximo 1 vez, se for natural.
- Nunca prometa valor de ganho (reais, %, "x vezes", prazo de resultado), nem dentro da cena em 2ª pessoa nem na máxima, que tem de ser verdadeira ao pé da letra. Frase que precisaria de ressalva no "Antes de gravar" é reescrita. Fé no fecho só se for crença dele; se não souber, feche pela regra 10 da seção 4.

## 6. Formato de entrega

```markdown
## "[Título curto: a mensagem]"

**Mensagem:** [a tese pelo ângulo, numa frase de até 12 palavras, com o objeto ou a pessoa que o pedido não nomeia]
**Molde:** [J1 Mandamentos] · referência: [código do vídeo do Joel] · **Filtro:** [16]/24 = vida [2]x2 · tese [2]x2 · ângulo [2] · concreto [3] · voz [3] · âncora [0] (com a história: [18])
**Duração:** [~45 s com a lacuna, ~41 s sem · ~130 palavras com a lacuna] · **Tom:** [conversa firme; acelera no meio; freia no fecho]

[cena: plano único, do peito para cima, olhar na lente, fundo liso]
"[1ª frase: o gancho, no segundo 0.]

[Parágrafos curtos, um por batida do molde, com a cabeça repetida. [pausa] no máximo 2 vezes.]

[Fecho em até 7 palavras.]"

**Texto na tela:** legenda da fala desde o 1º quadro, 1 a 3 palavras por tela; palavra-chave destacada: "[palavra]"
**Capa:** "[até 6 palavras, ordem ou tese]"
**Legenda do post:** [1 ou 2 frases, até 15 palavras: a moral como ordem ou sentença em "você". Sem hashtag. Pedido só se fizer sentido: "Marque [quem precisa ouvir isso]."]
**Como falar:** [1 ou 2 linhas: velocidade, onde acelerar, onde frear, onde fica a pausa]
**Ganchos alternativos:** 1. [tipo]: "[gancho]" · 2. [tipo]: "[gancho]" · 3. [tipo]: "[gancho]"
**Antes de gravar:** [o que preencher ou conferir: a história real nas lacunas, em 1ª pessoa; cada frase em "eu" que afirma fato ou hábito (confirme ou troque por uma sua); o número, a fonte, a data]
```

- A fala vai entre aspas, em parágrafos curtos, com no máximo 3 [cena: ...]. Nenhum pedido falado em vídeo de mensagem (dna §3, regra 12).
- Duração: o topo do Joel fica entre 30 e 60 s. O padrão é de 35 a 60 s (100 a 175 palavras); história completa ou mandamento de data, até 90 s; curto, de 15 a 24 s.
- Entregue só o roteiro pronto; o checklist da seção 8 é interno.

## 7. Modos

### escolha (sem tema)
1. `date`. Proponha 3 mensagens de vida com ângulo próprio, de temas que viralizam no Joel (dna §8): cansaço e esforço, a palavra e a boca, saúde e corpo, filho e casa, dinheiro e escolha, recomeço. Se houver data real na semana (segunda-feira, fim de mês, data comemorativa), uma delas pode usar.
2. Para cada uma: a 1ª frase, o molde, a nota no filtro. Escreva o roteiro completo da maior nota e ofereça as outras.

### tema
1. `date`. Se o tema vier abstrato ("disciplina", "foco"), ache a coisa concreta da vida em que ele aparece e escreva a mensagem sobre ela.
2. Siga o fluxo da seção 3 e entregue 1 roteiro com 3 ganchos alternativos de tipos diferentes.
3. Se o tema for oferta, lançamento ou evento, diga em 1 linha que no Joel esse tipo rende abaixo da mediana (anúncio: 0,3x) e proponha a mensagem de vida que leva até a oferta na legenda.
4. Se o tema pedido já é ideia batida (moldes §7, Não faça 18) ou fala do Joel (disciplina quando ninguém olha e pagar o preço, DUWtkSmAJI9; não desistir hoje, DQF9FQKgEMw; quem reclama perde, C25NpotAcrA), essa ideia não aparece nem em paráfrase no gancho e na 2ª frase: entre direto pelo ângulo próprio.

### curto
1. Molde J3 (regra de bolso) ou J1 compacto: gancho, 4 a 7 frases, fecho; 40 a 70 palavras; de 15 a 24 s com a lacuna, somando os freios do "Como falar" (trecho "bem mais devagar" conta o dobro; cada repetição lenta, mais 0,5 s). No curto, a voz tem no máximo 1 rodada, e a frase longa não é exigida. O gancho nomeia o que está em jogo (filho, corpo, casa, dinheiro, alguém que espera), além da ferramenta.
2. A frase de impacto tem de ser do Adriel: nada de máxima batida (moldes §7, Não faça 18) nem bordão do Joel, e o mesmo filtro vale para os ganchos alternativos, a capa e a legenda.

### ganchos
1. 10 ganchos para o tema, de pelo menos 5 tipos de `moldes.md` §3 (ordem, sentença, profecia, espelho, meta, condicional, moldura, caso; a cena em 2ª pessoa é subtipo do espelho, na forma do nº 21, e a "cena" do dna §4 é outra pessoa falando primeiro). Cada um com o tipo, a tese implícita em até 8 palavras e o tempo até a promessa (a 175 palavras/min).
2. Por gancho: "você" ou imperativo nas 3 primeiras palavras (na moldura e no caso, "você" ou "pra você" na 1ª frase); ordem e sentença em até 5 palavras na 1ª frase; teste do cartaz (moldes §7, Não faça 18); nenhum parente pressuposto vivo; nada que deixe de ser verdade antes do fim do mês; trocadilho como motor, no máximo 1 por banco. Marque o melhor pela clareza na 1ª escuta, pelo objeto e pelo que está em jogo, em 1 linha; o número do dna §4 entra como contexto, não como desempate.

### revisar
1. Leia o roteiro (texto colado ou caminho de arquivo).
2. Dê a nota no filtro e ache o molde mais próximo.
3. Rode o checklist da seção 8 e o `checar_copia.py`.
4. Entregue: (a) o diagnóstico, só com os itens que falharam, agrupados em mensagem, estrutura, voz e cópia, cada um com a correção em 1 linha; (b) a nota antes e depois; (c) a versão reescrita no formato da seção 6. Preserve os fatos reais e o jeito do autor; não invente prova.

### atualizar
1. Veja a data da última coleta (03/10/2026; confira com `ls -l ~/.claude/skills/joeljota/dados/indice.md`). Com menos de 30 dias, avise e pergunte se ele quer mesmo rodar.
2. Avise antes: leva de 2 a 3 horas num Mac de 8 GB; usa uma sessão do Instagram já logada (o script copia só cookies e preferências para uma pasta temporária e apaga no fim); no máximo uma vez por mês. Se o Chrome de automação estiver sem login, a última coleta usou o Opera GX: `IGPROFILE="$HOME/Library/Application Support/com.operasoftware.OperaGX" BROWSER_BIN="/Applications/Opera GX.app/Contents/MacOS/Opera"`.
3. Com o sim dele, em ordem:
   - `bash scripts/atualizar_base.sh` (lista de reels, detalhes dos 150 mais vistos + 30 recentes, download e legendas em lotes);
   - Workflow com `scriptPath` = `scripts/wf_classificar.js` (classifica as legendas);
   - `python3 scripts/selecionar.py <journal.jsonl do workflow>` (grau motivacional e os 20 motivacionais);
   - `bash scripts/processar.sh` (transcrição com tempo por palavra, OCR, cortes, prosódia, fichas e números de linguagem);
   - Workflow com `scriptPath` = `scripts/wf_analise.js` e `args` gerados por `python3 -c "import json; s=json.load(open('$HOME/.cache/joeljota/users/joeljota.json'))['sel']; c=list(dict.fromkeys(s['viral']+s['recentes']+s['motivacionais'])); print(json.dumps({'viral':s['viral'],'recentes':s['recentes'],'motivacionais':s['motivacionais'],'lotes':[c[i:i+5] for i in range(0,len(c),5)]}))"` (reescreve `references/`);
   - copie `~/.cache/joeljota/users/joeljota.json` para `dados/joeljota.json`, refaça os preenchimentos de `moldes.md` §8 se o tom mudou, atualize a data e os números das seções 1 e 4 deste arquivo e rode `checar_copia.py` nas duas referências;
   - apague os vídeos com `rm -rf ~/.cache/joeljota/videos`.

## 8. Checklist final

É interno: na entrega, o que ficou pendente vai para o "Antes de gravar"; no modo revisar, os itens que falharam viram o diagnóstico.

- [ ] Tese pelo ângulo, em até 12 palavras, para um "você", sobre algo concreto da vida (passos 3 e 4); nota 16 ou mais no filtro.
- [ ] Ângulo próprio (o cansaço como pedido e o sucesso nos filhos são do Joel); nada reprovado no teste do cartaz nem ideia já dita pelo Joel (moldes §7, Não faça 18), também nos ganchos alternativos, na capa e na legenda.
- [ ] Uma ideia só; o gancho sai da Mensagem, não do pedido virado em ordem (passo 9).
- [ ] Fala no 0 s, "você" e o objeto do tema no começo, tema claro até 3 s.
- [ ] Fecho curto, sem pedido falado, sem slogan novo nem círculo com a frase-título.
- [ ] Toda prova é do Adriel (ou lacuna marcada), de terceiro com fonte ou fábula de domínio público; nenhum número ou estudo sem fonte e data (passo 7); nenhum detalhe de enfeite sem fato por trás; data do calendário só quando é o assunto (passo 1).
- [ ] Toda afirmação sobre quem assiste vale para a maioria de quem tem o problema, ou o gancho nomeia o subtipo; nenhum parente pressuposto vivo ou por perto ("o remédio da sua mãe"): use condicional ou "um dia"; nada que deixe de ser verdade antes do fim do mês.
- [ ] Nada do que a seção 5 deixa de fora do Joel (biografia, cena remontada pelos objetos, esqueleto de vídeo de tema vizinho, bordões), também na lacuna e no "Antes de gravar"; `checar_copia.py` sem nenhum "COPIADO".
- [ ] Nenhuma frase-modelo desta skill nem frase dos exemplos dos moldes ("DO MOLDE" reescrito, passo 10).
- [ ] Nenhuma promessa de ganho nem de prazo de resultado; nada que precise de ressalva no "Antes de gravar" (seção 5).
- [ ] Voz do Adriel pela seção 5: nada do que ela proíbe, contrações, "você" no singular, o imperativo numa forma só; nenhuma palavra de autoajuda genérica (moldes §7, Não faça 6).
- [ ] Lido em voz alta sem travar e sem soar como texto escrito.
- [ ] Mensagem, Molde, Filtro, Duração (conta do passo 9), Tom, fala entre aspas com no máximo 3 [cena: ...] e 2 [pausa], Texto na tela, Capa, Legenda, Como falar, 3 ganchos alternativos e Antes de gravar.

## 9. Mapa dos arquivos

```
joeljota/
├── SKILL.md                    este manual
├── README.md
├── references/
│   ├── dna-joeljota.md         o estilo medido: 15 regras, ganchos, estrutura, voz, retórica, crenças, motivacional, visual, conflitos
│   └── moldes.md               9 moldes (J1 a J9), 35 ganchos, 23 frases de impacto e fechos, bordões, direção, faça e não faça, exemplos de vida (§8)
├── scripts/
│   ├── checar_copia.py         confere se um texto repete 6 palavras seguidas do Joel ou 4 dos exemplos dos moldes
│   ├── atualizar_base.sh       coleta do Instagram (lista, detalhes, download, legendas em lotes)
│   ├── wf_classificar.js       workflow: classifica as legendas (tema e grau motivacional)
│   ├── selecionar.py           grava a classificação e escolhe os 20 motivacionais
│   ├── processar.sh            transcrição com tempo por palavra, OCR, cortes, prosódia, fichas, linguagem
│   ├── wf_analise.js           workflow: análise vídeo a vídeo, 8 frentes, verificação, síntese e crítica
│   └── (peças)                 detalhes.mjs, transcrever_corpus.py, prosodia.py, fichas.py, linguagem.py
│                               (reaproveitam collect, download, OCR e cortes da skill modelagem)
└── dados/                      base de 03/10/2026 (consulta; não editar à mão)
    ├── indice.md               números de todos os 70 vídeos e do perfil
    ├── linguagem.md            tamanho de frase, pessoa, contrações, perguntas, n-gramas
    ├── prosodia.md             início da fala, palavras/min no início, meio e fim, pausas, volume
    ├── pesquisa-web.md         quem é o Joel, com fontes (contexto, não estilo)
    ├── fichas/                 uma ficha por vídeo (transcrição, legenda, texto na tela); só local
    ├── midia/                  quadro do gancho, prancha de 8 quadros e capa de cada vídeo; só local
    └── joeljota.json           todos os reels com views, detalhes e classificação; só local
```
