#!/usr/bin/env python3
"""
next-version.py <current_version> <stg_branch_name>

Computes the next VERSION value for a stg branch, server-side.

Rules:
  - If current has no pre-release suffix (clean release):
      sprint branch (target patch == 0): emit MAJOR.MINOR.(PATCH+1)-rc.0
      hotfix branch (target patch > 0):  emit MAJOR.MINOR.(PATCH+1)-hotfix.0
  - If current has rc.N:     emit MAJOR.MINOR.PATCH-rc.(N+1)
  - If current has hotfix.N: emit MAJOR.MINOR.PATCH-hotfix.(N+1)
  - Ceiling rule: if computed next > target, exit 2 ("sprint target reached")

Exit codes:
  0 — success, prints next version to stdout
  1 — parse error
  2 — ceiling reached (prints reason to stdout, caller should log and skip)
"""
import re, sys


def parse(v):
    m = re.match(r'^(\d+)\.(\d+)\.(\d+)(?:-(rc|hotfix)\.(\d+))?$', v.strip())
    if not m:
        sys.exit(f"ERROR: cannot parse version '{v}'")
    major, minor, patch = int(m.group(1)), int(m.group(2)), int(m.group(3))
    label = m.group(4)   # "rc", "hotfix", or None
    n = int(m.group(5)) if m.group(5) else None
    return major, minor, patch, label, n


def version_tuple(major, minor, patch, label, n):
    """Comparable tuple. pre-release sorts below release; rc < hotfix < release."""
    label_order = {"rc": 0, "hotfix": 1, None: 2}
    lo = label_order[label]
    return (major, minor, patch, lo, n if n is not None else -1)


def format_version(major, minor, patch, label=None, n=None):
    base = f"{major}.{minor}.{patch}"
    if label is not None:
        return f"{base}-{label}.{n}"
    return base


if len(sys.argv) != 3:
    sys.exit(f"Usage: {sys.argv[0]} <current_version> <stg_branch_name>")

current_str = sys.argv[1].strip()
branch_str  = sys.argv[2].strip()

# Parse stg branch name → target version
m = re.match(r'^stg-(\d+\.\d+\.\d+)$', branch_str)
if not m:
    sys.exit(f"ERROR: cannot parse stg branch name '{branch_str}' (expected stg-X.Y.Z)")
target_str = m.group(1)

cur_major, cur_minor, cur_patch, cur_label, cur_n = parse(current_str)
tgt_major, tgt_minor, tgt_patch, _, _ = parse(target_str)

# Determine next value
if cur_label is None:
    # Clean release: start a new pre-release series
    next_patch = cur_patch + 1
    suffix = "hotfix" if tgt_patch > 0 else "rc"
    next_major, next_minor, next_patch_val = cur_major, cur_minor, next_patch
    next_label, next_n = suffix, 0
elif cur_label in ("rc", "hotfix"):
    next_major, next_minor, next_patch_val = cur_major, cur_minor, cur_patch
    next_label, next_n = cur_label, cur_n + 1
else:
    sys.exit(f"ERROR: unrecognised label '{cur_label}'")

next_str = format_version(next_major, next_minor, next_patch_val, next_label, next_n)

# Ceiling check: next must not exceed target
next_tup   = version_tuple(next_major, next_minor, next_patch_val, next_label, next_n)
target_tup = version_tuple(tgt_major, tgt_minor, tgt_patch, None, None)

if next_tup > target_tup:
    print(f"sprint target reached: {next_str} > {target_str}")
    sys.exit(2)

print(next_str)
