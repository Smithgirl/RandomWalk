# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:42:44 2018

@author: JINGYUE
"""
# Python code for 3-D random walk. 
import matplotlib as mpl # a 2D plotting library for Python
from mpl_toolkits import mplot3d # three-dimensional plots are enabled by importing the mplot3d toolkit, included with the main Matplotlib installation
import matplotlib.pyplot as plt # a collection of functions that make some change to a figure  
import random # a module in python
import math

n=input("how many walkers would you like to have\n")
n=int(n)
m=input("how many steps would you like to take per walk\n")
m=int(m)
sum=0
squared_sum=0

mpl.rcParams['legend.fontsize'] = 10 # to set the legend fontsize
fig = plt.figure() # to create a figure object
ax = fig.gca(projection='3d')  # Once this submodule (i.e. mplot3d) is imported, a three-dimensional axes can be created by passing the keyword projection='3d' to any of the normal axes creation routines:
                               # gca: If fig is a variable holding a figure, fig.gca() returns the axes associated with the figure. If there’s a projection=… argument to gca, the axes returned are those tagged with the indicated tag (which is commonly a string, but can be an instance of a projection class).
for i in range(n):   
    xyz = [[0, 0, 0]]  # an empty list xyz
    cur = [0, 0, 0] # a list with three numeric elements
    
    for _ in range(m):  # the for loop generate 10000 mew 3D coordinates to xyz list
        for axis in range(0, 3):
            cur[axis] += random.choice([-1, 1])
        xyz.append(cur[:])
    
    x, y, z = zip(*xyz) # to create a list of three lists, each has a series of numbers for x, y, z coordinates, respectively
    ax.plot(x, y, z, label='3D Random walker ' + str(i+1))  # to plot a 3D graph with the input for x,y,z
    #print ('\nfinal position of the walker', i, 'is at', x[-1], y[-1], z[-1])
    ax.scatter(x[-1], y[-1], z[-1], c='r', marker='o')   # the last position is marked red and in a circle
    ax.scatter(x[0], y[0], z[0], c='g', marker='o')
    #ax.legend() # call to place a legend on the axes when there arent many walkers
    d=math.sqrt(x[-1]**2 + y[-1]**2 + z[-1]**2)
    sum += d
    squared_sum += (x[-1]**2+y[-1]**2 + z[-1]**2)
    
plt.show()
print('sample sum of the final displacements is',sum)
print('sample mean of the final displacements is',sum/n)
print('sample squared mean of the final displacements is',squared_sum/n)    
plt.close('all')