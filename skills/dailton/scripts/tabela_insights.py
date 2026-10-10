"""Tabela de insights por post a partir de ig/cap/m-<code>.net.json (consulta PolarisMediaInsightsBaseSurfaceQuery).
uso: python3 tabela_insights.py <pasta cap> <posts.json> <saida.json>"""
import json, sys, glob, os

cap_dir, posts_f, out_f = sys.argv[1:4]
posts = {p['code']: p for p in json.load(open(posts_f))}
def v(m, k, dim=None):
    r = ((m.get(k) or {}).get('value') or {}).get('results') or []
    if dim is None:
        return r[0]['total_value'] if r else None
    return next((x['total_value'] for x in r if str((x.get('dimension_values') or [None])[0]) == dim), 0)
rows = []
for f in sorted(glob.glob(os.path.join(cap_dir, 'm-*.net.json'))):
    code = os.path.basename(f)[2:-9]
    m = None
    for c in json.load(open(f)):
        if c.get('fn') == 'PolarisMediaInsightsBaseSurfaceQuery':
            try:
                m = json.loads(c['body'])['data']['media']
            except Exception:
                pass
    if not m:
        print(code, 'sem dados'); continue
    views = v(m, 'umapi_unified_total_content_views_count')
    seg, nseg = v(m, 'umapi_content_views_count_follow_type_breakdowns', '1'), v(m, 'umapi_content_views_count_follow_type_breakdowns', '2')
    r = {'code': code, 'tipo': posts.get(code, {}).get('tipo'), 'data': posts.get(code, {}).get('data'),
         'views': views, 'views_seguidores': seg, 'views_nao_seguidores': nseg,
         'pct_nao_seg': round(100 * nseg / (seg + nseg), 1) if (seg + nseg) else None,
         'alcance': v(m, 'umapi_media_organic_account_reach_or_promoted_people_based_reach'),
         'curtidas': v(m, 'umapi_likes_count'), 'comentarios': v(m, 'umapi_comments_count'),
         'salvamentos': v(m, 'umapi_saves_count'), 'compartilhamentos': v(m, 'umapi_reshares_count'),
         'visitas_perfil': v(m, 'umapi_profile_views_from_impressions_count'), 'follows': v(m, 'umapi_follows_from_impressions_count'),
         'interacoes': v(m, 'umapi_total_interactions_count'),
         'legenda': (posts.get(code, {}).get('legenda') or '')[:90].replace('\n', ' ')}
    rows.append(r)
rows.sort(key=lambda r: r['data'] or '')
json.dump(rows, open(out_f, 'w'), ensure_ascii=False, indent=1)
for r in rows:
    print(f"{r['data']} {r['code']} {r['tipo']:<19} views {r['views']} (não-seg {r['pct_nao_seg']}%) alcance {r['alcance']} "
          f"curt {r['curtidas']} com {r['comentarios']} salv {r['salvamentos']} comp {r['compartilhamentos']} "
          f"visitas {r['visitas_perfil']} follows {r['follows']} | {r['legenda'][:60]}")
