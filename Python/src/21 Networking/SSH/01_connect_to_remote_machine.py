import paramiko

paramiko.util.log_to_file('ssh.log') # sets up logging

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect('192.168.2.5', username='python', password='this is a demo account')


def execute(cmd, hostname, port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        ssh.connect(hostname, port, username, password) 
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print stdout.readlines()
        ssh.close()
    except Exception,e:
        print 'whoops: ' + str(e)

execute(cmd="uname -a", hostname="192.168.1.140", port=22, username="pi", password="3.14159")
