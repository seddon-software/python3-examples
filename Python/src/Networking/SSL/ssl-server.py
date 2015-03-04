import traceback
import socket
import ssl
import SimpleHTTPServer

PORT = 443

def do_request(tcp_stream, from_addr):
    filename = tcp_stream.read()
    filename = "files/" + filename
    try:
        f = open(filename,"r")
        all = str(f.readlines())
        f.close()
    except Exception, e:
        all = "Invalid File"
        
    tcp_stream.write(all)
    
    

sd = socket.socket()
sd.bind(('localhost', PORT))
sd.listen(5)

print("serving on port", PORT)

while True:
    try:
        newsocket, from_addr = sd.accept()
        ssl_socket = ssl.wrap_socket(newsocket,
                                     server_side=True,
                                     certfile='localhost.pem',
                                     ssl_version=ssl.PROTOCOL_TLSv1)
        
        do_request(ssl_socket, from_addr)
        
    except Exception:
        traceback.print_exc()

