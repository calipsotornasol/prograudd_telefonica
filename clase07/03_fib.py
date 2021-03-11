def fibonacci(N):
    L = []
    a = 0
    b = 1
    while len(L) < N:
        c = a
        a = b
        b = c + b
        L.append(a)
    return L

print(fibonacci(10))
