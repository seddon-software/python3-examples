import tarfile


# It's worth mentioning that you can get better compression when you tar and then compress than if you were to compress each file individually
fileName = "Perl.tar.gz"

tar = tarfile.open(fileName, "w:gz")
# tar.add("zips/Perl", arcname=fileName)
tar.add(".", arcname=fileName)
tar.close()