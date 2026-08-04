# Home Lab

## Overview

This repository documents the design, implementation, and ongoing development of my home lab. The lab serves as both a learning environment and a portfolio project focused on system administration, networking, virtualization, and infrastructure management.

The primary goals of this project are:

* Learn Proxmox virtualization
* Build and manage a Windows Active Directory environment
* Improve Linux administration skills
* Learn enterprise networking concepts including VLANs and managed switching
* Implement centralized backups and storage
* Practice infrastructure documentation and change management

---

# Current Project Status

## Phase 1 – Core Infrastructure (In Progress)

### Planned Hardware

| Component           | Model                                                    | Status                   |
| ------------------- | -------------------------------------------------------- | ------------------------ |
| Virtualization Host | Minisforum MS-01 (Core i5-12600H Barebone - Refurbished) | Waiting for availability |
| Memory              | Crucial 32GB DDR5 (2×16GB)                               | Planned                  |
| Storage             | Silicon Power 2TB NVMe SSD                               | Planned                  |
| Switch              | TP-Link Omada ES210X-M2                                  | Planned                  |
| Raspberry Pi        | Raspberry Pi 5 (8GB)                                     | Complete                 |
| Internet            | Starlink                                                 | Complete                 |

### Future Hardware

* CyberPower CP1500PFCLCD UPS
* Asustor Flashstor 6 NAS
* Bambu Lab P1S Combo
* Lab Rax 10-inch Rack

---

# Planned Software

## Hypervisor

* Proxmox VE

## Virtual Machines

* Windows Server
* Windows 11
* Ubuntu Server
* Docker Host

## Raspberry Pi Services

* Pi-hole
* Tailscale
* Homepage
* Uptime Kuma
## Current Progress

### Raspberry Pi (Lab-Pi01)
- Raspberry Pi OS Lite (64-bit) installed.
- Booting successfully from NVMe SSD.
- SSH configured and verified.
- Hostname: `lab-pi01`
- Remote management working.

### Docker
- Docker Engine installed.
- Docker verified with `hello-world`.
- Basic Docker commands learned:
  - `docker ps`
  - `docker ps -a`
  - `docker images`
  - `docker rm`

---

# Roadmap

* [x] Plan hardware
* [x] Select networking equipment
* [x] Prepare Raspberry Pi
* [ ] Purchase MS-01
* [ ] Install Proxmox
* [ ] Configure networking
* [ ] Deploy Windows Server
* [ ] Configure Active Directory
* [ ] Print Lab Rax
* [ ] Add UPS
* [ ] Add Flashstor NAS

---

# Repository Structure

```text
docs/
images/
diagrams/
README.md
```

As the project grows, this repository will include diagrams, configuration notes, and build documentation.
