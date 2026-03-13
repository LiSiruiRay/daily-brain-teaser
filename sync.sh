#!/bin/zsh

# Usage: ./sync.sh "your commit message"
# If no message provided, prompts for one.

if [ -n "$1" ]; then
  MSG="$1"
else
  printf "Commit message: "
  read MSG
fi

git add . && git commit -m "$MSG" && git pull origin main --rebase && git push
