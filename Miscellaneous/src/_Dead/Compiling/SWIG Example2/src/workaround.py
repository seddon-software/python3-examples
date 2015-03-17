# Force g++ for linking
import distutils.sysconfig
old_customize_compiler = distutils.sysconfig.customize_compiler
def customize_compiler(compiler):
    print "************* using workaround.py to force g++"
    old_customize_compiler(compiler)
    if compiler.compiler_type == 'mingw32':
        compiler.set_executables(compiler='g++ -O Wall')
        compiler.set_executables(compiler_so='g++ -mdll -O -Wall')
        compiler.set_executables(linker_so='gcc -shared')
        compiler.set_executables(linker_exe='g++')
        compiler.set_executables(compiler_cxx='g++ -O -Wall')
        compiler.dll_libraries = []
distutils.sysconfig.customize_compiler = customize_compiler
