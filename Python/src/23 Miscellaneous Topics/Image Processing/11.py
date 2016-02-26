import os, sys
from PIL import Image


os.chdir("images")
infile = "llns.jpg"

outfile = os.path.splitext(infile)[0] + ".cropped.jpg"
try:
    img = Image.open(infile)
    box = (0, 0, 800, 600)
    box = (40, 60, 760, 250)
    img = img.crop(box)
    img.show()
    img.save(outfile, "JPEG")
except IOError, e:
    print e
