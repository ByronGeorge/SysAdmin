from subprocess import run, PIPE
import sys

###
### Note this install is for the debian flavor of linux
###

def installDocker():
    packages = ["ca-certificates", "curl", "gnupg", "lsb-release"]
    # Loop through packages and install them
    for package in packages:
        try:
            command = f"echo Y | sudo apt-get install {package}"
            res = run(command, shell=True, check=True, stdout=PIPE, stderr=PIPE)
            print(res)
        except:
            print(f"Failed to download {package}.")
            sys.exit(1)
    
    # Make directory for keyring
    run('sudo mkdir -p /etc/apt/keyrings')

    # Use Curl to download the gpg key
    run('curl -fsSL  https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg')

    # Add repo to source list
    command1 = 'echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg]'
    command2 = ' https://download.docker.com/linux/debian $(lsb_release -cs) stable"'
    command3 = ' | sudo tee /etc/apt/sources.list.d/docker.list >/dev/null'
    commands = [command1, command2, command3]
    totalCommand = ''.join(commands)
    run(totalCommand)

    # Perform an update on packages
    run('sudo apt-get update')

    # Install docker
    dockerInstall = f"echo Y | sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin"
    run(dockerInstall)

installDocker()