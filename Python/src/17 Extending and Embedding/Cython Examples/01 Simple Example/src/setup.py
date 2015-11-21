import sys
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize


name = 'MyCython_Package'
version = '2.0'

extensions = [
    Extension("*", ["*.pyx"], extra_compile_args=["-w"])
]
setup(
    name = name,
    version = version,
    author = "CRS Enterprises Ltd",
    author_email='seddon-software@keme.co.uk',
    maintainer = "CRS Enterprises Ltd",
    maintainer_email ='seddon-software@keme.co.uk',
    url='http://www.keme.co.uk/~seddon-software',
    description = "Cython hello world example",
    long_description = """This is a simple example,
        to use Cython""",
    download_url = "local",
    classifiers = ["Developers", "Python Programming Course"],
    platforms = sys.platform,
    license = "none",
    ext_modules = cythonize(extensions)
)

print "setup is creating an egg info file called:"
print "\t{}-{}-py2.7.egg-info".format(name, version)
# import sys
# from distutils.core import setup, Extension
# from Cython.Build import cythonize
# 
# setup (
#         name = 'HelloWorld Package',
#         version = '1.0',
#         author = "CRS Enterprises Ltd",
#         author_email='seddon-software@keme.co.uk',
#         maintainer = "CRS Enterprises Ltd",
#         maintainer_email ='seddon-software@keme.co.uk',
#         url='http://www.keme.co.uk/~seddon-software',
#         description = "Cython hello world example",
#         long_description = """This is a simple example,
#             to use Cython""",
#         download_url = "local",
#         classifiers = ["Developers", "Python Programming Course"],
#         platforms = sys.platform,
#         license = "none",
#         ext_modules = cythonize("hello.pyx")
#         )
