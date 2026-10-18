#!/usr/bin/env bash
# Optional local publisher. Requires gh CLI + an authenticated GitHub account.
# No GitHub creation is attempted by the build or validation process.
set -euo pipefail

REPO_NAME="${1:-ux-reverse-engineering}"
VISIBILITY="${2:---private}"

if [[ "$VISIBILITY" != "--private" && "$VISIBILITY" != "--public" ]]; then
  echo "Use: ./scripts/publish-github.sh [repo-name] [--private|--public]" >&2
  exit 2
fi
if ! command -v gh >/dev/null 2>&1; then
  echo "Instale GitHub CLI (gh) e execute gh auth login antes de publicar." >&2
  exit 1
fi
gh auth status >/dev/null
cd "$(dirname "$0")/.."
if [[ ! -d .git ]]; then
  git init -b main
fi
if [[ -n "$(git status --porcelain)" ]]; then
  echo "Existem mudanças locais. Faça commit antes de publicar." >&2
  exit 1
fi
if git remote get-url origin >/dev/null 2>&1; then
  echo "Remote origin já existe. Revise antes de publicar." >&2
  exit 1
fi
# Always requires explicit execution by owner; private is the default.
gh repo create "$REPO_NAME" "$VISIBILITY" --source=. --remote=origin --push
