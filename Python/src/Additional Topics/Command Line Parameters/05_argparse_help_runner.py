import subprocess, os

subprocess.call("python 05_argparse_help.py --help".split())
print "-------------------------------------------"
subprocess.call("python 05_argparse_help.py -h".split())
