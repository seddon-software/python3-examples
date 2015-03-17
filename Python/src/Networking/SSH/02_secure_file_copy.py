import paramiko
from paramiko.ssh_exception import SSHException

paramiko.util.log_to_file('ssh.log') # sets up logging

def secureFileCopy(localFile, remoteFile, hostname, port, username, password):
    try:
        transport = paramiko.Transport((hostname, port))
        transport.connect(username = username, password = password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(remotepath=remoteFile, localpath=localFile)
    except SSHException, e:
        print e
    except IOError, e:
        print e.errno, e.strerror
    except Exception, e:
        print e.errno, e.strerror
    finally:
        try:
            sftp.close()
            transport.close()
        except:
            pass
    

secureFileCopy(localFile="files/test1.txt", 
               remoteFile="test1.txt", 
               hostname="172.27.250.211", 
               port=22, 
               username="python", 
               password="this is a demo account")


