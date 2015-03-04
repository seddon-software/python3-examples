############################################################
#
#    simple http server
#
############################################################

import SimpleHTTPServer
import SocketServer

# minimal web server.  
# serves files relative to the current directory.

PORT = 8001
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

"""
try the following URL's
    http://localhost:8001/cgi/f1.html
    http://localhost:8001/cgi/f2.html
    http://localhost:8001/cgi/f3.html
"""
