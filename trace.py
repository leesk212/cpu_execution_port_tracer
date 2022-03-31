import matplotlib.pyplot as plt

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

legend = []
init_flag = 0

# FIle open through 10s
for time in range(0, 10000):
    #print(time)
    FILE_NAME = './tmp1/tmp_log_' + str(time) + '.txt'
    fd = open(FILE_NAME)
    lines = fd.readlines()
    times.append(time)

    for core, line in enumerate(lines):
        if core == 1 and init_flag == 0: # column
            # Take port_name legend 
            line = line.strip().split(' ')

            column = []
            for each in line:
                if len(each) > 0:
                    column.append(each)
            column = column[1:]

            port_name = []
            for index, each in enumerate(column):
                if index % 2 == 1:
                    port_name.append(each)
            for _ in port_name:
                legend_ = 'port_'+_
                legend.append(legend_)
                print(legend_)
            init_flag += 1

        if core > 1:  # Erase first \n and column
            line = line.strip().split(' ')  # Erase \n on end of string
            cycle = []
            for each in line:
                if len(each) > 0:
                    cycle.append(each)
            cycle = cycle[1:]
            for index in range(4):
                uops[index].append(cycle[index])
init_flag = 0

# FIle open through 10s
for time in range(0, 10000):
    #print(time)
    FILE_NAME = './tmp2/tmp_log_' + str(time) + '.txt'
    fd = open(FILE_NAME)
    lines = fd.readlines()

    for core, line in enumerate(lines):
        if core == 1 and init_flag == 0: # column
            # Take port_name legend
            line = line.strip().split(' ')

            column = []
            for each in line:
                if len(each) > 0:
                    column.append(each)
            column = column[1:]

            port_name = []
            for index, each in enumerate(column):
                if index % 2 == 1:
                    port_name.append(each)
            for _ in port_name:
                legend_ = 'port_'+_
                legend.append(legend_)
                print(legend_)
            init_flag += 1

        if core > 1:  # Erase first \n and column
            line = line.strip().split(' ')  # Erase \n on end of string
            cycle = []
            for each in line:
                if len(each) > 0:
                    cycle.append(each)
            cycle = cycle[1:]
            for index in range(4,8):
                uops[index].append(cycle[index-4])

print("|||||||||||||||||||||||before|||||||||||||||||||||||")

# Distribution by CPU core
for core in range(8):
    port0 = []
    port1 = []
    port2 = []
    port3 = []
    port4 = []
    port5 = []
    port6 = []
    port7 = []
    ports = [ port0,port1,port2,port3,port4,port5,port6,port7 ]

    for index, uop in enumerate(uops):
        for index_2, each in enumerate(uop):
            if index_2 % 8 == core:
                ports[index].append(int(each))
    
    for i in range(8):
        plt.plot(times, ports[i], label=legend[i])
    
    plt.title('Core '+str(core))
    plt.legend()
    plt.savefig('./result_png/trace_result_core_'+str(core))
    plt.show()
