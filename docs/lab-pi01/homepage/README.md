# Homepage

**Status:** ✅ Production  
**Version:** Latest  
**Last Updated:** 2026-08-05

---

## Purpose

Homepage provides a centralized dashboard for accessing homelab services from a single web interface.

## Features

- Service dashboard
- Docker integration
- System widgets
- Bookmarks
- Custom service icons

## Configuration Files

- compose.yaml
- services.yaml
- widgets.yaml
- bookmarks.yaml
- docker.yaml

## Access

https://homepage.home.arpa

## Notes

- Published through Nginx Proxy Manager.
- Secured using the homelab wildcard SSL certificate.
- Accessible from any trusted device on the local network.

---

## Change History

### 2026-08-05

#### Added

- HTTPS support using the wildcard certificate.

#### Changed

- Migrated from a dedicated certificate to the wildcard certificate.

#### Fixed

- Homepage host validation.
- Subject Alternative Name (SAN) configuration.

### 2026-07-30

#### Added

- Initial Homepage deployment.
- Homepage dashboard configuration.
