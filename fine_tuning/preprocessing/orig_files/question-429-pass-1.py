def lenOfLongestGP(sett, n):
    if n < 2:
        return n
    if n == 2:
        return 2 if (sett[1] % sett[0] == 0)else 1
    sett .sort()
    L = [[0 for i in range(n)]for i in range(n)]
    llgp = 1
    for i in range(0, n - 1):
        if sett[n - 1] % sett[i] == 0:
            L[i][n - 1] = 2
            if 2 > llgp:
                llgp = 2
        else:
            L[i][n - 1] = 1
    L[n - 1][n - 1] = 1
    for j in range(n - 2, 0, -1):
        i = j - 1
        k = j + 1
        while i >= 0 and k <= n - 1:
            if sett[i] * sett[k] < sett[j] * sett[j]:
                k += 1
            elif sett[i] * sett[k] > sett[j] * sett[j]:
                if sett[j] % sett[i] == 0:
                    L[i][j] = 2
                else:
                    L[i][j] = 1
                i -= 1
            else:
                if sett[j] % sett[i] == 0:
                    L[i][j] = L[j][k] + 1
                    if L[i][j] > llgp:
                        llgp = L[i][j]
                else:
                    L[i][j] = 1
                i -= 1
                k += 1
        while i >= 0:
            if sett[j] % sett[i] == 0:
                L[i][j] = 2
            else:
                L[i][j] = 1
            i -= 1
    return llgp


if __name__ == '__main__':
    set1 = [1, 3, 9, 27, 81, 243]
    n1 = len(set1)
    print(lenOfLongestGP(set1, n1))
    set2 = [1, 3, 4, 9, 7, 27]
    n2 = len(set2)
    print(lenOfLongestGP(set2, n2))
    set3 = [2, 3, 5, 7, 11, 13]
    n3 = len(set3)
    print(lenOfLongestGP(set3, n3))
