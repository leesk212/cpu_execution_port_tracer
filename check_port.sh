#!/bin/bash

number=0

echo "MSR Driver loading"
sudo ./Driver_linux/install.sh


echo "Detection Start"

while [ ${number} -le 600 ]
do 
    ./pmc_test2 > ./tmp/tmp_log_${number}.txt
    sleep 0.005
    ((number++))
done

echo "Detection Finish"
echo "Print Plot"
python trace.py
