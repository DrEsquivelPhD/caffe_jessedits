#!/usr/bin/python

import numpy as np
import sys
import matplotlib.pyplot as plt

with open(sys.argv[1]) as f:
    data = f.read()

data = data.split('\n')

x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]
z = [row.split(' ')[2] for row in data]

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Plot title...")    
ax1.set_xlabel('iterations')
ax1.set_ylabel('accuracy')

ax1.plot(x,y, c='r', label='the data')

leg = ax1.legend()

plt.show()
