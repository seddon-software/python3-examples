import subprocess, os

# parser.add_argument("-v", "--verbose", action="store_true")


subprocess.call("python 03_optional_args.py 123 456".split())
print "-------------------------------------------"
subprocess.call("python 03_optional_args.py".split())
print "-------------------------------------------"
subprocess.call("python 03_optional_args.py -v".split())
print "-------------------------------------------"
subprocess.call("python 03_optional_args.py --verbose".split())
print "-------------------------------------------"

