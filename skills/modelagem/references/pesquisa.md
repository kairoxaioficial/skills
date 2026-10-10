# Pesquisa e checagem: só fato real, com fonte e data

Os cinco criadores modelados ganham alcance com **novidade**, **número** e **demonstração**. Por isso a pesquisa vem antes do roteiro, e nenhum dado entra no vídeo sem fonte e data conferidas.

## 1. Regras de ouro

1. **Descubra a data de hoje antes de tudo** (`date` no terminal). O que o modelo "sabe" pode estar velho; notícia de IA envelhece em dias.
2. **Todo número, data, preço, nome de produto, recurso ou estatística** precisa de uma fonte primária (anúncio oficial, documentação, relatório original) **ou** de duas fontes independentes confiáveis. Anote link e data de publicação de cada uma.
3. **Não achou fonte? O dado sai do roteiro.** Nunca estime, arredonde para cima nem "complete" um número.
4. **Separe anúncio de disponibilidade.** Anunciado não é lançado; lançado nos EUA não é disponível no Brasil; beta não é versão final; grátis com limite não é grátis. Diga no roteiro o que vale para quem assiste no Brasil.
5. **Preço em dólar vira contexto, não promessa.** Se citar valor, diga a moeda e a data do preço.
6. **Nada de promessa de ganho financeiro** ("você vai faturar R$ 10 mil"). Mostre o mecanismo e o caso real com fonte, nunca o resultado garantido.
7. **Print viral não é fonte.** Confirme na conta ou no site oficial. Se for vídeo feito com IA, confirme a ferramenta e o autor original e dê o crédito.
8. **Nome do produto escrito como a empresa escreve** (ChatGPT, Gemini, NotebookLM, n8n, Claude, Veo, Sora, Midjourney...).
9. **Cite falando, como os criadores fazem**: "a própria Google anunciou ontem", "segundo o relatório da McKinsey deste ano". No fim do roteiro, liste as fontes com link e data.

## 2. Onde pesquisar (nesta ordem)

**Radar rápido (manchetes datadas, Brasil e EUA):**

```bash
python3 ~/.claude/skills/modelagem/scripts/radar.py 7             # últimos 7 dias
python3 ~/.claude/skills/modelagem/scripts/radar.py 3 "Sora" "n8n" # 3 dias + termos extras
```

O radar lê o Google News (pt-BR e en-US) e as buscas em alta do Google Trends Brasil. Ele serve para **achar** a pauta; a checagem vem das fontes abaixo. Os links do Google News são redirecionamentos: para ler a matéria, busque o título com WebSearch ou abra o site do veículo.

**Fonte primária (sempre que existir):** blog ou newsroom oficial da empresa (OpenAI, Google e DeepMind, Anthropic, Meta, Microsoft, Apple, NVIDIA, xAI, Mistral, DeepSeek, Alibaba/Qwen, ByteDance, Runway, Midjourney, ElevenLabs, HeyGen, Perplexity, Canva, CapCut, n8n, Make, Zapier), changelog, documentação, página de preços, repositório no GitHub, perfil oficial no X ou Threads.

**Imprensa de tecnologia:** The Verge, TechCrunch, Ars Technica, Wired, Reuters, Bloomberg, The Information, VentureBeat, 9to5Mac, 9to5Google, Engadget. No Brasil: Tecnoblog, Olhar Digital, Canaltech, TecMundo, Exame, InfoMoney, Valor Econômico, Folha, Estadão, g1, StartSe, Mobile Time.

**Dados e pesquisas (para ganchos com número):** Stanford AI Index, McKinsey State of AI, Microsoft Work Trend Index, Gartner, IDC, Pew Research, LinkedIn Economic Graph, a16z Top 100 GenAI Apps, Similarweb, Sensor Tower, Cetic.br (TIC Empresas e TIC Domicílios), IBGE, Sebrae, FGV, CNI, Datafolha, Google Trends Brasil.

**Termômetro do que está bombando:** Google Trends Brasil, busca do próprio Instagram e do TikTok, Product Hunt, GitHub Trending, Hugging Face (modelos em alta), LMArena (ranking de modelos), X e Reddit (r/ChatGPT, r/singularity, r/LocalLLaMA).

WebSearch devolve resultados dos EUA; para notícia brasileira, prefira o radar e o WebFetch direto no site do veículo.

## 3. Da notícia à pauta: o filtro de viralidade

Dê de 0 a 3 pontos em cada critério. Só vira roteiro o que somar **10 ou mais**:

| Critério | 0 | 3 |
|---|---|---|
| Novidade | notícia de mais de um mês | saiu nas últimas 72 horas |
| Bolso ou negócio do público | curiosidade técnica | mexe em dinheiro, emprego, cliente ou tempo de quem assiste |
| Dá para mostrar | só conceito | tem vídeo, resultado ou antes e depois que cabe na tela |
| Choque ou surpresa | esperado | parece mentira até ver a prova |
| Cabe em 30 a 60 segundos | precisa de aula | uma ideia, um exemplo, uma consequência |

Os temas que mais somam nos dados dos cinco criadores estão em `dna-dos-criadores.md` (seção de temas).

## 4. Checklist de fatos antes de entregar

- [ ] Data de hoje conferida e "ontem", "essa semana" corretos em relação a ela.
- [ ] Cada número do roteiro tem fonte e data no bloco FONTES.
- [ ] Disponibilidade no Brasil, idioma e preço conferidos (ou o roteiro diz que ainda não chegou).
- [ ] Nenhum superlativo sem prova ("a melhor IA do mundo" só com ranking citado).
- [ ] Nenhuma promessa de ganho em reais.
- [ ] Crédito dado quando o exemplo mostrado é trabalho de outra pessoa.
