import subprocess, time, os
from threading import Thread

def startServer():
    # server keeps running, so start in on a separate thread 
    params = "python server.py".split()
    serverThread = Thread(target=subprocess.call, args=(params,))
    serverThread.start()

def startClients(n):
    for i in range(n):
        cmd = "python client.py"
        subprocess.call(cmd.split())
   
startServer()
startClients(20)

