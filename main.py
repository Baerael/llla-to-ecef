import matplotlib.pyplot as plt
import numpy as np
import random
import math
import csv
import time

file = open('data.csv')
csvreader = csv.reader(file)

rows = []
for row in csvreader:
        rows.append(row)
rows

# • Time since the Unix epoch [seconds] • WGS84 Latitude [degrees]
# • WGS84 Longitude [degrees]
# • WGS84 altitude [kilometers]

fig = plt.figure()
ax  = plt.axes(projection='3d')

a    = 6378137
e    = 8.181919084261345e-2
a_sq = a**2
e_sq = e**2
b_sq = a_sq*(1 - e_sq)

for row in rows:
    epoch = float(row[0])
    lat   = float(row[1]) * np.pi / 180
    lon   = float(row[2]) * np.pi / 180
    alt   = float(row[3]) 

    N = a / np.sqrt(1 - e_sq*np.sin(lat)**2)
    X = (N + alt) * np.cos(lat) * np.cos(lon)
    Y = (N + alt) * np.cos(lat) * np.sin(lon)
    Z = ( (b_sq / a_sq) * N + alt) * np.sin(lat)

    print(
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch)), 
        "latitude %.2f"  % float(row[1]), 
        "longitude %.2f" % float(row[2]), 
        "altitude %.2f"  % alt 
    )

    ax.scatter(X, Y, Z, c=Z, cmap='Blues_r', linewidth=1);
    plt.pause(0.001)
plt.show()