#!/usr/bin/env python

def isInternalIp(ip_addr):
    # Internal Addresses are 192.168.1.x
    quads = ip_addr.split('.')
    if (quads[0] == "192" and quads[1] == "168" and quads[2] == "1"):
        ret_val = True
    else:
        ret_val = False
    
    return ret_val
    
addr = raw_input("Enter an IP Address: ")

if (isInternalIp(addr)):
    addr_type = "Internal"
else:
    addr_type = "External"
    
print "{} is {}".format(addr,  addr_type)
