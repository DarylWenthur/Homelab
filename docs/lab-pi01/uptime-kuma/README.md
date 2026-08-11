# Uptime Kuma

**Status:** ✅ Production  
**Version:** Latest  
**Last Updated:** 2026-08-10  

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
- Backup API

All current monitors are reporting **UP**.

---

## Backup Monitoring

### Endpoint
http://192.168.1.250:5055/api

### Validation

- JSON Query: $.status
- Expected: 🟢 SUCCESS


### Behavior

| Status | Result |
|--------|--------|
| 🟢 SUCCESS | UP |
| 🟡 STALE | DOWN (alert) |
| 🔴 FAILED | DOWN (alert) |

### Notes

- Backup runs weekly
- Stale threshold set to 8 days
- Alerts sent to Discord on failure or stale state

---

## Configuration Files

- compose.yaml

## Access

https://uptime.home.arpa

## Notes

All monitored services use the homelab `home.arpa` infrastructure.

---

## Change History

### 2026-08-10

#### Added

- Backup API monitoring
- JSON status validation (`$.status`)
- Discord alerting for backup failures and stale state

#### Verified

- Backup monitor operational
- Alerts triggering correctly for FAILED and STALE states

---

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
