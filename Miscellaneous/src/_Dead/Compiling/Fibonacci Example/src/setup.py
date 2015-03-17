from distutils.core import setup, Extension


# Force g++ for linking
import distutils.sysconfig
old_customize_compiler = distutils.sysconfig.customize_compiler
def customize_compiler(compiler):
    print "************* Customize"
    old_customize_compiler(compiler)
    if compiler.compiler_type == 'mingw32':
        compiler.set_executables(compiler='g++ -std=c++11 -O Wall')
        compiler.set_executables(compiler_so='g++ -mdll -std=c++11 -O -Wall')
        compiler.set_executables(linker_so='g++ -shared')
        compiler.set_executables(linker_exe='g++')
        compiler.set_executables(compiler_cxx='g++ -O -Wall')
        compiler.dll_libraries = []
distutils.sysconfig.customize_compiler = customize_compiler

 
mymodule = Extension('fib', sources = ['fibmodule.cpp'])
 
setup (name = 'FibonacciPackage',
        version = '1.0',
        description = 'This is a demo package',
        ext_modules = [mymodule])
