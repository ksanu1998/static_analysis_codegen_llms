def updateMatrix(n, q, mat):
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 0:
                mat[i][j] = q
            else:
                mat[i][j] = mat[i][j] - 1
    return mat