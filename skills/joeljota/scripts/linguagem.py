# python3 linguagem.py [pasta_trabalho] — números da fala do Joel por grupo (viral, recentes, motivacionais, todos):
# tamanho de frase, ritmo, pessoa gramatical, contrações, perguntas, imperativos, antíteses e n-gramas recorrentes
# (candidatos a bordão, contados por vídeo). Saída: ../dados/linguagem.md
import sys, os, json, re, glob, statistics as st
from collections import Counter
W = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/.cache/joeljota')
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dados'))
U = 'joeljota'; V = f'{W}/videos/{U}'
d = json.load(open(f'{W}/users/{U}.json')); sel = d.get('sel', {})
STOP = set('a o as os um uma uns umas de do da dos das no na nos nas em por para pra pro com sem que se e é ou mas mais menos já não sim eu tu ele ela nós vós eles elas você vocês me te lhe nos vos meu minha seu sua teu tua isso isto aquilo esse essa este esta aquele aquela ao aos à às como quando onde porque porquê então aí lá cá tá né foi ser ter tem tinha vai vou era são está estão estou muito pouco tudo nada todo toda todos todas qual quais quem cara gente coisa coisas também só sobre até depois antes ainda bem mesmo cada outro outra pelo pela pelos pelas num numa dele dela deles delas'.split())
TR = {}; cat = d.get('categorias', {})
for f in glob.glob(f'{V}/*.tr.json'):
    t = json.load(open(f)); c = os.path.basename(f)[:-8]
    # fora: sem fala válida, outro idioma e vídeos em que quem fala é só o convidado (classificação da análise)
    if t.get('flag') == 'ok' and t.get('language') == 'pt' and cat.get(c, {}).get('quem_fala') not in ('convidado', 'sem fala'): TR[c] = t
