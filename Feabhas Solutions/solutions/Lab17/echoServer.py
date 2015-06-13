import socket
import sys
 
HOST = ''   # All available interfaces
PORT = 8888 # Arbitrary non-privileged port

mainSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

# Bind on socket and interface
try:
    mainSocket.bind((HOST, PORT))
except socket.error , msg:
    print ('Bind failed. Error Code : {} message - {}').format(msg[0],msg[1])
    sys.exit()
     
print('Socket bind complete')

# Listen out for connections
mainSocket.listen(2)
print("mainSocket listening...")
try:
    while True:
        # Accept new connection from main connection
        conn, addr = mainSocket.accept()
        incoming = conn.recv(1024)
        print("User connected from {}:{} and sent us: \n{}").format(addr[0],addr[1],incoming)
        conn.sendall(incoming)
        conn.close()
except Exception:
    mainSocket.close()  
