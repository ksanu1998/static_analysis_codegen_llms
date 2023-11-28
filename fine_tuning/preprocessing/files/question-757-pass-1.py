def maximumSubsequenceSum(A, N):
    # Initialize variables
    max_sum = 0
    current_sum = 0
    difference = 0

    # Sort the array in non-decreasing order
    A.sort()

    # Iterate through the array
    for i in range(N):
        # Calculate the difference between the current index and the previous index
        difference = i - A[i]

        # Check if the difference is positive
        if difference > 0:
            # Calculate the sum of the subsequence
            current_sum += A[i]

            # Check if the sum is greater than the maximum sum
            if current_sum > max_sum:
                max_sum = current_sum

        # If the difference is negative, reset the sum and difference
        else:
            current_sum = 0
            difference = 0

    # Return the maximum sum
    return max_sum
