# rpi-dns-home

My Raspeberry Pi DNS Server at Home

## Install

```
ssh-keygen -t rsa -b 4096 -f dns-server.key -C '' -N ''
```

## Running

```
docker-compose run --rm ansible
```
