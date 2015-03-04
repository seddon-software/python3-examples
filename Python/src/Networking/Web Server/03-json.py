############################################################
#
#    fine control
#
############################################################

import BaseHTTPServer
import cgi, random, sys
import cgitb, urlparse
import urlparse
cgitb.enable()

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.requestline)
        o = urlparse.urlparse(self.path)
        a = urlparse
        qs = o[4]
        print(qs)
        d = urlparse.parse_qs(qs)
        print("x = ", d['x'])
        x = d['x'][0]
        y = d['y'][0]
        z = d['z'][0]
        
        try:
            # f = open("cgi" + self.path, "r")
            print("x = ", x, "y = ", y, "z = ", z)
        except:
            self.send_error(404, "Input Error")
            return
            
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        try:
            # redirect stdout to client
            stdout = sys.stdout
            sys.stdout = self.wfile
            
            # download file
            print('{')
            print('"x": "101",')
            print('"y": "202",')
            print('"z": "303"')
            print('}')

            #print("x: " + x + "<br>" + "y: " + y + "<br>" + "z: " + z + "<br>")
        finally:
            sys.stdout = stdout # restore

PORT = 18080
SERVER = "localhost"
httpd = BaseHTTPServer.HTTPServer((SERVER, PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()


"""
try the following URL's
    http://localhost:8002/f1.html
    http://localhost:8002/f2.html
    http://localhost:8002/f3.html
"""
