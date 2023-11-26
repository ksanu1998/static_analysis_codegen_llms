def LengthlongestPrefixSuffix(s):
    n = len(s)
    lps = [0 for i in range(n)]
    len1 = 0
    i = 1
    while (i < n):
        if (s[i] == s[len1]):
            len1 += 1
            lps[i] = len1
            i += 1
        else:
            if (len1 != 0):
                len1 = lps[len1 - 1]
            else:
                lps[i] = 0
                i += 1
    res = lps[n - 1]
    if (res > int(n / 2)):
        return int(n / 2)
    else:
        return res


def longestPrefixSuffix(s):
    len1 = LengthlongestPrefixSuffix(s)
    prefix = ""
    for i in range(len1):
        prefix += s[i]
    return prefix


if __name__ == '__main__':
    s = "abcab"
    ans = longestPrefixSuffix(s)
    if (ans == ""):
        print("-1")
    else:
        print(ans)
