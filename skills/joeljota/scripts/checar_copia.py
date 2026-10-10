# python3 checar_copia.py <arquivo | -> [n]  — confere um texto (roteiro, legenda, referência; "-" lê da entrada padrão):
# 1) sequências de n palavras (padrão 6) que existam nas transcrições e legendas do Joel (../dados/fichas): "COPIADO";
# 2) sequências de 4 palavras iguais aos exemplos de references/moldes.md (§8 e amostras entre colchetes): "DO MOLDE".
# Sai com código 1 se houver "COPIADO". "DO MOLDE" é aviso: reescreva se veio de um exemplo.
import sys, os, re, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
n = int(sys.argv[2]) if len(sys.argv) > 2 else 6
src = sys.stdin.read() if sys.argv[1] == '-' else open(sys.argv[1]).read()
words = lambda s: re.findall(r'[\wÀ-ú]+', s.lower())
grams = lambda w, k: {' '.join(w[i:i + k]) for i in range(len(w) - k + 1)}
fichas = glob.glob(f'{D}/dados/fichas/*.md')
if not fichas: sys.exit(f'sem fichas em {D}/dados/fichas: rode scripts/processar.sh antes')
joel = set()
for f in fichas:
    joel |= grams(words(open(f).read().split('## Legenda do post', 1)[-1]), n)  # só legenda, texto na tela e transcrição
hits = sorted(grams(words(src), n) & joel)
m = open(f'{D}/references/moldes.md').read(); antes, _, s8 = m.partition('## §8')
exemplos = s8 + '\n' + '\n'.join(re.findall(r'\[([^\]]+)\]', antes))
molde = sorted(grams(words(src), 4) & grams(words(exemplos), 4)) if os.path.realpath(sys.argv[1]) != os.path.realpath(f'{D}/references/moldes.md') else []
print('\n'.join([f'COPIADO: {h}' for h in hits] + [f'DO MOLDE: {h}' for h in molde]) or f'ok: nada do Joel ({n} palavras, {len(fichas)} fichas) nem dos exemplos dos moldes')
sys.exit(1 if hits else 0)
