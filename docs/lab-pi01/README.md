# Lab-Pi01

## Hardware

- Raspberry Pi 5 (8GB)
- NVMe SSD boot drive
- Raspberry Pi OS Lite (64-bit)
- PNY 32GB USB backup drive
  - Label: `Lab_Backups`
  - Filesystem: exFAT
  - UUID: `987E-4EEF`

## Configuration

Hostname: `lab-pi01`

SSH: Enabled

Boot Device:

- NVMe SSD (`/dev/nvme0n1p2`)

Backup Mount:

- `/srv/backups`
- Backup drive is normally unmounted
- Automatically mounted during scheduled backups

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

| Service             | URL                                                        |
| ------------------- | ---------------------------------------------------------- |
| Homepage            | [https://homepage.home.arpa](https://homepage.home.arpa)   |
| Portainer           | [https://portainer.home.arpa](https://portainer.home.arpa) |
| Nginx Proxy Manager | [https://npm.home.arpa](https://npm.home.arpa)             |
| Uptime Kuma         | [https://uptime.home.arpa](https://uptime.home.arpa)       |
| Pi-hole             | [https://pihole.home.arpa](https://pihole.home.arpa)       |

## DNS

Pi-hole provides internal DNS for the homelab using the `home.arpa` domain.

The Pi itself uses Pi-hole (`192.168.1.250`) as its DNS server.

Configured DNS records include:

- homepage.home.arpa
- portainer.home.arpa
- npm.home.arpa
- uptime.home.arpa
- pihole.home.arpa

Verified:

- `npm.home.arpa` → `192.168.1.250`
- `pihole.home.arpa` → `192.168.1.250`
- Internet DNS resolution

## Reverse Proxy

Nginx Proxy Manager provides reverse proxy services for hosted applications using friendly internal hostnames.

## SSL

- Private Root Certificate Authority (CA)
- Root CA trusted by Windows
- Wildcard certificate (`*.home.arpa`)
- HTTPS enabled for hosted services
- HTTP/2 enabled
- No browser certificate warnings

## Backup System

Backups are stored on the dedicated PNY USB drive.

Backup location:

```text
/srv/backups/Backups/lab-pi01/

## Security

- UFW enabled
  - Allowed ports: 22, 80, 443, 5055

- fail2ban enabled
  - Active jails:
    - sshd
    - nginx-auth

## Backup Service

- API endpoint active on port 5055
