def findPalindrome(C):
    # Find the length of the longest palindromic substring
    # that can be formed by removing a substring from C
    # Time complexity: O(n^2)
    # Space complexity: O(n)

    n = len(C)
    dp = [0] * (n + 1)

    for i in range(n):
        dp[i] = 1

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            if C[i] == C[j]:
                dp[i] = max(dp[i], dp[j] + 2)
            else:
                dp[i] = max(dp[i], dp[j])

    return dp[0]
