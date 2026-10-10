# python3 stats.py [usersdir] [midiadir] [saida.json] -> números comparativos dos criadores (base do relatório)
import json, os, re, sys, statistics as st, datetime as dt
UD, VD, OUT = (sys.argv[1:4] + ['users', 'videos', 'stats.json'][len(sys.argv[1:4]):])
U = ['oalanicolas', 'inventormiguel', 'rodrigotadewald', 'odanilogato', 'ddiasmatt']
def load(p):
    try: return json.load(open(p))
    except Exception: return None
med = lambda xs: round(st.median(xs), 2) if xs else None
CTA = {'comenta/comente': r'coment[ae]|comentar', 'palavra-chave (digite/escreva)': r'\bdigit[ae]\b|\bescrev[ae]\b', 'link na bio': r'link na bio|link da bio', 'salva': r'\bsalv[ae]\b', 'compartilha/envia': r'compartilh|\benvi[ae]\b|manda pr', 'segue/siga': r'\bsig[ae]\b|\bsegue\b|seguir'}
out = {}
for u in U:
    if not os.path.exists(f'{UD}/{u}.json'): continue
    d = json.load(open(f'{UD}/{u}.json')); it = d['items']; det = d['details']
    nonpin = [i for i in it if not i['pinned']]
    plays = [i['play_count'] for i in it if i.get('play_count') is not None]
    rec = {'seguidores': d['followers'], 'posts': d['media_count'], 'reels': len(it), 'reels_com_views': len(plays), 'views_mediana_todos': med(plays),
           'views_mediana_ult50': med([i['play_count'] for i in nonpin[:50] if i.get('play_count') is not None]), 'views_mediana_50a200': med([i['play_count'] for i in nonpin[50:200] if i.get('play_count') is not None]), 'views_mediana_antigos': med([i['play_count'] for i in nonpin[200:] if i.get('play_count') is not None])}
    for grp in ['top15', 'last15']:
        codes = d['sel'][grp]; g = {}
        rows = [(next(i for i in it if i['code'] == c), det[c]) for c in codes]
        g['views_mediana'] = med([i['play_count'] or 0 for i, _ in rows]); g['views_min'] = min(i['play_count'] or 0 for i, _ in rows); g['views_max'] = max(i['play_count'] or 0 for i, _ in rows)
        g['multiplo_da_mediana'] = round(g['views_mediana'] / rec['views_mediana_todos'], 1) if rec['views_mediana_todos'] else None
        g['likes_por_view_%'] = med([100 * (i['like_count'] or 0) / max(i['play_count'] or 1, 1) for i, _ in rows])
        g['coment_por_mil_views'] = med([1000 * (i['comment_count'] or 0) / max(i['play_count'] or 1, 1) for i, _ in rows])
        g['duracao_mediana_s'] = med([x.get('duration') or 0 for _, x in rows])
        trs = [load(f'{VD}/{u}/{c}.tr.json') or {} for c in codes]
        vis = [load(f'{VD}/{u}/{c}.vis.json') or {} for c in codes]
        ocr = [load(f'{VD}/{u}/{c}.ocr.json') or [] for c in codes]
        g['transcritos'] = sum(1 for t in trs if t)
        g['sem_fala_%'] = round(100 * sum(1 for t in trs if t and t.get('flag') != 'ok') / max(g['transcritos'], 1))
        g['fala_nao_pt_%'] = round(100 * sum(1 for t in trs if t.get('flag') == 'ok' and t.get('language') not in (None, 'pt')) / max(g['transcritos'], 1))
        wpm = []
        for t in trs:
            s = t.get('segments') or []
            if t.get('flag') == 'ok' and t.get('language') == 'pt' and s and s[-1]['end'] - s[0]['start'] > 5: wpm.append(len(t['text'].split()) / (s[-1]['end'] - s[0]['start']) * 60)
        g['palavras_por_min_mediana'] = med(wpm)
        g['trocas_de_cena_por_min_mediana'] = med([v['cuts'] / v['duration'] * 60 for v in vis if v.get('duration')])
        g['texto_na_tela_no_1o_frame_%'] = round(100 * sum(1 for o in ocr if o and o[0]['lines']) / len(codes))
        caps = [x.get('caption') or '' for _, x in rows]
        g['legenda_caracteres_mediana'] = med([len(c) for c in caps]); g['hashtags_mediana'] = med([len(re.findall(r'#\w+', c)) for c in caps])
        g['cta_na_legenda_%'] = {k: round(100 * sum(1 for c in caps if re.search(p, c, re.I)) / len(caps)) for k, p in CTA.items()}
        g['colab_%'] = round(100 * sum(1 for _, x in rows if x.get('coauthors')) / len(rows))
        g['musica_licenciada_%'] = round(100 * sum(1 for _, x in rows if x.get('music')) / len(rows))
        g['provavel_anuncio'] = [c for (i, _), c in zip(rows, codes) if (i['like_count'] or 0) / max(i['play_count'] or 1, 1) < 0.003]
        if grp == 'last15':
            ts = sorted(x['taken_at'] for _, x in rows)
            g['periodo'] = f"{dt.datetime.fromtimestamp(ts[0]):%Y-%m-%d} a {dt.datetime.fromtimestamp(ts[-1]):%Y-%m-%d}"
            g['posts_por_semana'] = round((len(ts) - 1) / max((ts[-1] - ts[0]) / 86400 / 7, 0.01), 1)
        else:
            ys = [dt.datetime.fromtimestamp(x['taken_at']).year for _, x in rows]; g['anos'] = {y: ys.count(y) for y in sorted(set(ys))}
        rec[grp] = g
    out[u] = rec
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('stats', OUT, list(out))
