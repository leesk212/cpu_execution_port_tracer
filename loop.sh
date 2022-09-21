#!/bin/bash
cnt=0
while [ $cnt -lt $1 ]
do
	./concat.sh > ./monitering_result/$cnt.txt
	((cnt++))
done
