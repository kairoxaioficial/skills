# python3 download.py <usersdir> <videosdir> perfil...  — baixa mp4 + capa dos selecionados (15 mais vistos + 15 mais recentes)
import sys, json, os, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
udir, vdir, users = sys.argv[1], sys.argv[2], sys.argv[3:]
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 'Referer': 'https://www.instagram.com/'}
jobs = []
for u in users:
    d = json.load(open(f'{udir}/{u}.json')); os.makedirs(f'{vdir}/{u}', exist_ok=True)
    for code in dict.fromkeys(d['sel']['top15'] + d['sel']['last15']):
        det = d['details'].get(code) or {}
        if det.get('video_url'): jobs.append((det['video_url'], f'{vdir}/{u}/{code}.mp4'))
        if det.get('thumb_url'): jobs.append((det['thumb_url'], f'{vdir}/{u}/{code}.cover.jpg'))
def get(job):
    url, path = job
    if os.path.exists(path) and os.path.getsize(path) > 1000: return 'skip'
    err = None
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180) as r: data = r.read()
            open(path, 'wb').write(data); return 'ok'
        except Exception as e:
            err = e; time.sleep(5 * (k + 1))
    return f'ERRO {os.path.basename(path)} {err}'
with ThreadPoolExecutor(4) as ex:
    res = list(ex.map(get, jobs))
print(len(jobs), 'arquivos', res.count('ok'), 'baixados', res.count('skip'), 'já existiam')
for r in res:
    if r.startswith('ERRO'): print(r)
