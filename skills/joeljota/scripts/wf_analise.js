export const meta = {
  name: 'joeljota-analise',
  description: 'Engenharia reversa do estilo do @joeljota: vídeo a vídeo, 8 dimensões, verificação adversarial, síntese das referências e crítica',
  phases: [
    { title: 'Vídeo a vídeo', detail: 'análise de cada um dos 70 reels (lotes de 5)' },
    { title: 'Dimensões', detail: '8 analistas cruzam todos os vídeos' },
    { title: 'Verificar', detail: 'um cético por dimensão tenta refutar as afirmações' },
    { title: 'Síntese', detail: 'escreve references/dna-joeljota.md e references/moldes.md' },
    { title: 'Crítica', detail: 'crítico de completude + correção' },
  ],
}
const DIR = '/Users/adriel/.claude/skills/joeljota/dados', REF = '/Users/adriel/.claude/skills/joeljota/references'
const G = args
const grupoDe = c => ['viral', 'recentes', 'motivacionais'].filter(g => G[g].includes(c)).map(g => `${g.toUpperCase()}#${G[g].indexOf(c) + 1}`).join(' ')
const REGRAS = 'Regras de evidência: toda afirmação vem dos dados (cite códigos de vídeo e números); nada de conhecimento prévio sobre o Joel. A transcrição é do Whisper e pode errar nomes. Citação literal: no máximo 15 palavras por trecho (material de análise interno).'
const S = { type: 'string' }
const VIDEO = {
  type: 'object',
  properties: {
    videos: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          code: S, quem_fala: { type: 'string', description: 'joel | joel e outros | convidado | sem fala' }, formato: S, tema: S,
          tese: { type: 'string', description: 'a mensagem central em 1 frase, parafraseada' },
          publico: { type: 'string', description: 'com quem ele fala neste vídeo' },
          gancho: {
            type: 'object',
            properties: {
              tipo: S, molde: { type: 'string', description: 'fórmula parafraseada com [lacunas]' },
              primeira_frase: { type: 'string', description: 'até 12 palavras literais da 1ª frase' },
              segundos_ate_a_promessa: { type: 'number' }, imagem: S, texto_na_tela: S,
            },
            required: ['tipo', 'molde', 'primeira_frase', 'segundos_ate_a_promessa', 'imagem', 'texto_na_tela'],
          },
          batidas: { type: 'array', items: { type: 'object', properties: { inicio_pct: { type: 'number' }, funcao: S, resumo: S }, required: ['inicio_pct', 'funcao', 'resumo'] } },
          recursos: { type: 'array', items: S, description: 'recursos retóricos com exemplo curto (até 8 palavras)' },
          frases_de_impacto: { type: 'array', items: S, description: '1 a 3 frases mais fortes, literais, até 15 palavras cada' },
          bordoes: { type: 'array', items: S, description: 'expressões de até 5 palavras com cara de assinatura' },
          historia: { type: 'string', description: 'história contada: de quem, tipo, onde entra (%); ou "não"' },
          provas: { type: 'string', description: 'números, estudos, nomes, exemplos; se cita fonte' },
          pessoa: { type: 'string', description: 'como se dirige: você, vocês, eu, a gente, nós' },
          tom: S, intensidade: { type: 'integer', minimum: 1, maximum: 5 },
          ritmo: { type: 'string', description: 'velocidade, pausas, frases curtas x longas, repetição' },
          fecho: { type: 'object', properties: { tipo: S, molde: S }, required: ['tipo', 'molde'] },
          cta: S,
          visual: { type: 'string', description: 'enquadramento, cenário, figurino, legenda queimada, música, cenas de apoio, cortes' },
          por_que_funciona: S,
        },
        required: ['code', 'quem_fala', 'formato', 'tema', 'tese', 'publico', 'gancho', 'batidas', 'recursos', 'frases_de_impacto', 'bordoes', 'historia', 'provas', 'pessoa', 'tom', 'intensidade', 'ritmo', 'fecho', 'cta', 'visual', 'por_que_funciona'],
      },
    },
  },
  required: ['videos'],
}
const promptVideo = lote => `Você é analista sênior de vídeo curto do mercado brasileiro e está fazendo a engenharia reversa do estilo do Joel Jota (@joeljota) para que outra pessoa consiga escrever roteiros no estilo dele.

Para CADA código abaixo:
1. Leia com Read a ficha ${DIR}/fichas/<código>.md inteira (métricas, legenda do post, texto na tela, transcrição com tempo [m:ss]).
2. Olhe com Read ${DIR}/midia/<código>.hook.jpg (o que aparece em 0,4 s) e ${DIR}/midia/<código>.sheet.jpg (8 quadros espalhados pelo vídeo).
3. Preencha a análise. Batidas = a espinha do vídeo, cada uma com início em % da duração e a função (gancho, contexto, história, virada, tese, prova, exortação, frase final, pedido etc.). "segundos_ate_a_promessa" = em que segundo fica claro do que o vídeo trata. "quem_fala" = quem fala a maior parte do tempo (se for outra pessoa, diga quem, pelo que a ficha e as imagens mostram).
${REGRAS}

Códigos e grupos (VIRAL#n = n-ésimo mais visto de todos os tempos; RECENTE#n = n-ésimo mais recente; MOTIVACIONAL#n = n-ésimo motivacional mais visto fora dos outros dois grupos):
${lote.map(c => `- ${c} ${grupoDe(c)}`).join('\n')}`

