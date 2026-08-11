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

## Repository Structure

### Overview

The repository is organized to reflect a clean, rebuildable homelab configuration.

---

### Top-Level Layout


Homelab/
├── docs/
├── docker/
├── scripts/
├── services/


---

### Directory Breakdown

#### docs/

Documentation for all systems, organized by service and function.

---

#### docker/

Docker-based services and configurations.


docker/
├── homepage/
├── nginx-proxy-manager/
├── pihole/
├── portainer/
├── uptime-kuma/


Each service contains:
- `compose.yaml`
- service-specific configuration files (if applicable)

---

#### scripts/

Automation and operational scripts.

- Backup scripts
- Maintenance scripts

---

#### services/

Custom services and APIs.

- Backup API (`backup_service.py`)
- Weather service (custom Python application)

---

### Design Principles

- Clear separation of concerns
- Rebuildable from repository
- No runtime or generated files stored
- All critical configuration tracked in Git

---

### Notes

- Live system paths (`/srv/...`) are mapped into this structure
- Repository reflects **clean configuration**, not raw system state

## Deployment Workflow

### Overview

Defines how configurations are managed between GitHub (source of truth) and the live system (Raspberry Pi).

---

### Workflow Model


GitHub → Pi → Runtime


- GitHub = clean configuration (source of truth)
- Pi = deployed configuration
- Runtime = active services

---

### Standard Workflow

1. Update or create configuration in repository
2. Commit and push changes to GitHub
3. Pull changes to the Pi
4. Apply configuration (restart service or container)
5. Verify system behavior

---

### Commands

Pull latest changes:


git pull


Apply changes (example):


docker compose down
docker compose up -d


Restart system service (example):


sudo systemctl restart backup-api


---

### Verification

- Confirm service is running
- Check logs if needed
- Validate via UI or API endpoint

---

### Alternative Workflow (Live → Repo Sync)

Used when changes originate on the Pi:

1. Copy updated files from `/srv/...` into repository
2. Clean file (remove runtime or sensitive data)
3. Commit and push to GitHub

---

### Notes

- GitHub remains the source of truth
- Live system should not drift from repository
- All changes should be reflected back into GitHub
