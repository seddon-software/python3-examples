# inspecting source files

import os

# select a package by name
# package = "string"
package = "timeit"

# load package dynamically
p = __import__(package)

compiledFileName = p.__file__
sourceFileName = compiledFileName[:-1]
os.system("cat " + sourceFileName)

print
print "compiled file:", compiledFileName
print "source file:", sourceFileName

