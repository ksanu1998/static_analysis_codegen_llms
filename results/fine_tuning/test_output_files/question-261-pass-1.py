def addNDigits(a, b, n):
    if (a % b == 0):
        print(a)
        return
    for i in range(1, n):
        a = a + 1
        if (a % b == 0):
            print(a)
            return


if __name__ == "__main__":
    a = 12
    b = 3
    n = 2
    addNDigits(a, b, n)
