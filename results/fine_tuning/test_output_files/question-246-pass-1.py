def removeZero(n):
    if (n == 0):
        return 1
    return 0


if __name__ == "__main__":
    a = 123
    b = 456
    c = 567
    if (removeZero(a + b - c)):
        print("Yes")
    else:
        print("No")
