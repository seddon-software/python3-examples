############################################################
#
#    client
#
############################################################

import socket
import time
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to well known address
mySocket.connect(('localhost', 7001))

# send and receive messages
for n in range(1, 20):
    mySocket.send('This is message {0} from client'.format(n))
    response = mySocket.recv(100).rstrip(); 
    print "CLIENT: {0}:".format(response)
    time.sleep(random.randint(5, 50)/10.0)

mySocket.send('exit')
mySocket.close()


1