phase('Vídeo a vídeo')
const porLote = await pipeline(G.lotes, lote => agent(promptVideo(lote), { label: `vídeos ${lote[0]}…`, phase: 'Vídeo a vídeo', schema: VIDEO, model: 'sonnet' }))
const analises = porLote.filter(Boolean).flatMap(r => r.videos).map(v => ({ ...v, grupos: grupoDe(v.code) }))
const faltam = G.lotes.flat().filter(c => !analises.some(v => v.code === c))
if (faltam.length) log(`sem análise vídeo a vídeo: ${faltam.join(', ')}`)
log(`${analises.length} vídeos analisados`)
const JSON_ANALISES = JSON.stringify(analises)

const DIMS = [
  { key: 'ganchos', foco: 'GANCHOS E OS 3 PRIMEIROS SEGUNDOS: tipos de abertura com contagem por grupo, fórmulas (moldes parafraseados com [lacunas]), tempo até a promessa, o que aparece na imagem e no texto da tela, qual tipo acompanha mais views (múltiplo da mediana).' },
  { key: 'estrutura', foco: 'ESTRUTURA, ARCO E RETENÇÃO: espinhas típicas em batidas com % de tempo; 5 a 8 esqueletos recorrentes com nome; onde entram história, virada, tese, exortação e frase final; duração e número de palavras típicos (curtos de até 20 s x médios x longos); como ele fecha; o que segura a atenção no meio.' },
  { key: 'linguagem', foco: `LINGUAGEM, LÉXICO E RITMO DA FALA: use também ${DIR}/linguagem.md (números por grupo e n-gramas recorrentes) e ${DIR}/prosodia.md (quando começa a falar, palavras/min no início, meio e fim, pausas, faixa de volume). Registro, pessoa gramatical, tamanho de frase, contrações, palavras e expressões assinatura (até 5 palavras, com em quantos vídeos aparecem), vícios de linguagem, como trata o espectador, palavras que ele NÃO usa, velocidade, pausas e repetições.` },
  { key: 'retorica', foco: 'RETÓRICA E RECURSOS DE IMPACTO: repetição e anáfora, perguntas (retóricas ou diretas), antítese e construções "não é X, é Y" (conte quantos vídeos usam), paralelismo "quem X, Y", metáforas (esporte, natação, natureza, guerra, família), números e estudos (cita fonte?), histórias (dele, de crianças, de atletas, de clientes, fábulas e parábolas, Bíblia), confronto ou provocação, humor, autoridade, imperativos. Para cada recurso: frequência, exemplo-molde parafraseado e quando ele usa.' },
  { key: 'crencas', foco: 'TEMAS, CRENÇAS E VISÃO DE MUNDO: as teses que ele defende de novo e de novo, os inimigos que ele nomeia (preguiça, desculpa, vitimismo, reclamação etc.), o que ele valoriza (disciplina, família, fé, trabalho, filhos), os temas por grupo e quais temas viralizam mais; o público e a promessa do perfil.' },
  { key: 'motivacional', foco: `ANATOMIA DO VÍDEO MOTIVACIONAL (os de intensidade alta e os do grupo MOTIVACIONAIS; use também ${DIR}/prosodia.md para ritmo, pausas e volume): arco emocional, como ele constrói a intensidade, onde sobe o tom, música, frases de impacto (moldes parafraseados), como é a frase final, o que faz a mensagem parecer impactante e não clichê; diferenças entre os motivacionais que viralizaram e os outros.` },
  { key: 'visual', foco: 'VISUAL, EDIÇÃO, LEGENDA DO POST E CTA: enquadramento, cenários, figurino, palco x podcast x selfie x treino, legenda queimada e estilo, texto fixo, música, cortes por minuto, capa; legenda do post (tamanho, estrutura, tom, hashtags, emojis, CTA, palavra-chave como VALENDO); tipos de CTA na fala e onde entram; colabs. Olhe com Read pelo menos 15 imagens .sheet.jpg de grupos diferentes em ' + DIR + '/midia/.' },
  { key: 'viral', foco: `O QUE SEPARA O VIRAL DO RESTO: compare VIRAL x RECENTES x MOTIVACIONAIS com números (views, múltiplo da mediana, likes/views, comentários/views, duração, palavras/min, formato, tema, gancho, intensidade). Use ${DIR}/indice.md. Hipóteses sustentadas por dados com códigos, e o que NÃO parece importar. Tendência de alcance ao longo do tempo.` },
]
const DIM_SCHEMA = {
  type: 'object',
  properties: {
    relatorio: { type: 'string', description: 'relatório em Markdown, denso, 1.200 a 2.500 palavras' },
    afirmacoes: {
      type: 'array',
      items: { type: 'object', properties: { afirmacao: S, evidencias: { type: 'array', items: S }, tipo: { type: 'string', enum: ['contagem', 'padrão qualitativo', 'hipótese'] } }, required: ['afirmacao', 'evidencias', 'tipo'] },
      description: '8 a 15 afirmações mais importantes para quem vai imitar o estilo',
    },
  },
  required: ['relatorio', 'afirmacoes'],
}
const VER_SCHEMA = {
  type: 'object',
  properties: {
    vereditos: { type: 'array', items: { type: 'object', properties: { afirmacao: S, veredito: { type: 'string', enum: ['confirmada', 'parcial', 'refutada'] }, correcao: S, checagem: S }, required: ['afirmacao', 'veredito', 'correcao', 'checagem'] } },
  },
  required: ['vereditos'],
}
const promptDim = d => `Você analisa o estilo do Joel Jota (@joeljota) a partir de ${analises.length} reels: os 30 mais vistos de todos os tempos (VIRAL), os 20 mais recentes (RECENTES) e os 20 motivacionais mais vistos fora desses (MOTIVACIONAIS).

Sua dimensão: ${d.foco}

Dados:
- Análise vídeo a vídeo (JSON abaixo), feita por outros analistas.
- Índice com números de todos os vídeos: ${DIR}/indice.md
- Fichas completas (transcrição com tempo, legenda, texto na tela): ${DIR}/fichas/<código>.md. Abra as fichas para conferir e contar; não confie só no JSON.
- Números da fala: ${DIR}/linguagem.md; da entrega (pausas, velocidade, volume): ${DIR}/prosodia.md
- Pesquisa web sobre ele (contexto, não estilo): ${DIR}/pesquisa-web.md
${REGRAS}
Compare sempre os grupos. Separe o que é do Joel falando do que é de convidado. Termine o relatório com "Regras práticas para escrever como ele" (5 a 10 itens).

Análise vídeo a vídeo:
${JSON_ANALISES}`
const promptVer = (d, r) => `Você é um verificador cético. Outro analista fez afirmações sobre o estilo do Joel Jota (@joeljota) na dimensão "${d.key}". Tente REFUTAR cada uma usando os dados brutos: as fichas em ${DIR}/fichas/<código>.md (transcrição, legenda, texto na tela), ${DIR}/indice.md, ${DIR}/linguagem.md e ${DIR}/prosodia.md. Para contagens, conte de novo. Procure contraexemplos fora dos vídeos citados. Na dúvida, "parcial" com a correção exata.

Afirmações:
${r.afirmacoes.map((a, i) => `${i + 1}. [${a.tipo}] ${a.afirmacao} (evidências: ${a.evidencias.join(', ')})`).join('\n')}`
phase('Dimensões')
const dims = await pipeline(
  DIMS,
  d => agent(promptDim(d), { label: `dimensão: ${d.key}`, phase: 'Dimensões', schema: DIM_SCHEMA }),
  (r, d) => r && agent(promptVer(d, r), { label: `verificar: ${d.key}`, phase: 'Verificar', schema: VER_SCHEMA }).then(v => ({ key: d.key, ...r, vereditos: v ? v.vereditos : [] })),
)
const ok = dims.filter(Boolean)
const refutadas = ok.flatMap(d => d.vereditos.filter(v => v.veredito === 'refutada').map(v => `${d.key}: ${v.afirmacao}`))
log(`${ok.length}/8 dimensões; afirmações refutadas: ${refutadas.length}`)

