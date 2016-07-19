import socket, ssl, pprint

print "OPENSSL_VERSION_INFO: ", ssl.OPENSSL_VERSION_INFO
sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# require a certificate from the server
ssl_sock = ssl.wrap_socket(sd,
                           ca_certs="PCA-3.pem",
                           cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(('www.verisign.com', 443))

print "Peer: ", repr(ssl_sock.getpeername())
print "Cipher: ", ssl_sock.cipher()
print "Peer cert: ", pprint.pformat(ssl_sock.getpeercert())

try:
    PEM_Certificate = ssl.get_server_certificate(('www.verisign.com', 443), 
                                          ca_certs="PCA-3.pem")
    DER_Certificate = ssl.PEM_cert_to_DER_cert(PEM_Certificate)
    print PEM_Certificate
    print DER_Certificate
except socket.error, e:
    print e

# Set a simple HTTP request -- use httplib in actual code.
ssl_sock.write("""GET / HTTP/1.0\rHost: www.verisign.com\r\n\r\n""")

# Read a chunk of data.  Will not necessarily
# read all the data returned by the server.
data = ssl_sock.read()
print data

# note that closing the SSLSocket will also close the underlying socket
ssl_sock.close()
