#!/bin/bash

number=0

echo "MSR Driver loading"
sudo ./Driver_linux/install.sh > log.txt

echo "Trace Execution port"

echo "Detection Start"

while [ ${number} -le 10000 ]
do	
    ./pmc_test-1 > ./tmp1/tmp_log_${number}.txt
    ./pmc_test-2 > ./tmp2/tmp_log_${number}.txt
    ((number++))
done

echo "Detection Finish"
echo "Print Plot"
taskset -c 15 python trace.py
