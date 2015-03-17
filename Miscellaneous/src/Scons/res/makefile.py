#SConstruct
import platform
import os

# get list of source and exe files
source = Glob('*.cpp')
source_files = []
exe_files = []

for entry in source:
    source_files.append(entry.name)
    exe_files.append(entry.name.replace('.cpp', '.exe'))
    
# check if we need to change toolchains
if platform.system() == 'Windows':
    env = Environment(tools = ['mingw'], ENV = os.environ)
else:
    env = Environment(ENV = os.environ)

# build multiple targets based on source name
for (src, exe) in zip(source_files, exe_files):
    env.Program(source=src, target=exe)

# psuedo target
Command('run_all_programs', None, exe_files)

  