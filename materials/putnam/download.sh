#!/bin/zsh

BASE="https://kskedlaya.org/putnam-archive"
DEST="$(dirname "$0")"

for year in $(seq 1985 2025); do
  for suffix in "" "s"; do
    for ext in pdf tex; do
      file="${year}${suffix}.${ext}"
      url="${BASE}/${file}"
      out="${DEST}/${file}"
      if [ -f "$out" ]; then
        echo "skip $file"
        continue
      fi
      echo "downloading $file ..."
      curl -sf -o "$out" "$url" || echo "  not found: $file"
    done
  done
done

echo "done."
