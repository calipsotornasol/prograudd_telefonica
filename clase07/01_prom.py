def promedio(z):
    s = 0
    for e in z:
        s += e
    return s/len(z)
    
L = [1,2,3,4]
#print('Promedio L1', promedio(L))

#L2 = [1,1,1,1]
#print('Promedio L2', promedio(L2))
promedio(L)

