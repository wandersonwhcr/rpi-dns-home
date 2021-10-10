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

## Running

```
docker-compose run --rm ansible
```
