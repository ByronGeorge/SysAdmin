import sys
from subprocess import run, PIPE

def run_minecraft(name, minecraft_world):
    # Split the whole command into parts for readability
    run_command = "sudo docker run"
    options = f" -d -ti -p 25565:25565 -e EULA=TRUE --name {name}"
    options_cont = " -v ${HOME}" + f"{minecraft_world}:/data itzg/minecraft-server"

    # Take the commands and put them into a list
    commands = [run_command, options, options_cont]

    # Use that list to join the commands into one string
    command = ''.join(commands)

    # Run the command
    res = run(command, shell=True, check=True, stdout=PIPE, stderr=PIPE)
    print(res)

try:
    run_minecraft("my-minecraft", "/minecraft/test-world")
except:
    print(f"failed to start docker container and run minecraft")
    sys.exit(1)