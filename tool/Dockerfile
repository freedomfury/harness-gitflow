FROM almalinux/9-minimal:9.7

# System deps: Python, pip, git, curl
RUN microdnf install -y python3.12 python3.12-pip git gettext && \
    microdnf clean all && \
    ln -sf /usr/bin/python3.12 /usr/bin/python3 && \
    ln -sf /usr/bin/python3.12 /usr/bin/python && \
    ln -sf /usr/bin/pip3.12 /usr/bin/pip

# MinIO client
RUN curl -fsSL https://dl.min.io/client/mc/release/linux-amd64/mc \
    --output /usr/local/bin/mc && \
    chmod +x /usr/local/bin/mc

WORKDIR /opt/imageflow

# Copy SDK and CLI packages
COPY harness-code-api-client/ ./harness-code-api-client/
COPY harness-pipeline-api-client/ ./harness-pipeline-api-client/
COPY harness-platform-api-client/ ./harness-platform-api-client/
COPY harness-cli/ ./harness-cli/

# Install everything
RUN pip install --no-cache-dir \
    -e ./harness-code-api-client \
    -e ./harness-pipeline-api-client \
    -e ./harness-platform-api-client \
    -e ./harness-cli

# Verify installs
RUN harness-cli --help > /dev/null && \
    python -c "from api_specification_client import AuthenticatedClient; print('Code SDK OK')" && \
    python -c "from pipeline_service_api_reference_client import AuthenticatedClient; print('Pipeline SDK OK')" && \
    python -c "from harness_next_gen_software_delivery_platform_api_reference_client import AuthenticatedClient; print('Platform SDK OK')"

CMD ["/bin/bash"]
