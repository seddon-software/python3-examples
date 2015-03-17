# Force g++ for linking
import distutils.sysconfig
old_customize_compiler = distutils.sysconfig.customize_compiler
def customize_compiler(compiler):
    print "************* using workaround.py to force g++"
    old_customize_compiler(compiler)
    if compiler.compiler_type == 'mingw32':
        compiler.set_executables(compiler='g++ -std=c++11  -O Wall')
        compiler.set_executables(compiler_so='g++ -std=c++11 -mdll -O -Wall')
        compiler.set_executables(linker_so='g++ -std=c++11 -shared')
        compiler.set_executables(linker_exe='g++ -std=c++11')
        compiler.set_executables(compiler_cxx='g++ -std=c++11 -O -Wall')
        compiler.dll_libraries = []
distutils.sysconfig.customize_compiler = customize_compiler
