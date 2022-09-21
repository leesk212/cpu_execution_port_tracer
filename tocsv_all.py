import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

temp_array = np.empty((0,10000),int)

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
    times.append(time) 
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


temp_array = np.append(temp_array,np.array([uop_0]),axis=0)
temp_array = np.append(temp_array,np.array([uop_1]),axis=0)
temp_array = np.append(temp_array,np.array([uop_2]),axis=0)
temp_array = np.append(temp_array,np.array([uop_3]),axis=0)
temp_array = np.append(temp_array,np.array([uop_4]),axis=0)
temp_array = np.append(temp_array,np.array([uop_5]),axis=0)
temp_array = np.append(temp_array,np.array([uop_6]),axis=0)
temp_array = np.append(temp_array,np.array([uop_7]),axis=0)

temp_array =temp_array.T
print(temp_array.shape)

df = pd.DataFrame(temp_array)
df.to_csv(sys.argv[1]+'.csv')


