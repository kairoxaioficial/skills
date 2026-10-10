# skills

Skills de criação de conteúdo para o Claude Code, criadas sob medida para o perfil @adrielr.ia. Cada uma vive em `skills/<nome>/` com o `SKILL.md`, as referências e os scripts que usa.

## Instalação

```bash
git clone https://github.com/kairoxaioficial/skills.git
cd skills
./install.sh                    # menu: escolhe quais instalar
./install.sh dailton viral      # instala só as citadas
./install.sh todas              # instala todas
```

As skills são copiadas para `~/.claude/skills/` (ou para `$CLAUDE_SKILLS_DIR`). Se já existir uma pasta com o mesmo nome, ela vira backup (`<nome>.bak-<data>`) antes da cópia. Depois, abra uma nova sessão do Claude Code e chame `/<nome>`.

## As skills

### cienciatododia
Ideias, títulos, ganchos e roteiros de vídeos de tecnologia no estilo do canal Ciência Todo Dia (Pedro Loos): curiosidade científica explicada para o público geral, lacuna de curiosidade, cenários hipotéticos, números chocantes comparados ao dia a dia e desenvolvimento em escada. Serve para vídeo longo do YouTube (10 a 20 min) e para short/reel (30 a 60 s), e avalia se um tema tem potencial viral.
Uso: `/cienciatododia <tema>`, `ideias`, `avaliar: <tema>`, `short: <tema>`, `longo: <tema>`.

### joeljota
Roteiros de Reels com mensagem de impacto no estilo do Joel Jota, baseados na análise medida de 70 reels dele (30 mais vistos, 20 recentes, 20 motivacionais): gancho no segundo zero, frases curtas com cabeça repetida, voz encenada, virada perto da metade, fecho curto sem pedido e direção de gravação.
Uso: `/joeljota <tema>`, `curto <tema>`, `ganchos <tema>`, `revisar <roteiro>`, `atualizar`.

### dailton
Estrategista de conteúdo viral no método do Dailton Rolim (@dailton_rolim), feito a partir de 2 aulas transcritas e de 35 reels medidos. Diagnostica perfil e reels pelos insights, monta o teste dos 8 formatos, cria pautas com nota de viralidade, escreve roteiro de cerca de 44 s (gancho até 7 s, explicação até 30 s, CTA sutil até 7 s), cria títulos de tela e ganchos, adapta vídeo viral em tela dividida e revisa roteiro ou vídeo pelo checklist de 22 critérios.
Uso: `/dailton diagnostico`, `formatos`, `pauta <tema>`, `roteiro <tema>`, `ganchos <tema>`, `tela-dividida <viral>`, `revisar <roteiro ou vídeo>`, `plano`, `atualizar`.
Observação: o `atualizar` usa `scripts/detalhes.mjs` da joeljota, e a transcrição de vídeo usa o binário `scripts/transcrever_apple` (macOS).

### criacao-conteudo
Estrategista de conteúdo para Instagram por funil: topo (atração), meio (consciência) e fundo (aquecimento e conversão), no modelo AIDA. Cria e revisa roteiro de Reels, carrossel, post, legenda, gancho, CTA, pauta, calendário e semana de conteúdo, conteúdo de autoridade, depoimento e lançamento. Cobre também análise de perfil, bio, regra dos 9, tráfego para seguidores (Meta Ads) e oratória.
Uso: pedidos como "cria um carrossel", "roteiro de reels", "analisa meu perfil", "melhora minha bio".

### modelagem
Roteiros de Reels sobre IA no padrão medido de 5 criadores brasileiros de IA (Danilo Gato, Miguel Lannes, Alan Nicolas, Rodrigo Tadewald e Mateus Dias; 150 reels), sempre com fatos reais pesquisados na hora, com fonte e data. Faz radar de novidades de IA, pautas com nota de viralidade, roteiro completo, pautas da semana, roteiro no estilo de um dos 5 e revisão.
Uso: `/modelagem <tema>`, `novidades [dias]`, `semana`, `estilo <criador> <tema>`, `revisar <roteiro>`, `atualizar`.

### viral
Narrativa viral e edição no padrão do criador americano Kallaway, medidas em 30 reels e no vídeo dele sobre neurociência do storytelling. Reestrutura roteiros no loop aposta, grande pergunta, virada e re-gancho (gancho em 3 camadas, zona de lock-in, CTA de palavra-chave) e edita o vídeo gravado em tela dividida (gráfico em cima, rosto embaixo, legenda de 1 palavra) com HTML/GSAP e ffmpeg. Funciona sozinha ou depois da modelagem.
Uso: `/viral roteiro <tema>`, `revisar <roteiro>`, `edicao <video.mp4>`, `gancho <tema>`.

## O que não está no repositório

Mídia, transcrições completas e fichas dos vídeos de terceiros (`dados/midia/`, `dados/fichas/`, `dados/dossie/` etc.) ficam só na máquina local. As skills funcionam sem elas; o comando `atualizar` de cada uma recria a base quando preciso.
