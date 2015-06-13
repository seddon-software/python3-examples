#!/usr/bin/env python

# Get the IP Address
addr = raw_input("Enter an IP Address: ")

dotted_quad = addr.split('.')

#Some validation
length_ok = True
if (len(dotted_quad) != 4):
    length_ok = False
    message = "Incorrect length"
    print "Error with the address: {}".format(message)
    

if (length_ok):
    # Cast from String to Ints
    dotted_quad[0] = int(dotted_quad[0])
    dotted_quad[1] = int(dotted_quad[1])
    dotted_quad[2] = int(dotted_quad[2])
    dotted_quad[3] = int(dotted_quad[3])

    addr_ok = True
    message = ""
    valid_range = range(256)
    
    if (not dotted_quad[0] in valid_range):
        message = "1st value out of range"
        
    if (not dotted_quad[1] in valid_range):
        addr_ok = False
        message = "2nd value out of range"
        
    if (not dotted_quad[2] in valid_range):
        addr_ok = False
        message = "3rd value out of range"
        
    if (not dotted_quad[3] in valid_range):
        addr_ok = False
        message = "4th value out of range"
        
    if (not addr_ok):
        print "Error with the address: {}".format(message)
    else:
        print "The address elements are: {} {} {} {}".format(dotted_quad[0],  dotted_quad[1],  dotted_quad[2],  dotted_quad[3])

        # Classify
        if (dotted_quad[0] < 128):
            print "Class A"
        elif(dotted_quad[0] >= 128 and dotted_quad[0] < 192):
            print "Class B"
        elif(dotted_quad[0] >= 192 and dotted_quad[0] < 224):
            print "Class C" 
        elif(dotted_quad[0] >= 224 and dotted_quad[0] < 240):
            print "Class D"
        elif(dotted_quad[0] >= 250 and dotted_quad[0] < 256):
            print "Class E"
        else:
            # Catch if someone enters a wrong number
            print "Unknown class"
    
