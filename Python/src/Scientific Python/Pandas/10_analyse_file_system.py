import os, pylab

def summarize_files(topdir):
    filedata = []
    for path, dirs, files in os.walk(topdir):
        for name in files:
            fullname = os.path.join(path,name)
            if os.path.exists(fullname):
                data = {
                'path'     : path,
                'filename' : name,
                'size'     : os.path.getsize(fullname),
                'ext'      : os.path.splitext(name)[1],
                'mtime'    : os.path.getmtime(fullname)
            }
            filedata.append(data)
    return filedata

import pandas
filedata = pandas.DataFrame(summarize_files("/Users/seddon/home/workspace"))
print "Top 5 most common file extensions:"
print filedata['ext'].value_counts()[:5]
pyfiles = filedata[filedata['ext'] == '.py']
print
print "Biggest file size = {} bytes".format(pyfiles['size'].max())
print "Average file size = {:.1f} bytes".format(pyfiles['size'].mean())
print "Standard deviation = {:.1f} bytes".format(pyfiles['size'].std())

# create a histogram and plot it
pyfiles['size'].hist(bins=30)
pylab.show()
