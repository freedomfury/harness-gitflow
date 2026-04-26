#!/usr/bin/env bash
# bump-version.sh <stg-branch>
#
# Reads the current VERSION from the target stg branch, computes the next
# pre-release version, and writes it to the local VERSION file.
#
# Usage:
#   scripts/bump-version.sh stg-0.2.0
#   scripts/bump-version.sh stg-0.1.1
#
# Rules:
#   stg-X.Y.0  (patch = 0) → sprint branch  → uses rc.N label
#   stg-X.Y.Z  (patch > 0) → hotfix branch  → uses hotfix.N label
#
# Examples:
#   stg VERSION 0.1.0       → 0.1.1-rc.0
#   stg VERSION 0.1.1-rc.2  → 0.1.1-rc.3
#   stg VERSION 0.1.1       → 0.1.2-rc.0   (hotfix landed, base moved up)

set -euo pipefail

STG_BRANCH="${1:-}"
if [ -z "$STG_BRANCH" ]; then
  echo "Usage: $0 <stg-branch>"
  echo "  Example: $0 stg-0.2.0"
  exit 1
fi

git fetch origin "$STG_BRANCH" --quiet
STG_VERSION=$(git show "origin/$STG_BRANCH:VERSION")
TARGET_VERSION=$(echo "$STG_BRANCH" | sed 's/^stg-//')

echo "stg branch:    $STG_BRANCH"
echo "stg VERSION:   $STG_VERSION"
echo "sprint target: $TARGET_VERSION"

NEW_VERSION=$(python3 - <<EOF
import re, sys

stg_ver    = "$STG_VERSION"
target_ver = "$TARGET_VERSION"

m = re.match(r'^(\d+)\.(\d+)\.(\d+)(?:-(rc|hotfix)\.(\d+))?\$', stg_ver)
if not m:
    print(f"ERROR: cannot parse stg VERSION: {stg_ver}", file=sys.stderr)
    sys.exit(1)

major = int(m.group(1))
minor = int(m.group(2))
patch = int(m.group(3))
label = m.group(4)   # 'rc', 'hotfix', or None
n     = int(m.group(5)) if m.group(5) else None

t = re.match(r'^(\d+)\.(\d+)\.(\d+)\$', target_ver)
if not t:
    print(f"ERROR: cannot parse target version: {target_ver}", file=sys.stderr)
    sys.exit(1)
target_patch = int(t.group(3))
is_hotfix    = target_patch > 0
new_label    = 'hotfix' if is_hotfix else 'rc'

if label is None:
    # Clean release — first bump: increment patch, start at N=0
    print(f"{major}.{minor}.{patch + 1}-{new_label}.0")
elif label in ('rc', 'hotfix'):
    # Existing pre-release — increment N, keep same patch and label
    print(f"{major}.{minor}.{patch}-{label}.{n + 1}")
else:
    print(f"ERROR: unknown pre-release label: {label}", file=sys.stderr)
    sys.exit(1)
EOF
)

echo "new VERSION:   $NEW_VERSION"
echo "$NEW_VERSION" > VERSION
echo "written to VERSION"
