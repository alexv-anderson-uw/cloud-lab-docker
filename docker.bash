#!/bin/bash

# From https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-convenience-script

# Update indices
sudo apt-get update
# Install packages to allow apt to work over HTTPS
sudo apt-get --yes install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
# Add Docker's PGP key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# Add Docker's stable repository
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get install -y docker-ce docker-ce-cli