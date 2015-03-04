import os

os.chdir("..")
print "Adding ..."
print os.getcwd()
print "... to PATH"
os.environ["PATH"] = os.getcwd() + ";" + os.environ["PATH"]



