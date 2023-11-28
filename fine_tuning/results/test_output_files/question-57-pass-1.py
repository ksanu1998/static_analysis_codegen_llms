def gcd(a, b):
    if (a == 0):
        return b
    c = a % b
    a = b
    b = c
    c = a % b
    return gcd(a, b)


def sumOfFractions(n):
    a = 1
    b = 2
    c = 3
    d = 4
    res = 0
    for i in range(1, n):
        res += (a / gcd(a, b))
        a = a + c
        b = b + d
        c = c + a
        d = d + b
    res += (a / gcd(a, b))
    print(res)


if __name__ == "__main__":
    sumOfFractions(4)
