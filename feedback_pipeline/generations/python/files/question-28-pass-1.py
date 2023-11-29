def maxLCMWithGivenSum(X):
    # Initialize the maximum LCM as 1
    max_lcm = 1

    # Loop through all pairs of integers from 1 to X
    for i in range(1, X + 1):
        for j in range(i, X + 1):
            # If the sum of the two integers is equal to X,
            # then they are the desired pair
            if i + j == X:
                # Get the least common multiple (LCM) of the two integers
                lcm = i * j

                # Update the maximum LCM if the current LCM is greater than the previous maximum
                if lcm > max_lcm:
                    max_lcm = lcm

    return max_lcm