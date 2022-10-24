# Commands
# curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
# sudo apt install nodejs

import sys
from subprocess import run, PIPE

def installNode():
    try:
        command = f"sudo apt install curl"
        res = run(command, shell=True, check=True, stdout=PIPE, stderr=PIPE)
        print(res)
        command = f"curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -"
        res = run(command, shell=True, check=True, stdout=PIPE, stderr=PIPE)
        print(res)
        command = f"sudo apt install nodejs"
        res = run(command, shell=True, check=True, stdout=PIPE, stderr=PIPE)
        print(res)
    except:
        print(f"Failed to download.")
        sys.exit(1)

installNode()

