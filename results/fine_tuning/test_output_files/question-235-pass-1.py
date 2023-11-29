def powerfulIntegers(x, y, bound):
    res = []
    for i in range(1, bound):
        if (i & 1):
            res.append(i)
    for i in range(1, bound):
        for j in range(1, bound):
            if (i & 1):
                res.append(i + j)
    for i in range(1, bound):
        for j in range(1, bound):
            if (i & 1):
                res.append(i - j)
    res.sort()
    for i in res:
        print(i, end=" ")


if __name__ == "__main__":
    x = 2
    y = 3
    bound = 10
    powerfulIntegers(x, y, bound)
