#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:29:35 2020

@author: danielaudd
"""
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

print(t1)

print(t2)

plt.figure()
plt.subplot(211)
plt.xlabel('t')
plt.ylabel('Exp(-t)Cos(2\u03C0t)')
plt.plot(t2, f(t2), 'bo') #Azul

plt.subplot(212)
plt.ylabel('Cos2\u03C0t')
plt.plot(t1, np.cos(2*np.pi*t1), 'r--')#Rojo

plt.suptitle('Graficos2')

plt.show()
plt.savefig('graficos2.png')