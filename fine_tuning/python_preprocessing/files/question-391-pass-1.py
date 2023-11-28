DP_s = 9


def getNumStrictMonotone(ln):
    # Initialize the DP table
    dp = [0] * (ln + 1)
    dp[0] = 1
    dp[1] = 1

    # Loop through the length of the number
    for i in range(2, ln + 1):
        # Get the current digit
        curr_digit = i % 10

        # Calculate the number of strict monotone numbers
        # that end with the current digit
        num_strict_monotone = 0
        for j in range(1, curr_digit):
            num_strict_monotone += dp[i - j]

        # Update the DP table
        dp[i] = num_strict_monotone

    return dp[ln]
