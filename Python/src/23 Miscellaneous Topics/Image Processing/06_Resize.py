import os, sys
import Image


os.chdir("images")
infile = "DSCN0639.JPG"


outfile = os.path.splitext(infile)[0] + ".resize.jpg"
try:
    img = Image.open(infile)
    img = img.resize((500, 500))
    img.show()
    img.save(outfile, "JPEG")
except IOError, e:
    print e
