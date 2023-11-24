#!/usr/bin/python3
import os
import matplotlib.pyplot as plt
import subprocess

n = []
time_normal = []
time_normal_bandwidth = []
time_normal_gflops = []
time_normal_nopt = []
time_normal_nopt_bandwidth = []
time_normal_nopt_gflops = []
time_AD = []
time_AD_bandwidth = []
time_AD_gflops = []
time_tile_50 = []
time_tile_50_bandwidth = []
time_tile_50_gflops = []
time_tile_100 = []
time_tile_100_bandwidth = []
time_tile_100_gflops = []
time_tile_200 = []
time_tile_200_bandwidth = []
time_tile_200_gflops = []
time_tile_500 = []
time_tile_500_bandwidth = []
time_tile_500_gflops = []
time_tile_1000 = []
time_tile_1000_bandwidth = []
time_tile_1000_gflops = []
i = 100
# for i in range(1000, 45000, 1000):
#     n.append(i)
#     output = subprocess.check_output("./nw_rw_opt" + " " + str(i), shell=True)
#     x = output.decode("utf-8")
#     y = x.split("\n")
#     # print(y)
#     # print()
#     # print(str(output).split("\n")[0])
#     time_normal.append(float(y[0]))
#     time_normal_gflops.append(float(y[1]))
#     time_normal_bandwidth.append(float(y[2]))


# for i in range(1000,45000,1000):
#     n.append(i)
#     output = subprocess.check_output("./nw_rw" +" "+ str(i), shell=True)
#     x = output.decode("utf-8")
#     y = x.split("\n")
#     time_normal_nopt.append(float(y[0]))
#     time_normal_nopt_gflops.append(float(y[1]))
#     time_normal_nopt_bandwidth.append(float(y[2]))

# for i in range(1000,39000,1000):
#     n.append(i)
#     output = subprocess.check_output("./nw_ad" +" "+ str(i), shell=True)
#     x = output.decode("utf-8")
#     y = x.split("\n")
#     time_AD.append(float(y[0]))
#     time_AD_gflops.append(float(y[1]))
#     time_AD_bandwidth.append(float(y[2]))

for i in range(1000,51000,1000):
    n.append(i)
    output = subprocess.check_output("./nw_tile_50" +" "+ str(i), shell=True)
    x = output.decode("utf-8")
    y = x.split("\n")
    time_tile_50.append(float(y[0]))
    time_tile_50_gflops.append(float(y[1]))
    time_tile_50_bandwidth.append(float(y[2]))

# for i in range(1000,51000,1000):
#     n.append(i)
#     output = subprocess.check_output("./nw_tile_100" +" "+ str(i), shell=True)
#     x = output.decode("utf-8")
#     y = x.split("\n")
#     time_tile_100.append(float(y[0]))
#     time_tile_100_gflops.append(float(y[1]))
#     time_tile_100_bandwidth.append(float(y[2]))

# for i in range(1000,51000,1000):
#     n.append(i)
#     output = subprocess.check_output("./nw_tile_200" +" "+ str(i), shell=True)
#     x = output.decode("utf-8")
#     y = x.split("\n")
#     time_tile_200.append(float(y[0]))
#     time_tile_200_gflops.append(float(y[1]))
#     time_tile_200_bandwidth.append(float(y[2]))

# for i in range(1000,51000,1000):
#     n.append(i)
#     output = subprocess.check_output("./nw_tile_500" +" "+ str(i), shell=True)
#     x = output.decode("utf-8")
#     y = x.split("\n")
#     time_tile_500.append(float(y[0]))
#     time_tile_500_gflops.append(float(y[1]))
#     time_tile_500_bandwidth.append(float(y[2]))

# for i in range(1000,51000,1000):
#     n.append(i)
#     output = subprocess.check_output("./nw_tile_1000" +" "+ str(i), shell=True)
#     x = output.decode("utf-8")
#     y = x.split("\n")
#     time_tile_1000.append(float(y[0]))
#     time_tile_1000_gflops.append(float(y[1]))
#     time_tile_1000_bandwidth.append(float(y[2]))

with open("output.txt", "a") as f:
    # f.writelines(str(time_normal))
    # f.writelines(str(time_normal_bandwidth))
    # f.writelines(str(time_normal_gflops))
    # f.writelines(str(time_normal_nopt))
    # print()
    # f.writelines(str(time_normal_nopt_bandwidth))
    # print()
    # f.writelines(str(time_normal_nopt_gflops))
    # print()
    # f.writelines(str(time_AD))
    # f.writelines("\n")
    # f.writelines(str(time_AD_bandwidth))
    # f.writelines("\n")
    # f.writelines(str(time_AD_gflops))
    # f.writelines("\n")

    f.writelines(str(time_tile_50))
    f.writelines("\n")
    
    f.writelines(str(time_tile_50_bandwidth))
    f.writelines("\n")

    f.writelines(str(time_tile_50_gflops))
    f.writelines("\n")
    
    # f.writelines(str(time_tile_100))
    # f.writelines("\n")
#
    # f.writelines(str(time_tile_100_bandwidth))
    # f.writelines("\n")
    
    # f.writelines(str(time_tile_100_gflops))
    # print()
    # f.writelines(str(time_tile_200))
    # f.writelines("\n")

    # f.writelines(str(time_tile_200_bandwidth))
    # f.writelines("\n")
    
    # f.writelines(str(time_tile_200_gflops))
    # f.writelines("\n")
    
    # f.writelines(str(time_tile_500))
    # f.writelines("\n")
    
    # f.writelines(str(time_tile_500_bandwidth))
    # f.writelines("\n")
    
    # f.writelines(str(time_tile_500_gflops))
    # f.writelines("\n")
    
    # f.writelines(str(time_tile_1000))
    #  f.writelines("\n")

    # f.writelines(str(time_tile_1000_bandwidth))
    #  f.writelines("\n")

    # f.writelines(str(time_tile_1000_gflops))
    #  f.writelines("\n")

