"""
## Build script
"""

import argparse
import fnmatch
import os
import re
from shutil import copyfile
import shutil
import sys
import codecs
from distutils.dir_util import copy_tree



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
    includeUnimplemented = args.extended
    ignoreClasses = args.tiny

    if (os.path.exists(outputDir)):
        print(f"Deleting {outputDir}")
        shutil.rmtree(outputDir)
    
    print("Building...")

    printDir(parser.input);

    print(parser.epilog)

if __name__ == "__main__":
    build()
