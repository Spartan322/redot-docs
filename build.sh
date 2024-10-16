#!/bin/bash

inputDir = $1
outputDir = $2

migdir = "./_migrated"

touch test.txt 
echo 'hello' >> test.txt 
mkdir -p $outputDir
cp test.txt $outputDir
cp test.txt $outputDir/index.html 

python migrate.py --tiny . $migdir
sphinx-build -b html -j 4 $migdir $outputDir
