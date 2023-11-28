def NumberOfShortestPaths(n, m):
    a = [[0 for i in range(m)]for j in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j] = 0
    i = n - 1
    while (i >= 0):
        for j in range(m):
            if (j == 0 or i == n - 1):
                a[i][j] = 1
            else:
                a[i][j] = a[i][j - 1] + a[i + 1][j]
        i -= 1
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=" ")
        print("",  end  = "")


if __name__ == '__main__':
    n = 5
    m = 2
    NumberOfShortestPaths(n, m)
