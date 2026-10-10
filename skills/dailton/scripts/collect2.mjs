// node collect.mjs <port> <outdir> <maxPages> perfil1 perfil2 ...
// Lista TODOS os reels de cada perfil (código, views, likes, comentários, fixado, coautores) pela aba de reels,
// reaproveitando a consulta GraphQL que o próprio Instagram faz (doc_id e tokens capturados na hora).
import fs from 'node:fs';
import { tab, sleep } from '/Users/adriel/.claude/skills/modelagem/scripts/cdp.mjs';
const [port, outdir, maxPages, ...users] = process.argv.slice(2);
fs.mkdirSync(outdir, { recursive: true });
const pick = n => { const m = n.node.media; return { code: m.code, pk: m.pk, play_count: m.play_count, view_count: m.view_count, like_count: m.like_count, comment_count: m.comment_count, pinned: (m.clips_tab_pinned_user_ids || []).length > 0, coauthors: (m.coauthor_producers || []).map(c => c.username), media_type: m.media_type, product_type: m.product_type }; };

async function open(u) {
  for (let attempt = 1; attempt <= 3; attempt++) {
    const T = await tab(port); const cap = []; const reqs = new Map();
    T.on(async m => {
      if (m.method === 'Network.requestWillBeSent' && /graphql/.test(m.params.request.url)) {
        const h = m.params.request.headers;
        reqs.set(m.params.requestId, { fn: h['X-FB-Friendly-Name'] || h['x-fb-friendly-name'] || '', url: m.params.request.url, post: m.params.request.postData || '', headers: h });
      }
      if (m.method === 'Network.loadingFinished' && reqs.has(m.params.requestId)) {
        const q = reqs.get(m.params.requestId); reqs.delete(m.params.requestId);
        if (!/PolarisProfilePageContentQuery|PolarisProfileReelsTabContentQuery/.test(q.fn)) return;
        const b = await T.send('Network.getResponseBody', { requestId: m.params.requestId });
        try { cap.push({ ...q, json: JSON.parse(b.result.body) }); } catch { }
      }
    });
    await T.send('Network.enable', { maxResourceBufferSize: 50e6, maxTotalBufferSize: 200e6 });
    await T.send('Page.enable');
    await T.send('Page.navigate', { url: `https://www.instagram.com/${u}/reels/` });
    await sleep(15000);
    for (let k = 0; k < 4 && !cap.some(c => /_connection/.test(c.fn)); k++) { await T.evalIn('window.scrollTo(0, document.body.scrollHeight)'); await sleep(7000); }
    const first = cap.find(c => c.fn === 'PolarisProfileReelsTabContentQuery');
    const conns = cap.filter(c => c.fn === 'PolarisProfileReelsTabContentQuery_connection');
    if (first && conns.length) return { T, prof: cap.find(c => c.fn === 'PolarisProfilePageContentQuery')?.json?.data?.user || {}, first, conns };
    console.log(u, 'sem captura na tentativa', attempt, cap.map(c => c.fn).join(','));
    await T.close(); await sleep(20000 * attempt);
  }
  return null;
}

for (const u of users) {
  const o = await open(u);
  if (!o) { console.log(u, 'ERRO: sem captura'); continue; }
  const { T, prof, first, conns } = o;
  const uid = JSON.parse(new URLSearchParams(first.post).get('variables')).user_id || prof.pk;
  const items = []; const seen = new Set();
  const add = conn => { for (const e of conn.edges) { const p = pick(e); if (!seen.has(p.code)) { seen.add(p.code); items.push(p); } } };
  add(first.json.data.fetch__XDTUserDict.clips_connection);
  let pi = first.json.data.fetch__XDTUserDict.clips_connection.page_info;
  for (const c of conns) { const cc = c.json?.data?.fetch__XDTUserDict?.clips_connection; if (cc) { add(cc); pi = cc.page_info; } }
  const tpl = conns[conns.length - 1];
  const hdr = {}; for (const [k, v] of Object.entries(tpl.headers)) if (/^(content-type|x-)/i.test(k)) hdr[k] = v;
  let pages = 0, err = '';
  while (pi?.has_next_page && pages < +maxPages) {
    const body = new URLSearchParams(tpl.post);
    body.set('variables', JSON.stringify({ after: pi.end_cursor, data: { include_feed_video: true, page_size: 12, target_user_id: uid }, first: 12, id: uid, __relay_internal__pv__PolarisShortDramaEnabledrelayprovider: true }));
    let cc = null;
    for (let k = 0; k < 3 && !cc; k++) {
      const res = await T.evalIn(`fetch(${JSON.stringify(tpl.url)}, {method:'POST', headers:${JSON.stringify(hdr)}, body:${JSON.stringify(body.toString())}}).then(async r => ({s:r.status, t: await r.text()}))`);
      try { cc = JSON.parse(res.t).data.fetch__XDTUserDict.clips_connection; } catch { err = res.s + ' ' + res.t.slice(0, 160); await sleep(30000 * (k + 1)); }
    }
    if (!cc) break;
    err = ''; add(cc); pi = cc.page_info; pages++;
    await sleep(2400 + Math.random() * 2000);
  }
  await T.close();
  const out = { username: u, user_id: uid, full_name: prof.full_name, followers: prof.follower_count, following: prof.following_count, media_count: prof.media_count, biography: prof.biography, is_verified: prof.is_verified, complete: !pi?.has_next_page, err, collected_at: new Date().toISOString(), items };
  fs.writeFileSync(`${outdir}/${u}.json`, JSON.stringify(out));
  console.log(u, 'followers', prof.follower_count, 'media', prof.media_count, 'reels', items.length, 'pages', pages, 'complete', out.complete, err);
  await sleep(4000);
}
process.exit(0);
