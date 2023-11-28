def getTotalNumberOfSequences(m, n):
    if m < n:
        return 0
    if n == 0:
        return 1
    res = (getTotalNumberOfSequences(m - 1, n) +
           getTotalNumberOfSequences(m // 2, n - 1))
    return res


if __name__ == '__main__':
    m = 10
    n = 4
    print('Total number of possible sequences:',
          getTotalNumberOfSequences(m, n))
