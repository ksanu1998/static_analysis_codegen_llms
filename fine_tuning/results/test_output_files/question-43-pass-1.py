def concat(a, b):
    c = 0
    for i in range(len(a)):
        c = c + (a[i] * 10 + b[i])
    return c


n = 10
for i in range(1, n):
    for j in range(1, n):
        if (concat(i, j) == 1000):
            print(i, j)
            break
    if (concat(i, j) == 1000):
        break
print("No astonishing number found")
