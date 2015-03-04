############################################################
#
#    server
#
############################################################

import SocketServer

class MyRequestHandler(SocketServer.StreamRequestHandler):
    def handle( self ):
        while(True):
            message = self.request.recv(100).rstrip();
            if message == "exit": break
            # echo back message
            self.request.sendall(message)

#SocketServer.TCPServer.allow_reuse_address = True
server = SocketServer.TCPServer(("", 2525), MyRequestHandler)
server.serve_forever()
