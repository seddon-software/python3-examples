import subprocess, os

subprocess.call("python 06_advanced_example.py 3 5 7 9 11".split())
print "-------------------------------------------"
subprocess.call("python 06_advanced_example.py --log logfile.txt 3 5 7 9 11".split())
