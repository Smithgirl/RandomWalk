# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:07:44 2018

@author: JINGYUE
"""
# Python code for 2-D random walk. 
import random
import math
from matplotlib import pyplot as plt
import numpy as np

n=input("how many walkers would you like to have\n")
n=int(n)
m=input("how many steps would you like to take per walk\n")
m=int(m)
sum=0
squared_sum=0

for k in range(n):
    x = [0]
    y = [0]
    
    for j in range(m):
        #step_x = random.randint(0,1) 
        #if step_x == 1:
        if random.random() < 0.5:   # this generates more fluctuation than the previous version
            x.append((x[j] + 1)  + np.random.normal())
        else:
            x.append((x[j] - 1)  + np.random.normal())
        
        #step_y = random.randint(0,1)
        #if step_y == 1:
        if random.random() < 0.5:
            y.append((y[j] + 1)   + np.random.normal())
        else:
            y.append((y[j] - 1)   + np.random.normal())
            
    plt.plot(x,y)
    #print ('final position of the walker', k+1, 'is at', x[-1], y[-1])
    plt.scatter(x[-1], y[-1], c='r', marker='o')
    plt.scatter(x[0], y[0], c='g', marker='o')
    d=math.sqrt(x[-1]**2+y[-1]**2)
    sum += d
    squared_sum += (x[-1]**2+y[-1]**2)
    
plt.show()
print('sample sum of the final displacements is',sum)
print('sample mean of the final displacements is',sum/n)
print('sample squared mean of the final displacements is',squared_sum/n)    
plt.close('all')