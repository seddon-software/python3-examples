import subprocess,os

os.chdir("stage")
subprocess.call("python setup.py install".split())
