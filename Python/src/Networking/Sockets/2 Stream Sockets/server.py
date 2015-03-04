############################################################
#
#    stream socket server
#
############################################################

import socket, sys
from threading import Thread

def communicateWithClient(newsocket, messageNo):
    # wait for message and echo
    message = newsocket.recv(100)
    print "SERVER:", message
    sys.stdout.flush()
    
    # send response and close socket immediately
    response = "{0}: {1}".format(messageNo, message)
    newsocket.send(response)
    newsocket.close()


listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenSocket.bind(('', 7001))
listenSocket.listen(5)    # set up backlog buffer
messageNo = 1

print "Server starting"
while True:
    # accept client connections
    newsocket, remoteIPandPORT = listenSocket.accept()
    print "SERVER: opened a new connection:", remoteIPandPORT
    sys.stdout.flush()
    clientThread = Thread(target=communicateWithClient, args=(newsocket, messageNo))
    messageNo = messageNo + 1
    clientThread.start()
