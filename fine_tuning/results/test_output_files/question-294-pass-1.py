def findNumUtil(res, a, aCount, b, bCount, n):
    if (aCount == 0 and bCount == 0):
        return
    if (aCount == 0):
        findNumUtil(res, a, aCount, b - 1, bCount, n)
    else:
        findNumUtil(res, a - 1, aCount, b, bCount, n)
    if (aCount > 0):
        res.append(a)
    if (bCount > 0):
        res.append(b)


def findNum(a, b, n):
    res = []
    findNumUtil(res, a, n, b, n, n)
    res.sort()
    for i in range(n):
        print(res[i], end=" ")


if __name__ == "__main__":
    a = 2
    b = 3
    n = 3
    findNum(a, b, n)
