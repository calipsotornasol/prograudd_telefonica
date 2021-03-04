s = "Hola mundo!"
print('tamaño s', len(s))

# concatenar
s1 = 'Hola' + ' '
s2 = 'Chao'
s3 = s1 + s2
print(s3)

# acceso, la primera posición comienza en 0
print(s1[2]) # imprime el 4to element

# substring
s4 = s[1:5]
print('s[1:5] = ', s4)

# actualizar string: concatenar
print(s[1:])
nuevo = "T" + s[1:]
print(nuevo)

# actualizar string: reemplazar
#nuevo2 = "m{}".format(s[1:])
#print(nuevo2)
