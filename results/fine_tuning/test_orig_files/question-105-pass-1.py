mod = 1000000007



def countSubsets(a, n):
    # Initialize the dp array
    dp = [0] * (n + 1)

    # Initialize the AND, OR, and XOR values of the empty subset
    and_val = 1
    or_val = 0
    xor_val = 0

    # Loop through the array
    for i in range(1, n + 1):
        # Calculate the AND, OR, and XOR values of the current subset
        and_val = (and_val * a[i - 1]) % mod
        or_val = (or_val + a[i - 1]) % mod
        xor_val = (xor_val + (a[i - 1] * (i % 2))) % mod

        # Update the dp array
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod

        # Calculate the number of subsets with the same AND, OR, and XOR values
        dp[i] = (dp[i] + (and_val * or_val * xor_val)) % mod

    return dp[n]
