# Pi-hole

**Status:** ✅ Production  
**Version:** Latest  
**Last Updated:** 2026-08-05

---

## Purpose

Pi-hole provides internal DNS resolution and network-wide ad blocking for the homelab.

## Features

- Local DNS
- DNS filtering
- Ad blocking
- Internal hostname resolution

## Configuration Files

- compose.yaml
- dns-records.md
- blocklists.md

## Access

https://pihole.home.arpa/admin

## Notes

Pi-hole hosts the DNS records used by Homepage and Nginx Proxy Manager.

---

## Change History

### 2026-08-05

#### Added

- HTTPS support.
- Internal DNS records for hosted services.

#### Changed

- Published through Nginx Proxy Manager.

#### Fixed

- DNS resolution for internal services.

### 2026-07-28

#### Added

- Initial Pi-hole deployment.
