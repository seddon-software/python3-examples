import zipfile, os

outDirectory = "files/Perl"
if not os.path.exists(outDirectory): os.mkdir(outDirectory)
os.chdir(outDirectory)

zipfile.ZipFile("../../zips/Perl.zip", "r").extractall()


