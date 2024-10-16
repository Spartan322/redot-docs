"""
## Build script
"""

import argparse
import os
from shutil import copyfile
import shutil
from distutils.dir_util import copy_tree
import subprocess


def run_command(command):
    print(f"Running command {command}")
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    (output, err) = p.communicate()

    #print(output)
    #This makes the wait possible
    p_status = p.wait()

    #This will give you the output of the command being executed
    print(f"Command output: {output}")

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

    print("trying os.system")
    os.system("ls -la")

    print("trying touch")
    os.system("touch test.txt") 
    print("trying echo")
    os.system("echo 'hello' >> test.txt") 
    print("trying mkdir")
    os.system(f"mkdir -p {outputDir}") 
    print("trying cp")
    os.system(f"cp test.txt {outputDir}")
    print("trying cp")
    os.system(f"cp test.txt {outputDir}/index.html") 

    migdir = "_migrated"
    run_command(f"python migrate.py --tiny . {migdir}")

    #This command could have multiple commands separated by a new line \n
    run_command(f"sphinx-build -b html -j 4 {migdir} {outputDir}")

    print(parser.epilog)

if __name__ == "__main__":
    build()