const PACOTE = ok.map(d => `# DIMENSÃO ${d.key}\n\n${d.relatorio}\n\n## Verificação\n${d.vereditos.map(v => `- [${v.veredito}] ${v.afirmacao}${v.veredito !== 'confirmada' ? ` → CORREÇÃO: ${v.correcao}` : ''}`).join('\n')}`).join('\n\n')
phase('Síntese')
const sintese = await agent(`Você vai escrever as duas referências da skill /joeljota, que escreve roteiros de Reels no estilo do Joel Jota (@joeljota) com uma mensagem impactante. Quem grava os roteiros é o Adriel (não é o Joel), falando para a câmera; ele não pode usar as histórias pessoais, a biografia nem os bordões de marca do Joel como se fossem dele.

Insumos: 8 relatórios de dimensão com a verificação adversarial (abaixo). Onde a verificação marcou "parcial" ou "refutada", use a CORREÇÃO e nunca a afirmação original. Use também ${DIR}/indice.md, ${DIR}/linguagem.md, ${DIR}/prosodia.md e ${DIR}/pesquisa-web.md.

Escreva com Write, em português do Brasil, prosa clara, sem emoji:

1. ${REF}/dna-joeljota.md — o DNA do estilo, com números e códigos de vídeo como prova:
   §1 Base e limites (o que foi coletado, datas, grupos, o que os dados não dizem)
   §2 Quem é e a tese do perfil (5 linhas)
   §3 As 15 regras mais fortes do estilo (cada uma com o número ou o código que a sustenta)
   §4 Ganchos (tipos com frequência por grupo e o que viraliza)
   §5 Estrutura e arco (as espinhas com % de tempo; duração e palavras; curtos x médios x longos)
   §6 Linguagem e voz (registro, frase, pessoa, ritmo em palavras/min e pausas, bordões de até 5 palavras com contagem, o que ele não usa)
   §7 Retórica e recursos de impacto (frequência e quando usar cada um)
   §8 Crenças e temas (as teses que ele repete; os temas que viralizam)
   §9 Anatomia do vídeo motivacional
   §10 Visual, edição, legenda do post e CTA
   §11 Viral x resto x recentes (o que separa, o que não importa)
   §12 Pontos de conflito para quem modela e a recomendação para cada um (ex.: histórias pessoais do Joel; bordões de marca dele; números ou estudos sem fonte; construções que soam texto de IA como "não é X, é Y", que o Adriel não usa: registre a frequência real no Joel e dê a alternativa que mantém o efeito)

2. ${REF}/moldes.md — o kit de escrita:
   §1 Tabela de moldes (6 a 10 esqueletos com nome curto e código J1, J2..., quando usar, duração, palavras, referência de código de vídeo)
   §2 Cada molde: batidas com % de tempo, função de cada batida e frases-molde PARAFRASEADAS com [lacunas]
   §3 Banco de 30 a 40 ganchos (moldes com [lacunas], agrupados por tipo, com o código de referência)
   §4 Banco de 20 a 30 frases de impacto e fechos (moldes parafraseados com [lacunas])
   §5 Transições, marcadores de oralidade e bordões genéricos (até 5 palavras cada, com quantos vídeos usam); separe os bordões de marca do Joel, que o Adriel não deve usar
   §6 Direção de gravação (tom, intensidade, pausas, ênfases, olhar, gestos, cenário, música), texto na tela, legenda do post e CTA no padrão dele
   §7 Lista "faça" e "não faça" para soar como ele, e não como texto de IA

DIREITOS AUTORAIS (obrigatório): não copie trechos das transcrições nem das legendas com mais de 5 palavras seguidas. Bordões e marcadores de até 5 palavras podem ser citados. Todo o resto vira molde parafraseado com [lacunas].

Ao terminar, responda só com os dois caminhos e 8 bullets com os achados mais fortes.

${PACOTE}`, { label: 'síntese das referências', phase: 'Síntese' })

