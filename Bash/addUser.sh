#!/bin/bash

sudo useradd -ms /bin/bash mcadmin
echo 'mcadmin:Password' | sudo chpasswd && history -d -1
echo 'mcadmin    ALL=(ALL)   NOPASSWD: ALL' | sudo tee -a /etc/sudoers.d/designated
sudo chmod 0440 /etc/sudoers.d/designated