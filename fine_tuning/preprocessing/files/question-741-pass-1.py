def smallestMaximum(N, K):
    # Initialize the smallest maximum value to infinity
    smallest_max = float('inf')
    # Loop through all possible sums from 1 to N
    for sum in range(1, N + 1):
        # If the sum is divisible by K
        if sum % K == 0:
            # Update the smallest maximum value
            smallest_max = min(smallest_max, sum)
    # Return the smallest maximum value
    return smallest_max
