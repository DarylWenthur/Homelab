# Backup System

**Status:** ✅ Production  
**Last Updated:** 2026-08-10  

---

## Purpose

Performs automated backups and writes status for monitoring systems.

---

## Script Location


/srv/scripts/automated-backup-lab-pi01.sh


---

## Status File


/srv/homepage/config/backup-status.txt


---

## Status File Format


SUCCESS
Mon Aug 10 16:08:04 PDT 2026
1786403284


- Line 1: Status (SUCCESS / FAILED)
- Line 2: Timestamp (human readable)
- Line 3: Unix timestamp (used for stale detection)

---

## Script Output

Successful run writes:


echo "SUCCESS" > "$STATUS_FILE"
echo "$(date)" >> "$STATUS_FILE"
echo "$(date +%s)" >> "$STATUS_FILE"


---

## Failure Behavior

On failure, script should write:


echo "FAILED" > "$STATUS_FILE"
echo "$(date)" >> "$STATUS_FILE"
echo "$(date +%s)" >> "$STATUS_FILE"


---

## Schedule

- Runs weekly (cron)

---

## Integration

- Homepage → displays status via API
- Uptime Kuma → monitors status via API
- Discord → alerts on failure or stale

---

## Testing

Force failure:


echo "FAILED" > /srv/homepage/config/backup-status.txt
echo "test" >> /srv/homepage/config/backup-status.txt
echo "1000000000" >> /srv/homepage/config/backup-status.txt


Force stale:


echo "SUCCESS" > /srv/homepage/config/backup-status.txt
echo "Old" >> /srv/homepage/config/backup-status.txt
echo "1000000000" >> /srv/homepage/config/backup-status.txt


Restore:


bash /srv/scripts/automated-backup-lab-pi01.sh


---

## Notes

- Status file is the single source of truth
- API reads this file for all monitoring
- Stale threshold handled by API (8 days)
