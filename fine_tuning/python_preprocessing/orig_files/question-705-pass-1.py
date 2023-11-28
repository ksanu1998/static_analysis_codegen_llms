def checkOrtho(x1, y1, x2, y2, x3, y3, x4, y4):
    if (x2 - x1 == 0 and x4 - x3 == 0):
        return False
    elif (x2 - x1 == 0):
        m2 = (y4 - y3) / (x4 - x3)
        if (m2 == 0):
            return True
        else:
            return False
    elif (x4 - x3 == 0):
        m1 = (y2 - y1) / (x2 - x1)
        if (m1 == 0):
            return True
        else:
            return False
    else:
        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y4 - y3) / (x4 - x3)
        if (m1 * m2 == -1):
            return True
        else:
            return False


if __name__ == '__main__':
    x1 = 0
    y1 = 4
    x2 = 0
    y2 = -9
    x3 = 2
    y3 = 0
    x4 = -1
    y4 = 0
    if (checkOrtho(x1, y1, x2, y2, x3, y3, x4, y4)):
        print("Yes")
    else:
        print("No")