phase('Crítica')
const CRIT = {
  type: 'object',
  properties: { problemas: { type: 'array', items: { type: 'object', properties: { arquivo: S, secao: S, problema: S, correcao: S, gravidade: { type: 'string', enum: ['alta', 'média', 'baixa'] } }, required: ['arquivo', 'secao', 'problema', 'correcao', 'gravidade'] } } },
  required: ['problemas'],
}
const critica = await agent(`Você é o crítico de completude e correção das referências da skill /joeljota: ${REF}/dna-joeljota.md e ${REF}/moldes.md. Leia as duas inteiras. Compare com os relatórios e vereditos abaixo e com os dados (${DIR}/indice.md, ${DIR}/linguagem.md, ${DIR}/prosodia.md, fichas em ${DIR}/fichas/).
Procure: (a) afirmação sem prova ou contra um veredito; (b) achado forte dos relatórios que ficou de fora; (c) molde vago, genérico ou com cara de texto de IA; (d) trecho copiado da fala ou da legenda com mais de 5 palavras seguidas (confira nas fichas); (e) seção pedida que faltou; (f) contradição entre os dois arquivos.
Não edite nada; só liste os problemas.

${PACOTE}`, { label: 'crítico', phase: 'Crítica', schema: CRIT })
const graves = critica ? critica.problemas.filter(p => p.gravidade !== 'baixa') : []
let correcao = null
if (graves.length) {
  correcao = await agent(`Corrija com Edit os arquivos ${REF}/dna-joeljota.md e ${REF}/moldes.md conforme a lista abaixo (confira cada problema nos dados antes de mudar: ${DIR}/indice.md, ${DIR}/linguagem.md, ${DIR}/prosodia.md, ${DIR}/fichas/). Mantenha a estrutura de seções. Nada de citação literal com mais de 5 palavras seguidas. Responda com 1 linha por problema: corrigido ou não (e por quê).

${graves.map((p, i) => `${i + 1}. [${p.gravidade}] ${p.arquivo} ${p.secao}: ${p.problema} → ${p.correcao}`).join('\n')}`, { label: 'correção', phase: 'Crítica' })
}
return {
  videos: analises.length, faltam, refutadas,
  dimensoes: ok.map(d => ({ key: d.key, afirmacoes: d.afirmacoes.length, vereditos: d.vereditos.reduce((a, v) => ({ ...a, [v.veredito]: (a[v.veredito] || 0) + 1 }), {}) })),
  sintese, problemas: critica ? critica.problemas.length : null, graves: graves.length, correcao,
}