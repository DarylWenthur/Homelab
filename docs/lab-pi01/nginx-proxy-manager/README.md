# Nginx Proxy Manager

**Status:** ✅ Production  
**Version:** Latest  
**Last Updated:** 2026-08-05

---

## Purpose

Nginx Proxy Manager provides reverse proxy services and HTTPS for internal homelab applications.

## Features

- Reverse proxy
- SSL certificate management
- HTTP to HTTPS redirection
- HTTP/2 support

## Configuration Files

- compose.yaml
- proxy-hosts.md
- ssl.md

## Managed Services

- Homepage
- Portainer
- Pi-hole
- Uptime Kuma

## Access

https://npm.home.arpa

## Notes

All services are secured using a wildcard certificate issued by the homelab Root Certificate Authority.

---

## Change History

### 2026-08-05

#### Added

- Wildcard SSL certificate.

#### Changed

- All proxy hosts migrated to HTTPS.

#### Fixed

- Certificate validation.
- HTTPS configuration.

### 2026-07-28

#### Added

- Initial Nginx Proxy Manager deployment.
