#!/bin/bash

INPUT_DIR="."
OUTPUT_DIR="_temp/html"

MIG_DIR="./_migrated"
BUILD_DIR="redot-docs-build"
BRANCH_DIR="$/en/master"

touch test.txt 
echo 'hello' >> test.txt 
mkdir -p $OUTPUT_DIR
cp test.txt $OUTPUT_DIR
cp test.txt $OUTPUT_DIR/index.html 

python migrate.py --tiny $INPUT_DIR $MIG_DIR
sphinx-build -b html -j 4 $MIG_DIR $OUTPUT_DIR

git clone git@github.com:Redot-Engine/$BUILD_DIR.git

echo "mkdir -p $BUILD_DIR$BRANCH_DIR"
mkdir -p $BUILD_DIR$BRANCH_DIR
echo "cp -r $MIG_DIR/* $BUILD_DIR$BRANCH_DIR"
cp -r $MIG_DIR/* $BUILD_DIR$BRANCH_DIR

cd $BUILD_DIR
ls -la
git push -f
