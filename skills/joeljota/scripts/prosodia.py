# python3 prosodia.py [pasta_trabalho] — como o Joel fala, em números, a partir do tempo por palavra (transcrever_corpus.py)
# e do volume (ffmpeg ebur128): quando começa a falar, velocidade no início/meio/fim, pausas, faixa de volume.
# Saída: ../dados/prosodia.md
import sys, os, json, re, subprocess, statistics as st
W = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/.cache/joeljota')
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dados'))
U = 'joeljota'; V = f'{W}/videos/{U}'
d = json.load(open(f'{W}/users/{U}.json')); sel = d['sel']; cat = d.get('categorias', {})
med = lambda xs: round(st.median(xs), 2) if xs else None
def loud(mp4):
    e = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', mp4, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    i = re.findall(r'I:\s+(-?[\d.]+) LUFS', e); lra = re.findall(r'LRA:\s+([\d.]+) LU', e)
    return (float(i[-1]) if i else None), (float(lra[-1]) if lra else None)
rows = {}
for c in dict.fromkeys(sel['viral'] + sel['recentes'] + sel.get('motivacionais', [])):
    p = f'{V}/{c}.tr.json'
    if not os.path.exists(p): continue
    t = json.load(open(p))
    if not t.get('words_ok') or t.get('flag') != 'ok' or cat.get(c, {}).get('quem_fala') in ('convidado', 'sem fala'): continue
    w = [x for s in t['segments'] for x in s.get('words', []) if x['w']]
    if len(w) < 20: continue
    a, b = w[0]['s'], w[-1]['e']; fala = b - a
    gaps = [(w[k + 1]['s'] - w[k]['e'], w[k]['e']) for k in range(len(w) - 1)]
    third = lambda k: [x for x in w if a + k * fala / 3 <= x['s'] < a + (k + 1) * fala / 3]
    wpm3 = [round(len(third(k)) / (fala / 3) * 60) for k in range(3)]
    dur = (d['details'].get(c) or {}).get('duration') or b
    big = max(gaps, key=lambda g: g[0])
    i, lra = loud(f'{V}/{c}.mp4')
    rows[c] = {'1a_palavra_s': round(a, 2), 'ppm': round(len(w) / fala * 60), 'ppm_inicio_meio_fim': wpm3,
               'pausas_0.5s_por_min': round(sum(1 for g, _ in gaps if g >= 0.5) / (fala / 60), 1), 'pausas_1s_por_min': round(sum(1 for g, _ in gaps if g >= 1.0) / (fala / 60), 1),
               'maior_pausa_s': round(big[0], 2), 'maior_pausa_em_%': round(100 * big[1] / dur), 'fala_%_do_video': round(100 * fala / dur),
               'loudness_LUFS': i, 'LRA_LU': lra}
    print(c, rows[c], flush=True)
groups = {'viral': sel['viral'], 'recentes': sel['recentes'], 'motivacionais': sel.get('motivacionais', []), 'todos': list(rows)}
K = ['1a_palavra_s', 'ppm', 'pausas_0.5s_por_min', 'pausas_1s_por_min', 'maior_pausa_s', 'maior_pausa_em_%', 'fala_%_do_video', 'loudness_LUFS', 'LRA_LU']
L = ['# Prosódia do @joeljota (como ele fala)', '',
     'Tempo por palavra do whisper-large-v3-turbo; volume pelo ebur128 do ffmpeg (LRA = faixa de variação do volume, em LU; música de fundo também conta). Medianas por grupo; só vídeos em que o Joel fala.', '',
     '| Medida (mediana) | ' + ' | '.join(groups) + ' |', '|---|' + '---|' * len(groups)]
for k in K:
    L.append(f'| {k} | ' + ' | '.join(str(med([rows[c][k] for c in cs if c in rows and rows[c][k] is not None])) for cs in groups.values()) + ' |')
for n, lab in enumerate(['início', 'meio', 'fim']):
    L.append(f'| palavras/min no {lab} | ' + ' | '.join(str(med([rows[c]['ppm_inicio_meio_fim'][n] for c in cs if c in rows])) for cs in groups.values()) + ' |')
L.append('| vídeos | ' + ' | '.join(str(sum(1 for c in cs if c in rows)) for cs in groups.values()) + ' |')
L += ['', '## Por vídeo', '', '| Código | ' + ' | '.join(K) + ' | ppm início/meio/fim |', '|---|' + '---|' * (len(K) + 1)]
L += [f'| {c} | ' + ' | '.join(str(r[k]) for k in K) + f' | {"/".join(map(str, r["ppm_inicio_meio_fim"]))} |' for c, r in rows.items()]
open(f'{B}/prosodia.md', 'w').write('\n'.join(L) + '\n')
print('prosodia', len(rows), 'vídeos ->', f'{B}/prosodia.md')
