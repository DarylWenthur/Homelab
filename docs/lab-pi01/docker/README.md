# Docker

## Purpose

Docker is used to host all self-hosted applications on Lab-Pi01.

## Deployed Containers

- Homepage
- Nginx Proxy Manager
- Pi-hole
- Portainer
- Uptime Kuma

## Configuration

Docker Compose is used to deploy and manage all containers.

Each application has its own compose file for easier maintenance.

## Notes

- Containers restart automatically.
- Persistent data is stored in mounted volumes.
- Compose files do not contain passwords or sensitive information.
