import subprocess,os,sys

sys.path.append('../..')
import set_paths
os.chdir("../src")

# must run build first
subprocess.call("python setup.py install".split())
