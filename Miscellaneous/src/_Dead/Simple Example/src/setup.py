from distutils.core import setup, Extension
 
module1 = Extension('hello', sources = ['hellomodule.c'])
 
setup (name = 'SimpleExample',
        version = '1.0',
        description = 'This is a demo package',
        ext_modules = [module1])
