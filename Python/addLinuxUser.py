import os
import subprocess
import sys
import getpass

def add_user():
    username = "mcadmin"

    # Gets the password with *** as input 
    # password = getpass.getpass()
    password = "password"

    try:
        subprocess.run(['useradd', '-p', password,username])
    except:
        print(f"Failed to add user.")
        sys.exit(1)


add_user()