import os, sys

def setPath():
    
    # Changing the PATH to locate Gnuplot
#    if sys.platform == 'darwin': gnuplotBinaries = "/usr/local/bin/"
    if sys.platform == 'darwin': gnuplotBinaries = "/Applications/Gnuplot.app/Contents/MacOS"
#    if sys.platform == 'darwin': gnuplotBinaries = "/Library/Frameworks/GTK+.framework/Resources/bin/"
    if sys.platform == 'win32':  gnuplotBinaries = "G:/Workspace/Python/Python/src/Plotting/gnuplot/scripts/gnuplot/binary"
    if sys.platform == 'linux2': gnuplotBinaries = ""

    # Changing the PATH to locate gnuplot
    os.environ["PATH"] = gnuplotBinaries + ":" + os.environ["PATH"]
    print os.environ["PATH"]

setPath()


