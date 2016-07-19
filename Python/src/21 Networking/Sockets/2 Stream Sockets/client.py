############################################################
#
#    stream socket client
#
############################################################

import socket, sys

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('localhost', 7001))    
message = "This is a message from a client: "
clientSocket.send(message)   
response = clientSocket.recv (100) # blocking call
print "CLIENT:", response
sys.stdout.flush()
clientSocket.close()
