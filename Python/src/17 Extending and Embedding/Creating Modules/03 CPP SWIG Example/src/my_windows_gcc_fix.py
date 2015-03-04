import distutils.sysconfig

class MyCompiler:

    # you call this to hook into the framework
    def set_overrides(self):
        # hook into current compiler
        self.hook_to_compiler = distutils.sysconfig.customize_compiler
        # reset to our compiler
        distutils.sysconfig.customize_compiler = self.customize_compiler

    # this will be called by the framework (distutils)
    def customize_compiler(self, compiler):
        # call the MinGW compiler first to set all default options
        self.hook_to_compiler(compiler)

        # now override required options        
        compiler.set_executables(compiler='g++ -O Wall')
        compiler.set_executables(compiler_so='g++ -mdll -O -Wall')
        compiler.set_executables(linker_so='g++ -shared')
        compiler.set_executables(linker_exe='g++')
        compiler.set_executables(compiler_cxx='g++ -O -Wall')
        compiler.dll_libraries = []
        
import platform
if platform.system() == "Windows":  
    MyCompiler().set_overrides()



