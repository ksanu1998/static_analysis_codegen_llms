def getPower(p):
    if (p == 0):
        return 1
    if (p == 1):
        return 0
    if (p == 2):
        return 1
    return (getPower(p - 1) + getPower(p - 2))


def countOddEven(n):
    p = getPower(n)
    print(p)


if __name__ == "__main__":
    n = 5
    countOddEven(n)
