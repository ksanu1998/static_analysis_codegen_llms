def printPattern(n, m):
    if (m > 2 * (n + 1) or m < n - 1):
        print("-1", end="")
    elif (abs(n - m) <= 1):
        while (n > 0 and m > 0):
            print("01", end="")
            n -= 1
            m -= 1
        if (n != 0):
            print("0", end="")
        if (m != 0):
            print("1", end="")
    else:
        while (m - n > 1 and n > 0):
            print("110", end="")
            m = m - 2
            n = n - 1
        while (n > 0):
            print("10", end="")
            n -= 1
            m -= 1
        while (m > 0):
            print("1", end="")
            m -= 1


if __name__ == '__main__':
    n = 4
    m = 8
    printPattern(n, m)
