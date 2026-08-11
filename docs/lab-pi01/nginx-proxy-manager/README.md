# Nginx Proxy Manager

**Status:** ✅ Production  
**Last Updated:** 2026-08-10  

---

## Purpose

Nginx Proxy Manager provides reverse proxy, SSL termination, and domain routing for homelab services.

---

## Features

- Reverse proxy management
- SSL certificate automation
- Internal domain routing (`home.arpa`)
- Clean web UI for proxy configuration

---

## Services Routed

- Homepage → https://home.home.arpa  
- Uptime Kuma → https://uptime.home.arpa  
- Portainer → https://portainer.home.arpa  
- Pi-hole → https://pihole.home.arpa  
- Backup API → https://backup.home.arpa  

---

## Backup API Proxy

### Internal Service


http://192.168.1.250:5055


---

### Public Endpoint


https://backup.home.arpa


---

### Notes

- Removes need to expose port `5055`
- Unified access through NPM
- Used for browser access (not required by Homepage or Kuma)

---

## Configuration

- Managed via NPM web UI
- Hosts configured with:
  - Domain → service mapping
  - SSL enabled (internal CA or Let's Encrypt)

---

## Access

https://npm.home.arpa

---

## Notes

All services are routed through `home.arpa` internal DNS.

---

## Change History

### 2026-08-10

#### Added

- Backup API reverse proxy (`backup.home.arpa`)

#### Verified

- Backup API accessible via domain
- Proxy routing functioning correctly

---

### Previous

- Initial NPM setup and service routing

## Logs

- Log path: /srv/nginx-proxy-manager/data/logs/
- Used for monitoring and fail2ban integration

## Security

- Protected by fail2ban (nginx-auth jail)
- Monitors access logs for unauthorized requests
