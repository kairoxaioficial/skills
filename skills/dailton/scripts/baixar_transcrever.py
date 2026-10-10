"""Baixa os reels selecionados (video_url dos detalhes), transcreve com o transcritor nativo e tira quadros do início.
uso: python3 baixar_transcrever.py <perfil.json> <pasta saída> <topN por views> <recentesK>"""
import json, os, subprocess, sys, urllib.request

perfil, out, top_n, rec_k = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
S = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(perfil)); it = {i['code']: i for i in d['items']}; det = d.get('details', {})
ok = [c for c, v in det.items() if v and v.get('ok') and v.get('video_url')]
por_views = sorted(ok, key=lambda c: -(it[c].get('play_count') or 0))[:top_n]
recentes = sorted(ok, key=lambda c: -det[c]['taken_at'])[:rec_k]
os.makedirs(out, exist_ok=True)
for c in dict.fromkeys(por_views + recentes):
    mp4, wav = f'{out}/{c}.mp4', f'{out}/{c}.wav'
    try:
        if not os.path.exists(mp4):
            req = urllib.request.Request(det[c]['video_url'], headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=60) as r, open(mp4, 'wb') as f:
                f.write(r.read())
        subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', mp4, '-vn', '-ac', '1', '-ar', '16000', wav], check=True)
        subprocess.run([f'{S}/transcrever_apple', wav, f'{out}/{c}'], check=True, capture_output=True)
        for t in ('0.4', '2.5'):
            subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-ss', t, '-i', mp4, '-frames:v', '1', '-vf', 'scale=270:-2',
                            f'{out}/{c}_{t}.jpg'], check=True)
        os.remove(wav)
        print('ok', c)
    except Exception as e:
        print('falhou', c, str(e)[:120])
