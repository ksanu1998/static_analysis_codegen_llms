from math import sqrt


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def commDiv(a, b):
    n = gcd(a, b)
    result = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                result += 1
            else:
                result += 2
    return result


if __name__ == "__main__":
    a = 12
    b = 24
    print(commDiv(a, b))