groups = {'viral': sel.get('viral', []), 'recentes': sel.get('recentes', []), 'motivacionais': sel.get('motivacionais', []), 'todos': list(TR)}
words = lambda s: re.findall(r"[\wÀ-ú]+(?:-[\wÀ-ú]+)?", s.lower())
sents = lambda s: [x.strip() for x in re.split(r'(?<=[.!?])\s+', s) if words(x)]
per100 = lambda n, w: round(100 * n / max(w, 1), 2)
PAT = {
    'você/vocês': r'\b(você|vocês|cê|ocê)\b', 'eu/me/meu': r'\b(eu|me|meu|minha|comigo)\b', 'a gente/nós': r'\b(a gente|nós|nosso|nossa)\b',
    'tá/tô/pra/pro/né/cê': r'\b(tá|tô|pra|pro|né|cê|tava|tamo)\b', 'perguntas (?)': r'\?', 'exclamações (!)': r'!',
    'imperativos comuns': r'\b(faça|faz|para de|pare|levanta|levante|vai|vá|entenda|entende|olha|escuta|pensa|pense|acorda|anota|lembra|lembre|começa|comece|seja|sê|tenha|bora|vem|corre|treina|trabalha|decide|decida|assume|assuma|aprende|aprenda|cuida|cuide)\b',
    '"não é X, é Y" e variações': r'\bnão (é|era|são|foi) [^.?!]{1,60}?[,;]\s*(é|era|são|foi)\b|\bnão é sobre\b|\bo problema não é\b',
    'número/dado': r'\b\d+[\d.,]*\b|\b(mil|milhão|milhões|bilhão|bilhões|por cento|%)',
    'disciplina/constância': r'\b(disciplin\w*|const[aâ]nc\w*|consist\w*|h[áa]bito\w*|rotina\w*)\b',
    'Deus/fé': r'\b(deus|jesus|fé|oração|bíblia|senhor)\b', 'família/filho(a)/esposa': r'\b(família|filh[oa]s?|esposa|mulher|marido|pai|mãe)\b',
    'esporte/natação/atleta': r'\b(nata[çc]\w*|nadador\w*|atleta\w*|treino\w*|treinador\w*|competi\w*|olimp\w*|piscina|medalha\w*|campe\w*)\b',
    'dinheiro/negócio/venda': r'\b(dinheiro|rico\w*|empresa\w*|neg[óo]cio\w*|vend\w*|client\w*|empreend\w*|lucro|fatur\w*)\b',
}
L = ['# Linguagem do @joeljota em números', '', f'Transcrições em português com fala válida: {len(TR)}. "por 100" = ocorrências a cada 100 palavras. "% vídeos" = vídeos do grupo em que aparece ao menos 1 vez.', '']
L += ['| Medida | ' + ' | '.join(groups) + ' |', '|---|' + '---|' * len(groups)]
rows = {}
for g, codes in groups.items():
    cs = [c for c in codes if c in TR]; T = [TR[c] for c in cs]
    allw = sum(len(words(t['text'])) for t in T)
    sl = [len(words(s)) for t in T for s in sents(t['text'])]
    wpm = [len(words(t['text'])) / ((t['segments'][-1]['end'] - t['segments'][0]['start']) / 60) for t in T if t['segments'] and t['segments'][-1]['end'] - t['segments'][0]['start'] > 5]
    r = {'vídeos com fala': len(cs), 'palavras por vídeo (mediana)': st.median([len(words(t['text'])) for t in T]) if T else '-',
         'palavras por minuto (mediana)': round(st.median(wpm)) if wpm else '-', 'palavras por frase (mediana)': st.median(sl) if sl else '-',
         'palavras por frase (p25–p75)': f'{sorted(sl)[len(sl) // 4]}–{sorted(sl)[3 * len(sl) // 4]}' if sl else '-',
         '% frases com até 5 palavras': f'{100 * sum(1 for x in sl if x <= 5) / max(len(sl), 1):.0f}%', '% frases com 20+ palavras': f'{100 * sum(1 for x in sl if x >= 20) / max(len(sl), 1):.0f}%',
         '1ª frase é pergunta (% vídeos)': f'{100 * sum(1 for t in T if sents(t["text"]) and sents(t["text"])[0].endswith("?")) / max(len(T), 1):.0f}%'}
    for k, p in PAT.items():
        n = sum(len(re.findall(p, t['text'].lower())) for t in T); v = sum(1 for t in T if re.search(p, t['text'].lower()))
        r[k] = f'{per100(n, allw)} por 100 · {100 * v / max(len(T), 1):.0f}% vídeos'
    rows[g] = r
for k in rows['todos']: L.append(f'| {k} | ' + ' | '.join(str(rows[g].get(k, '-')) for g in groups) + ' |')
def grams(t, n):
    w = words(t); return {' '.join(w[i:i + n]) for i in range(len(w) - n + 1)}
L += ['', '## Expressões que mais se repetem entre vídeos (candidatas a bordão)', '', 'Contagem = em quantos vídeos aparece (todos os vídeos com fala). Só n-gramas com ao menos 1 palavra fora da lista de palavras vazias.', '']
for n in (5, 4, 3, 2):
    cnt = Counter(g for t in TR.values() for g in grams(t['text'], n) if sum(x not in STOP for x in g.split()) >= (1 if n > 2 else 2))
    top = [(g, k) for g, k in cnt.most_common(400) if k >= 3][:45 if n > 2 else 30]
    L += [f'**{n} palavras:** ' + ' · '.join(f'{g} ({k})' for g, k in top), '']
uni = Counter(x for t in TR.values() for x in set(words(t['text'])) if x not in STOP and len(x) > 3)
L += ['## Palavras de conteúdo mais frequentes (em quantos vídeos)', '', ' · '.join(f'{w} ({k})' for w, k in uni.most_common(120)), '']
os.makedirs(B, exist_ok=True); open(f'{B}/linguagem.md', 'w').write('\n'.join(L) + '\n')
print('linguagem', len(TR), 'transcrições ->', f'{B}/linguagem.md')
