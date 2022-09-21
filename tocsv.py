import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

times = []

uop_0 = []
uop_1 = []
uop_2 = []
uop_3 = []
uop_4 = []
uop_5 = []
uop_6 = []
uop_7 = []

uops = [uop_0, uop_1, uop_2, uop_3,uop_4,uop_5,uop_6,uop_7]

for time in range(0,10000):
    times.append(str(time)) 
    FILE_NAME = '/home/csl/Desktop/test_cpu_execution_port_tracer/cpu_execution_port_tracer/monitering_result/'+str(time)+'.txt'
    fd = open(FILE_NAME)
    lines = fd.readlines()

    Datas = lines[1].strip().split(" ")
    Data = []
    for data in Datas:
        if len(data) > 0:
            Data.append(data)
    print(Data)
    #exit() 
    uop_0.append(int(Data[0]))
    uop_1.append(int(Data[1]))
    uop_2.append(int(Data[2]))
    uop_3.append(int(Data[3]))
    uop_4.append(int(Data[4]))
    uop_5.append(int(Data[5]))
    uop_6.append(int(Data[6]))
    uop_7.append(int(Data[7]))

for each_ops in uops:
    print(each_ops)


plt.title('Core 0')
plt.plot(times,uop_0,label='uop_0')
plt.plot(times,uop_1,label='uop_1')
plt.plot(times,uop_2,label='uop_2')
plt.plot(times,uop_3,label='uop_3')
plt.plot(times,uop_4,label='uop_4')
plt.plot(times,uop_5,label='uop_5')
plt.plot(times,uop_6,label='uop_6')
plt.plot(times,uop_7,label='uop_7')
plt.legend()
plt.grid()
plt.show() 


