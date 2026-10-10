// node details.mjs <port> <usersdir> perfil1 ...  — escolhe os 15 mais vistos + os 15 mais recentes e busca os detalhes
// (data, duração, legenda, link do vídeo, capa, música, coautores) de cada um.
import fs from 'node:fs';
import { tab, sleep } from './cdp.mjs';
const [port, dir, ...users] = process.argv.slice(2);
const T = await tab(port, 'https://www.instagram.com/'); await sleep(8000);
const fetchInfo = pk => T.evalIn(`(async()=>{const c=(document.cookie.match(/csrftoken=([^;]+)/)||[])[1];const r=await fetch('/api/v1/media/${pk}/info/',{headers:{'x-ig-app-id':'936619743392459','x-requested-with':'XMLHttpRequest','x-csrftoken':c}});const t=await r.text();try{const it=JSON.parse(t).items[0];const vv=(it.video_versions||[]).slice().sort((a,b)=>a.width-b.width);const v=vv.find(x=>x.width>=480)||vv[vv.length-1];const cm=it.clips_metadata||{};return {ok:true,taken_at:it.taken_at,duration:it.video_duration,caption:it.caption?.text||'',play_count:it.play_count,ig_play_count:it.ig_play_count,like_count:it.like_count,comment_count:it.comment_count,video_url:v?.url||null,thumb_url:it.image_versions2?.candidates?.[0]?.url||null,music:cm.music_info?.music_asset_info?{title:cm.music_info.music_asset_info.title,artist:cm.music_info.music_asset_info.display_artist}:null,original_sound:!!cm.original_sound_info,audio_type:cm.audio_type||null,coauthors:(it.coauthor_producers||[]).map(x=>x.username),usertags:(it.usertags?.in||[]).map(x=>x.user?.username),paid_partnership:!!it.is_paid_partnership,has_audio:it.has_audio,product_type:it.product_type,media_type:it.media_type}}catch(e){return {ok:false,s:r.status,t:t.slice(0,200)}}})()`);
for (const u of users) {
  const f = `${dir}/${u}.json`; const d = JSON.parse(fs.readFileSync(f)); const items = d.items;
  const top = items.filter(i => i.play_count != null).sort((a, b) => b.play_count - a.play_count).slice(0, 15).map(i => i.code);
  const pinned = items.filter(i => i.pinned).map(i => i.code);
  const recentCand = items.filter(i => !i.pinned).slice(0, 15).map(i => i.code);
  const want = [...new Set([...top, ...pinned, ...recentCand])];
  d.details = d.details || {};
  for (const code of want) {
    if (d.details[code]?.ok) continue;
    const it = items.find(i => i.code === code);
    let info = null;
    for (let k = 0; k < 3 && !info?.ok; k++) {
      info = await fetchInfo(it.pk);
      if (!info?.ok) { console.log(u, code, 'falhou', JSON.stringify(info).slice(0, 120)); await sleep(30000 * (k + 1)); }
    }
    d.details[code] = info;
    await sleep(1500 + Math.random() * 1500);
  }
  const withTs = [...new Set([...pinned, ...recentCand])].filter(c => d.details[c]?.ok).sort((a, b) => d.details[b].taken_at - d.details[a].taken_at);
  d.sel = { top15: top, last15: withTs.slice(0, 15) };
  fs.writeFileSync(f, JSON.stringify(d));
  console.log(u, 'detalhes', Object.values(d.details).filter(x => x?.ok).length, '/', want.length, 'top15', top.length, 'last15', d.sel.last15.length);
}
await T.close(); process.exit(0);
