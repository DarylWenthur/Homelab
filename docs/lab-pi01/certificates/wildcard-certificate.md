# Wildcard Certificate

The homelab uses a wildcard certificate to secure all services under the `home.arpa` domain.

## Covered Services

- homepage.home.arpa
- portainer.home.arpa
- npm.home.arpa
- uptime.home.arpa
- pihole.home.arpa

## Deployment

The wildcard certificate is installed in Nginx Proxy Manager and assigned to each proxy host.
