#!/bin/bash
cnt=0
prompt=3000
while [ $cnt -lt $1 ]
do
	./concat.sh > ./monitering_result/$cnt.txt
	
	((cnt++))

	if [ "$cnt" -eq "$prompt" ];
	then
		echo "crpytojacking start"
	fi	
done
