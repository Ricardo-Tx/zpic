# run the original python compilation program

from subprocess import run

run("cd python/source && python3 setup.py build_ext --build-lib=\"../lib\"", shell=True)


# Copy contents of python/lib/ after compilation.
# We could change the python/source/Makefile BUILD_LIB library but we'd rather not 
# alter the current compilation process, rather append to it.
# We could also change the Makefile to add a copy command but that would not be platform agnostic
# Also, python/lib/ contains .py files which should also be present in the wheel 

from distutils.dir_util import copy_tree

copy_tree("python/lib", "src/zpic")