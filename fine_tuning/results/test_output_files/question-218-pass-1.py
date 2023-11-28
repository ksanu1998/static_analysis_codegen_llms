def getMaxNum(a, b, c):
    if (c == 1):
        return 0
    if (c == 2):
        if (a % 2 == 0):
            return (a / 2)
        else:
            return 0
    if (c == 3):
        if (a % 3 == 0):
            return (a / 3)
        else:
            return 0
    if (c == 4):
        if (a % 4 == 0):
            return (a / 4)
        else:
            return 0
    if (c == 5):
        if (a % 5 == 0):
            return (a / 5)
        else:
            return 0
    if (c == 6):
        if (a % 6 == 0):
            return (a / 6)
        else:
            return 0
    if (c == 7):
        if (a % 7 == 0):
            return (a / 7)
        else:
            return 0
    if (c == 8):
        if (a % 8 == 0):
            return (a / 8)
        else:
            return 0
    if (c == 9):
        if (a % 9 == 0):
            return (a / 9)
        else:
            return 0
    if (c == 10):
        if (a % 10 == 0):
            return (a / 10)
        else:
            return 0


if __name__ == "__main__":
    a = 10
    b = 100
    c = 10
    print(getMaxNum(a, b, c))
