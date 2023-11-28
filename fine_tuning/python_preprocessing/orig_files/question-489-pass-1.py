def longestSubstring(s):
    dp = [1024 for i in range(1024)]
    res, mask = 0, 0
    dp[0] = -1
    for i in range(len(s)):
        mask ^= 1 << (ord(s[i]) - ord('0'))
        res = max(res, i - dp[mask])
        for j in range(10):
            res = max(res, i - dp[mask ^ (1 << j)])
        dp[mask] = min(dp[mask], i)
    return res


if __name__ == '__main__':
    s = "3242415"
    print(longestSubstring(s))
