# rpi-dns-home

My Raspeberry Pi DNS Server at Home

## Technologies

* Ansible
* Raspberry Pi
* SSH
* udhcpd
* ISC DHCP Client
* Unbound

## Install

```
RASPBERRY_ADDR=192.168.0.2
```

```
ssh-keygen -t rsa -b 4096 -f dns-server.key -C '' -N ''
ssh-copy-id -i dns-server.key.pub pi@$RASPBERRY_ADDR
ssh -i dns-server.key pi@$RASPBERRY_ADDR hostname
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
    raspberry_addr: "192.168.0.2"
    raspberry_cidr: "192.168.0.2/24"
    raspberry_hostname: "tingle"
    raspberry_domain: "home"
    raspberry_router_addr: "192.168.0.1"
    raspberry_dhcpd_start: "192.168.0.10"
    raspberry_dhcpd_end: "192.168.0.254"
    raspberry_dhcpd_subnet: "255.255.255.0"
    raspberry_unbound_allow_cidr: "192.168.0.0/24"
    raspberry_hosts:
      - name: "foobar"
        ip_addr: "192.168.0.3"
        hw_addr: "AA:BB:CC:DD:EE:FF"
      - name: "bazqux"
        ip_addr: "192.168.0.4"
        hw_addr: "00:11:22:AA:BB:CC"
EOF
```

## Running

```
docker-compose run --rm ansible
```

## License

This package is opensource and available under MIT license described in
[LICENSE](https://github.com/wandersonwhcr/rpi-dns-home/blob/main/LICENSE).
