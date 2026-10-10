# python3 dossie.py <usersdir> <midiadir> <outdir> perfil...
# Monta um dossiê por criador: perfil, distribuição de views, tabela resumo e, para cada vídeo selecionado,
# métricas, legenda, transcrição com tempo e texto na tela (OCR). É a entrada da análise por criador.
import sys, json, os, re, subprocess, statistics as st, datetime as dt
udir, vdir, odir, users = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
OCR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ocr')
os.makedirs(odir, exist_ok=True)
fmt = lambda n: f'{n:,}'.replace(',', '.') if isinstance(n, int) else str(n)
tok = lambda x: re.findall(r'\w+', x.lower())
def load(p):
    try: return json.load(open(p))
    except Exception: return None
def ocr_img(p):
    try: return json.loads(subprocess.run([OCR, p], capture_output=True, text=True).stdout.splitlines()[0])['lines']
    except Exception: return []
def ocr_view(ocr, transcript, speech_ok):
    """Separa o texto fixo (em >= 50% dos frames) do texto que aparece ao longo do vídeo; tira legendas que só repetem a fala."""
    if not ocr: return [], []
    n = len(ocr); cnt = {}
    for fr in ocr:
        for l in set(fr['lines']): cnt[l] = cnt.get(l, 0) + 1
    persist = [l for l, c in cnt.items() if n >= 4 and c / n >= 0.5]
    vocab = set(tok(transcript)); seen = set(); tl = []
    for fr in ocr:
        for l in fr['lines']:
            if l in seen or l in persist: continue
            seen.add(l); w = tok(l)
            if speech_ok and w and sum(x in vocab for x in w) / len(w) >= 0.7: continue
            tl.append(f"[{fr['t']}s] {l}")
    return persist, tl
for u in users:
    d = json.load(open(f'{udir}/{u}.json')); items = d['items']
    plays = sorted(i['play_count'] for i in items if i.get('play_count') is not None)
    med = st.median(plays) if plays else 0
    q = lambda p: plays[min(len(plays) - 1, int(p * len(plays)))] if plays else 0
    L = [f'# Dossiê @{u} — {d.get("full_name")}', '',
         f'- Seguidores: {fmt(d.get("followers"))} | posts totais: {fmt(d.get("media_count"))} | reels coletados: {len(items)} (lista completa: {d.get("complete")}) | coleta: {d["collected_at"][:10]}',
         f'- Bio: {(d.get("biography") or "").replace(chr(10), " / ")}',
         f'- Views (plays) de TODOS os reels: mediana {fmt(int(med))} | p25 {fmt(q(.25))} | p75 {fmt(q(.75))} | p90 {fmt(q(.9))} | máx {fmt(plays[-1] if plays else 0)}', '']
    top, last = d['sel']['top15'], d['sel']['last15']
    rows = []
    for code in dict.fromkeys(top + last):
        det = d['details'].get(code) or {}; it = next(i for i in items if i['code'] == code)
        tags = ([f'TOP#{top.index(code) + 1}'] if code in top else []) + ([f'RECENTE#{last.index(code) + 1}'] if code in last else [])
        tr = load(f'{vdir}/{u}/{code}.tr.json') or {}; vis = load(f'{vdir}/{u}/{code}.vis.json') or {}; ocr = load(f'{vdir}/{u}/{code}.ocr.json') or []
        speech_ok = tr.get('flag') == 'ok'
        persist, tl = ocr_view(ocr, tr.get('text', ''), speech_ok)
        hook_ocr = ocr_img(f'{vdir}/{u}/{code}.hook.jpg')
        pc = it.get('play_count') or 0
        lr = (it.get('like_count') or 0) / max(pc, 1)
        if lr < 0.003: tags.append('PROVÁVEL-ANÚNCIO(likes/views<0,3%)')
        segs = tr.get('segments', []); words = len(tr.get('text', '').split())
        speech = (segs[-1]['end'] - segs[0]['start']) if segs else 0
        wpm = round(words / speech * 60) if speech > 5 and speech_ok else None
        dur = det.get('duration') or vis.get('duration')
        cpm = round(vis['cuts'] / dur * 60, 1) if vis.get('cuts') is not None and dur else None
        date = dt.datetime.fromtimestamp(det['taken_at']).strftime('%Y-%m-%d') if det.get('taken_at') else '?'
        rows.append((tags, code, date, dur, pc, it.get('like_count'), it.get('comment_count'), wpm, cpm))
        audio = 'som original' if det.get('original_sound') else ('música: ' + json.dumps(det.get('music'), ensure_ascii=False) if det.get('music') else '?')
        L += [f'## {" ".join(tags)} — https://www.instagram.com/reel/{code}/', '',
              f'- Data: {date} | duração: {round(dur or 0, 1)}s | views: {fmt(pc)} ({round(pc / med, 1) if med else "?"}x a mediana) | likes: {fmt(it.get("like_count"))} | comentários: {fmt(it.get("comment_count"))} | fixado: {it.get("pinned")}',
              f'- Palavras faladas: {words} | ritmo: {wpm} palavras/min | mudanças de cena (>0.3): {vis.get("cuts")} ({cpm}/min) | áudio: {audio} | coautores: {det.get("coauthors") or it.get("coauthors")} | parceria paga: {det.get("paid_partnership")}',
              f'- Transcrição: idioma {tr.get("language")} | qualidade {tr.get("flag")} | motor {tr.get("engine")} | likes/views {lr:.2%} | comentários/views {(it.get("comment_count") or 0) / max(pc, 1):.3%}',
              f'- Texto na tela no 1º frame (OCR): {" / ".join(hook_ocr) or "(nenhum)"}',
              f'- Texto fixo na tela (aparece em ≥50% dos frames): {" / ".join(persist) or "(nenhum)"}',
              f'- Imagens: {vdir}/{u}/{code}.hook.jpg (1º frame) | {vdir}/{u}/{code}.sheet.jpg (8 frames) | {vdir}/{u}/{code}.cover.jpg (capa)', '',
              '**Legenda (caption):**', '', '> ' + (det.get('caption') or '(sem legenda)').replace('\n', '\n> '), '',
              '**Transcrição (com tempo):**', '']
        L += ([f'[{s["start"]:.1f}-{s["end"]:.1f}] {s["text"]}' for s in segs] if speech_ok else ['(sem fala útil: ' + (tr.get('text', '')[:120] or 'vazio') + ')'])
        L += ['', '**Texto na tela ao longo do vídeo (OCR a cada 2s' + (', sem as legendas que repetem a fala' if speech_ok else '') + '):**', ''] + (tl[:80] or ['(nenhum)']) + ['']
    hdr = ['| tags | código | data | dur(s) | views | likes | coment. | pal/min | cortes/min |', '|---|---|---|---|---|---|---|---|---|']
    tab = [f'| {" ".join(t)} | {c} | {da} | {round(du or 0)} | {fmt(p)} | {fmt(l)} | {fmt(cm)} | {w} | {cp} |' for t, c, da, du, p, l, cm, w, cp in rows]
    L[6:6] = ['## Tabela resumo', ''] + hdr + tab + ['']
    open(f'{odir}/{u}.md', 'w').write('\n'.join(L))
    print(u, 'dossiê', len(rows), 'vídeos', sum(1 for r in rows if r[7]), 'com fala útil')
