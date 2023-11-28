def isKPalDP(str1, str2, m, n):
    if m == 0 and n == 0:
        return True
    elif m == 0 or n == 0:
        return False
    elif str1[m - 1] == str2[n - 1]:
        return isKPalDP(str1, str2, m - 1, n - 1)
    else:
        return isKPalDP(str1, str2, m - 1, n) or isKPalDP(str1, str2, m, n - 1)
