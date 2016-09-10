from multiprocessing import Process, Pipe

def child(connection):
    n = connection.recv()
    message = "child received {}".format(n)
    connection.send(message)
    connection.close()

# create 2 connections
parent_connection, child_connection = Pipe()

# create the 2 way pipe
pipe = Process(target=child, args=(child_connection,))

# start sending and receiving
pipe.start()
parent_connection.send(100)
print(parent_connection.recv())
p.join()