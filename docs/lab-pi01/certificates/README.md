# Certificates

**Status:** ✅ Production  
**Version:** 1.0  
**Last Updated:** 2026-08-05

---

## Purpose

Provides trusted HTTPS certificates for all internal homelab services.

## Components

- Private Root Certificate Authority (CA)
- Wildcard SSL certificate (`*.home.arpa`)

## Documentation

- ca-overview.md
- wildcard-certificate.md

## Notes

Private keys are never stored in this repository.

---

## Change History

### 2026-08-05

#### Added

- Root Certificate Authority.
- Wildcard SSL certificate.

#### Changed

- All services migrated to HTTPS.

#### Fixed

- Subject Alternative Name (SAN) configuration.
