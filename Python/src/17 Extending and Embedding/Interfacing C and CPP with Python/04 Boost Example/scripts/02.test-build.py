import sys, os, re

def modifyPythonPathWithStage():
    base = "../src/build/"
    # search for directory begining with 'lib'
    for root, dirs, files in os.walk(base):
        for dir in dirs:
            if re.search(r"^lib", dir) != None: 
                stage = dir
    try:
        sys.path.append(base + stage)
    except:
        print "must build application first"
        sys.exit()
        
            
modifyPythonPathWithStage()            

import greeting
print greeting.greet()
print greeting.average(5.0, 6.0)

