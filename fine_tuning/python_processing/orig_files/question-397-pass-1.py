def lcs(X, Y, m, n):
    L = [[0 for i in range(n + 1)]for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                L[i][j] = 0
            elif (X[i - 1] == Y[j - 1]):
                L[i][j] = L[i - 1][j - 1] + 2 * (ord(X[i - 1]) - 48)
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L[m][n]


def findMinCost(X, Y):
    m = len(X)
    n = len(Y)
    cost = 0
    for i in range(m):
        cost += ord(X[i]) - 48
    for i in range(n):
        cost += ord(Y[i]) - 48
    ans = cost - lcs(X, Y, m, n)
    return ans


X = "3759"
Y = "9350"
print("Minimum Cost to make two strings ",
      "identical is = ", findMinCost(X, Y))
