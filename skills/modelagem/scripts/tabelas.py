# python3 tabelas.py <usersdir> <stats.json> <saida.md> -> tabela comparativa + tabelas de TOP 15 e ÚLTIMOS 15 por criador
import json, sys, datetime as dt
UD, SJ, OUT = sys.argv[1:4]
U = [('odanilogato', 'Danilo Gato'), ('inventormiguel', 'Miguel Lannes (Inventor Miguel)'), ('oalanicolas', 'Alan Nicolas'), ('rodrigotadewald', 'Rodrigo Tadewald'), ('ddiasmatt', 'Mateus Dias')]
S = json.load(open(SJ)); U = [x for x in U if x[0] in S]
n = lambda x: f'{x:,.0f}'.replace(',', '.') if isinstance(x, (int, float)) else str(x)
p = lambda x: '—' if x is None else (f'{x:.1f}'.replace('.', ',') if isinstance(x, float) else str(x))
L = ['| Métrica | ' + ' | '.join(f'@{u}' for u, _ in U) + ' |', '|---|' + '---|' * len(U)]
def row(label, f): L.append(f'| {label} | ' + ' | '.join(f(S[u]) for u, _ in U) + ' |')
row('Seguidores', lambda s: n(s['seguidores'])); row('Reels no perfil (com contagem de views)', lambda s: f"{n(s['reels'])} ({n(s.get('reels_com_views', s['reels']))})")
row('Views: mediana de todos os reels', lambda s: n(s['views_mediana_todos']))
row('Views: mediana dos 50 mais recentes', lambda s: n(s['views_mediana_ult50']))
row('TOP 15: faixa de views', lambda s: f"{n(s['top15']['views_min'])} a {n(s['top15']['views_max'])}")
row('TOP 15: mediana (x a mediana geral)', lambda s: f"{n(s['top15']['views_mediana'])} ({p(s['top15']['multiplo_da_mediana'])}x)")
row('ÚLTIMOS 15: mediana (x a mediana geral)', lambda s: f"{n(s['last15']['views_mediana'])} ({p(s['last15']['multiplo_da_mediana'])}x)")
row('Posts por semana (últimos 15)', lambda s: p(s['last15']['posts_por_semana']))
row('Duração mediana TOP / ÚLTIMOS (s)', lambda s: f"{p(s['top15']['duracao_mediana_s'])} / {p(s['last15']['duracao_mediana_s'])}")
row('Palavras por minuto TOP / ÚLTIMOS', lambda s: f"{p(s['top15']['palavras_por_min_mediana'])} / {p(s['last15']['palavras_por_min_mediana'])}")
row('Vídeos sem fala TOP / ÚLTIMOS (%)', lambda s: f"{s['top15']['sem_fala_%']} / {s['last15']['sem_fala_%']}")
row('Texto na tela no 1º frame TOP / ÚLTIMOS (%)', lambda s: f"{s['top15']['texto_na_tela_no_1o_frame_%']} / {s['last15']['texto_na_tela_no_1o_frame_%']}")
row('Trocas de cena por minuto TOP / ÚLTIMOS', lambda s: f"{p(s['top15']['trocas_de_cena_por_min_mediana'])} / {p(s['last15']['trocas_de_cena_por_min_mediana'])}")
row('Likes por view TOP / ÚLTIMOS (%)', lambda s: f"{p(s['top15']['likes_por_view_%'])} / {p(s['last15']['likes_por_view_%'])}")
row('Comentários por mil views TOP / ÚLTIMOS', lambda s: f"{p(s['top15']['coment_por_mil_views'])} / {p(s['last15']['coment_por_mil_views'])}")
row('Legenda: caracteres (mediana) TOP / ÚLTIMOS', lambda s: f"{n(s['top15']['legenda_caracteres_mediana'])} / {n(s['last15']['legenda_caracteres_mediana'])}")
row('Legenda pede comentário TOP / ÚLTIMOS (%)', lambda s: f"{s['top15']['cta_na_legenda_%']['comenta/comente']} / {s['last15']['cta_na_legenda_%']['comenta/comente']}")
row('TOP 15 com cara de anúncio (likes/views < 0,3%)', lambda s: str(len(s['top15']['provavel_anuncio'])))
out = ['\n'.join(L)]
for u, nome in U:
    d = json.load(open(f'{UD}/{u}.json')); it = {i['code']: i for i in d['items']}
    for grp, tit in [('top15', 'os 15 mais vistos de todos os tempos'), ('last15', 'os 15 mais recentes')]:
        T = [f'\n**@{u} ({nome}): {tit}**\n', '| # | Reel | Data | Duração | Views | Likes | Comentários |', '|---|---|---|---|---|---|---|']
        for k, c in enumerate(d['sel'][grp], 1):
            x = d['details'][c]; i = it[c]
            flag = ' (provável anúncio)' if (i['like_count'] or 0) / max(i['play_count'] or 1, 1) < 0.003 else ''
            T.append(f"| {k} | [{c}](https://www.instagram.com/reel/{c}/){flag} | {dt.datetime.fromtimestamp(x['taken_at']):%d/%m/%Y} | {round(x.get('duration') or 0)} s | {n(i['play_count'])} | {n(i['like_count'])} | {n(i['comment_count'])} |")
        out.append('\n'.join(T))
open(OUT, 'w').write('\n'.join(out)); print('tabelas', OUT, len('\n'.join(out)), 'caracteres')
