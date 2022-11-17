import sys
import os
from subprocess import run, PIPE

def terraformApply(tfFile):
    os.chdir(tfFile)
    applyCommand = f"terraform apply -no-color -auto-approve"
    res = run(applyCommand, shell=True, check=True, stdout=PIPE, stderr=PIPE)
    terraformOutput = res.stdout.decode('utf-8')
    hostname = terraformOutput[terraformOutput.find('ec2_hostname = "'):]
    hostname = hostname.split(" ")[2]
    hostname = hostname.replace('"', "")
    return hostname.strip()

def copyFiles(files, identityFile, host):
    copyCommand = f"scp -r -i {identityFile} {files} admin@{host}:~/das-bot"
    res = run(copyCommand, shell=True, check=True, stdout=PIPE, stderr=PIPE)
    print(res)
    print(f"Copied {files} to {host}")

def openSSH(identityFile, host):
    sshCommand = f"ssh -i {identityFile} admin@{host}"
    res = run(sshCommand, shell=True, check=True, stdout=PIPE, stderr=PIPE)
    print(res)

hostname = terraformApply("C:\\Projects\\terraform")
copyFiles("C:\\Projects\\das-bot-mini", "C:\\Projects\\terraform\\ec2_tf_rsa", hostname)
openSSH("C:\\Projects\\terraform\\ec2_tf_rsa", hostname)
