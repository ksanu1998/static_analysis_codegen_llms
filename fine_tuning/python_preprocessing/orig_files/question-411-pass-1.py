def lcs(str1, str2, m, n):
    L = [[0 for i in range(n + 1)]for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                L[i][j] = 0
            elif (str1[i - 1] == str2[j - 1]):
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L[m][n]


def printMinDelAndInsert(str1, str2):
    m = len(str1)
    n = len(str2)
    leng = lcs(str1, str2, m, n)
    print("Minimum number of deletions = ", m - leng, sep=' ')
    print("Minimum number of insertions = ", n - leng, sep=' ')


str1 = "heap"
str2 = "pea"
printMinDelAndInsert(str1, str2)
