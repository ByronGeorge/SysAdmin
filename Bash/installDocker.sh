#!/bin/bash

sudo apt-get update
packages=("ca-certificates" "curl" "gnupg" "lsb-release")

for p in ${packages[@]}; do
    echo "Y" | sudo apt-get install $p
done

sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list >/dev/null

#sudo chmod a+r /etc/apt/keyrings/docker.gpg

sudo apt-get update
echo "Y" | sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin