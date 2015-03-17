import subprocess,os,sys


os.chdir("../server")
subprocess.call("python -m SimpleHTTPServer 8000".split())

