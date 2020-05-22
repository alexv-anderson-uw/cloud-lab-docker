#!/bin/bash

# # From https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-convenience-script

# # Update indices
# sudo apt-get update
# # Install packages to allow apt to work over HTTPS
# sudo apt-get --yes --force-yes install \
#     apt-transport-https \
#     ca-certificates \
#     curl \
#     gnupg-agent \
#     software-properties-common
# # Add Docker's PGP key
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# # Add Docker's stable repository
# sudo add-apt-repository \
#    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
#    $(lsb_release -cs) \
#    stable"

# # Update indices to include Docker's repository
# sudo apt-get update
# # Install Docker and its dependencies
# sudo apt-get --yes --force-yes install docker-ce docker-ce-cli containerd.io

wget https://download.docker.com/linux/ubuntu/dists/bionic/pool/stable/amd64/docker-ce_19.03.9~3-0~ubuntu-bionic_amd64.deb
sudo dpkg -i docker-ce_19.03.9~3-0~ubuntu-bionic_amd64.deb
rm docker-ce_19.03.9~3-0~ubuntu-bionic_amd64.deb
