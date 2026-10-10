export const meta = {
  name: 'joeljota-classificar',
  description: 'Classifica pela legenda os 184 reels coletados do @joeljota (tema e grau motivacional)',
  phases: [{ title: 'Classificar', detail: '6 lotes de ~31 legendas' }],
}
const W = '/Users/adriel/.cache/joeljota/legendas'
const SCHEMA = {
  type: 'object',
  properties: {
    videos: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          code: { type: 'string' },
          categoria: { type: 'string', enum: ['motivação e mentalidade', 'alta performance e hábitos', 'negócios, vendas e liderança', 'dinheiro e carreira', 'família e relacionamentos', 'fé e espiritualidade', 'saúde, corpo e esporte', 'humor e entretenimento', 'bastidores e vida pessoal', 'oferta e divulgação', 'outro'] },
          subtema: { type: 'string', description: 'até 6 palavras' },
          motivacional: { type: 'integer', minimum: 0, maximum: 3 },
          mensagem: { type: 'string', description: 'ideia central parafraseada, até 20 palavras' },
          emocao: { type: 'string', description: 'emoção dominante, até 4 palavras' },
        },
        required: ['code', 'categoria', 'subtema', 'motivacional', 'mensagem', 'emocao'],
      },
    },
  },
  required: ['videos'],
}
const prompt = k => `Você classifica reels do Joel Jota (@joeljota, criador brasileiro de alta performance) pela LEGENDA do post.

Leia com Read o arquivo ${W}/lote-${k}.md. Cada vídeo começa com "## <código>" e traz views, data, duração, coautores, se tem música licenciada e a legenda.

Devolva UM item para CADA código do arquivo, sem pular nenhum:
- categoria: o assunto principal.
- subtema: até 6 palavras.
- motivacional (0 a 3):
  0 = não é motivacional (informa, ensina técnica, entretém, divulga oferta, evento, convidado ou podcast);
  1 = tem uma lição de vida no fundo, mas o foco é ensinar ou informar (ex.: dica de liderança com uma moral);
  2 = motivacional: o objetivo principal é mover a pessoa a mudar ou agir com uma mensagem de vida (disciplina, persistência, propósito, família como motivo, superação, responsabilidade, fé);
  3 = mensagem motivacional pura: frase de impacto, exortação, reflexão de vida curta e forte, "mensagem para você", fábula ou história com moral.
- mensagem: a ideia central parafraseada em até 20 palavras. Não copie a legenda.
- emocao: emoção dominante em até 4 palavras.
Se a legenda for vaga, use a duração, os coautores e o tom para decidir e prefira o grau mais baixo na dúvida.`
phase('Classificar')
const res = await parallel([1, 2, 3, 4, 5, 6].map(k => () => agent(prompt(k), { label: `lote ${k}`, phase: 'Classificar', schema: SCHEMA, model: 'sonnet' })))
const videos = res.filter(Boolean).flatMap(r => r.videos)
log(`${videos.length} classificados`)
return { videos }