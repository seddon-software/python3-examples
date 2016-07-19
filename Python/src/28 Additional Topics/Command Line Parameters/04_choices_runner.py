import subprocess, os


subprocess.call("python 04_choices.py eggs".split())
print "-------------------------------------------"
subprocess.call("python 04_choices.py spam eggs ham".split())
print "-------------------------------------------"
subprocess.call("python 04_choices.py bacon spam eggs".split())
print "-------------------------------------------"

