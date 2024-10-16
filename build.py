"""
## Build script
"""

import argparse
import os
from shutil import copyfile
import shutil
from distutils.dir_util import copy_tree
import subprocess



def printDir(inputDirectory):
    for root, dirs, files in os.walk(inputDirectory):
        print(f"root found: {root}")
    pass

def build():
    parser = argparse.ArgumentParser(
                    prog='Build',
                    description='Builds the project.',
                    epilog='Done. Made by @Craptain')
    
    parser.add_argument('input', help='Input directory relative to current')
    parser.add_argument('output', help='Output directory relative to current')
    parser.add_argument('-v', '--verbose', action='store_true') 

    args = parser.parse_args()
    verbose = args.verbose
    if (verbose):
        print("arguments:")
        print(args)

    inputDir = args.input
    if (args.output != '.' and not args.output.startswith('/')):
        outputDir = args.output
    else:
        print("output can't be . or start with /")
        exit(1)

    if (os.path.exists(outputDir)):
        print(f"Deleting {outputDir}")
        shutil.rmtree(outputDir)
    
    print("Building...")

    printDir(inputDir)

    print("trying os.system")
    os.system("ls -la")

    print("trying subprocess.run")
    subprocess.run(["touch", "test.txt"]) 
    subprocess.run(["echo", "hello >> test.txt"]) 
    subprocess.run(["mkdir", "_build"]) 
    subprocess.run(["cp", "test.txt _build"]) 

    print("Printing dir again")
    printDir(inputDir)

    print(parser.epilog)

if __name__ == "__main__":
    build()
