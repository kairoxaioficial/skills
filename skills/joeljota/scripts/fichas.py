# python3 fichas.py [pasta_trabalho]  — uma ficha por vídeo baixado (métricas, legenda, transcrição com tempo, texto na tela,
# imagens) + índice com números do perfil. É a entrada da análise. Saída: ../dados/fichas/<código>.md, ../dados/indice.md
# e ../dados/midia/ (imagens e json de cada vídeo, para a análise não depender do cache).
import sys, os, json, re, glob, shutil, statistics as st, datetime as dt
W = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/.cache/joeljota')
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dados'))
U = 'joeljota'; V = f'{W}/videos/{U}'; MID = f'{B}/midia'
os.makedirs(f'{B}/fichas', exist_ok=True); os.makedirs(MID, exist_ok=True)
d = json.load(open(f'{W}/users/{U}.json')); items = {i['code']: i for i in d['items']}; det = d.get('details', {}); sel = d.get('sel', {})
cat = d.get('categorias', {})
plays = sorted(i['play_count'] for i in d['items'] if i.get('play_count') is not None)
med = st.median(plays) if plays else 1
fmt = lambda n: f'{n:,}'.replace(',', '.') if isinstance(n, int) else str(n)
tok = lambda x: re.findall(r'\w+', x.lower())
mmss = lambda s: f'{int(s // 60)}:{int(s % 60):02d}'
def load(p):
    try: return json.load(open(p))
    except Exception: return None
def tags(c):
    t = [f'{g.upper()}#{sel[g].index(c) + 1}' for g in ('viral', 'recentes', 'motivacionais') if c in sel.get(g, [])]
    return [x.replace('RECENTES', 'RECENTE').replace('MOTIVACIONAIS', 'MOTIVACIONAL') for x in t]
def ocr_view(ocr, transcript, speech_ok):
    """Texto fixo (em >= 50% dos frames) e texto que aparece ao longo do vídeo, sem as legendas que só repetem a fala."""
    if not ocr: return [], []
    n = len(ocr); cnt = {}
    for fr in ocr:
        for l in set(fr['lines']): cnt[l] = cnt.get(l, 0) + 1
    persist = [l for l, k in cnt.items() if n >= 4 and k / n >= 0.5]
    vocab = set(tok(transcript)); seen = set(); tl = []
    for fr in ocr:
        for l in fr['lines']:
            if l in seen or l in persist: continue
            seen.add(l); w = tok(l)
            if speech_ok and w and sum(x in vocab for x in w) / len(w) >= 0.7: continue
            tl.append(f"[{fr['t']}s] {l}")
    return persist, tl
