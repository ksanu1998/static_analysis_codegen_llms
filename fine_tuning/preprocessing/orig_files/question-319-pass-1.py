import sys


def maximumOccurrence(s):
    n = len(s)
    freq = [0] * (26)
    dp = [[0 for i in range(26)]for j in range(26)]
    for i in range(n):
        c = (ord(s[i]) - ord('a'))
        for j in range(26):
            dp[j] += freq[j]
        freq += 1
    answer = -sys .maxsize
    for i in range(26):
        answer = max(answer, freq[i])
    for i in range(26):
        for j in range(26):
            answer = max(answer, dp[i][j])
    return answer


if __name__ == '__main__':
    s = "xxxyy"
    print(maximumOccurrence(s))
