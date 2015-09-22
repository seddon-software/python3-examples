import subprocess,os,sys
sys.path.append('../..')
import set_paths

os.chdir("../src")
os.system("python setup.py build_ext --inplace")
