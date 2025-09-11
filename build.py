from subprocess import run
from distutils.dir_util import copy_tree
from os import name
from pathlib import Path

# compilation options
PYTHON = 'python3'
ARGS = "--build-lib=\"../lib\""

if name == 'nt':
    PYTHON = 'python'
    ARGS += " --compiler=mingw32"


cwd = Path.cwd()

# run the original python compilation program
run(f"cd {cwd / 'python' / 'source'} && {PYTHON} setup.py build_ext {ARGS}", shell=True)
run(f"cd {cwd / 'contrib' / 'python' / 'source'} && {PYTHON} setup.py build_ext {ARGS}", shell=True)

# Copy contents of python/lib/ after compilation.
# We could change the python/source/Makefile BUILD_LIB library but we'd rather not 
# alter the current compilation process, rather append to it.
# We could also change the Makefile to add a copy command but that would not be platform agnostic
# Also, python/lib/ contains .py files which should also be present in the wheel 
copy_tree(
    str(cwd / 'python' / 'lib'), 
    str(cwd / 'src' / 'zpic')
)
copy_tree(
    str(cwd / 'contrib' / 'python' / 'lib'), 
    str(cwd / 'src' / 'zpic' / 'contrib')
)
