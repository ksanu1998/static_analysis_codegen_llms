def solve(X, Y, N, K):
    # Initialize the dp table with 0s
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # Loop through each row and column of the table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # If the current character is the same as the previous character, the cost is 0
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # If the current character is not the same as the previous character, the cost is 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Initialize the longest equal substring with cost less than K
    longest_substring = ""
    current_cost = 0

    # Loop through each row of the table
    for i in range(1, N + 1):
        # If the current cost is less than K, try to extend the longest equal substring
        if current_cost < K:
            # If the current character is the same as the previous character, extend the longest equal substring
            if X[i - 1] == Y[i]:
                longest_substring += X[i - 1]
                current_cost += 1
            # If the current character is not the same as the previous character, reset the longest equal substring
            else:
                longest_substring = ""
                current_cost = 0

    return longest_substring
