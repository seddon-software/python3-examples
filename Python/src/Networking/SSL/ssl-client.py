import socket, ssl, pprint

sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_ssl_sock = ssl.wrap_socket(sd,
                           ca_certs="localhost.pem",
                           cert_reqs=ssl.CERT_NONE,
                           ssl_version=ssl.PROTOCOL_TLSv1)

local_ssl_sock.connect(('localhost', 443))

# ask server to serve a file
local_ssl_sock.write("f4")

data = local_ssl_sock.read()
print data

# note that closing the SSLSocket will also close the underlying socket
local_ssl_sock.close()
