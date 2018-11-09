# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:07:39 2018

@author: JINGYUE
"""
# Python code for 1-D random walk. 
import random
from matplotlib import pyplot as plt
from pandas.plotting import autocorrelation_plot

n=input("how many walkers would you like to have\n")
n=int(n)
m=input("how many steps would you like to take per walk\n")
m=int(m)
sum=0
squared_sum=0
#random_pos = list()
#random_pos.append(0)

for l in range(1, n+1):     # for each walker
    #random.seed(26082018)           # can be used to fix a single outputted random walk
    random_walk = [0]

    for i in range(1, m+1):    # in each step
        movement = -1 if random.random() < 0.5 else 1
        value = random_walk[i-1] + movement
        random_walk.append(value)
        
    plt.plot(random_walk)
    #print ('final position of the walker', l, 'is at', random_walk[-1])
    plt.scatter(m,random_walk[-1], c='r', marker='o')
    plt.scatter(0,random_walk[0], c='g', marker='o')
    sum += random_walk[m]
    squared_sum += random_walk[m]**2
    #random_pos.append(random_walk[m])
    
#print('the list of final positions are', random_pos)
plt.show()
print('sample sum of the final displacements is',sum)
print('sample mean of the final displacements is',sum/n)
print('sample squared mean of the final displacements is',squared_sum/n)
autocorrelation_plot(random_walk)
plt.show()
plt.close('all')    # just to save memory space