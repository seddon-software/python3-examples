############################################################
#
#    server
#
############################################################

import SocketServer
import socket
import threading

class MyRequestHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        try:
            while(True):
                message = self.request.recv(100).rstrip()
                print "SERVER: ", message
                if message == "exit": break
                # echo request back to client
                self.wfile.write(message)
        except socket.error, e:
            print "error ..."

# specify THreadingMixIn first because otherwise it will override 
# methods in TCPServer 
class MyServer(SocketServer.ThreadingMixIn, 
               SocketServer.TCPServer): pass

server = MyServer(("localhost", 7001), MyRequestHandler)
print "Server on port 7001"

server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()


