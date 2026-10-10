# python3 ocr_frames.py <videos_root> [perfil...] : texto na tela a cada 2 s -> <código>.ocr.json [{t, lines}]
import glob, os, json, subprocess, tempfile, shutil, sys
root, users = sys.argv[1], sys.argv[2:]
OCR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ocr')
files = [f for u in (users or ['*']) for f in sorted(glob.glob(f'{root}/{u}/*.mp4'))]
for mp4 in files:
    out = mp4[:-4] + '.ocr.json'
    if os.path.exists(out): continue
    tmp = tempfile.mkdtemp()
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-i', mp4, '-vf', 'fps=1/2,scale=720:-2', '-q:v', '3', f'{tmp}/f%04d.jpg'])
    frames = sorted(glob.glob(f'{tmp}/*.jpg'))
    by = {}
    for line in subprocess.run([OCR] + frames, capture_output=True, text=True).stdout.splitlines():
        try: j = json.loads(line); by[j['f']] = j['lines']
        except Exception: pass
    json.dump([{'t': i * 2, 'lines': by.get(f, [])} for i, f in enumerate(frames)], open(out, 'w'), ensure_ascii=False)
    shutil.rmtree(tmp)
    print(os.path.relpath(mp4, root), len(frames), 'frames', flush=True)
