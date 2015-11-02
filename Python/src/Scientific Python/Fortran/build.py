import subprocess, os
import distutils.sysconfig
srcFile = "fortran_code.f90"

# determine path to f2py
lib = distutils.sysconfig.get_python_lib()
f2py = lib + "/../../../bin/f2py"
f2py = os.path.abspath(f2py)

# modify PATH for gfortran
os.environ['PATH'] = '/usr/local/bin:' + os.environ['PATH']

# execute command to generate shared object from Fortran file
cmd = f2py + " -c -m fortran_lib " + srcFile
subprocess.call(cmd.split())

# run python code that calls Fortran
subprocess.call("python call-fortran-function.py".split())
