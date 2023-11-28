import math


def countSubstr(s):
    n = len(s)
    auxArr = [0 for i in range(n)]
    if (s[0] == '1'):
        auxArr[0] = 1
    for i in range(0, n):
    if (s[i] == '1'):
        auxArr[i] = auxArr[i - 1] + 1
    else:
        auxArr[i] = auxArr[i - 1]
    count = 0
    for i in range(n - 1, -1, -1):
        if (s[i] == '1'):
            count += auxArr[i]
    return count


s = "1101"
print(countSubstr(s))
