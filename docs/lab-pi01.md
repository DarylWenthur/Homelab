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

### System

- Docker
- Docker Compose
- Git
- Curl
- Wget
- Vim
- htop
- btop
- unzip
- dnsutils

### Services

- Homepage
- Portainer
- Uptime Kuma
- Nginx Proxy Manager

## Project Structure

```text
/srv
├── homepage
├── nginx-proxy-manager
├── portainer
└── uptime-kuma
```

## Proxy Hosts

- homepage.home.arpa
- portainer.home.arpa
- uptime.home.arpa
- npm.home.arpa

## Verified

- SSH access
- Internet connectivity
- Docker Engine
- Docker Compose
- Homepage running
- Portainer running
- Uptime Kuma running
- Nginx Proxy Manager running

## Next Steps

- Install Pi-hole
- Configure local DNS
- Connect DNS with Nginx Proxy Manager
- Access services using `.home.arpa` hostnames
