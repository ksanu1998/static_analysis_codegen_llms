def LCSubStr(s, t, n, m):
    # Create a 2D array to store the length of the common substring
    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    # Fill in the first row and first column of the array
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Return the last value of the array
    return dp[n][m]
