#!/bin/bash

number=0
flag=$1

echo "MSR Driver loading"
sudo ./Driver_linux/install.sh > log.txt

echo "Trace Execution port"

if [ ${flag} -eq 1 ]
then
	echo "Execution 0,1,2,3 port" 
	./pmc_test2 startcounters 150 151 152 153
elif [ ${flag} -eq 2 ]
then
	echo "Execution 4,5,6,7 port"
	./pmc_test2 startcounters 154 155 156 157
fi

echo "Detection Start"

while [ ${number} -le 6000 ]
do	
    ./pmc_test2 > ./tmp/tmp_log_${number}.txt
    sleep 0.01
    ((number++))
    
    #time=$(date +%s)
    #echo "Elapsed_Time: $(($time - $StartTime))" 
done

echo "Detection Finish"
echo "Print Plot"
python trace.py
