def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while (i < j):
        if (s[i] is not s[j]):
            return False
        i += 1
        j -= 1
    return True


def getIndex(S1, S2, n):
    S = ""
    for i in range(n):
        S = S + S1[i]
        Temp = ""
        for j in range(i + 1, n):
            Temp += S2[j]
        if (isPalindrome(S + Temp)):
            return i
    return -1


S1 = "abcdf"
S2 = "sfgba"
n = len(S1)
print(getIndex(S1, S2, n))
