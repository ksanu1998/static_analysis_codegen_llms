def getResult(n):
    if (n < 10):
        return 0
    a = 0
    b = 0
    for i in range(1, 10):
        a = a * 10 + i
        b = b * 10 + (i * 2)
        if (a == b):
            print(a)
            return 1
    return 0


if __name__ == "__main__":
    getResult(123456789)
