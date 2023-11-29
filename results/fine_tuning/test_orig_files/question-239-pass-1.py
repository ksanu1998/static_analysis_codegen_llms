def updateMatrix(n, q, mat):

def updateMatrix(n, q, mat):
    for i in range(n):
        for j in range(n):
            if i // 2 == j // 2 and i % 2 == j % 2:
                mat[i][j] += 1
    return mat
