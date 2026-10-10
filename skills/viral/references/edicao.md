# Edição no padrão Kallaway: o que foi medido e a receita para reproduzir

Medido nos 30 vídeos do dossiê (método em `analise-kallaway.md` §6). Quadros baixados em 720x1280 a 23,98 fps; as medidas abaixo já estão convertidas para 1080x1920 (x1,5). A §9 adapta tudo às regras do Adriel e a §10 traz a receita técnica testada (código completo nas §10.4 a §10.9).

## 1. O padrão numa tela

| Item | Medida |
|---|---|
| Layout dominante | **tela dividida**: painel de gráfico em cima (fundo liso com quadriculado discreto), cartão do rosto com cantos arredondados embaixo, legenda de 1 palavra entre os dois |
| Tempo no layout dividido | 70% (mediana TOP); 76% nos recentes |
| Saídas do dividido | 4,7 por minuto (TOP), cada uma com mediana de 3,25 s: close do rosto em tela cheia (a maioria), B-roll em tela cheia ou gráfico em tela cheia |
| Bloco contínuo no dividido | 6,25 s (TOP) |
| Cortes por minuto (troca de cena > 0,3) | 9,6 (TOP); intervalo mediano de 4,4 s |
| 1º close em tela cheia | entre 2,0 e 3,5 s em 7 dos 11 TOP olhados quadro a quadro (TOP#2, #6, #7, #8, #10, #12, #15) |
| Troca de visual no gancho | 1 por segundo, mais ou menos, nos 4 primeiros segundos (TOP#1, #2, #7) |
| Texto no 1º quadro | 30 de 30 (o título já está entrando no quadro 0) |
| Legenda | 1 palavra por bloco (palavras curtas juntam: "is the", "so good"), sem caixa nem karaokê, nome do método em serifa itálica |
| Som | voz na frente, trilha baixa e contínua por baixo (espectrograma de TOP#1 e TOP#7); efeitos não identificáveis |

A edição é a mesma em 0,4x (REC#1) e em 36,9x (TOP#1): ela segura a retenção, mas o pico veio do assunto e do gancho (análise §4.6).

## 2. Geometria (1080x1920)

```
y    0 ┌──────────────────────────────┐
     128│  Título linha 1 (64 px)       │  2 linhas, centradas, Inter 800,
     255│  Título linha 2 (84 px)       │  1 palavra em serifa itálica ou acento
     290│                              │
        │  PAINEL DE GRÁFICO           │  objeto central ~620–900 px de largura
        │  (mockup, lista, número,     │  troca a cada ideia (4–7 s)
        │   gráfico, grade de provas)  │
    1170│                              │
    1242│        legenda (54 px)       │  centro da palavra
    1405│ ╭──────────────────────────╮ │  cartão: x 67–1013 (946 px), cantos 33 px
        │ │  rosto, plano aberto      │ │  passa da borda de baixo (cantos de baixo somem)
    1920└─┴──────────────────────────┴─┘
```

- **Cartão do rosto:** 946 px de largura, margem de 67 px dos lados, topo em 1405, cantos de cerca de 33 px. A proporção é 16:9: no Kallaway, o cartão é o quadro inteiro de uma câmera horizontal, com ele em plano médio, estante iluminada e luz ciano de fundo.
- **O boné passa por cima da borda do cartão** (cerca de 90 px acima do topo, TOP#7 e outros): recorte da pessoa sobreposto. É detalhe opcional (§10.11).
- **Close em tela cheia:** rosto ocupando a largura, olhos perto de 36% da altura, fundo desfocado. Parece um recorte vertical da mesma gravação 4K ou uma segunda câmera; não há zoom animado dentro do close, a troca é seca.
- **Legenda no close:** branca, 60 px, centro perto de 1160 (60% da altura), sobre o peito, com sombra suave.
- **Painel:** o objeto central fica entre y 290 e 1170. No TOP#7 aos 1,5 s, o celular simulado vai de x 285 a 792 e de y 288 a 1167.

## 3. Ritmo dos primeiros segundos (3 exemplos, a cada 0,5 s)

| s | TOP#1 DaiCxAkOpNb (fundo escuro) | TOP#2 DZU1D_8OI62 (fundo claro) | TOP#7 DY2BBsIuFcC (claro → escuro) |
|---|---|---|---|
| 0,0 | título entrando com desfoque + clipe de outro criador num quadro | título + ícone da ferramenta pulsando | título + tela de métricas em branco |
| 0,5–1,5 | cérebro num círculo vermelho | cartão de perfil com seguidores subindo (1,5 s) | gráfico de retenção caindo em rosa |
| 2,0 | grade de miniaturas de vídeos | idem | **close** em tela cheia |
| 3,0 | grade vermelha com celular | **close** em tela cheia | close; nome em serifa itálica (3,5 s) |
| 4,0–5,5 | símbolo do infinito; título do método | caixa da ferramenta com o comando sendo digitado letra a letra | volta ao dividido, fundo preto, curva se desenhando |
| 8–12 | cérebro ligado ao infinito por linha; caça-níquel; zoom no infinito com "1" (capítulo) | close (8,5 s) e relatório saindo | rótulos entrando um por um na curva |

## 4. Legendas

- **Uma palavra por bloco**, no tempo exato da fala. Palavras de até 3 letras se juntam à seguinte ("é o", "de responder"); às vezes vão 2 ou 3 palavras quando formam um termo ("Body block 1", "2 to 3").
- **Fonte:** grotesca pesada (equivalente livre: Inter 800), caixa como falado, pontuação mantida, letter-spacing -0,02 em. 54 px no dividido; 60 a 64 px no close.
- **Cor:** branca no fundo escuro, preta no claro. Na variante clara do TOP#5, um selo cinza arredondado com texto branco.
- **Destaque:** o nome do método e o termo-chave saem em **serifa itálica** (equivalente livre: Instrument Serif Italic), tanto na legenda quanto no título ("Application", "story ladder", "Comprehension Maxing", "Boring Businesses"). Não há palavra colorida na legenda nem karaokê.
- **Entrada:** troca seca de palavra (nenhuma animação perceptível a 2 quadros por segundo).

## 5. Título (texto da abertura)

- 2 linhas centradas no topo (y 128 a 255): a linha 1 menor (64 px) e a linha 2 maior (84 px), Inter 800 com letter-spacing -0,035 em.
- **Uma palavra de destaque**: serifa itálica ("*Crazy Viral*", "*Changed*", "*Killer* Hook") ou cor de acento vermelha, às vezes sublinhada de vermelho (TOP#2, #8) ou dentro de uma tarja vermelha (TOP#4, #9, #10).
- **Entrada palavra a palavra** com desfoque que some (blur de ~14 px para 0, subindo ~24 px, 0,45 s por palavra, 0,06 s entre elas). O quadro 0 já mostra a 1ª palavra entrando.
- Fica na tela durante todo o bloco dividido; muda de texto quando muda o capítulo ("Traditional *Story Arc*" → "Modern *Story Arc*", TOP#7).

## 6. Painel de gráfico: o catálogo

| Peça | Como anima | Onde |
|---|---|---|
| Grade de provas: miniaturas de vídeos com selo verde de views | entram em cascata (0,1 s entre elas), selo aparece depois | TOP#6 0 s, TOP#10 0 s, TOP#15 0 s |
| Celular ou janela simulada (perfil, app, relatório) | sobe e escala; número subindo dentro (contador) | TOP#2, #7, #8 |
| Comando sendo digitado | letra a letra, cerca de 4 s | TOP#2 4–8 s |
| Documento com barras coloridas (roteiro) | barras crescem da esquerda; a seção falada acende em cor | TOP#3, #4, #11, #13 |
| **Lista-mapa numerada** (01 a 06) | itens desfocados; o item falado fica nítido e claro; **volta a cada passo** como marcador de progresso | TOP#3 11 s e 88 s, TOP#13 10, 21, 38 e 57 s, REC#1 6 s |
| Símbolo recorrente do método (infinito, escada) | zoom grande com o número do passo na troca de capítulo | TOP#1 11, 35, 51 e 75 s; TOP#10 4 s |
| Curva ou gráfico | traço se desenha com brilho; rótulos em selos brancos entram um a um; picos ganham pontos | TOP#7 4–60 s, TOP#12 5–10 s |
| Linha do tempo | câmera corre na horizontal pelos anos | TOP#6 4–7 s |
| Tabela preenchida ao vivo | célula a célula, conforme a fala | TOP#13 33–56 s |
| Tela cheia de B-roll (filme, cassino, celebridade) | corte seco, 2 a 4 s, legenda continua | TOP#1 72–81 s, TOP#7 42 s |
| Cartão do CTA | "Comment" + palavra em serifa itálica entre aspas + subtítulo em vermelho + prévia da isca | TOP#1 100 s, TOP#7 72 s |

Regra de casamento: cada imagem corresponde à palavra dita naquele instante (é o que ele ensina no TOP#12). Quando ele fala "três coisas", aparecem três fichas; quando fala "cassino", aparece o caça-níquel.

## 7. Paleta e tipografia medidas

| Papel | Escuro | Claro |
|---|---|---|
| Fundo | #080808 a #101010, quadriculado de ~27 px quase invisível | #E0E0E0 / #D8D8D8, quadriculado #D2D2D0 |
| Texto | #FFFFFF | #111111 |
| Acento | vermelho #B8000A a #C8000A (uso: palavra do título, tarja, curva, botões) | o mesmo |
| Apoio | verde #19C34A (selos de views, barras), amarelo (marcadores), roxo com brilho (curva "moderna", CTA do TOP#1) | — |
| Fontes | grotesca pesada para tudo + serifa itálica para o termo-chave | — |

## 8. Áudio

Voz sempre na frente. Por baixo, trilha contínua e baixa: no espectrograma do TOP#1 e do TOP#7 há energia grave constante e notas sustentadas entre as palavras, sem silêncio. Não dá para afirmar efeitos sonoros; se usar, só nas trocas de capítulo e baixos.

## 9. Adaptação ao Adriel

As regras de marca da `/modelagem` §5 vencem. Na prática:

| No Kallaway | No Adriel |
|---|---|
| Painel com telas gravadas, apps e vídeos de outros criadores | painel **desenhado em código**: título, lista-mapa, número, seta, gráfico simples, cartão de CTA. Sem gravação de tela e sem vídeo de terceiros |
| Print de notícia, perfil ou relatório | imagem estática **opcional**, no máximo 1 por vídeo, 2 a 3 s, com data visível; a decisão é dele (`/modelagem` §5) |
| B-roll de filme ou celebridade | não usar (direito de imagem e regra de marca) |
| Brilho neon, roxo, degradê | não usar: o Adriel recusa glow, roxo e degradê. Gráfico chapado, acento só onde importa |
| Vermelho Kallaway | `acento` vem da marca do Adriel; sugestão: verde #1DB954 no fundo escuro e #0B7A35 no claro (confirmar com ele) |
| Close e cartão vindos de 2 câmeras ou de 4K | 1 câmera basta: gravar em 4K horizontal (cartão = quadro inteiro; close = recorte vertical) ou vertical (cartão = recorte do peito para cima) |

**Teste A/B sugerido**: dividido com painel (padrão Kallaway) × tela cheia com cortes e legenda (padrão atual da `/modelagem`). Medir envios por alcance e seguidores ganhos (as métricas dele).

## 10. Receita técnica (testada em 30/09/2026 neste Mac)

### 10.1 Visão geral

```
gravacao.mp4 ─► cortar.py ─► bruto.mp4 ─► transcrever.py ─► palavras.json
                                                         │
                         plano de edição (SKILL.md) ─► timeline.json
                                                         │
          overlay.html + render.mjs (Chrome + GSAP, quadro a quadro) ─► overlay.mov (alfa)
                                                         │
                 montar.py (ffmpeg: fundo, cartão, close, overlay, trilha) ─► final.mp4
```

Teste feito com um clipe sintético de 13,5 s (voz do `say`, fundo de barras): render do overlay em 45 s (cerca de 3,3 s de render para cada segundo de vídeo) e montagem em 16 s. Um vídeo de 90 s leva perto de 5 min de render.

### 10.2 Pré-requisitos (uma vez por máquina)

- `ffmpeg` em `~/.local/bin/ffmpeg` (sem `ffprobe`: os scripts não dependem dele), `node` 24, Google Chrome em `/Applications`, `python3` com `mlx_whisper`, `PIL` e `cv2` (todos presentes neste Mac).
- Fontes locais da `conteudo-motion`: `~/.claude/skills/conteudo-motion/fontes/inter/Inter.ttf` e `.../instrument-serif/InstrumentSerif-Italic.ttf` (só leitura).
- Mac de 8 GB: não rodar o whisper e o Chrome ao mesmo tempo; um vídeo por vez.

### 10.3 Pasta de trabalho

```bash
P=~/Movies/viral/$(date +%Y-%m-%d)-<slug>; mkdir -p "$P" && cd "$P"
npm init -y >/dev/null && npm i puppeteer-core@23 gsap --silent   # 1 vez por pasta (~20 s)
# copie a gravação para "$P/gravacao.mp4" e crie os 6 arquivos das seções 10.4 a 10.9 com Write, exatamente como estão
```

### 10.4 Cortar pausas

#### `cortar.py`

```python
# python3 cortar.py gravacao.mp4 bruto.mp4  -> tira respiros/pausas > 0,30 s usando os tempos de palavra do whisper
import json, subprocess, sys
import mlx_whisper
src, out = sys.argv[1], sys.argv[2]
r = mlx_whisper.transcribe(src, path_or_hf_repo="mlx-community/whisper-large-v3-turbo", language="pt", word_timestamps=True)
ws = [(float(w["start"]), float(w["end"])) for s in r["segments"] for w in s.get("words", [])]
PAD, GAP = 0.08, 0.30                     # folga em volta da fala; pausa maior que isso sai
keep = []
for s, e in ws:
    s, e = max(0, s - PAD), e + PAD
    if keep and s - keep[-1][1] <= GAP: keep[-1][1] = max(keep[-1][1], e)
    else: keep.append([s, e])
parts = ''.join(f"[0:v]trim={a:.3f}:{b:.3f},setpts=PTS-STARTPTS[v{i}];[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[a{i}];" for i, (a, b) in enumerate(keep))
fc = parts + ''.join(f"[v{i}][a{i}]" for i in range(len(keep))) + f"concat=n={len(keep)}:v=1:a=1[v][a]"
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-filter_complex', fc, '-map', '[v]', '-map', '[a]',
                '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-c:a', 'aac', '-b:a', '192k', out], check=True)
print(f"{len(keep)} trechos; {sum(b - a for a, b in keep):.1f} s de fala de {ws[-1][1]:.1f} s")
```

Tomadas repetidas (ele erra e fala de novo) não saem sozinhas: ache o trecho em `palavras.json` e corte antes, ou peça ao Adriel a tomada boa. Ritmo-alvo depois do corte: 200 a 230 palavras por minuto.

### 10.5 Transcrever com tempo de palavra e achar tempos

#### `transcrever.py`

```python
# python3 transcrever.py bruto.mp4  -> palavras.json na mesma pasta
import json, os, sys
import mlx_whisper
src = sys.argv[1]
r = mlx_whisper.transcribe(src, path_or_hf_repo="mlx-community/whisper-large-v3-turbo", language="pt", word_timestamps=True)
ws = [{"w": w["word"].strip(), "s": round(float(w["start"]), 2), "e": round(float(w["end"]), 2)} for s in r["segments"] for w in s.get("words", [])]
json.dump(ws, open(os.path.join(os.path.dirname(os.path.abspath(src)), "palavras.json"), "w"), ensure_ascii=False, indent=0)
print(len(ws), "palavras;", ws[-1]["e"], "s")
```

#### `acha.py`

```python
# python3 acha.py palavras.json "régua da delegação"  -> início e fim da 1ª ocorrência
import json, re, sys
n = lambda s: re.sub(r"[^\w]", "", s.lower())
ws = json.load(open(sys.argv[1])); alvo = [n(x) for x in sys.argv[2].split()]
for i in range(len(ws) - len(alvo) + 1):
    if [n(w["w"]) for w in ws[i:i + len(alvo)]] == alvo:
        print(ws[i]["s"], ws[i + len(alvo) - 1]["e"]); break
else:
    print("não achei")
```

Confira a transcrição: nome de ferramenta e marca costumam sair errados (corrija o `w` no `palavras.json`; os tempos ficam).

### 10.6 `timeline.json` (o plano de edição em dados)

```json
{
  "fps": 30,
  "dur": 13.5,
  "tema": "escuro",
  "acento": "#1DB954",
  "layout": [
    {"t0": 0, "t1": 3.2, "tipo": "split"},
    {"t0": 3.2, "t1": 5.6, "tipo": "close"},
    {"t0": 5.6, "t1": 13.5, "tipo": "split"}
  ],
  "titulo": {"l1": "O jeito mais rápido de", "l2": "responder *cliente* no [WhatsApp]"},
  "serifadas": ["régua", "delegação"],
  "graficos": [
    {"tipo": "numero", "t0": 0.3, "t1": 3.2, "valor": 3, "rotulo": "passos"},
    {"tipo": "lista", "t0": 5.6, "t1": 10.4, "titulo": "Régua da Delegação", "itens": ["Repetição", "Julgamento", "Limite"], "ativo": [{"t": 7.4, "i": 0}, {"t": 9.0, "i": 1}]},
    {"tipo": "seta", "t0": 9.0, "t1": 10.4, "alvo": "lista-1"},
    {"tipo": "cta", "t0": 10.4, "t1": 13.5, "palavra": "RÉGUA", "sub": "que eu te mando o modelo"}
  ]
}
```

| Campo | Regra |
|---|---|
| `dur` | duração do `bruto.mp4` (último `e` do `palavras.json` + 0,3 s) |
| `tema` | `escuro` ou `claro`. Hipótese do dossiê: abrir no claro (7 de 15 TOP) |
| `layout` | cobre de 0 a `dur` sem buraco. `close`: 2 a 4 s, umas 5 por minuto, nas frases de opinião, no nome do método, na virada e no re-gancho; o 1º entre 2 e 3,5 s. O resto é `split` |
| `titulo` | 2 linhas; `*palavra*` = serifa itálica; `[palavra]` = acento sublinhado. Mesmo assunto da 1ª frase, de 3 a 8 palavras |
| `serifadas` | palavras do nome do método (sem pontuação; a comparação ignora maiúscula e pontuação) |
| `graficos` | `numero` (valor que conta até o alvo + rótulo em serifa), `lista` (lista-mapa: `ativo` acende o item `i` no tempo `t`), `imagem` (`src` relativo à pasta, `selo` opcional; só a imagem opcional da §9), `seta` (desenha até `lista-<i>`; vem depois da lista no array), `cta` (palavra e subtítulo). Um gráfico novo a cada ideia (4 a 7 s) e, no gancho, até 1 por segundo |
| `trilha` | opcional: arquivo de música na pasta; `trilha_volume` padrão 0,10 (≈ -20 dB) |
| `zoom_close`, `rosto_x`, `rosto_y`, `cartao_crop_y` | ajuste do enquadramento (padrões 1,18 · 0,5 · 0,10 · 0,12) |

Todos os tempos saem do `palavras.json` (use o `acha.py`), nunca de segundo chutado.

### 10.7 `overlay.html` (camada de gráfico e legenda, determinística)

#### `overlay.html`

```html
<!doctype html>
<html><head><meta charset="utf-8">
<style>
@font-face{font-family:"Inter";src:url("FONTES/inter/Inter.ttf");font-weight:100 900}
@font-face{font-family:"Serif";src:url("FONTES/instrument-serif/InstrumentSerif-Italic.ttf");font-style:italic}
:root{--acento:#C1000F;--txt:#FFFFFF;--sub:#1A1A1A;--borda:#2A2A2A}
.claro{--txt:#111111;--sub:#FFFFFF;--borda:#D4D4D4}
html,body{margin:0;width:1080px;height:1920px;background:transparent;overflow:hidden}
body{font-family:Inter;color:var(--txt);-webkit-font-smoothing:antialiased}
#palco{position:absolute;inset:0}
.camada{position:absolute;inset:0}
#titulo{position:absolute;top:120px;left:60px;right:60px;text-align:center;font-weight:800;letter-spacing:-.035em;line-height:1.02}
#titulo .l1{font-size:64px;white-space:nowrap}
#titulo .l2{font-size:84px;white-space:nowrap}
.serif{font-family:Serif;font-style:italic;font-weight:400;letter-spacing:-.01em}
.acento{color:var(--acento);text-decoration:underline;text-decoration-thickness:6px;text-underline-offset:10px}
.pal{display:inline-block;white-space:pre}
#leg{position:absolute;left:0;right:0;text-align:center;font-weight:800;font-size:54px;letter-spacing:-.02em}
#leg.close{font-size:64px;color:#fff;text-shadow:0 2px 14px rgba(0,0,0,.55)}
#leg .serif{font-size:1.15em}
.lista{position:absolute;left:150px;right:150px;top:420px}
.lista h3{margin:0 0 34px;text-align:center;font-size:60px;font-weight:800;letter-spacing:-.03em}
.item{display:flex;align-items:center;gap:26px;height:104px;margin-bottom:18px;padding:0 30px;border-radius:16px;background:var(--sub);border:1px solid var(--borda);font-size:44px;font-weight:700}
.item b{background:var(--acento);color:#fff;border-radius:10px;padding:2px 16px;font-size:36px}
.item.on{background:#EDEDED;color:#111}
.claro .item.on{background:#111;color:#fff}
.num{position:absolute;left:0;right:0;top:420px;text-align:center}
.num .v{font-size:380px;font-weight:900;letter-spacing:-.06em;line-height:1}
.num .r{font-size:96px}
svg.seta{position:absolute;inset:0;overflow:visible}
.img{position:absolute;left:50%;top:330px;width:620px;transform:translateX(-50%);border-radius:28px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.45);border:6px solid var(--borda)}
.img img{display:block;width:100%}
.selo{position:absolute;left:24px;bottom:24px;background:#19C34A;color:#fff;font-weight:800;font-size:36px;border-radius:12px;padding:4px 16px}
.cta{position:absolute;left:60px;right:60px;top:430px;text-align:center}
.cta .a{font-size:92px;font-weight:800;letter-spacing:-.035em}
.cta .p{font-family:Serif;font-style:italic;font-size:120px}
.cta .s{margin-top:12px;font-size:52px;font-weight:800;color:var(--acento)}
</style></head>
<body><div id="palco"><div class="camada" id="graf"></div><div id="titulo"></div><div id="leg"></div></div>
<script src="GSAP"></script>
<script>
// Tudo determinístico: só tl.seek(t). Nada de Date, rAF, setTimeout ou transition CSS.
const el = (tag, cls, txt) => { const e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; };
const tl = gsap.timeline({ paused: true });
const th = gsap.timeline({ paused: true }); // título: roda 0,3 s adiantado para o 1º quadro já ter texto
let TL, BLOCOS, LAY;

// "responder *cliente* no [WhatsApp]" -> palavras com estilo (texto via textContent, nunca innerHTML)
function marcado(alvo, s) {
  for (const p of s.split(' ')) {
    const m = p.match(/^\*(.+)\*$/) || p.match(/^\[(.+)\]$/);
    const span = el('span', 'pal' + (p.startsWith('*') ? ' serif' : p.startsWith('[') ? ' acento' : ''), (m ? m[1] : p));
    alvo.append(span, document.createTextNode(' '));
  }
}

// Legenda: 1 palavra por bloco; palavra de até 3 letras junta com a próxima (máx. 2 palavras, 16 caracteres)
function blocos(pal) {
  const out = [];
  for (let i = 0; i < pal.length; i++) {
    const a = pal[i], b = pal[i + 1];
    if (b && a.w.replace(/\W/g, '').length <= 3 && (a.w + ' ' + b.w).length <= 16) { out.push({ txt: a.w + ' ' + b.w, s: a.s, e: b.e }); i++; }
    else out.push({ txt: a.w, s: a.s, e: a.e });
  }
  for (let i = 0; i < out.length - 1; i++) out[i].e = Math.max(out[i].e, out[i + 1].s); // sem buraco entre blocos
  return out;
}
const norm = s => s.toLowerCase().replace(/[^\p{L}\p{N}]/gu, '');
const layoutEm = t => (LAY.find(x => t >= x.t0 && t < x.t1) || LAY[LAY.length - 1]).tipo;

function montar(tlj, palavras) {
  TL = tlj; LAY = tlj.layout; BLOCOS = blocos(palavras);
  if (tlj.tema === 'claro') document.body.classList.add('claro');
  document.documentElement.style.setProperty('--acento', tlj.acento);
  // título em 2 linhas, entra palavra a palavra com desfoque
  const ti = document.getElementById('titulo');
  const l1 = el('div', 'l1'), l2 = el('div', 'l2'); marcado(l1, tlj.titulo.l1); marcado(l2, tlj.titulo.l2); ti.append(l1, l2);
  for (const l of [l1, l2]) { let f = parseFloat(getComputedStyle(l).fontSize); while (l.scrollWidth > ti.clientWidth && f > 30) l.style.fontSize = (f -= 2) + 'px'; } // cabe em 1 linha
  th.from(ti.querySelectorAll('.pal'), { opacity: 0, y: 24, filter: 'blur(14px)', duration: .45, stagger: .06, ease: 'power3.out' }, 0);
  const G = document.getElementById('graf');
  for (const g of tlj.graficos) {
    if (g.tipo === 'numero') {
      const box = el('div', 'num'), v = el('div', 'v', '0'), r = el('div', 'r serif', g.rotulo); box.append(v, r); G.append(box);
      const o = { n: 0 };
      tl.fromTo(box, { opacity: 0, scale: .85 }, { opacity: 1, scale: 1, duration: .35, ease: 'back.out(1.6)' }, g.t0)
        .to(o, { n: g.valor, duration: .6, ease: 'power2.out', onUpdate: () => v.textContent = Math.round(o.n) }, g.t0)
        .to(box, { opacity: 0, duration: .15 }, g.t1 - .15);
    }
    if (g.tipo === 'lista') {
      const box = el('div', 'lista'); box.append(el('h3', null, g.titulo));
      const itens = g.itens.map((t, i) => { const it = el('div', 'item'); it.id = 'lista-' + i; it.append(el('b', null, String(i + 1).padStart(2, '0')), el('span', null, t)); box.append(it); return it; });
      G.append(box);
      tl.fromTo(box, { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: .4, ease: 'power3.out' }, g.t0)
        .fromTo(itens, { filter: 'blur(8px)', opacity: .45 }, { filter: 'blur(8px)', opacity: .45, duration: .01 }, g.t0);
      for (const a of g.ativo) tl.to(itens[a.i], { filter: 'blur(0px)', opacity: 1, duration: .25 }, a.t).set(itens[a.i], { attr: { class: 'item on' } }, a.t);
      tl.to(box, { opacity: 0, duration: .15 }, g.t1 - .15);
    }
    if (g.tipo === 'imagem') {
      const box = el('div', 'img'), im = el('img'); im.src = g.src.startsWith("/") ? "file://" + g.src : g.src; box.append(im);
      if (g.selo) box.append(el('div', 'selo', g.selo));
      G.append(box);
      tl.fromTo(box, { opacity: 0, y: 60, scale: .9 }, { opacity: 1, y: 0, scale: 1, duration: .4, ease: 'power3.out' }, g.t0)
        .to(box, { opacity: 0, duration: .15 }, g.t1 - .15);
    }
    if (g.tipo === 'cta') {
      const box = el('div', 'cta'), a = el('div', 'a', 'Comenta '), q = el('span', 'p', '“' + g.palavra + '”');
      a.append(q); box.append(a, el('div', 's', g.sub)); G.append(box);
      tl.fromTo(box, { opacity: 0, scale: .92 }, { opacity: 1, scale: 1, duration: .35, ease: 'back.out(1.7)' }, g.t0)
        .to(box, { opacity: 0, duration: .15 }, g.t1 - .15);
    }
    if (g.tipo === 'seta') {
      const NS = 'http://www.w3.org/2000/svg', svg = document.createElementNS(NS, 'svg'); svg.setAttribute('class', 'seta');
      svg.setAttribute('viewBox', '0 0 1080 1920'); svg.setAttribute('width', 1080); svg.setAttribute('height', 1920);
      const alvo = document.getElementById(g.alvo).getBoundingClientRect();
      const dy = gsap.getProperty(document.getElementById(g.alvo).parentElement, 'y') || 0; // desconta o deslocamento inicial da lista
      const x = alvo.left - 20, y = alvo.top + alvo.height / 2 - dy; // seta entra pela esquerda (direita é zona dos botões do Reels)
      const p = document.createElementNS(NS, 'path');
      p.setAttribute('d', `M ${x - 110} ${y - 150} Q ${x - 100} ${y - 10} ${x} ${y} M ${x} ${y} l -40 -22 M ${x} ${y} l -26 34`);
      Object.entries({ fill: 'none', stroke: TL.acento, 'stroke-width': 10, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }).forEach(([k, v]) => p.setAttribute(k, v));
      svg.append(p); G.append(svg);
      const L = p.getTotalLength();
      svg.style.opacity = 0; tl.set(svg, { opacity: 1 }, g.t0).fromTo(p, { strokeDasharray: L, strokeDashoffset: L }, { strokeDashoffset: 0, duration: .45, ease: 'power2.inOut' }, g.t0).to(svg, { opacity: 0, duration: .15 }, g.t1 - .15);
    }
  }
}

// chamado pelo render a cada quadro
window.seek = (t) => {
  tl.seek(t, false); th.seek(t + 0.3, false);
  const close = layoutEm(t) === 'close';
  document.getElementById('titulo').style.visibility = close ? 'hidden' : 'visible';
  document.getElementById('graf').style.visibility = close ? 'hidden' : 'visible';
  const leg = document.getElementById('leg'), b = BLOCOS.find(x => t >= x.s && t < x.e);
  leg.className = close ? 'close' : '';
  leg.style.top = (close ? 1120 : 1210) + 'px';
  leg.replaceChildren();
  if (b) {
    b.txt.split(' ').forEach((w, i) => { if (i) leg.append(' '); leg.append(el('span', TL.serifadas.map(norm).includes(norm(w)) ? 'serif' : null, w)); });
  }
};
window.montar = montar;
</script></body></html>
```

Parâmetros de animação usados (todos do que foi medido): título com desfoque 14 px → 0, subida 24 px, 0,45 s, intervalo 0,06 s, `power3.out`; entrada de painel 0,35 a 0,4 s (`power3.out` ou `back.out(1.6)`); saída 0,15 s; item da lista-mapa acende em 0,25 s; seta se desenha em 0,45 s (`power2.inOut`); contador sobe em 0,6 s (`power2.out`); legenda troca seca.

Para acrescentar uma peça nova (grade de provas, curva, tabela), siga o mesmo contrato: crie o elemento em `montar` com `el()` e `textContent`, anime só dentro de `tl` com `t0`/`t1` da timeline, e saia em 0,15 s.

### 10.8 `render.mjs` (Chrome sem janela, quadro a quadro, com alfa)

#### `render.mjs`

```js
// node render.mjs <pasta-da-edicao>  -> grava <pasta>/overlay.mov (ProRes 4444 com alfa)
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import puppeteer from 'puppeteer-core';

const dir = path.resolve(process.argv[2] || '.');
const FONTES = path.join(process.env.HOME, '.claude/skills/conteudo-motion/fontes');
const GSAP = path.join(dir, 'node_modules/gsap/dist/gsap.min.js');
const tl = JSON.parse(fs.readFileSync(path.join(dir, 'timeline.json'), 'utf8'));
const palavras = JSON.parse(fs.readFileSync(path.join(dir, 'palavras.json'), 'utf8'));
const html = fs.readFileSync(path.join(dir, 'overlay.html'), 'utf8')
  .replaceAll('FONTES/', 'file://' + FONTES + '/').replace('src="GSAP"', `src="file://${GSAP}"`);
const tmp = path.join(dir, '.overlay.run.html'); fs.writeFileSync(tmp, html);

const browser = await puppeteer.launch({
  executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  headless: true, args: ['--allow-file-access-from-files', '--force-color-profile=srgb'],
});
const page = await browser.newPage();
await page.setViewport({ width: 1080, height: 1920, deviceScaleFactor: 1 });
await page.goto('file://' + tmp, { waitUntil: 'load' });
await page.evaluate(() => Promise.all(['800 84px Inter', '900 84px Inter', 'italic 84px Serif'].map(f => document.fonts.load(f)))); // fonte carregada antes de medir
await page.evaluate((a, b) => window.montar(a, b), tl, palavras);

const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-c:v', 'png', '-framerate', String(tl.fps), '-i', '-',
  '-c:v', 'prores_ks', '-profile:v', '4444', '-pix_fmt', 'yuva444p10le', path.join(dir, 'overlay.mov')], { stdio: ['pipe', 'inherit', 'inherit'] });
const N = Math.round(tl.dur * tl.fps);
for (let i = 0; i < N; i++) {
  await page.evaluate(t => window.seek(t), i / tl.fps);
  const png = await page.screenshot({ type: 'png', omitBackground: true });
  if (!ff.stdin.write(png)) await new Promise(r => ff.stdin.once('drain', r));
  if (i % 90 === 0) process.stdout.write(`quadro ${i}/${N}\n`);
}
ff.stdin.end();
await new Promise(r => ff.on('close', r));
await browser.close();
fs.rmSync(tmp);
console.log('ok overlay.mov');
```

### 10.9 `montar.py` (fundo, cartão, close, overlay e trilha)

#### `montar.py`

```python
# python3 montar.py <pasta>  (bruto.mp4 + timeline.json + overlay.mov) -> final.mp4
import json, subprocess, sys, os
import cv2
from PIL import Image, ImageDraw

d = sys.argv[1] if len(sys.argv) > 1 else '.'
P = lambda f: os.path.join(d, f)
tl = json.load(open(P('timeline.json')))
W, H = 1080, 1920
CX, CY, CW, R = 67, 1400, 946, 34              # cartão do rosto: margem 67, topo 1400, cantos 34 (passa da borda de baixo)
ZOOM = float(tl.get('zoom_close', 1.18))       # punch-in do close
FACE_Y = float(tl.get('rosto_y', 0.10))        # topo do recorte do close (fração da altura)
ROSTO_X = float(tl.get('rosto_x', 0.5))        # centro do rosto na gravação horizontal (fração da largura)
CROP_Y = float(tl.get('cartao_crop_y', 0.12))  # gravação vertical: de onde o cartão recorta (fração da altura)

cap = cv2.VideoCapture(P('bruto.mp4')); sw, sh = int(cap.get(3)), int(cap.get(4)); cap.release()
deitado = sw > sh                               # gravação horizontal: cartão = quadro inteiro; close = recorte vertical
CH = round(CW * sh / sw) if deitado else 560

claro = tl.get('tema') == 'claro'
bg = Image.new('RGB', (W, H), (226, 226, 224) if claro else (8, 8, 8))
g = ImageDraw.Draw(bg); cor = (212, 212, 210) if claro else (22, 22, 22)
for x in range(0, W, 27): g.line([(x, 0), (x, H)], fill=cor, width=1)   # papel quadriculado discreto
for y in range(0, H, 27): g.line([(0, y), (W, y)], fill=cor, width=1)
bg.save(P('.bg.png'))
m = Image.new('L', (CW, CH), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, CW - 1, CH - 1], R, fill=255); m.save(P('.mask.png'))

if deitado:
    cartao = f"[a]scale={CW}:{CH},format=rgba[c0]"
    cw = f"ih*9/16/{ZOOM}"
    close = f"[b]crop={cw}:ih/{ZOOM}:max(0\\,min(iw-{cw}\\,iw*{ROSTO_X}-{cw}/2)):ih*{FACE_Y},scale={W}:{H}[close]"
    pre = f"[0:v]fps={tl['fps']},split[a][b]"
else:
    cartao = f"[a]scale={CW}:-2,crop={CW}:{CH}:0:ih*{CROP_Y},format=rgba[c0]"
    close = f"[b]crop=iw/{ZOOM}:ih/{ZOOM}:(iw-iw/{ZOOM})/2:ih*{FACE_Y},scale={W}:{H}[close]"
    pre = f"[0:v]fps={tl['fps']},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},split[a][b]"

closes = [s for s in tl['layout'] if s['tipo'] == 'close']
en = '+'.join(f"between(t,{s['t0']},{s['t1'] - 0.001})" for s in closes) or '0'
fc = ';'.join([pre, cartao, "[c0][2:v]alphamerge[card]", f"[1:v][card]overlay={CX}:{CY}:shortest=1[split]", close,
               f"[split][close]overlay=0:0:enable='{en}'[base]", "[base][3:v]overlay=0:0:format=auto,format=yuv420p[v]"])
ins = ['-i', P('bruto.mp4'), '-loop', '1', '-i', P('.bg.png'), '-loop', '1', '-i', P('.mask.png'), '-i', P('overlay.mov')]
amap = '0:a'
if tl.get('trilha'):                            # trilha de fundo baixa e contínua (~ -20 dB sob a voz)
    ins += ['-stream_loop', '-1', '-i', P(tl['trilha'])]
    fc += f";[4:a]volume={tl.get('trilha_volume', 0.10)}[m];[0:a][m]amix=inputs=2:duration=first:normalize=0[a]"
    amap = '[a]'
cmd = ['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', fc, '-map', '[v]', '-map', amap, '-t', str(tl['dur']),
       '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-r', str(tl['fps']), '-c:a', 'aac', '-b:a', '192k',
       '-movflags', '+faststart', P('final.mp4')]
subprocess.run(cmd, check=True)
print('ok', P('final.mp4'), '| gravação', 'horizontal' if deitado else 'vertical', f'{sw}x{sh}')
```

### 10.10 Rodar e conferir

```bash
cd "$P"
python3 cortar.py gravacao.mp4 bruto.mp4
python3 transcrever.py bruto.mp4            # -> palavras.json
python3 acha.py palavras.json "<trecho>"    # para cada evento do plano
# escreva timeline.json (§10.6) com Write
node render.mjs .                           # -> overlay.mov
python3 montar.py .                         # -> final.mp4
ffmpeg -v error -y -i final.mp4 -vf "fps=2,scale=270:-2,tile=6x4" -frames:v 1 conf-00.jpg              # 0–12 s
ffmpeg -v error -y -ss 12 -i final.mp4 -vf "fps=1,scale=180:-2,tile=10x6" -frames:v 1 conf-resto.jpg   # 12–72 s
```

Abra as folhas com Read e confira: título inteiro e sem corte (o ajuste automático reduz a fonte até caber); legenda sincronizada e sem palavra cortada; close nas frases certas; nada do painel abaixo de y 1180 nem atrás do cartão; seta apontando o item; CTA visível nos últimos segundos; rosto bem enquadrado no cartão e no close (ajuste `cartao_crop_y`, `rosto_y`, `rosto_x`, `zoom_close`). No máximo 3 rodadas de ajuste; depois entregue com a lista do que ficou.

### 10.11 Opcionais (não implementados)

- **Boné saindo do cartão:** exige recorte da pessoa (segmentação). Caminho: máscara da pessoa por quadro (Vision do macOS ou um modelo de segmentação), recortar só a faixa entre y 1310 e 1405 e sobrepor depois do cartão. Não testado aqui.
- **Duas câmeras:** se o Adriel gravar com 2 ângulos, troque o `[close]` do `montar.py` por uma segunda entrada sincronizada.
- **Peças extras do Kallaway** (grade de provas com selos, curva que se desenha, tabela ao vivo, digitação): escreva no mesmo contrato do `overlay.html`. Sem brilho neon nem roxo para o Adriel.

### 10.12 Alternativa

Para reel 100% animado (sem o Adriel na câmera, com narração, personagem e pesquisa embutida), use a skill `conteudo-motion`. Ela tem kit pronto de peças GSAP, render quadro a quadro com conferência e mixagem. A `/viral` edita a gravação dele; a `conteudo-motion` cria o vídeo inteiro.
