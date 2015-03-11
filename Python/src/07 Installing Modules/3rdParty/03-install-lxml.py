import subprocess,os,sys
import set_path
# import set_proxy
    
def install(cmd):
    cmd = (installer + " " + cmd)
    print "****", cmd
    subprocess.call(cmd.split())
    
# on MACOS we need to do a static build, so set the STATIC_DEPS environment variable to true (see above)
subprocess.call("pip install lxml".split())

1



