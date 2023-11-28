def getCount(str1, n):
    cnt = 0
    i = 0
    while (i < n - 2):
        if (str1[i] == str1[i + 1] and str1[i] == str1[i + 2]):
            cnt += 1
            i = i + 2
        else:
            i += 1
    return cnt


str1 = "aabbbcc"
n = len(str1)
print(getCount(str1, n))
