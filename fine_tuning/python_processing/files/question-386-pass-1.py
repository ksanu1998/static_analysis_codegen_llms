INT_MAX = 100000000


def minimalSteps(s, n):
    # Initialize the dp table with infinite values
    dp = [INT_MAX] * (n + 1)

    # Base case: if the string is empty, the number of steps is 0
    dp[0] = 0

    # Loop through the string and calculate the minimum number of steps to form it
    for i in range(1, n + 1):
        # If the current character is not a letter, the number of steps is the same as the previous character
        if s[i - 1] not in "abcdefghijklmnopqrstuvwxyz":
            dp[i] = dp[i - 1]
        # If the current character is a letter, the number of steps is the minimum of the previous character and the previous character plus 1
        else:
            dp[i] = min(dp[i - 1], dp[i - 2] + 1)

    return dp[n]
