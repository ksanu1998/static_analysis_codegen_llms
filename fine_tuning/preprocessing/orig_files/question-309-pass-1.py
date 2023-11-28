def calculateSum(n):
    a1 = 1
    a2 = 2
    r = 2
    d = 1
    return ((n) * (2 * a1 + (n - 1) * d) / 2 + a2 * (pow(r, n) - 1) / (r - 1))


n = 5
print("Sum =", int(calculateSum(n)))
