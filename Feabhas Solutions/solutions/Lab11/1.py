#!/usr/bin/env python

class Host():
    """A simple class to describe a host"""
    
    ip = None
    hostname = None
    services = {} # An empty dictionary

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

