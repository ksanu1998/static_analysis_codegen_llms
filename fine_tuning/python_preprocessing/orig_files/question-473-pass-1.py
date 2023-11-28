def findSubsequence(S, ch):
    N = len(S)
    ans = 0
    for i in range(N):
        if (S[i] == ch):
            ans += 1
            ch = chr(ord(ch) + 1)
    return ans


def findMaxSubsequence(S):
    ans = 0
    for ch in range(ord('a'), ord('z') + 1):
        ans = max(ans, findSubsequence(S, chr(ch)))
    return ans


if __name__ == '__main__':
    S = "abcabefghijk"
    print(findMaxSubsequence(S))
