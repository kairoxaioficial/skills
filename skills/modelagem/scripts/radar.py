#!/usr/bin/env python3
"""Radar de novidades de IA com data real (Google News RSS, Brasil + EUA, e buscas em alta do Google Trends BR).

Uso:
  python3 radar.py                 # últimos 7 dias, temas padrão
  python3 radar.py 3               # últimos 3 dias
  python3 radar.py 14 "Sora" "n8n" # 14 dias + termos extras
Saída: AAAA-MM-DD | BR/US | veículo | manchete | link (do mais novo pro mais velho, sem duplicata).
"""
import sys, re, html, urllib.request, urllib.parse, email.utils

args = sys.argv[1:]
days = int(args.pop(0)) if args and args[0].isdigit() else 7
extra = args
BR = ['inteligência artificial', 'ChatGPT', 'Gemini IA', 'agente de IA', 'IA empresas', 'OpenAI', 'IA empregos', 'IA ganhar dinheiro'] + extra
US = ['AI launch', 'OpenAI', 'Google Gemini', 'Anthropic Claude', 'AI agents', 'AI video model', 'Meta AI', 'Nvidia AI'] + extra
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0 Safari/537.36'}


def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
            return r.read().decode('utf-8', 'ignore')
    except Exception as e:
        print(f'# falhou: {url[:90]} ({e})', file=sys.stderr)
        return ''


def news(q, hl, gl, ceid):
    url = 'https://news.google.com/rss/search?q=' + urllib.parse.quote(f'{q} when:{days}d') + f'&hl={hl}&gl={gl}&ceid={ceid}'
    for it in re.findall(r'<item>(.*?)</item>', get(url), re.S)[:15]:
        title = html.unescape(re.search(r'<title>(.*?)</title>', it, re.S).group(1))
        link = re.search(r'<link>(.*?)</link>', it, re.S).group(1)
        src = re.search(r'<source url="([^"]*)">(.*?)</source>', it, re.S)
        when = email.utils.parsedate_to_datetime(re.search(r'<pubDate>(.*?)</pubDate>', it).group(1))
        yield when, (html.unescape(src.group(2)) if src else '?'), title, link


rows, seen = [], set()
for qs, hl, gl, ceid, tag in [(BR, 'pt-BR', 'BR', 'BR:pt-419', 'BR'), (US, 'en-US', 'US', 'US:en', 'US')]:
    for q in qs:
        for when, src, title, link in news(q, hl, gl, ceid):
            key = re.sub(r'\W+', '', title.lower())[:70]
            if key in seen:
                continue
            seen.add(key)
            rows.append((when, tag, src, title, link))
rows.sort(key=lambda r: r[0], reverse=True)
print(f'# {len(rows)} manchetes dos últimos {days} dias (confira sempre a fonte primária antes de usar)')
for when, tag, src, title, link in rows:
    print(f'{when:%Y-%m-%d} | {tag} | {src} | {title} | {link}')
trends = [html.unescape(t) for t in re.findall(r'<title>(.*?)</title>', get('https://trends.google.com/trending/rss?geo=BR'))[1:]]
print('\n# Em alta agora no Google Brasil (Trends):', ', '.join(trends[:25]))
