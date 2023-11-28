def maxLength(s, n):
    # Initialize the dp array
    dp = [0] * (n + 1)

    # Initialize the maximum length
    max_len = 0

    # Loop through the string
    for i in range(1, n + 1):
        # Check if the current character is balanced
        if s[i - 1] == '(' or s[i - 1] == ')':
            # If the current character is balanced, set the maximum length
            max_len = max(max_len, dp[i - 1] + 2)
        else:
            # If the current character is not balanced, set the maximum length
            max_len = max(max_len, dp[i - 1])

        # Set the current character as balanced
        dp[i] = max(dp[i - 1] + 1, dp[i])

    # Return the maximum length
    return max_len
