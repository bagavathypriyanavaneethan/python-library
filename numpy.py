# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:37:13 2019

@author: Bagavathi Priya
"""
import matplotlib.pyplot as plt

#NUMPY
import numpy as np
a=np.array(([1,2,3],[4,5,6]))
print(a)

a=np.array(([1,2,3],[4,5,6]))
print(a.ndim)
print(a.shape)
print(a.size)

#RESHAPE
a=np.array(([1,2,3,6],[7,9,1,5]))
print(a.reshape(4,2))

print(a[0:,2])

a=np.linspace(1,6,5)
print(a)

print(a.max())
print(a.min())
print(a.sum())

#AXIS
a=np.array(([1,2,3,6],[7,9,1,5]))
print(a.sum(axis=0))
print(a.sum(axis=1))

#special function
x=np.arange(0,3*1.47,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()

a=np.array([1,2,3])
print(np.exp(a))
print(np.log(a))