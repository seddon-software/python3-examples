import os
import subprocess
gnuplotApp = "/Applications/Gnuplot.app/Contents/MacOS/Gnuplot.app"
p = subprocess.Popen(gnuplotApp + " 01-data-plot.py", shell = True)
os.waitpid(p.pid, 0)
