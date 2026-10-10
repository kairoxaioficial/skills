# python3 transcribe.py <videos_root> <usersdir> <top|recentes> [motor] perfil...
# Transcreve os vídeos selecionados de cada perfil (espera o marcador <perfil>/.baixado), na ordem pedida.
# motor: mlx (padrão, GPU, whisper-large-v3-turbo) ou fw-small / fw-medium (CPU, faster-whisper).
# Vários processos podem rodar juntos: cada vídeo é travado por um arquivo .tr.lock.
import sys, json, os, time, zlib, subprocess
root, udir, mode = sys.argv[1], sys.argv[2], sys.argv[3]
rest = sys.argv[4:]
engine = rest.pop(0) if rest and rest[0] in ('mlx', 'fw-small', 'fw-medium') else 'mlx'
users = rest
if engine == 'mlx':
    import mlx_whisper
    def run(p):
        r = mlx_whisper.transcribe(p, path_or_hf_repo='mlx-community/whisper-large-v3-turbo', language=None,
                                   condition_on_previous_text=False, temperature=0.0, verbose=None)
        return r.get('language'), [{'start': round(s['start'], 2), 'end': round(s['end'], 2), 'text': s['text'].strip()} for s in r['segments']]
    name = 'mlx-whisper-large-v3-turbo'
else:
    from faster_whisper import WhisperModel
    size = engine.split('-')[1]
    m = WhisperModel(size, device='cpu', compute_type='int8', cpu_threads=4)
    def run(p):
        segs, info = m.transcribe(p, beam_size=1, vad_filter=True, condition_on_previous_text=False, temperature=0.0)
        return info.language, [{'start': round(s.start, 2), 'end': round(s.end, 2), 'text': s.text.strip()} for s in segs]
    name = f'faster-whisper-{size}'
def flag_of(txt):
    w = txt.lower().split(); rep = max((w.count(x) for x in set(w)), default=0) / max(len(w), 1)
    cr = len(txt.encode()) / max(len(zlib.compress(txt.encode())), 1)
    return 'sem_fala_ou_alucinacao' if (len(w) < 8 or (len(w) > 20 and rep > 0.3) or cr > 3.0) else 'ok'
for u in users:
    while not os.path.exists(f'{root}/{u}/.baixado'): time.sleep(15)
    d = json.load(open(f'{udir}/{u}.json')); top = d['sel']['top15']; last = [c for c in d['sel']['last15'] if c not in top]
    order = top + last[::-1] if mode == 'top' else last + top[::-1]
    for c in order:
        mp4 = f'{root}/{u}/{c}.mp4'; out = mp4[:-4] + '.tr.json'
        if not os.path.exists(mp4) or os.path.exists(out): continue
        try: os.close(os.open(mp4[:-4] + '.tr.lock', os.O_CREAT | os.O_EXCL))
        except FileExistsError: continue
        t = time.time()
        if 'Audio:' not in subprocess.run(['ffmpeg', '-hide_banner', '-i', mp4], capture_output=True, text=True).stderr:
            json.dump({'language': None, 'flag': 'sem_fala_ou_alucinacao', 'engine': 'sem-faixa-de-audio', 'text': '', 'segments': []}, open(out, 'w'))
            print(f'{u}/{c} sem faixa de áudio', flush=True); continue
        try:
            lang, segs = run(mp4)
        except Exception as e:
            print('ERRO', mp4, str(e)[:150], flush=True); os.remove(mp4[:-4] + '.tr.lock'); continue
        txt = ' '.join(s['text'] for s in segs).strip()
        json.dump({'language': lang, 'flag': flag_of(txt), 'engine': name, 'text': txt, 'segments': segs}, open(out, 'w'), ensure_ascii=False)
        print(f'{u}/{c}', name, round(time.time() - t, 1), 's', len(txt), 'chars', flush=True)
