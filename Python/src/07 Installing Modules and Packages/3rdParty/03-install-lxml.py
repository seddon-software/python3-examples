import subprocess,sys
# import set_proxy
    

# on MACOS we need to do a static build, so set the STATIC_DEPS environment variable to true (see above)
if sys.platform == "darwin":    # OSX 10.8
    subprocess.call("STATIC_DEPS=true sudo pip install lxml".split())
else:
    subprocess.call("pip install lxml".split())
    

1



