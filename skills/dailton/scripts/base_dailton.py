"""Monta a base medida do perfil do Dailton para a skill: reels-dailton.md + transcrições + json de métricas."""
import datetime as dt, json, os, re, shutil, statistics as st, subprocess, sys

S, K = sys.argv[1], sys.argv[2]  # scratchpad, pasta da skill
V = f'{S}/ig/videos/dailton'; OCR = os.path.expanduser('~/.claude/skills/modelagem/scripts/ocr')
d = json.load(open(f'{S}/ig/users/dailton_rolim.json')); it = {i['code']: i for i in d['items']}; det = d['details']
os.makedirs(f'{K}/dados/reels', exist_ok=True)

def ocr(c):
    for t in ('2.5', '0.4'):
        f = f'{V}/{c}_{t}.jpg'
        if os.path.exists(f):
            out = subprocess.run([OCR, f], capture_output=True, text=True).stdout.strip()
            try:
                lines = [l for l in json.loads(out.splitlines()[0])['lines'] if len(l) > 3]
            except Exception:
                lines = []
            if lines:
                return ' '.join(lines)
    return ''

codes = sorted([f[:-4] for f in os.listdir(V) if f.endswith('.txt')], key=lambda c: -(it[c].get('play_count') or 0))
vals = sorted(i['play_count'] for i in d['items'] if i.get('play_count'))
L = ['# Base medida: reels do @dailton_rolim', '',
     f"Coleta em {dt.date.today():%d/%m/%Y} pela sessão logada do Adriel. Perfil: {d.get('followers'):,} seguidores, {d.get('media_count'):,} posts. "
     f"Lista de reels: os {len(vals)} mais recentes da aba de reels (a coleta não chegou aos mais antigos).".replace(',', '.'), '',
     '## Números dos 400 reels recentes', '',
     f"- Mediana de visualizações: {int(st.median(vals)):,}".replace(',', '.'),
     f"- 90% dos reels ficam abaixo de {vals[int(len(vals) * .9)]:,} visualizações".replace(',', '.'),
     f"- Reels com 1 milhão ou mais: {sum(v >= 1e6 for v in vals)} de {len(vals)}; com 100 mil ou mais: {sum(v >= 1e5 for v in vals)}",
     f"- Maior: {vals[-1]:,} visualizações".replace(',', '.'), '',
     '## Os reels analisados (25 mais vistos entre os recentes + 10 mais novos)', '',
     'Título na tela = texto lido por OCR no quadro de 2,5 s (a caixa de texto que ele põe no meio da tela).', '',
     '| Reel | Data | Views | Curtidas | Comentários | Duração | Título na tela | Legenda |', '|---|---|---|---|---|---|---|---|']
blocos = []
for c in codes:
    i, v = it[c], det[c]
    data = dt.datetime.fromtimestamp(v['taken_at']).strftime('%d/%m/%Y')
    tit = ocr(c).replace('|', '/')
    leg = (v.get('caption') or '').split('\n')[0][:80].replace('|', '/')
    L.append(f"| [{c}](https://www.instagram.com/reel/{c}/) | {data} | {i['play_count']:,} | {i['like_count']:,} | {i['comment_count']:,} | {round(v.get('duration') or 0)} s | {tit} | {leg} |".replace(',', '.'))
    texto = ' '.join(re.sub(r'^\[[^\]]+\]\s*', '', l).strip() for l in open(f'{V}/{c}.txt'))
    shutil.copy(f'{V}/{c}.txt', f'{K}/dados/reels/{c}.txt')
    som = 'música' if v.get('music') else ('som original' if v.get('original_sound') else '-')
    blocos += [f"### {c} · {i['play_count']:,} views · {round(v.get('duration') or 0)} s · {som}".replace(',', '.'), '',
               f"- Título na tela: {tit or '(sem texto legível)'}", f"- Legenda: {(v.get('caption') or '').strip()[:300]}",
               f"- Colaboradores: {', '.join(v.get('coauthors') or []) or 'nenhum'}", '', f"> {texto}", '']
L += ['', '## Transcrições (fala dele, transcrição automática; pode ter erros)', ''] + blocos
open(f'{K}/dados/reels-dailton.md', 'w').write('\n'.join(L) + '\n')
slim = {k: d.get(k) for k in ('username', 'user_id', 'followers', 'following', 'media_count', 'biography', 'collected_at')}
slim['items'] = d['items']
slim['details'] = {c: {k: x for k, x in v.items() if k not in ('video_url', 'thumb_url')} for c, v in det.items()}
json.dump(slim, open(f'{K}/dados/dailton_rolim.json', 'w'), ensure_ascii=False)
print('ok', len(codes), 'reels na base')
