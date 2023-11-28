MAX = 10000
CHAR_SIZE = 26


def precompute(mat, str, Len):
    for i in range(Len):
        for j in range(i, Len):
            mat[i][j] = mat[i][j-1] + (str[j]!= str[j-1])
    return mat
