# Building the imageflow Container

Everything is in `repo/tool/`. Build from that directory.

## Build

```bash
cd repo/tool
docker build -t freedomfury/imageflow:latest .
```

## Push

```bash
docker push freedomfury/imageflow:latest
```

## Test

```bash
# Interactive shell
docker run --rm -it \
  -e POC_HARNESS_ACCOUNT_ID="your-account-id" \
  -e POC_HARNESS_API_KEY="your-api-key" \
  freedomfury/imageflow:latest

# One-liner
docker run --rm \
  -e POC_HARNESS_ACCOUNT_ID="your-account-id" \
  -e POC_HARNESS_API_KEY="your-api-key" \
  freedomfury/imageflow:latest \
  -c "harness-cli repos list-repos"
```

## What's in the image

- **Base:** `almalinux/9-minimal:9.7`
- **Python 3.12** + pip + git
- **Code SDK** (`api_specification_client`) — 141 Harness Code endpoints
- **Pipeline SDK** (`pipeline_service_api_reference_client`) — 86 Pipeline endpoints
- **CLI** (`harness-cli`) — 225 auto-generated Click commands across both SDKs

## Directory structure

```
repo/tool/
├── Dockerfile
├── .dockerignore
├── harness-code-api-client/       # generated Code SDK
├── harness-pipeline-api-client/   # generated Pipeline SDK
└── harness-cli/                   # auto-generated CLI + generator script
    ├── generate.py                # regenerates CLI from SDKs
    ├── harness_cli/
    │   ├── config.py              # env var resolution, client factory
    │   ├── main.py                # Click entrypoint (auto-generated)
    │   ├── output.py              # response rendering + raw fallback
    │   └── commands/              # auto-generated command modules
    └── pyproject.toml
```
