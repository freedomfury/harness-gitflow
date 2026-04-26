#!/usr/bin/env bash
#
# file-store-lock-test.sh — Validate Harness File Store POST create-or-fail semantics under concurrency.
#
# Usage: tests/file-store-lock-test.sh [N]
#   N = number of parallel POST attempts (default 5)
#
# Requires: source activate (provides POC_HARNESS_API_KEY / POC_HARNESS_ACCOUNT_ID)
#
# Passes if: exactly 1 POST returns 200/201 and N-1 return 4xx with DUPLICATE_FIELD.
# Fails if:  all 200 (silent overwrite), or 0 success, or unexpected errors.
#
# Test target path in File Store: /image-build/stg/version.lock
# Folder hierarchy must already exist (created by Test 1.0 — this script assumes setup done).
#
set -uo pipefail

N="${1:-5}"

: "${POC_HARNESS_ACCOUNT_ID:?source activate first}"
: "${POC_HARNESS_API_KEY:?source activate first}"

ACCT="$POC_HARNESS_ACCOUNT_ID"
ORG="default"
PROJ="image_flow"
API="https://app.harness.io/gateway/ng/api"
LOCK_IDENT="version_lock"
LOCK_NAME="version.lock"
CTX_FOLDER="stg"

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# Ensure clean slate — delete the lock if it already exists from a previous run
curl -s -X DELETE \
  "$API/file-store/$LOCK_IDENT?accountIdentifier=$ACCT&orgIdentifier=$ORG&projectIdentifier=$PROJ" \
  -H "x-api-key: $POC_HARNESS_API_KEY" > /dev/null 2>&1 || true

echo "=== Firing $N parallel POSTs to create $CTX_FOLDER/$LOCK_NAME ==="

# Fire N parallel creates
for i in $(seq 1 "$N"); do
  (
    CODE=$(curl -s -o "$TMP/$i.body" -w "%{http_code}" \
      -H "x-api-key: $POC_HARNESS_API_KEY" \
      -F "identifier=$LOCK_IDENT" \
      -F "name=$LOCK_NAME" \
      -F "fileUsage=CONFIG" \
      -F "type=FILE" \
      -F "parentIdentifier=$CTX_FOLDER" \
      -F "content=holder-$i" \
      -X POST "$API/file-store?accountIdentifier=$ACCT&orgIdentifier=$ORG&projectIdentifier=$PROJ")
    echo "$CODE" > "$TMP/$i.code"
  ) &
done
wait

# Tally
SUCCESS=0
CONFLICT=0
OTHER=0
WINNER=""

for i in $(seq 1 "$N"); do
  CODE=$(cat "$TMP/$i.code")
  case "$CODE" in
    200|201)
      SUCCESS=$((SUCCESS+1))
      WINNER="$i"
      echo "  winner=$i (HTTP $CODE)"
      ;;
    400|409|422)
      # Verify it's DUPLICATE_FIELD specifically
      if grep -q "DUPLICATE_FIELD" "$TMP/$i.body" 2>/dev/null; then
        CONFLICT=$((CONFLICT+1))
      else
        OTHER=$((OTHER+1))
        echo "  attempt=$i HTTP $CODE NOT a duplicate error:"
        head -c 300 "$TMP/$i.body"; echo
      fi
      ;;
    *)
      OTHER=$((OTHER+1))
      echo "  attempt=$i UNEXPECTED HTTP $CODE:"
      head -c 300 "$TMP/$i.body"; echo
      ;;
  esac
done

echo "---"
echo "Total=$N success=$SUCCESS conflict=$CONFLICT other=$OTHER"

# Verify the winner's content is actually stored
if [ -n "$WINNER" ]; then
  STORED=$(curl -s -H "x-api-key: $POC_HARNESS_API_KEY" \
    "$API/file-store/files/$LOCK_IDENT/download?accountIdentifier=$ACCT&orgIdentifier=$ORG&projectIdentifier=$PROJ")
  echo "Stored content: $STORED"
  echo "Expected:       holder-$WINNER"
fi

# Cleanup: release the lock
curl -s -X DELETE \
  "$API/file-store/$LOCK_IDENT?accountIdentifier=$ACCT&orgIdentifier=$ORG&projectIdentifier=$PROJ" \
  -H "x-api-key: $POC_HARNESS_API_KEY" > /dev/null

# Exit status reflects pass/fail
if [ "$SUCCESS" -eq 1 ] && [ "$OTHER" -eq 0 ]; then
  echo "PASS"
  exit 0
else
  echo "FAIL"
  exit 1
fi
