# python3 transcrever_corpus.py [pasta_trabalho] — retranscreve o corpus da análise (viral + recentes + motivacionais)
# com o whisper-large-v3-turbo (mlx, GPU), em português e com tempo por palavra, por cima da transcrição rápida da coleta.
# O tempo por palavra alimenta prosodia.py (pausas, aceleração). Pula o que já foi feito (words_ok).
import sys, os, json, time, zlib, subprocess, tempfile
import mlx_whisper
W = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/.cache/joeljota')
U = 'joeljota'; V = f'{W}/videos/{U}'
d = json.load(open(f'{W}/users/{U}.json')); sel = d['sel']
corpus = list(dict.fromkeys(sel['viral'] + sel['recentes'] + sel.get('motivacionais', [])))
def flag_of(txt):  # mesmo critério de ../../modelagem/scripts/transcribe.py
    w = txt.lower().split(); rep = max((w.count(x) for x in set(w)), default=0) / max(len(w), 1)
    cr = len(txt.encode()) / max(len(zlib.compress(txt.encode())), 1)
    return 'sem_fala_ou_alucinacao' if (len(w) < 8 or (len(w) > 20 and rep > 0.3) or cr > 3.0) else 'ok'
feitos = 0
for c in corpus:
    mp4, out = f'{V}/{c}.mp4', f'{V}/{c}.tr.json'
    if not os.path.exists(mp4): print(c, 'sem mp4', flush=True); continue
    old = json.load(open(out)) if os.path.exists(out) else {}
    if old.get('words_ok') or old.get('engine') == 'sem-faixa-de-audio': continue
    t = time.time(); wav = os.path.join(tempfile.gettempdir(), f'joeljota-{c}.wav')
    # só os 5 primeiros minutos (as fichas também param aí); vídeo sem faixa de áudio não gera o wav
    if subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-t', '300', '-i', mp4, '-vn', '-ac', '1', '-ar', '16000', wav]).returncode or not os.path.exists(wav):
        json.dump({'language': None, 'flag': 'sem_fala_ou_alucinacao', 'engine': 'sem-faixa-de-audio', 'text': '', 'segments': []}, open(out, 'w'))
        print(c, 'sem faixa de áudio', flush=True); continue
    try:
        r = mlx_whisper.transcribe(wav, path_or_hf_repo='mlx-community/whisper-large-v3-turbo', language='pt', word_timestamps=True,
                                   condition_on_previous_text=False, temperature=0.0, verbose=None)
    except Exception as e:
        print('ERRO', c, str(e)[:150], flush=True); continue
    finally:
        os.remove(wav)
    segs = [{'start': round(s['start'], 2), 'end': round(s['end'], 2), 'text': s['text'].strip(),
             'words': [{'w': x['word'].strip(), 's': round(x['start'], 2), 'e': round(x['end'], 2)} for x in s.get('words', [])]} for s in r['segments']]
    txt = ' '.join(s['text'] for s in segs).strip()
    json.dump({'language': 'pt', 'flag': flag_of(txt), 'engine': 'mlx-whisper-large-v3-turbo+palavras', 'words_ok': True, 'text': txt, 'segments': segs},
              open(out, 'w'), ensure_ascii=False)
    feitos += 1
    print(c, round(time.time() - t, 1), 's', len(txt.split()), 'palavras', flush=True)
print('corpus', len(corpus), 'retranscritos agora', feitos)
