#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:13:31 2020

@author: danielaudd
"""


import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

print(t)

plt.plot(t,t**2, 'r--', label='t^2') #Rojo
plt.plot(t,t**3, 'g*' , label='t^3') #Verde
plt.legend()
plt.ylabel('f(t)')
plt.xlabel('t')
plt.title('Graficos1')
plt.savefig('graficos1.png')
plt.clf()

