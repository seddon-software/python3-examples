############################################################
#
#    client
#
############################################################

import socket
import time

def SendAndReceive(message):
    mySocket.sendall(message)
    response = mySocket.recv(100)
    print response
    

print "Client"
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('localhost', 7001))

SendAndReceive('25 * 40')
SendAndReceive('15 + 33 + 127')
SendAndReceive('junk....')

mySocket.close()

1
