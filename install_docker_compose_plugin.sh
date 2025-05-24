#!/bin/bash
# This script installs Docker Compose plugin

# Install dependencies
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg lsb-release

# Create keyrings directory
sudo install -m 0755 -d /etc/apt/keyrings

# Download Docker GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /tmp/docker.gpg

# Convert GPG key to keyring format
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg /tmp/docker.gpg

# Clean up
sudo rm /tmp/docker.gpg

# Add Docker repo to APT sources
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release; echo \"$VERSION_CODENAME\") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package index
sudo apt-get update

# Install Docker Compose plugin
sudo apt-get install -y docker-compose-plugin

# Verify installation
docker compose version
