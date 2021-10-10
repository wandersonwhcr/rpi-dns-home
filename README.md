# rpi-dns-home

My Raspeberry Pi DNS Server at Home

## Install

```
DNS_HOST=192.168.0.2
```

```
ssh-keygen -t rsa -b 4096 -f dns-server.key -C '' -N ''
ssh-copy-id -i dns-server.key.pub pi@$DNS_HOST
ssh -i dns-server.key pi@$DNS_HOST hostname
```

```
cat > inventory.yaml <<EOF
all:
  hosts:
    192.168.0.2:
  vars:
    ansible_become: true
    ansible_become_user: "root"
    ansible_host_key_checking: false
    ansible_python_interpreter: "/usr/bin/python"
    ansible_ssh_private_key_file: "dns-server.key"
    ansible_user: "pi"
    raspberry_cidr: "192.168.0.2/24"
    raspberry_router_addr: "192.168.0.1"
    raspberry_dhcpd_start: "192.168.0.10"
    raspberry_dhcpd_end: "192.168.0.254"
    raspberry_dhcpd_subnet: "255.255.255.0"
    raspberry_dhcpd_dns: "192.168.0.2"
EOF
```

## Running

```
docker-compose run --rm ansible playbooks/install.yaml
```
