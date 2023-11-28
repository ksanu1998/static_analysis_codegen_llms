import math


def Euler_totient_function(n):
    result = 1
    for i in range(2, n + 1):
        c = 0
        if n % i == 0:
            while (n % i == 0):
                c += 1
                n //= i
        if (c > 0):
            power = math .pow(i, c - 1)
            m = math .pow(i, c - 1) * (i - 1)
            result *= m
    if (n > 1):
        result *= (n - 1)
    return int(result)


for i in range(1, 13):
    print("Euler_totient_function(", i, "): ", end="")
    print(Euler_totient_function(i))
