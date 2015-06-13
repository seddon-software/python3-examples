#!/usr/bin/env python

class Host:
    """A simple class to describe a host"""
    
    ip = None
    hostname = None
    services = {}
    
    def __init__(self):
        # Clear out any values on init
        self.ip = None
        self.hostname = None
        self.services = {}
        
    def setIp(self,  ip):
        self.ip = ip
    
    def getIp(self):
        return self.ip
    
    def setHostname(self,  hostname):
        self.hostname = hostname
        
    def getHostname(self):
        return self.hostname
        
    def addService(self,  service):
        self.services.update(service)
    
    def hasService(self,  service):
        return self.services.get(service)
        
    def display(self):
        # Simple method to display the class
        print """
Host
--------------
IP Addr:     {}
hostname: {}
Services:    {}
""".format(self.ip,  self.hostname,  self.services)

class HostManager:
    host_list = []
    
    def addHost(self,  host):
        self.host_list.append(host)
        
    def findService(self,  service):
        hostnames = []
        for host in self.host_list:
            if (host.hasService(service)):
                hostnames.append(host.hostname)
        
        return hostnames

if (__name__ == "__main__"):
    myhost = Host()
    myhost.setIp("192.168.1.1")
    myhost.setHostname('server.local.net')
    myhost.addService({'ftp':21})
    myhost.addService({'www':80})

    myhost2 = Host()
    myhost2.setIp("192.168.1.2")
    myhost2.setHostname('server2.local.net')
    myhost2.addService({'www':80})

    manager = HostManager()
    manager.addHost(myhost)
    manager.addHost(myhost2)

    ftp_servers = manager.findService('ftp')
    print ftp_servers

    www_servers = manager.findService('www')
    print www_servers
