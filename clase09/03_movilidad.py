#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:29:04 2020

@author: danielaudd
"""


las_condes=list()
la_granja=list()


with open('IndiceDeMovilidad-IM.csv', 'r') as f:
    for line in f:
            s=line.split(',')
            if line.startswith('Regio'):
                fechas= s[6:]
            else:
                comuna=s[2]
                if comuna=='Las Condes':
                    las_condes=s[6:]
                elif comuna=='La Granja':
                    la_granja=s[6:]
                    
fechas[46]=fechas[46][:-1]
print(fechas)

#Convierto las listas de string del IM a float
im_lcondes=[]
for n in las_condes:
    im_lcondes.append(float(n));
    
im_lgranja=[]
for n in la_granja:
    im_lgranja.append(float(n));
    
print(im_lgranja)

import matplotlib.pyplot as plt
plt.plot(im_lcondes)
plt.plot(im_lgranja)
plt.ylabel('Indice Movilidad')
plt.xlabel('Fecha')
plt.title('Movilidad de Las Condes')
plt.savefig('Movilidad_lc.png', bbox_inches='tight', dpi=200)
plt.show()

#Voy a convertir los numeros a fechas para graficar
from datetime import datetime

dates=[]

for n in fechas:
    dates.append(datetime.strptime(n, '%Y-%m-%d').date())
    

plt.ylabel('Indice Movilidad')
plt.xlabel('Fecha')
plt.xticks(rotation=45)
plt.title('Movilidad')
plt.plot(dates,im_lcondes, label='Las Condes')
plt.plot(dates,im_lgranja, label='La Granja')
plt.legend()
plt.savefig('Movilidad.png', bbox_inches='tight', dpi=200)