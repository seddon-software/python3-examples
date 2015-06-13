#!/usr/bin/env python

# Find a hostname from an address
def addressToName(addr,  hosts):
    hostname = hosts.get(addr)
    return hostname
    

# Find an address from the name
def nameToAddress(name,  hosts):
    for (ip, hostname) in hosts.items():
        if (hostname == name):
            return ip
    
    # If we have got here, there is no match found
    return None
    
# Wrapper that picks which function to call
def lookup(thing,  hosts):
    first_char = thing[0]
    retval = None
    lookup_type = None
    funcs = {'name': addressToName, 'address': nameToAddress}    

    if (first_char.isdigit()):
        lookup_type = "name"
    else:
        lookup_type = "address"
        
    retval = funcs[lookup_type](thing, hosts)

    return (retval, lookup_type)
    
hosts = {'192.168.1.1':'gateway.local.net',  '192.168.1.2':'host1.local.net'}

query = raw_input("Enter a name or address: ")
(value, lookup_type) = lookup(query,  hosts)
if (value == None):
    print "Unknown host"
elif (lookup_type == "name"):
    print "The name of {} is {}".format(query, value)
else:
    print "The address of {} is {}".format(query, value)
