#!/bin/bash
cnt=0
while [ $cnt -lt 1 ]
do
    echo "Tracking "
    taskset -c 0,12 ./monitering_1
    taskset -c 0,12 ./monitering_2
    #taskset -c 1,13 ./monitering_1
    #taskset -c 1,13 ./monitering_2
    #taskset -c 2,14 ./monitering_1
    #taskset -c 2,14 ./monitering_2
    #taskset -c 3,15 ./monitering_1
    #taskset -c 3,15 ./monitering_2
    #taskset -c 4,16 ./monitering_1
    #taskset -c 4,16 ./monitering_2
    #taskset -c 5,17 ./monitering_1
    #taskset -c 5,17 ./monitering_2
    #taskset -c 6,18 ./monitering_1
    #taskset -c 6,18 ./monitering_2
    #taskset -c 7,19 ./monitering_1
    #taskset -c 7,19 ./monitering_2
    #taskset -c 8,20 ./monitering_1
    #taskset -c 8,20 ./monitering_2
    #taskset -c 9,21 ./monitering_1
    #taskset -c 9,21 ./monitering_2
    #taskset -c 10,22 ./monitering_1
    #taskset -c 10,22 ./monitering_2
    #taskset -c 11,23 ./monitering_1
    #taskset -c 11,23 ./monitering_2
    ((cnt++))
done
