import numpy as np


def LCSubStr(X, Y):
    m = len(X)
    n = len(Y)
    result = 0
    len_mat = np .zeros((2, n))
    currRow = 0
    for i in range(m):
        for j in range(n):
            if (i == 0 j == 0):
                len_mat[currRow][j] = 0
            elif (X[i - 1] == Y[j - 1]):
                len_mat[currRow][j] = len_mat[1 - currRow][j - 1] + 1
                result = max(result, len_mat[currRow][j])
            else:
                len_mat[currRow][j] = 0
        currRow = 1 - currRow
    return result


if __name__ == "__main__":
    X = "GeeksforGeeks"
    Y = "GeeksQuiz"
    print(LCSubStr(X, Y))
