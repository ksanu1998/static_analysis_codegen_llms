freq = [0] * 26


def checkPalindrome():
    oddCnt = 0
    for x in freq:
        if (x % 2 == 1):
            oddCnt += 1
    return oddCnt <= 1


def countPalindromePermutation(s, k):
    for i in range(k):
        freq[ord(s[i]) - 97] += 1
    ans = 0
    if (checkPalindrome()):
        ans += 1
    i = 0
    j = k
    while (j < len(s)):
        freq[ord(s[i]) - 97] -= 1
        i += 1
        freq[ord(s[j]) - 97] += 1
        j += 1
        if (checkPalindrome()):
            ans += 1
    return ans


str = "abbaca"
K = 3
print(countPalindromePermutation(str, K))
