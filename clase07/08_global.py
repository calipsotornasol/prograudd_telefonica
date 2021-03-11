X = 2

def funciona():
    global X
    X = X + 99
    print(X)

funciona()
print(X)