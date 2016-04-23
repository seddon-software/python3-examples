import py_compile, os

# py_compile.compile("myfile.py", "myfile.pyc")
py_compile.compile("myfile.py")
os.system("ls myfile.*")
1
