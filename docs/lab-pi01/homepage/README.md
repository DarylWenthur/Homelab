# Homepage

**Status:** ✅ Production  
**Last Updated:** 2026-08-10  

---

## Purpose

Homepage provides a centralized dashboard for homelab services and system status.

---

## Features

- Service dashboard
- Custom API widgets
- Docker service visibility
- Clean UI for lab monitoring

---

## Services Displayed

- Portainer
- Nginx Proxy Manager
- Pi-hole
- Uptime Kuma
- Backup Status

---

## Backup Status Widget

### Endpoint
http://192.168.1.250:5055/api

---

### Display

- Status (🟢 / 🟡 / 🔴)
- Timestamp of last backup

---

### Configuration
widget:
type: customapi
url: http://192.168.1.250:5055/api
refreshInterval: 10000
method: GET
display: block
mappings:
- field: status
label: ""
- field: time
label: ""

---

### Behavior

| Status | Meaning |
|--------|--------|
| 🟢 SUCCESS | Backup completed within 8 days |
| 🟡 STALE | Backup older than 8 days |
| 🔴 FAILED | Backup failed |

---

### Notes

- Labels intentionally removed for cleaner display
- Refresh interval set to 10 seconds
- Uses local API service running on port 5055

---

## Configuration Files

- compose.yaml
- services.yaml

---

## Access

https://home.home.arpa

---

## Change History

### 2026-08-10

#### Added

- Backup status widget (custom API)
- Status icons (🟢 🟡 🔴)
- Timestamp display for last backup

#### Verified

- Widget updates correctly
- API integration functional
- Status reflects backup script output
