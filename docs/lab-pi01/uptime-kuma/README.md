# Uptime Kuma

**Status:** ✅ Production  
**Version:** Latest  
**Last Updated:** 2026-08-07

---

## Purpose

Uptime Kuma monitors the availability and response time of homelab services.

## Features

- Service monitoring
- HTTPS monitoring
- Status dashboard
- Response time tracking

## Current Monitors

- Homepage
- Portainer
- Nginx Proxy Manager
- Pi-hole

All current monitors are reporting **UP**.

## Configuration Files

- compose.yaml

## Access

[https://uptime.home.arpa](https://uptime.home.arpa)

## Notes

All monitored services use the homelab `home.arpa` infrastructure.

---

## Change History

### 2026-08-07

#### Added

- Nginx Proxy Manager monitoring.
- Pi-hole monitoring.

#### Verified

- Homepage monitor operational.
- Portainer monitor operational.
- Nginx Proxy Manager monitor operational.
- Pi-hole monitor operational.

### 2026-08-05

#### Added

- HTTPS monitoring.

#### Changed

- Monitoring updated to use HTTPS endpoints.

### 2026-07-27

#### Added

- Initial Uptime Kuma deployment.
