"""Junta os posts do perfil a partir das respostas capturadas (consulta inicial + paginação).
uso: python3 posts.py <saida.json> <arquivo.net.json> [...]"""
import json, sys, datetime as dt

out, files = sys.argv[1], sys.argv[2:]
posts = {}
def walk(o):
    if isinstance(o, dict):
        if o.get('code') and o.get('pk') and 'taken_at' in o:
            yield o
        for v in o.values():
            yield from walk(v)
    elif isinstance(o, list):
        for v in o:
            yield from walk(v)
for f in files:
    for c in json.load(open(f)):
        if 'ProfilePosts' not in (c.get('fn') or ''):
            continue
        try:
            j = json.loads(c['body'])
        except Exception:
            continue
        for m in walk(j):
            cap = (m.get('caption') or {}).get('text') or ''
            posts[m['code']] = {
                'code': m['code'], 'pk': str(m['pk']).split('_')[0], 'dono': (m.get('user') or {}).get('username'),
                'coautores': [c.get('username') for c in (m.get('coauthor_producers') or [])],
                'tipo': m.get('product_type'), 'data': dt.datetime.fromtimestamp(m['taken_at']).strftime('%Y-%m-%d %H:%M'),
                'plays': m.get('play_count') or m.get('ig_play_count'), 'views': m.get('view_count'),
                'likes': m.get('like_count'), 'comments': m.get('comment_count'),
                'duracao': m.get('video_duration'), 'legenda': cap,
            }
ps = sorted(posts.values(), key=lambda p: p['data'], reverse=True)
json.dump(ps, open(out, 'w'), ensure_ascii=False, indent=1)
for p in ps:
    print(p['data'], p['code'], p['tipo'], p['dono'], p['coautores'], 'plays', p['plays'], 'likes', p['likes'], 'com', p['comments'],
          'dur', round(p['duracao'] or 0), '|', p['legenda'][:70].replace('\n', ' '))
print(len(ps), 'posts')
