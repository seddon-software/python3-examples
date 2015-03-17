import subprocess, os

subprocess.call("python 02_positional_args.py 123 456".split())
print "-------------------------------------------"
subprocess.call("python 02_positional_args.py 123 456 789".split())
print "-------------------------------------------"
subprocess.call("python 02_positional_args.py --help".split())

