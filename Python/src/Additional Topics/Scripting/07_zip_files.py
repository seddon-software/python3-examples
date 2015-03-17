############################################################
#
#    zip files
#
############################################################

import os
os.chdir("zipfiles")


import zipfile
zipfile.ZipFile("gp444win32.zip", "r").extractall()


import shutil
shutil.rmtree("gnuplot")
