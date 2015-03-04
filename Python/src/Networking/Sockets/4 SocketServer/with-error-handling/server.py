############################################################
#
#    server
#
############################################################

import SocketServer

class MyRequestHandler(SocketServer.StreamRequestHandler):
    
    def handle(self):
        try:
            while(True):
                message = self.request.recv(100).rstrip();
                if message == "exit": break
                # evaluate message
                response = eval(message)
                self.request.sendall(str(response))
        except socket.error, e:
            print "error ..."

class MyServer(SocketServer.TCPServer):
    def __init__(self, server_address, RequestHandlerClass):
        SocketServer.TCPServer.allow_reuse_address = True
        SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass)
        
    def handle_error(self, request, client_address):
        print "Illegal request"
        request.sendall("Illegal request")

print "Server"
server = MyServer(("localhost", 7001), MyRequestHandler)
server.serve_forever()
