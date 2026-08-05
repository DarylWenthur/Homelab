# Lab-Pi01

## Hardware

- Raspberry Pi
- NVMe SSD boot drive
- Raspberry Pi OS Lite (64-bit)

## Configuration

Hostname: `lab-pi01`

SSH: Enabled

Boot Device:
- NVMe SSD (`/dev/nvme0n1p2`)

## Installed Software

- Docker Engine
- Docker Compose
- Portainer
- Homepage
- Nginx Proxy Manager
- Pi-hole
- Uptime Kuma
- Git
- Curl
- Wget
- Vim
- htop
- btop
- unzip
- dnsutils

## Network Services

| Service | URL |
|---------|-----|
| Homepage | https://homepage.home.arpa |
| Portainer | https://portainer.home.arpa |
| Nginx Proxy Manager | https://npm.home.arpa |
| Uptime Kuma | https://uptime.home.arpa |
| Pi-hole | https://pihole.home.arpa |

## DNS

Pi-hole provides internal DNS for the homelab using the `home.arpa` domain.

Configured DNS records include:

- homepage.home.arpa
- portainer.home.arpa
- npm.home.arpa
- uptime.home.arpa
- pihole.home.arpa

## Reverse Proxy

Nginx Proxy Manager provides reverse proxy services for all hosted applications using friendly internal hostnames.

## SSL

- Private Root Certificate Authority (CA)
- Root CA trusted by Windows
- Wildcard certificate (`*.home.arpa`)
- HTTPS enabled for all services
- HTTP/2 enabled
- No browser certificate warnings

## Verified

- SSH access
- Internet connectivity
- Docker Engine
- Docker Compose
- Internal DNS resolution
- Reverse proxy
- HTTPS on all services
- Trusted wildcard certificate
