#!/usr/bin/env bash
# Generate vendor/ — the three Harness Python SDKs — from the LIVE OpenAPI specs.
#
# Specs are downloaded from Harness each run (nothing hard-coded), so the SDKs
# always reflect the current API. Needs:
#   - network (also needed for openapi-python-client, fetched via uvx)
#   - an API key: POC_HARNESS_API_KEY or HARNESS_PASSWORD_API in the env, OR in ./.env
#
#     cp .env.example .env   # add your API key
#     ./scripts/vendor.sh    # fetch specs + generate vendor/
#     uv sync                # then install
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cli_dir="$(cd "$here/.." && pwd)"
vendor_dir="$cli_dir/vendor"
specs_dir="$cli_dir/specs"   # local, gitignored; repopulated fresh each run

# --- resolve API key (env first, then ./.env) ---
api_key="${POC_HARNESS_API_KEY:-${HARNESS_PASSWORD_API:-}}"
if [ -z "$api_key" ] && [ -f "$cli_dir/.env" ]; then
  set -a; . "$cli_dir/.env"; set +a
  api_key="${POC_HARNESS_API_KEY:-${HARNESS_PASSWORD_API:-}}"
fi
if [ -z "$api_key" ]; then
  echo "ERROR: no API key found. Set POC_HARNESS_API_KEY or HARNESS_PASSWORD_API" >&2
  echo "       (in the env, or in $cli_dir/.env) and re-run." >&2
  exit 1
fi

# --- download the three OpenAPI specs ---
base="https://app.harness.io/gateway"
mkdir -p "$specs_dir"
echo "Downloading OpenAPI specs into $specs_dir ..."
curl -fsS -H "x-api-key: $api_key" "$base/code/openapi.yaml"         -o "$specs_dir/harness-code-openapi.yaml"
curl -fsS -H "x-api-key: $api_key" "$base/pipeline/api/openapi.yaml" -o "$specs_dir/harness-pipeline-openapi.yaml"
curl -fsS -H "x-api-key: $api_key" "$base/ng/api/openapi.yaml"       -o "$specs_dir/harness-platform-openapi.yaml"

# Guard against a silent HTML sign-in page (bad/expired key): each spec must be YAML.
for f in "$specs_dir"/harness-*-openapi.yaml; do
  if ! head -1 "$f" | grep -q '^openapi:'; then
    echo "ERROR: $f is not a valid OpenAPI spec (first line: $(head -1 "$f"))." >&2
    echo "       Usually the API key is invalid/expired and Harness returned its sign-in page." >&2
    exit 1
  fi
done

# --- generate the SDKs ---
# Pipeline spec has duplicate enum values and requires literal_enums
# (see docs/sdk-generation.md). Code and Platform generate cleanly without it.
config="$(mktemp)"
printf 'literal_enums: true\n' > "$config"
trap 'rm -f "$config"' EXIT

echo "Generating SDKs from $specs_dir into $vendor_dir ..."
rm -rf "$vendor_dir"
mkdir -p "$vendor_dir"

echo "  code SDK ..."
uvx openapi-python-client generate \
  --path "$specs_dir/harness-code-openapi.yaml" \
  --output-path "$vendor_dir/harness-code-api-client"

echo "  pipeline SDK (literal_enums) ..."
uvx openapi-python-client generate \
  --path "$specs_dir/harness-pipeline-openapi.yaml" \
  --output-path "$vendor_dir/harness-pipeline-api-client" \
  --config "$config"

echo "  platform SDK ..."
uvx openapi-python-client generate \
  --path "$specs_dir/harness-platform-openapi.yaml" \
  --output-path "$vendor_dir/harness-platform-api-client"

echo ""
echo "done — $(find "$vendor_dir" -name '*.py' | wc -l) python files under vendor/."
echo "next:  uv sync  (and uv lock if SDK versions changed)"
