def gcd(a, b):
    if (a == 0):
        return b
    if (b == 0):
        return a
    k = 0
    while (((a b) & 1) == 0):
        a = a >> 1
        b = b >> 1
        k = k + 1
    while ((a & 1) == 0):
        a = a >> 1
    while (b != 0):
        while ((b & 1) == 0):
            b = b >> 1
        if (a > b):
            temp = a
            a = b
            b = temp
        b = (b - a)
    return (a << k)


a = 34
b = 17
print("Gcd of given numbers is ", gcd(a, b))
