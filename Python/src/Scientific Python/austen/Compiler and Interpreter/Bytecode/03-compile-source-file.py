import py_compile, os

py_compile.compile("myfile.py")
os.system("ls")
os.system("hexdump -c myfile.pyc")
1
