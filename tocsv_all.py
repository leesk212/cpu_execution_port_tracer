import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

temp_array = np.empty((0,10000),int)

core_0 = [[],[],[],[],[],[],[],[]]
core_1 = [[],[],[],[],[],[],[],[]]
core_2 = [[],[],[],[],[],[],[],[]]
core_3 = [[],[],[],[],[],[],[],[]]
core_4 = [[],[],[],[],[],[],[],[]]
core_5 = [[],[],[],[],[],[],[],[]]
core_6 = [[],[],[],[],[],[],[],[]]
core_7 = [[],[],[],[],[],[],[],[]]
core_8 = [[],[],[],[],[],[],[],[]]
core_9 = [[],[],[],[],[],[],[],[]]
core_10 = [[],[],[],[],[],[],[],[]]
core_11 = [[],[],[],[],[],[],[],[]]
cores = [core_0,core_1,core_2,core_3,core_4,core_5,core_6,core_7,core_8,core_9,core_10,core_11]

for time in range(0,10000):
    #times.append(time) 
    FILE_NAME = '/home/csl/Desktop/test_cpu_execution_port_tracer/cpu_execution_port_tracer/monitering_result/'+str(time)+'.txt'
    fd = open(FILE_NAME)
    lines = fd.readlines()

    for i,line in enumerate(lines):
        if i > 0:
            Datas = line.strip().split(" ")

            Data = []
            for data in Datas:
                if len(data) > 0:
                    Data.append(int(data))
            #Data is values of each execution port of each core
            for j in range(8):
                cores[i-1][j].append(Data[j])
#print(cores)
# tocsv_all (list to numpy)
for i,core_index in enumerate(range(len(cores))):
    print(str(i))
    for uop_index in range(8):
        print('before',end=' ')
        print(len(cores[core_index][uop_index]))
        if len(cores[core_index][uop_index]) <  10000:
            lack = 10000 - len(cores[core_index][uop_index])
            print(lack)
            for i in range(lack):
                cores[core_index][uop_index].append(cores[core_index][uop_index][10000-lack-1])
        print('after',end=' ')
        print(len(cores[core_index][uop_index]))
        temp_array = np.append(temp_array,np.array([cores[core_index][uop_index]]),axis=0)

temp_array =temp_array.T
print(temp_array.shape)

col = []
for k in range(12):
    for p in range(8):
        col.append('core_'+str(k)+'_port_'+str(p))

df = pd.DataFrame(temp_array,columns=col)
df.to_csv(sys.argv[1]+'.csv')
