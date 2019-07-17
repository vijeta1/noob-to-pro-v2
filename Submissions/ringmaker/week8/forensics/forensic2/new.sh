#!/bin/sh

for i in {1..40};do
unzip flag.zip
bzip2 -d flag.zip.gz.bz2
gzip -d flag.zip.gz
done
