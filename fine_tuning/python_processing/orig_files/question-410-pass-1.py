def getTotalNumberOfSequences(m, n):
    T = [[0 for i in range(n + 1)]for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                T[i][j] = 0
            elif i < j:
                T[i][j] = 0
            elif j == 1:
                T[i][j] = i
            else:
                T[i][j] = T[i - 1][j] + T[i // 2][j - 1]
    return T[m][n]


if __name__ == '__main__':
    m = 10
    n = 4
    print('Total number of possible sequences ',
          getTotalNumberOfSequences(m, n))
