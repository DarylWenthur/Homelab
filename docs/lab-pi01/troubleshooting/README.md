# Troubleshooting

This directory contains notes about issues encountered while building the homelab.

Topics include:

- Docker
- Homepage
- Nginx Proxy Manager
- Pi-hole
- Certificates

These notes document solutions for future reference and disaster recovery.

## System Validation Checklist

### Purpose

Provides a consistent process to verify that all homelab services are functioning correctly.

---

### Backup System

Check status file:


cat /srv/homepage/config/backup-status.txt


Expected:
- Line 1 = SUCCESS or FAILED
- Line 2 = timestamp
- Line 3 = unix timestamp

---

### Backup API

Check service:


sudo systemctl status backup-api


Test endpoint:


curl http://localhost:5055/api


Expected:
- JSON response
- Status shows SUCCESS / FAILED / STALE

---

### Homepage

- Open: https://home.home.arpa
- Verify backup widget displays:
  - Status icon
  - Timestamp
- No missing data or errors

---

### Uptime Kuma

- Open: https://uptime.home.arpa
- Verify:
  - Backup monitor is UP
  - Status matches API

---

### Nginx Proxy Manager

- Open: https://npm.home.arpa
- Verify:
  - backup.home.arpa is configured
  - Proxy is online

---

### Full System Check

After reboot:

1. Verify services start automatically
2. Confirm API responds
3. Confirm Homepage loads correctly
4. Confirm monitoring is active

---

### Notes

- This checklist reflects actual manual validation steps
- Used after changes, updates, or system restart
