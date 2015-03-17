from distutils.core import setup, Extension
from distutils.ccompiler import new_compiler
from mycompiler import *
    
# import workaround       # force setup to use g++ instead of gcc
#new_compiler(plat=None, compiler=MyCompiler(), verbose=0, dry_run=0, force=0)

MyCompiler().set_new_compiler()


example_module = Extension('_myexample',
                           language='c++',
                           swig_opts=['-c++'],
                           sources=['myexample.i', 'hello.cpp'],
                           )

setup (name = 'CPP SWIG example',
       version = '1.0',
       author      = "CRS Enterprises Ltd",
       description = """This is
a SWIG example that defines two C++ functions and
uses the STL""",
       ext_modules = [example_module],
       py_modules = ["myexample"],
       )
