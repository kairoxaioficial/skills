#!/bin/bash
# visual.sh <videos_root> [perfil...] : trocas de cena (scene>0.3), folha de contato 4x2 e frame do gancho (0,4 s)
root="$1"; shift; users=("$@"); [ ${#users[@]} -eq 0 ] && users=("*")
for u in "${users[@]}"; do for f in "$root"/$u/*.mp4; do
  [ -f "$f" ] || continue
  b="${f%.mp4}"; [ -f "$b.vis.json" ] && continue
  dur=$(ffmpeg -hide_banner -i "$f" 2>&1 | sed -n 's/.*Duration: \([0-9:.]*\).*/\1/p' | awk -F: '{print $1*3600+$2*60+$3}')
  times=$(ffmpeg -hide_banner -hwaccel videotoolbox -i "$f" -an -vf "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -o "pts_time:[0-9.]*" | cut -d: -f2)
  cuts=$(printf "%s" "$times" | grep -c .)
  ffmpeg -hide_banner -loglevel error -y -hwaccel videotoolbox -i "$f" -vf "fps=8/$dur,scale=240:-2,tile=4x2" -frames:v 1 -q:v 4 "$b.sheet.jpg"
  ffmpeg -hide_banner -loglevel error -y -ss 0.4 -i "$f" -frames:v 1 -vf scale=480:-2 -q:v 3 "$b.hook.jpg"
  echo "{\"duration\": $dur, \"cuts\": $cuts, \"cut_times\": [$(printf "%s" "$times" | head -60 | paste -sd, -)]}" > "$b.vis.json"
  echo "$(basename "$f") dur=$dur cuts=$cuts"
done; done
