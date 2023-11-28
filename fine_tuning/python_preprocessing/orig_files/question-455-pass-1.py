def findPalindrome(C):
    S = C[::-1]
    C = C[:] + '&' + S
    n = len(C)
    longestPalindrome = [0 for i in range(n)]
    longestPalindrome[0] = 0
    ll = 0
    i = 1
    while (i < n):
        if (C[i] == C[ll]):
            ll += 1
            longestPalindrome[i] = ll
            i += 1
        else:
            if (ll != 0):
                ll = longestPalindrome[ll - 1]
            else:
                longestPalindrome[i] = 0
                i += 1
    ans = C[0:longestPalindrome[n - 1]]
    return ans


def findAns(s):
    A = ""
    B = ""
    F = ""
    i = 0
    j = len(s) - 1
    ll = len(s)
    while (i < j and s[i] == s[j]):
        i = i + 1
        j = j - 1
    if (i > 0):
        A = s[0:i]
        B = s[ll - i:ll]
    if (ll > 2 * i):
        C = s[i:i + (len(s) - 2 * i)]
        D = findPalindrome(C)
        C = C[::-1]
        E = findPalindrome(C)
        if (len(D) > len(E)):
            F = D
        else:
            F = E
    answer = A + F + B
    return answer


if __name__ == "__main__":
    str = "abcdefghiedcba"
    print(findAns(str))
