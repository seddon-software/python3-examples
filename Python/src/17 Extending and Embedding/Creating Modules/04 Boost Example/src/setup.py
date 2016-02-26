import sys
from distutils.core import setup, Extension

 
mymodule = Extension('greeting',
        include_dirs = ['/Users/seddon/work/boost_1_57_0'],
        libraries = ['boost_python'],
        library_dirs = ['/Users/seddon/work/boost_1_57_0/stage/lib'],
#         library_dirs = ['/Users/seddon/work/boost_1_57_0/stage/lib/static'],
        sources = ['greeting.cpp'])

setup (name = 'GreetingPackage',
        version = '1.0',
        author = "CRS Enterprises Ltd",
        author_email='seddon-software@keme.co.uk',
        maintainer = "CRS Enterprises Ltd",
        maintainer_email ='seddon-software@keme.co.uk',
        url='http://www.keme.co.uk/~seddon-software',
        description = "simple example",
        long_description = """This is a simple example,
            to wrap up a C module""",
        download_url = "local",
        classifiers = ["Developers", "Python Programming Course"],
        platforms = sys.platform,
        license = "none",
        ext_modules = [mymodule])


# module1 = Extension('demo',
#                     define_macros = [('MAJOR_VERSION', '1'),
#                                      ('MINOR_VERSION', '0')],
#                     include_dirs = ['/usr/local/include'],
#                     libraries = ['tcl83'],
#                     library_dirs = ['/usr/local/lib'],
#                     sources = ['demo.c'])