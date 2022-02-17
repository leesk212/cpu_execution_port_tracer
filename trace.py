import matplotlib.pyplot as plt

times = []
uop_0 = []
uop_1 = []
uop_2 = []
uop_3 = []

uops = [uop_0, uop_1, uop_2, uop_3]

legend = []
init_flag = 0

# FIle open through 10s
for time in range(0, 6000):
    #print(time)
    FILE_NAME = './tmp/tmp_log_' + str(time) + '.txt'
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
                legend_ = 'uop_'+_
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

# Distribution by CPU core
for core in range(8):
    port0 = []
    port1 = []
    port2 = []
    port3 = []
    ports = [ port0,port1,port2,port3 ]

    for index, uop in enumerate(uops):
        for index_2, each in enumerate(uop):
            if index_2 % 8 == core:
                ports[index].append(int(each))

    plt.plot(times, port0, label=legend[0])
    plt.plot(times, port1, label=legend[1])
    plt.plot(times, port2, label=legend[2])
    plt.plot(times, port3, label=legend[3])
    plt.title('Core '+str(core))
    plt.legend()
    plt.savefig('./result_png/trace_result_core_'+str(core))
    plt.show()
