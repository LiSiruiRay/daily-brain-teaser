#!/usr/bin/env bash
# Run hourly from crontab. At 03:00 / 13:00 America/Los_Angeles it dispatches the
# GitHub workflow (DST-safe: the server clock is UTC and Debian cron has no CRON_TZ).
set -euo pipefail

case "$(TZ=America/Los_Angeles date +%H)" in
  03) slot=am ;;
  13) slot=pm ;;
  *)  exit 0 ;;
esac

echo "$(date -Is) dispatching slot=$slot"
gh workflow run generate_question.yml -R LiSiruiRay/daily-brain-teaser -f slot="$slot"
