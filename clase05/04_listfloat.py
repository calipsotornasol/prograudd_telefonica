# calcula producto punto
x = [0.30, 0.60, 0.10]
y = [0.50, 0.10, 0.40]
total = 0.0
n=len(y)
print(n)
for i in range(n):
    total += x[i]*y[i]
print(total)