import sys
from distutils.core import setup, Extension

# force setup to use g++ instead of gcc
import my_windows_gcc_fix

# normal setup code
example_module = Extension('_myexample',
                           language='c++',
                           swig_opts=['-c++'],
                           sources=['myexample.i', 'hello.cpp'],
                           )

setup (
       name = 'CPP SWIG example',
       version = '1.0',
       author = "CRS Enterprises Ltd",
       author_email='seddon-software@keme.co.uk',
       maintainer = "CRS Enterprises Ltd",
       maintainer_email ='seddon-software@keme.co.uk',
       url='http://www.keme.co.uk/~seddon-software',
       description = "CPP SWIG example",
       long_description = """This is a SWIG example that defines
            two C++ functions and uses the STL""",
       download_url = "local",
       classifiers = ["Developers", "Python Programming Course"],
       platforms = sys.platform,
       license = "none",
       ext_modules = [example_module],
       py_modules = ["myexample"],
       )
