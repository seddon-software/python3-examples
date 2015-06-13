#!/usr/bin/env python

import serial
import platform
import sys

ERR_UNKNOWN_SYSTEM = 1

my_system = platform.system()

# Open the port
if (my_system == 'Linux'):
    # Linux
    port = serial.Serial('/dev/ttyUSB0', 9600, timeout=10)
elif (my_system == 'Darwin'):
    port = serial.Serial('/dev/ttys000', 9600, timeout=10)
elif (my_system == 'Windows'):
    #Windows
    port = serial.Serial('COM1', 9600, timeout=10)
else:
    print "Unsupported OS"
    sys.exit(ERR_UNKNOWN_SYSTEM)
    
# Are we the 1st or 2nd system?
order = ""
while ((not order == "1") and (not order == "2") ):
    order = raw_input('Are we First (1) or Second (2): ')
    
if (order == "1"):
    msg = ""
    while True: # Run forever
        msg = raw_input("Enter your message: ")
        # Write the message to the other system
        port.write(msg)
        if (msg.lower() == "quit"):
            port.close()
            sys.exit(0)
        
        # Wait for a repsonse
        answer = port.read(1024)
        
        if (answer == "quit"):
            print "Your partner quit."
            port.close()
            sys.exit(0)
elif (order == "2"):
    msg = ""
    while (not msg  == "quit"):
        # Wait for a repsonse
        answer = port.read(1024)
        
        if (answer == "quit"):
            print "Your partner quit."
            port.close()
            sys.exit(0)

        msg = raw_input("Enter your message: ")
        # Write the message to the other system
        port.write(msg)
else:
    print "Only two clients are supported."
    port.close()
    sys.exit(0)

    

    
