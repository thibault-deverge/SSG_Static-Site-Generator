#!/usr/bin/env bash
set -e

if [ -z "$1" ]; then
  REPO_NAME="${GITHUB_REPOSITORY##*/}"

  if [ -n "$REPO_NAME" ]; then
    BASEPATH="/${REPO_NAME}/"
  else
    BASEPATH="/"
  fi
else
  BASEPATH="$1"
fi

python3 -m src.main "$BASEPATH"
