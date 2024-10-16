#!/bin/bash

INPUT_DIR=$1
OUTPUT_DIR=$2

MIG_DIR="./_migrated"

touch test.txt 
echo 'hello' >> test.txt 
mkdir -p $OUTPUT_DIR
cp test.txt $OUTPUT_DIR
cp test.txt $OUTPUT_DIR/index.html 

python migrate.py --tiny $INPUT_DIR $MIG_DIR
sphinx-build -b html -j 4 $MIG_DIR $OUTPUT_DIR

# do we have node?
node --version

# do we have git?
git --version

