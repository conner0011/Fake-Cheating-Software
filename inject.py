import os
import time
import psutil
import requests
import json
import sys

# This is a simple function to check if a process is running.
def checkIfProcessRunning(processName):
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


#This function just loops until the battlebit game is running (additionally, I'm not sure if the process name is correct.)
def wait():
    x = True
    while x == True:
        if checkIfProcessRunning("battlebit.exe"):
            time.sleep(1.5)
            x = False
            return True
        else:
            time.sleep(1.5)
            wait()


# This is a simple function to send a message to a webhook in discord.
# Originally this was going to be used to send a message of their username or something that idenifies them in-game so they can be banned.
def sendDiscordMessage(message):
    url = "Ur webhook"
    payload = {'content': message}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.text)
