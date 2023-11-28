def nthElement(a, b, n):
    seq = []
    for i in range(1, n + 1):
        seq .append(a * i)
    seq .sort()
    i = 1
    k = n
    while (i <= n and k > 0):
        try:
            z = seq .index(b * i)
        except ValueError:
            seq .append(b * i)
            seq .sort()
            k -= 1
        i += 1
    return seq[n - 1]


a = 3
b = 5
n = 5
print(nthElement(a, b, n))
