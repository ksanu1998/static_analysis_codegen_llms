def getfactor(n, p):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    if (n % p == 0):
        return 1
    if (getfactor(n - 1, p) == 1):
        return 1
    return 0


if __name__ == "__main__":
    n = 10
    p = 3
    if (getfactor(n, p) == 1):
        print("Yes")
    else:
        print("No")
