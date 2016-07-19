Assuming SSL is setup:

1. Start up Oracle VirtualBox
2. Launch foo and bar Ubuntu sessions
3. Login with passwords foo and bar
4. Consult the README-SSH.txt on machine foo
5. Run ssh commands from Windows 7:
        ssh -p 5022 foo@foo-VirtualBox
        ssh -p 6022 bar@bar-VirtualBox
        scp -P 5022 foo@foo-VirtualBox:/home/foo/R.txt localfile   (note -P)
        scp -P 6022 bar@bar-VirtualBox:/home/bar/R.txt localfile   (note -P)
where ssh is installed in C:\MinGW\msys\1.0\bin

_______________________________________________________________________


To set the machines up to begin with:

On the Ubuntu machine:
======================

1. Install ssh
--------------

sudo apt-get install openssh-server


2. Run the following commands to set keys
-----------------------------------------

ssh-keygen -t rsa
cd ~/.ssh
cp id_rsa.pub authorized_keys


3. Set up networking
--------------------

# set up NAT port forwarding with
# Host = 4022
# Guest = 22


On the host (Windows 7)
-----------------------

ssh -p 5022 foo@foo-VirtualBox
scp -P 5022 foo@foo-VirtualBox:/home/foo/R.txt localfile   (note -P)
