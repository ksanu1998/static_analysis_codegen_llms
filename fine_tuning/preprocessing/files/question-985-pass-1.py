import math


def Euler_totient_function(n):
    count = 0
    for i in range(1, n + 1):
        if math.gcd(i, n) == 1:
            count += 1
    return count
