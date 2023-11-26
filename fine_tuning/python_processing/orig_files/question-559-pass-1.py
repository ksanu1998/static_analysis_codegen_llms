def isPalindrome(s, i, j):
    while (i < j):
        if (s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True


def getIndex(s1, s2, length):
    i = 0
    j = length - 1
    while (i < j):
        if (s1[i] != s2[j]):
            break
        i += 1
        j -= 1
    if (i == j):
        return i - 1
    elif (isPalindrome(s2, i, j)):
        return i - 1
    elif (isPalindrome(s1, i, j)):
        return j
    return -1


if __name__ == "__main__":
    s1 = "abcdf"
    s2 = "sfgba"
    length = len(s1)
    print(getIndex(s1, s2, length))
