def updateMatrix(n, q, mat):
    for i in range(q):
        x, y = 0, 0
        if (mat[x][y] == 1):
            mat[x][y] = 0
        else:
            mat[x][y] = 1
    for i in range(n):
        for j in range(n):
            if (mat[i][j] == 1):
                print("1", end=" ")
            else:
                print("0", end=" ")
        print("")


if __name__ == "__main__":
    n = 4
    q = 2
    mat = [[1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1]]
    updateMatrix(n, q, mat)
