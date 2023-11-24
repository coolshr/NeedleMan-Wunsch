#!/usr/bin/python3
import os
import matplotlib.pyplot as plt
import subprocess

n = []
time_normal = []
time_AD = []
time_tile_50 = []
time_tile_100 = []
time_tile_200 = []
time_tile_500 = []
time_tile_1000 = []
time_tile_2000 = []
i = 100
for i in range(1000,51000,1000):
    n.append(i)
    output = subprocess.
while i < 1000000000:
    output = subprocess.check_output("./saxpy " + str(i), shell=True)
    i = i * 10
    t = output.decode("utf-8").split("\n")
    n.append(i)
    Time.append(float(t[0]))
    print(t)
plt.plot(n, Time, label="Time")
plt.legend()
plt.xlabel("n")
plt.xscale("log")
plt.title("icc -axCORE-AVX2   -O3  -g ")