rows = []
for mp4 in sorted(glob.glob(f'{V}/*.mp4')):
    c = os.path.basename(mp4)[:-4]; it = items.get(c, {}); x = det.get(c) or {}
    for f in glob.glob(f'{V}/{c}.*'):
        if f.endswith(('.jpg', '.json')): shutil.copy2(f, MID)
    tr = load(f'{V}/{c}.tr.json') or {}; vis = load(f'{V}/{c}.vis.json') or {}; ocr = load(f'{V}/{c}.ocr.json') or []
    ok = tr.get('flag') == 'ok'; segs = tr.get('segments', []); text = tr.get('text', '')
    words = len(text.split()); speech = (segs[-1]['end'] - segs[0]['start']) if segs else 0
    wpm = round(words / speech * 60) if speech > 5 and ok else None
    dur = x.get('duration') or vis.get('duration') or 0
    pc = it.get('play_count') or 0; lk = it.get('like_count') or 0; cm = it.get('comment_count') or 0
    date = dt.datetime.fromtimestamp(x['taken_at']).strftime('%Y-%m-%d') if x.get('taken_at') else '?'
    persist, tl = ocr_view(ocr, text, ok)
    first_ocr = ' / '.join(ocr[0]['lines']) if ocr and ocr[0]['lines'] else '(nenhum)'
    tg = tags(c); k = cat.get(c, {})
    audio = 'som original' if x.get('original_sound') else (f"música: {x['music'].get('title')} — {x['music'].get('artist')}" if x.get('music') else '?')
    L = [f'# {c} {" ".join(tg)}', '', f'https://www.instagram.com/reel/{c}/', '',
         f'- Data: {date} | duração: {round(dur, 1)}s | views: {fmt(pc)} ({round(pc / med, 1)}x a mediana do perfil) | likes: {fmt(lk)} ({lk / max(pc, 1):.2%}) | comentários: {fmt(cm)} ({cm / max(pc, 1):.3%}) | fixado: {it.get("pinned")}',
         f'- Áudio: {audio} | coautores: {x.get("coauthors") or it.get("coauthors") or []} | marcados: {x.get("usertags") or []} | parceria paga: {x.get("paid_partnership")}',
         f'- Fala: {words} palavras | {wpm} palavras/min | idioma {tr.get("language")} | qualidade {tr.get("flag")} | trocas de cena: {vis.get("cuts")} ({round(vis["cuts"] / dur * 60, 1) if vis.get("cuts") is not None and dur else "?"}/min)',
         f'- Imagens: {MID}/{c}.hook.jpg (0,4 s) | {MID}/{c}.sheet.jpg (8 quadros) | {MID}/{c}.cover.jpg (capa)']
    if k: L.append(f'- Classificação: {json.dumps(k, ensure_ascii=False)}')
    L += ['', '## Legenda do post', '', (x.get('caption') or '(sem legenda)').strip(), '',
          '## Texto na tela', '', f'- 1º quadro: {first_ocr}', f'- Fixo (≥50% dos quadros): {" / ".join(persist) or "(nenhum)"}']
    L += [f'- {t}' for t in tl[:40]] + ([f'- (+{len(tl) - 40} linhas)'] if len(tl) > 40 else [])
    L += ['', '## Transcrição (Whisper; pode errar nomes próprios)', '']
    L += [f'[{mmss(s["start"])}] {s["text"]}' for s in segs if s['start'] < 300] or ['(sem fala)']
    if segs and segs[-1]['start'] >= 300: L.append(f'(transcrição cortada nos primeiros 5 min de {mmss(segs[-1]["end"])})')
    open(f'{B}/fichas/{c}.md', 'w').write('\n'.join(L) + '\n')
    first = ' '.join(text.split()[:5])  # no máximo 5 palavras do Joel (regra de cópia)
    rows.append((tg, c, date, round(dur), pc, round(pc / med, 1), lk / max(pc, 1), cm / max(pc, 1), wpm, k.get('categoria', ''), first))
key = lambda r: (0 if r[0] else 1, -r[4])
nonpin = [i for i in d['items'] if not i.get('pinned') and i.get('play_count') is not None]
q = lambda p: plays[min(len(plays) - 1, int(p * len(plays)))]
I = [f'# @{U} — {d.get("full_name")}', '',
     f'- Coleta: {d.get("collected_at", "")[:10]} | seguidores: {fmt(d.get("followers"))} | posts: {fmt(d.get("media_count"))} | reels listados: {len(d["items"])} (lista completa: {d.get("complete")})',
     f'- Bio: {(d.get("biography") or "").replace(chr(10), " / ")}',
     f'- Views de todos os reels: mediana {fmt(int(med))} | p25 {fmt(q(.25))} | p75 {fmt(q(.75))} | p90 {fmt(q(.9))} | p99 {fmt(q(.99))} | máx {fmt(plays[-1])}',
     f'- Mediana de views por faixa da aba (recentes → antigos): ' + ' | '.join(f'{a}-{b}: {fmt(int(st.median([i["play_count"] for i in nonpin[a:b]])))}' for a, b in ((0, 50), (50, 200), (200, 500), (500, 1000), (1000, 99999)) if nonpin[a:b]),
     f'- Vídeos com ficha: {len(rows)} (grupos: viral {len(sel.get("viral", []))}, recentes {len(sel.get("recentes", []))}, motivacionais {len(sel.get("motivacionais", []))})', '',
     '| Grupos | Código | Data | Dur (s) | Views | x mediana | Likes/views | Coment./views | Pal./min | Categoria | Início da fala (5 palavras) |', '|---|---|---|---|---|---|---|---|---|---|---|']
I += [f'| {" ".join(r[0])} | {r[1]} | {r[2]} | {r[3]} | {fmt(r[4])} | {r[5]} | {r[6]:.2%} | {r[7]:.3%} | {r[8]} | {r[9]} | {r[10]} |' for r in sorted(rows, key=key)]
open(f'{B}/indice.md', 'w').write('\n'.join(I) + '\n')
print('fichas', len(rows), '->', f'{B}/fichas', '| índice', f'{B}/indice.md')
