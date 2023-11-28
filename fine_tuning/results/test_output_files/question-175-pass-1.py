def GCD(a, b):
    if (a > b):
        a, b = b, a
    if (b == 0):
        return a
    c = GCD(a % b, b)
    return c


def reachable(D, n):
    gcd = GCD(D[0], D[1])
    if (gcd == 0):
        return 0
    if (gcd == 1):
        return 1
    if (gcd == D[0]):
        return 2
    if (gcd == D[1]):
        return 1
    return 0


if __name__ == "__main__":
    D = [1, 2]
    n = 2
    print(reachable(D, n))
