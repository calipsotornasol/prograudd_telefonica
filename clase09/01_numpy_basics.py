import numpy as np

print('Crear un arreglo de 2 elementos con zeros')

a=np.zeros(2)

print(a)

print('Crear un arreglo de 2 elementos con unos')

b=np.ones(2)

print(b)

print('Crear un arreglo de 4 elementos consecutivos del 0 al 3')

c=np.arange(4)

print(c)

print('Crear un arreglo elementos consecutivos del 2 al 8, saltandose 2')

d=np.arange(2, 9, 2)

print(d)

print('Crear un arreglo 0 al 10, espaciados')

e=np.linspace(0, 10, num=4)

print(e)

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
arr2= np.sort(arr)

print('Ordenar un arreglo')
print(arr2)

print('Concatenar')

z=np.concatenate((a, b))
print(z)

print('Crear un arreglo de 3 filas y cuatro columnas')
f = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(f)




