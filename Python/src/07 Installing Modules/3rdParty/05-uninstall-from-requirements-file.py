import subprocess,os,sys
import set_path
# import set_proxy

    
def install(cmd):
    cmd = (installer + " " + cmd)
    print "****", cmd
    subprocess.call(cmd.split())
    
subprocess.call("pip uninstall -r requirements.txt".split())

1



