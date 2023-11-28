def count(a, b):
    m = len(a)
    n = len(b)
    lookup = [[0] * (n + 1)for i in range(m + 1)]
    for i in range(n + 1):
        lookup[0][i] = 0
    for i in range(m + 1):
        lookup[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + lookup[i - 1][j]
            else:
                lookup[i][j] = lookup[i - 1][j]
    return lookup[m][n]


if __name__ == '__main__':
    a = "GeeksforGeeks"
    b = "Gks"
    print(count(a, b))
