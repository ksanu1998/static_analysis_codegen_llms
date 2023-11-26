def longest_subseq(n, k, s):
    dp = [0] * n
    max_length = [0] * 26
    for i in range(n):
        curr = ord(s[i]) - ord('a')
        lower = max(0, curr - k)
        upper = min(25, curr + k)
        for j in range(lower, upper + 1):
            dp[i] = max(dp[i], max_length[j] + 1)
        max_length[curr] = max(dp[i], max_length[curr])
    return max(dp)


def main():
    s = "geeksforgeeks"
    n = len(s)
    k = 3
    print(longest_subseq(n, k, s))


main()
