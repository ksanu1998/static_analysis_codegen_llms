def countSubStr(str, n, x):
    res = 0
    count = 0
    for i in range(n):
        if (str[i] == x):
            res += ((count + 1) * (n - i))
            count = 0
        else:
            count += 1
    return res


str = "abcabc"
n = len(str)
x = 'c'
print(countSubStr(str, n, x))
