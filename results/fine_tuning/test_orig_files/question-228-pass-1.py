import math



def max_gcd(n, p):
    gcd = 0
    for i in range(1, n+1):
        for j in range(1, p+1):
            if i*j > n*p:
                break
            if i*j > gcd:
                gcd = i*j
    return gcd
