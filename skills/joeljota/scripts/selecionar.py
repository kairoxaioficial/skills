# python3 selecionar.py <journal.jsonl | classificacao.json> [pasta_trabalho]
# Lê a classificação das legendas (resultado do workflow wf_classificar.js: o journal.jsonl dele ou um JSON {"videos": [...]}),
# grava em categorias e escolhe sel.motivacionais = os 20 mais vistos com grau motivacional >= 2 fora dos virais e recentes.
import sys, os, json
src = sys.argv[1]; W = sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser('~/.cache/joeljota')
F = f'{W}/users/joeljota.json'; d = json.load(open(F)); it = {i['code']: i for i in d['items']}
vids = []
if src.endswith('.jsonl'):
    for l in open(src):
        try: o = json.loads(l)
        except ValueError: continue
        if o.get('type') == 'result':
            v = o.get('result') or o.get('value') or {}
            vids += (json.loads(v) if isinstance(v, str) else v).get('videos') or []
else:
    vids = json.load(open(src))['videos']
d['categorias'] = {v['code']: {k: v[k] for k in ('categoria', 'subtema', 'motivacional', 'mensagem', 'emocao')} for v in vids if v['code'] in d['details']}
falta = [c for c in d['details'] if c not in d['categorias']]
if falta: print('AVISO: sem classificação', len(falta), falta[:10])
fora = set(d['sel']['viral'] + d['sel']['recentes'])
d['sel']['motivacionais'] = [c for c in sorted(d['categorias'], key=lambda c: -(it[c].get('play_count') or 0))
                             if d['categorias'][c]['motivacional'] >= 2 and c not in fora][:20]
json.dump(d, open(F, 'w'))
print('classificados', len(d['categorias']), '| motivacionais', len(d['sel']['motivacionais']))
