import subprocess, mypackage, mypackage.mystuff

# display help on user defined modules
subprocess.call("python -m pydoc mypackage".split())
subprocess.call("python -m pydoc mypackage.mystuff".split())
