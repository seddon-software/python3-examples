import os, sys
from PIL import Image


os.chdir("images")
infile = "DSCF0437.JPG"
outfile = os.path.splitext(infile)[0] + ".flipped.jpg"
try:
    img = Image.open(infile)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.show()
except IOError, e:
    print e
    