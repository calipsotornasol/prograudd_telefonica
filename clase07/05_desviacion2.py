from math import sqrt

def prom(seq):
    return sum(seq)/len(seq)
    
def desviacion(seq):
    p = prom(seq)
    d = 0
    for e in seq:
        d += (e - p)*(e - p)
    return sqrt(d / (len(seq)-1))
    
L = [30, 40, 30, 30]
print(desviacion(L))
