#!/bin/bash

wget https://download.docker.com/linux/ubuntu/dists/bionic/pool/stable/amd64/docker-ce_19.03.9~3-0~ubuntu-bionic_amd64.deb
sudo dpkg -i docker-ce_19.03.9~3-0~ubuntu-bionic_amd64.deb
rm docker-ce_19.03.9~3-0~ubuntu-bionic_amd64.deb
