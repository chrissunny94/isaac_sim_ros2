#!/bin/bash
# Ensure the user exists (avoid UID/GID conflicts)
if ! id -u sim >/dev/null 2>&1; then
    groupadd -g 1000 sim
    useradd -m -u 1000 -g 1000 -s /bin/bash sim
fi

# Set up sudo
if ! grep -q "^sim ALL" /etc/sudoers.d/sim 2>/dev/null; then
    apt-get update && apt-get install -y sudo \
        && usermod -aG sudo sim \
        && echo "sim ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/sim \
        && chmod 0440 /etc/sudoers.d/sim
fi

# Remove any existing conflicting container
if [ "$(docker ps -aq -f name=isaac-sim)" ]; then
    echo "Removing existing container..."
    docker rm -f isaac-sim
fi

# Build and start container
docker compose -f .devcontainer/docker-compose.yml up -d --build
