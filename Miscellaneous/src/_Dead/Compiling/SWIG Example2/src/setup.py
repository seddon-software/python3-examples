from distutils.core import setup, Extension



import workaround       # force setup to use g++ instead of gcc

example_module = Extension('_example',
                           language='c++',
                           swig_opts=['-c++'],
                           sources=['hello.i'],
                           )

setup (name = 'SWIG example',
       version = '1.0',
       author      = "CRS Enterprises Ltd",
       description = """Simple SWIG example""",
       ext_modules = [example_module],
       py_modules = ["example.py"],
       )
