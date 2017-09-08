#!/bin/sh

for i in {1..200}
do
    git checkout -b $i
    echo $1 >> README.txt
    git commit -am "Update README $i"
    git checkout master
    echo $i
done
