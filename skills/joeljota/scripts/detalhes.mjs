// node detalhes.mjs <port> <arquivo.json> <topN> <recentesK>
// Busca os detalhes (data, duração, legenda, link do vídeo, capa, música, coautores) dos topN reels mais vistos,
// dos recentesK primeiros da aba de reels e dos fixados. Grava em details e monta sel.viral (30) e sel.recentes (20).
// Adaptado de ../../modelagem/scripts/details.mjs (mesma consulta /api/v1/media/<pk>/info/).
import fs from 'node:fs';
import { tab, sleep } from '../../modelagem/scripts/cdp.mjs';
const [port, f, topN, recK] = process.argv.slice(2);
const d = JSON.parse(fs.readFileSync(f)); const items = d.items;
const byViews = items.filter(i => i.play_count != null).sort((a, b) => b.play_count - a.play_count);
const want = [...new Set([...byViews.slice(0, +topN), ...items.filter(i => i.pinned), ...items.filter(i => !i.pinned).slice(0, +recK)].map(i => i.code))];
const T = await tab(port, 'https://www.instagram.com/'); await sleep(8000);
const fetchInfo = pk => T.evalIn(`(async()=>{const c=(document.cookie.match(/csrftoken=([^;]+)/)||[])[1];const r=await fetch('/api/v1/media/${pk}/info/',{headers:{'x-ig-app-id':'936619743392459','x-requested-with':'XMLHttpRequest','x-csrftoken':c}});const t=await r.text();try{const it=JSON.parse(t).items[0];const vv=(it.video_versions||[]).slice().sort((a,b)=>a.width-b.width);const v=vv.find(x=>x.width>=480)||vv[vv.length-1];const cm=it.clips_metadata||{};return {ok:true,taken_at:it.taken_at,duration:it.video_duration,caption:it.caption?.text||'',play_count:it.play_count,ig_play_count:it.ig_play_count,like_count:it.like_count,comment_count:it.comment_count,video_url:v?.url||null,thumb_url:it.image_versions2?.candidates?.[0]?.url||null,music:cm.music_info?.music_asset_info?{title:cm.music_info.music_asset_info.title,artist:cm.music_info.music_asset_info.display_artist}:null,original_sound:!!cm.original_sound_info,audio_type:cm.audio_type||null,coauthors:(it.coauthor_producers||[]).map(x=>x.username),usertags:(it.usertags?.in||[]).map(x=>x.user?.username),paid_partnership:!!it.is_paid_partnership,has_audio:it.has_audio,product_type:it.product_type,media_type:it.media_type}}catch(e){return {ok:false,s:r.status,t:t.slice(0,200)}}})()`);
d.details = d.details || {};
let n = 0;
for (const code of want) {
  if (d.details[code]?.ok) continue;
  const it = items.find(i => i.code === code);
  let info = null;
  for (let k = 0; k < 3 && !info?.ok; k++) {
    info = await fetchInfo(it.pk);
    if (!info?.ok) { console.log(code, 'falhou', JSON.stringify(info).slice(0, 120)); await sleep(30000 * (k + 1)); }
  }
  d.details[code] = info;
  if (++n % 25 === 0) { fs.writeFileSync(f, JSON.stringify(d)); console.log('detalhes', n, '/', want.length); }
  await sleep(1500 + Math.random() * 1500);
}
const recent = want.filter(c => d.details[c]?.ok).sort((a, b) => d.details[b].taken_at - d.details[a].taken_at);
const viral = byViews.slice(0, 30).map(i => i.code), recentes = recent.slice(0, 20);
// top15/last15: só para reaproveitar download.py e transcribe.py da modelagem (baixam e transcrevem top15 + last15).
d.sel = { ...(d.sel || {}), viral, recentes, top15: [...new Set([...viral, ...recentes, ...want])].filter(c => d.details[c]?.ok), last15: [] };
fs.writeFileSync(f, JSON.stringify(d));
console.log('detalhes ok', Object.values(d.details).filter(x => x?.ok).length, '/', want.length, 'viral', d.sel.viral.length, 'recentes', d.sel.recentes.length);
await T.close(); process.exit(0);
