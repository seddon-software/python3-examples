#!/usr/bin/env python

#############################
# Simple Python HTTP server #
#############################

import BaseHTTPServer
import CGIHTTPServer
import cgitb
import os


# This line enables CGI error reporting
cgitb.enable()

# Server setup
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/cgi-bin"]

# Enable server
os.system('clear')
print
print 'Feabhas http service'
print
print 'HTTP server running...'
httpd = server(server_address, handler)
httpd.serve_forever()
