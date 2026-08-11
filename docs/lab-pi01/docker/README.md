# Docker

## Purpose

Docker is used to host all self-hosted applications on Lab-Pi01.

## Deployed Containers

- Homepage
- Nginx Proxy Manager
- Pi-hole
- Portainer
- Uptime Kuma

## Configuration

Docker Compose is used to deploy and manage all containers.

Each application has its own compose file for easier maintenance.

## Notes

- Containers restart automatically.
- Persistent data is stored in mounted volumes.
- Compose files do not contain passwords or sensitive information.

## GitHub Configuration Sync

### Overview

Core system files from the live environment are synchronized to GitHub to maintain a clean, rebuildable configuration state.

---

### Source (Live System)

- `/srv/scripts/` → backup scripts  
- `/srv/homepage/config/` → API + homepage config  

---

### Destination (Repository)


scripts/
services/
docker/homepage/


---

### Included Files

- `.sh` → automation scripts  
- `.py` → API services  
- `.yaml` → service configuration  

---

### Excluded Files

- Runtime data (`backup-status.txt`)  
- Logs  
- `__pycache__/`  
- Generated or temporary files  

---

### Process

1. Copy files from `/srv` into repository
2. Remove sensitive data or temporary content
3. Verify file correctness
4. Commit and push to GitHub

---

### Purpose

- Maintain a clean source of truth
- Enable full system rebuild from repository
- Track configuration changes over time

---

### Notes

- GitHub contains **clean versions**, not raw system state  
- Live system may contain temporary or runtime data not stored in GitHub 
