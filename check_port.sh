#!/bin/bash

StartTime=$(date +%s)
number=0

echo "MSR Driver loading"
sudo ./Driver_linux/install.sh > log.txt


echo "Detection Start"

while [ ${number} -le 1000 ]
do	
    ./pmc_test2 > ./tmp/tmp_log_${number}.txt
    sleep 0.01
    ((number++))
    
    time=$(date +%s)
    echo "Elapsed_Time: $(($time - $StartTime))" 
done

echo "Detection Finish"
echo "Print Plot"
python trace.py
