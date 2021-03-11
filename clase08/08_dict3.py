d = {"Python": 1991, "C": 1972, "Java": 1996}
#Imprimiendo llaves
print('Llaves')
print('------------------------------------')
for key in d:
    print(key)
print('------------------------------------')

print('Valores')
print('------------------------------------')
#Imprimiendo valores
for value in d.values():
    print(value)
print('------------------------------------')   

print('Llaves y valores')
print('------------------------------------')
#Imprimiendo llave y valor al mismo tiempo
for key,value in d.items():
    print(key, value)
print('------------------------------------')