#!/usr/bin/env python3
"""
version-check.py <dev_version> <stg_version> <target_version>

Enforces:
  dev_version > stg_version      (must be bumped above current stg base)
  dev_version <= target_version  (must not exceed sprint target)

Version format: MAJOR.MINOR.PATCH[-( rc|hotfix ).N]
Sort order:     hotfix.N < rc.N < release  (within same MAJOR.MINOR.PATCH)
"""
import re, sys


def parse(v):
    m = re.match(r'^(\d+)\.(\d+)\.(\d+)(?:-(rc|hotfix)\.(\d+))?$', v)
    if not m:
        sys.exit(f"ERROR: cannot parse version '{v}'")
    major, minor, patch = int(m.group(1)), int(m.group(2)), int(m.group(3))
    label = m.group(4)
    n = int(m.group(5)) if m.group(5) else None
    # pre-release sorts below release; within pre-release, sort by label then n
    pre = (0, label, n) if label else (1,)
    return (major, minor, patch) + pre


if len(sys.argv) != 4:
    sys.exit(f"Usage: {sys.argv[0]} <dev_version> <stg_version> <target_version>")

dev_str, stg_str, target_str = sys.argv[1], sys.argv[2], sys.argv[3]
dev    = parse(dev_str)
stg    = parse(stg_str)
target = parse(target_str)

if dev <= stg:
    sys.exit(
        f"FAIL: dev VERSION {dev_str} must be > stg VERSION {stg_str}\n"
        f"  Run: scripts/bump-version.sh <stg-branch>"
    )

if dev > target:
    sys.exit(
        f"FAIL: dev VERSION {dev_str} exceeds sprint target {target_str}\n"
        f"  This branch targets {target_str}. Max allowed: {target_str}"
    )

print(f"OK: {dev_str} > {stg_str} and {dev_str} <= {target_str}")
