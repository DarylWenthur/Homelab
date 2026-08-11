#!/bin/bash

STATUS_FILE="/srv/homepage/config/backup-status.txt"

set -e

MOUNT_POINT="/srv/backups"
BACKUP_SCRIPT="/srv/scripts/backup-lab-pi01.sh"
BACKUP_DIR="$MOUNT_POINT/Backups/lab-pi01"

echo "========================================"
echo "       Lab-Pi01 Automated Backup"
echo "========================================"
echo

echo "Mounting backup drive..."
sudo mount "$MOUNT_POINT"

if ! mountpoint -q "$MOUNT_POINT"; then
    echo "ERROR: Backup drive did not mount."
    exit 1
fi

echo "Backup drive mounted successfully."
echo

BEFORE=$(find "$BACKUP_DIR" -maxdepth 1 -type f -name 'lab-pi01-*.tar.gz' 2>/dev/null | wc -l)

echo "Running backup..."
sudo "$BACKUP_SCRIPT"

AFTER=$(find "$BACKUP_DIR" -maxdepth 1 -type f -name 'lab-pi01-*.tar.gz' | wc -l)

if [ "$AFTER" -le "$BEFORE" ]; then
    echo
    echo "ERROR: No new backup archive was created."

    echo "FAILED" > "$STATUS_FILE"
    echo "$(date)" >> "$STATUS_FILE"

    sudo umount "$MOUNT_POINT"
    exit 1
fi

echo
echo "New backup archive verified."
echo

sync

echo "Unmounting backup drive..."
sudo umount "$MOUNT_POINT"

echo
echo "========================================"
echo "       Backup completed successfully"
echo "========================================"
echo "SUCCESS" > "$STATUS_FILE"
echo "$(date)" >> "$STATUS_FILE"
echo "$(date +%s)" >> "$STATUS_FILE"
