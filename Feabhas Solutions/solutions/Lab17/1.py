#!/usr/bin/env python
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'www.feabhas.com'
port = 80

try:
    sock.connect((host,port))
except:
    print "Error"
    sys.exit(1)
print 'Connected to ', host, ' on port ', port

message = "GET / HTTP/1.1\r\nHost: www.feabhas.com\r\n\r\n"
sock.sendall(message)
reply = 1 # An arbitary value that is not ""
data = "" # Holds the final response
while (not reply == ""):
    reply = sock.recv(1024)
    data += reply

# Count the headers
header = data.split('<h1')
print "H1",  len(header)-1 # Reduce by one as a split splits into two parts (eitherside of the match

header = data.split('<h2')
print "H2",  len(header)-1

header = data.split('<h3')
print "H3",  len(header)-1

sock.close()

