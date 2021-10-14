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
ssh-keygen -t rsa -b 4096 -f server.key -C '' -N ''
ssh-copy-id -i server.key.pub pi@$RASPBERRY_ADDR
ssh -i server.key pi@$RASPBERRY_ADDR hostname
```

```
cat > inventory.yaml <<EOF
all:
  vars:
    ansible_user: "pi"
    ansible_ssh_private_key_file: "server.key"
    ansible_host_key_checking: false
    ansible_become: true
    ansible_become_user: "root"
    ansible_python_interpreter: "/usr/bin/python"
  children:
    rpi:
      hosts:
        192.168.0.2:
      vars:
        # Basic
        rpi_addr: "192.168.0.2"
        rpi_cidr: "192.168.0.2/24"
        rpi_router_addr: "192.168.0.1"
        rpi_name: "raspberry"
        rpi_domain: "home"
        # Allow and Reject
        rpi_cidr_allow: "192.168.0.0/24"
        # DHCP Daemon
        rpi_dhcpd_addr_start: "192.168.0.100"
        rpi_dhcpd_addr_end: "192.168.0.200"
        rpi_dhcpd_addr_subnet: "255.255.255.0"
        # Hosts
        rpi_hosts:
          # Raspberry
          - name: "raspberry"
            ip_addr: "192.168.0.2"
            hw_addr: "AA:BB:CC:00:11:22"
          # FooBar
          - name: "foobar"
            ip_addr: "192.168.0.3"
            hw_addr: "DD:EE:FF:33:44:55"
EOF
```

## Running

```
docker-compose run --rm ansible
```

## License

This package is opensource and available under MIT license described in
[LICENSE](https://github.com/wandersonwhcr/rpi-dns-home/blob/main/LICENSE).
