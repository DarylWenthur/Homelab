# Backup Status API

**Status:** ✅ Production  
**Last Updated:** 2026-08-10  

---

## Purpose

Provides backup status via HTTP API for Homepage and Uptime Kuma.

---

## File Location


/srv/homepage/config/backup_service.py


---

## Service


backup-api.service


---

## Endpoint


http://192.168.1.250:5055/api


---

## Response Format


{
"status": "🟢 SUCCESS",
"time": "Mon Aug 10 16:08:04 PDT 2026"
}


---

## Data Source


/srv/homepage/config/backup-status.txt


---

## Status File Format


SUCCESS
Mon Aug 10 16:08:04 PDT 2026
1786403284


---

## Logic

- Reads status file
- Calculates age using unix timestamp
- Returns status based on conditions

---

## Status Behavior

| Condition | Result |
|----------|--------|
| < 8 days | 🟢 SUCCESS |
| > 8 days | 🟡 STALE |
| Failure | 🔴 FAILED |
| Error | 🔴 UNKNOWN |

---

## Stale Threshold


691200 seconds (8 days)


---

## Service Management

Start / restart:


sudo systemctl restart backup-api


Status:


sudo systemctl status backup-api


Logs:


journalctl -u backup-api -n 50


---

## Testing


curl http://localhost:5055/api


---

## Notes

- Runs on port 5055
- Used by Homepage widget
- Used by Uptime Kuma monitor
