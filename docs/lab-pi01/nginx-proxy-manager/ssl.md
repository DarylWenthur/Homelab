# SSL Configuration

## Certificate Authority

A private Root Certificate Authority (CA) is used to secure all internal services.

## Certificate

Wildcard certificate:

*.home.arpa

## Trust

The Root CA is installed on client devices, allowing browsers to trust all certificates issued by the homelab CA.

## Notes

Private keys are stored securely and are not included in this repository.
