// node flat.mjs <arquivo.net.json> <regex do nome da consulta> [max linhas por consulta]
// Achata as respostas JSON capturadas em linhas caminho=valor, sem ruído (urls, imagens, ids internos).
import fs from 'node:fs';
const [file, re, max = 150] = process.argv.slice(2);
const cap = JSON.parse(fs.readFileSync(file, 'utf8'));
const flat = (o, p = '', out = []) => {
  if (o && typeof o === 'object') for (const [k, v] of Object.entries(o)) flat(v, p ? p + '.' + k : k, out);
  else if (o !== null && o !== '') out.push(p + '=' + String(o).slice(0, 90));
  return out;
};
for (const c of cap) {
  if (!new RegExp(re).test(c.fn || ("URL " + c.url.split("?")[0]))) continue;
  let j; try { j = JSON.parse((c.body || '').replace(/^for \(;;\);/, '')); } catch { console.log('##', c.fn || c.url, 'não-json'); continue; }
  const lines = flat(j.data ?? j).filter(l => !/__typename|extensions|is_final|image|profile_pic|url=|_url|__isNode|cursor|strong_id|fbid|pk_id/.test(l));
  console.log('##', c.fn || c.url.split('?')[0], lines.length, 'campos');
  console.log(lines.slice(0, +max).join('\n'));
}
