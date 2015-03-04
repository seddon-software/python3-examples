import paramiko

class Server(object):
    def __init__(self, username, password, hostname, port=22):
        self.transport = paramiko.Transport((hostname, port))
        self.transport.connect(username=username, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def upload(self, local, remote):
        self.sftp.put(local, remote)

    def download(self, remote, local):
        self.sftp.get(remote, local)

    def close(self):
        if self.transport.is_active():
            self.sftp.close()
            self.transport.close()

    # with-statement support
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.close()


paramiko.util.log_to_file('ssh.log') # sets up logging

ubuntuServer = Server(username="python", 
                        password="this is a demo account", 
                        hostname="192.168.2.5", 
                        port=22) 

# upload and download a file
ubuntuServer.upload(local="files/test1.txt", remote="test1.txt")
ubuntuServer.download(remote="test1.txt", local="files/test1.txt")
ubuntuServer.close()


        