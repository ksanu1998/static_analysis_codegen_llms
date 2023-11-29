def gcd(a, b):
    if (a == 0):
        return b
    c = a
    a = b
    b = c
    while (a!= 0):
        c = a
        a = b
        b = c
    return b


n = 12
m = 15


if (gcd(n, m) == 1):
    print("GCD of", n, "and", m, "is", gcd(n, m))
else:
    print("GCD of", n, "and", m, "is", gcd(n, m))
