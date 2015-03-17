import argparse
from argparse import Namespace

# This example shows how to supply optional arguements (e.g. -v or --verbose)
# The store_true option automatically creates a default value of False

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

print args.__dict__
if args.verbose:
    print "This example examines optional arguments"
else:
    print "optional args"
