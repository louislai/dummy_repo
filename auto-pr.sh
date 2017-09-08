#!/bin/sh

for i in {1..200}
do
    hub pull-request "PR $i" -b louislai:master -h louislai:$i -m "PR $i"
done
