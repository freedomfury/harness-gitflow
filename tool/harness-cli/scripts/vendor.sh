#!/usr/bin/env bash
# Generate vendor/ — the three Harness Python SDKs — from the OpenAPI specs.
#
# vendor/ is generated code: it is gitignored and NOT shipped in the tarball.
# This script is the one setup step a recipient runs after unpacking:
#
#     ./scripts/vendor.sh          # build vendor/ from specs/
#     cp .env.example .env         # then add your credentials
#     uv sync                      # then install
#
# It runs openapi-python-client via `uvx` (no separate install; uv is already
# required for `uv sync`). The first run fetches openapi-python-client from
# PyPI; the Harness specs themselves ship in specs/, so NO Harness credentials
# or network access to Harness is needed to generate.
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cli_dir="$(cd "$here/.." && pwd)"            # .../harness-cli
vendor_dir="$cli_dir/vendor"

# Specs ship in specs/ (inside the tarball) or live in examples/ (dev repo).
specs_dir=""
for cand in "$cli_dir/specs" "$cli_dir/../../examples"; do
  if [ -f "$cand/harness-code-openapi.yaml" ]; then specs_dir="$(cd "$cand" && pwd)"; break; fi
done
if [ -z "$specs_dir" ]; then
  echo "ERROR: OpenAPI specs not found." >&2
  echo "       Put harness-{code,pipeline,platform}-openapi.yaml in ./specs/ and re-run." >&2
  exit 1
fi

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
echo "next:  cp .env.example .env  (add credentials), then  uv sync"
