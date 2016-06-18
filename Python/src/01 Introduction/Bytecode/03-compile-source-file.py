import py_compile, os

py_compile.compile("myfile.py")
os.system("ls myfile.*")

