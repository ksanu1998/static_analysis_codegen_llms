def gcd(a, b):
    return gcd(b, a % b)if b > 0 else a


def countGCD(L, R, g):
    L = (L + g - 1) // g
    R = R // g
    ans = 0
    for i in range(L, R + 1):
        for j in range(L, R + 1):
            if (gcd(i, j) == 1):
                ans = ans + 1
    return ans


L = 1
R = 11
g = 5
print(countGCD(L, R, g))
