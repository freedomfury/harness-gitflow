#!/usr/bin/env bash
set -euo pipefail

# ---------------------------------------------------------------------------
# Harness Delegate + Docker Runner install script
# Run on the delegate host as root (or with sudo).
# ---------------------------------------------------------------------------

# Required env vars (export before running, or pass on the command line):
#   HARNESS_ACCOUNT_ID    your Harness account ID
#   HARNESS_DELEGATE_TOKEN  delegate token from Harness UI > Account > Delegates > Tokens
: "${HARNESS_ACCOUNT_ID:?set HARNESS_ACCOUNT_ID before running}"
: "${HARNESS_DELEGATE_TOKEN:?set HARNESS_DELEGATE_TOKEN before running}"

ACCOUNT_ID="$HARNESS_ACCOUNT_ID"
DELEGATE_TOKEN="$HARNESS_DELEGATE_TOKEN"
MANAGER_URL="${HARNESS_MANAGER_URL:-https://app.harness.io}"
DELEGATE_NAME="${HARNESS_DELEGATE_NAME:-image-flow-delegate}"
DELEGATE_IMAGE="us-docker.pkg.dev/gar-prod-setup/harness-public/harness/delegate:26.03.88803"
RUNNER_PORT="3000"
RUNNER_BIN="/usr/local/bin/harness-docker-runner"
RUNNER_CONFIG="/etc/harness-runner/config.env"

# ---------------------------------------------------------------------------
# 1. Install Docker if not present, ensure it starts on boot
# ---------------------------------------------------------------------------
echo "--- checking docker"
if ! command -v docker &>/dev/null; then
  echo "docker not found — installing"
  apt-get update -qq
  apt-get install -y -qq ca-certificates curl gnupg
  install -m 0755 -d /etc/apt/keyrings
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    -o /etc/apt/keyrings/docker.asc
  chmod a+r /etc/apt/keyrings/docker.asc
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" > /etc/apt/sources.list.d/docker.list
  apt-get update -qq
  apt-get install -y -qq docker-ce docker-ce-cli containerd.io docker-buildx-plugin
  echo "docker installed"
else
  echo "docker already installed"
fi

systemctl enable containerd
systemctl enable docker
systemctl start docker
docker info > /dev/null 2>&1 || { echo "ERROR: Docker failed to start"; exit 1; }
echo "docker OK (enabled on boot)"

# ---------------------------------------------------------------------------
# 2. Download the Harness Docker Runner binary
# ---------------------------------------------------------------------------
echo "--- downloading harness docker runner"
ARCH=$(uname -m)
case "$ARCH" in
  x86_64)  RUNNER_ARCH="amd64" ;;
  aarch64) RUNNER_ARCH="arm64" ;;
  *)       echo "ERROR: unsupported arch $ARCH"; exit 1 ;;
esac

curl -fsSL \
  "https://github.com/harness/harness-docker-runner/releases/latest/download/harness-docker-runner-linux-${RUNNER_ARCH}" \
  -o "$RUNNER_BIN"
chmod +x "$RUNNER_BIN"
echo "runner installed at $RUNNER_BIN"

# ---------------------------------------------------------------------------
# 3. Write runner config
# ---------------------------------------------------------------------------
echo "--- writing runner config"
mkdir -p /etc/harness-runner
cat > "$RUNNER_CONFIG" <<EOF
ACCOUNT_ID=${ACCOUNT_ID}
DELEGATE_TOKEN=${DELEGATE_TOKEN}
MANAGER_HOST_AND_PORT=${MANAGER_URL}
HTTPS_BIND=127.0.0.1:${RUNNER_PORT}
SKIP_PREPARE_SERVER=true
SERVER_INSECURE=true
EOF
chmod 600 "$RUNNER_CONFIG"

# ---------------------------------------------------------------------------
# 4. Install systemd service for the runner
# ---------------------------------------------------------------------------
echo "--- installing harness-runner systemd service"
cat > /etc/systemd/system/harness-runner.service <<EOF
[Unit]
Description=Harness Docker Runner
Documentation=https://docs.harness.io
After=network-online.target docker.service
Wants=network-online.target
Requires=docker.service

[Service]
Type=simple
EnvironmentFile=${RUNNER_CONFIG}
ExecStart=${RUNNER_BIN} server
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=journal
SyslogIdentifier=harness-runner

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable harness-runner
systemctl restart harness-runner
echo "harness-runner service enabled and started"
echo "  status:  systemctl status harness-runner"
echo "  logs:    journalctl -u harness-runner -f"

# ---------------------------------------------------------------------------
# 5. Start the Harness Delegate container
# ---------------------------------------------------------------------------
echo "--- starting delegate container"
docker rm -f "$DELEGATE_NAME" 2>/dev/null || true
docker run -d \
  --name "$DELEGATE_NAME" \
  --network=host \
  --restart=always \
  -e DELEGATE_NAME="$DELEGATE_NAME" \
  -e NEXT_GEN="true" \
  -e DELEGATE_TYPE="DOCKER" \
  -e ACCOUNT_ID="$ACCOUNT_ID" \
  -e DELEGATE_TOKEN="$DELEGATE_TOKEN" \
  -e DELEGATE_TAGS="" \
  -e MANAGER_HOST_AND_PORT="$MANAGER_URL" \
  -e RUNNER_URL="http://localhost:${RUNNER_PORT}" \
  "$DELEGATE_IMAGE"
echo "delegate container started"

# ---------------------------------------------------------------------------
# 6. Start the auto-upgrader container
# ---------------------------------------------------------------------------
echo "--- starting auto-upgrader"
docker rm -f "${DELEGATE_NAME}-upgrader" 2>/dev/null || true
docker run -d \
  --name "${DELEGATE_NAME}-upgrader" \
  --cpus=0.5 \
  --memory=256m \
  --restart=always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -e ACCOUNT_ID="$ACCOUNT_ID" \
  -e MANAGER_HOST_AND_PORT="$MANAGER_URL" \
  -e UPGRADER_WORKLOAD_NAME="$DELEGATE_NAME" \
  -e UPGRADER_TOKEN="$DELEGATE_TOKEN" \
  -e CONTAINER_STOP_TIMEOUT=3600 \
  -e SCHEDULE="0 */1 * * *" \
  harness/upgrader:latest
echo "upgrader container started"

# ---------------------------------------------------------------------------
# Done
# ---------------------------------------------------------------------------
echo ""
echo "=== install complete ==="
echo ""
echo "  runner:    systemctl status harness-runner"
echo "             journalctl -u harness-runner -f"
echo "  delegate:  docker logs -f $DELEGATE_NAME"
echo "  upgrader:  docker logs -f ${DELEGATE_NAME}-upgrader"
echo ""
echo "Delegate will appear in Harness UI in ~2 minutes:"
echo "  Account Settings → Account Resources → Delegates"
