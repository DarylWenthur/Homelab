# Local DNS Records

Pi-hole provides local DNS resolution for internal services.

| Hostname            | IP Address    |
| ------------------- | ------------- |
| homepage.home.arpa  | 192.168.1.250 |
| portainer.home.arpa | 192.168.1.250 |
| npm.home.arpa       | 192.168.1.250 |
| uptime.home.arpa    | 192.168.1.250 |
| pihole.home.arpa    | 192.168.1.250 |

## Pi DNS Configuration

`lab-pi01` uses Pi-hole as its DNS server:

```text
nameserver 192.168.1.250
