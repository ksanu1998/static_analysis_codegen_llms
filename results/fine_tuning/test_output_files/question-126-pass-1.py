def findNumberOfEvenCells(n, q, size):
    res = [0] * q
    for i in range(q):
        res[i] = 0
    for i in range(n):
        for j in range(n):
            if (size[i][j] % 2 == 0):
                res[i] += 1
    for i in range(q):
        print(res[i])


if __name__ == "__main__":
    n = 4
    q = 2
    size = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]
    findNumberOfEvenCells(n, q, size)
