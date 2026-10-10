// Driver CDP de uma aba persistente: node ig.mjs <porta> <cmd> [args]
//   nav <url> <prefixo> [esperaMs] | click <x> <y> <prefixo> [esperaMs] | clicktext <texto> <prefixo> [esperaMs]
//   wheel <dy> <prefixo> [esperaMs] | shot <prefixo> | eval <js>
// Cada ação grava <prefixo>.png (tela), <prefixo>.txt (texto visível) e <prefixo>.net.json (respostas api/graphql).
import fs from 'node:fs';
const [port, cmd, ...a] = process.argv.slice(2);
const sleep = ms => new Promise(r => setTimeout(r, ms));
const list = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
let t = list.find(x => x.type === 'page');
if (!t) t = await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`, { method: 'PUT' })).json();
const ws = new WebSocket(t.webSocketDebuggerUrl);
await new Promise((ok, fail) => { ws.onopen = ok; ws.onerror = fail; });
let id = 0; const pend = new Map(); const handlers = [];
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); } else handlers.forEach(h => h(m)); };
const send = (method, params = {}) => new Promise(r => { const i = ++id; pend.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
const ev = async expr => {
  const r = await send('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true });
  return r.result?.exceptionDetails ? 'ERRO ' + JSON.stringify(r.result.exceptionDetails).slice(0, 300) : r.result?.result?.value;
};
const reqs = new Map(); const cap = [];
handlers.push(async m => {
  if (m.method === 'Network.requestWillBeSent') {
    const u = m.params.request.url, h = m.params.request.headers;
    if (/(instagram|facebook)\.com\/(api|graphql)|\/ajax\//.test(u))
      reqs.set(m.params.requestId, { url: u, fn: h['X-FB-Friendly-Name'] || h['x-fb-friendly-name'] || '', post: (m.params.request.postData || '').slice(0, 4000) });
  }
  if (m.method === 'Network.loadingFinished' && reqs.has(m.params.requestId)) {
    const q = reqs.get(m.params.requestId); reqs.delete(m.params.requestId);
    const b = await send('Network.getResponseBody', { requestId: m.params.requestId });
    cap.push({ ...q, body: b.result?.body });
  }
});
await send('Network.enable', { maxResourceBufferSize: 50e6, maxTotalBufferSize: 200e6 });
await send('Page.enable');

async function record(prefix, waitMs) {
  await sleep(+waitMs || 0);
  const text = String(await ev('document.body ? document.body.innerText : ""'));
  fs.writeFileSync(prefix + '.txt', text);
  const s = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(prefix + '.png', Buffer.from(s.result.data, 'base64'));
  fs.writeFileSync(prefix + '.net.json', JSON.stringify(cap));
  const names = cap.map(c => c.fn || c.url.split('?')[0].replace(/^https:\/\/[^/]+/, '')).join(', ');
  console.log(`url=${await ev('location.href')} | texto=${text.length}c | rede=${cap.length}: ${names.slice(0, 1800)}`);
}
const mouse = async (x, y) => {
  for (const type of ['mouseMoved', 'mousePressed', 'mouseReleased'])
    await send('Input.dispatchMouseEvent', { type, x: +x, y: +y, button: 'left', clickCount: 1 });
};

if (cmd === 'nav') { await send('Page.navigate', { url: a[0] }); await record(a[1], a[2] || 8000); }
else if (cmd === 'click') { await mouse(a[0], a[1]); await record(a[2], a[3] || 5000); }
else if (cmd === 'clicktext') {
  const r = await ev(`(() => { const want = ${JSON.stringify(a[0])}.toLowerCase();
    const els = [...document.querySelectorAll('a,button,[role=button],[role=tab],[role=link],span,div')].filter(e => e.offsetParent && (e.innerText || '').trim().toLowerCase() === want);
    const el = els[els.length - 1] || [...document.querySelectorAll('a,button,[role=button],[role=tab],[role=link]')].find(e => (e.innerText || '').toLowerCase().includes(want));
    if (!el) return null; el.scrollIntoView({ block: 'center' }); const b = el.getBoundingClientRect(); return [b.x + b.width / 2, b.y + b.height / 2]; })()`);
  if (!r) console.log('texto não encontrado:', a[0]); else { await mouse(r[0], r[1]); await record(a[1], a[2] || 5000); }
}
else if (cmd === 'clicklabel') {
  const r = await ev(`(() => { const want = ${JSON.stringify(a[0])}.toLowerCase();
    const el = [...document.querySelectorAll('[aria-label]')].find(e => e.getAttribute('aria-label').toLowerCase() === want);
    if (!el) return null; const b = (el.closest('a,button,[role=button],[role=link]') || el).getBoundingClientRect(); return [b.x + b.width / 2, b.y + b.height / 2]; })()`);
  if (!r) console.log('rótulo não encontrado:', a[0]); else { await mouse(r[0], r[1]); await record(a[1], a[2] || 5000); }
}
else if (cmd === 'wheel') { await send('Input.dispatchMouseEvent', { type: 'mouseWheel', x: 640, y: 450, deltaX: 0, deltaY: +a[0] }); await record(a[1], a[2] || 3000); }
else if (cmd === 'shot') await record(a[0], 0);
else if (cmd === 'eval') { const v = await ev(a[0]); console.log(typeof v === 'string' ? v.slice(0, 6000) : JSON.stringify(v).slice(0, 6000)); }
ws.close(); process.exit(0);
