import pip

moduleName = "mymodule-1.0.zip"

cmd = "install http://localhost:8000/repo/" + moduleName
print "pip {0}".format(cmd)
pip.main(cmd.split())
pip.main("show mymodule".split())

