import sys



def maxSubArraySum(a, n, k, i):
    # Initialize variables
    max_sum = 0
    current_sum = 0
    start_index = i
    end_index = i

    # Loop through the array
    for j in range(i, n):
        # Update the current sum
        current_sum += a[j]

        # Check if the current sum is greater than the maximum sum
        if current_sum > max_sum:
            max_sum = current_sum
            start_index = i
            end_index = j

        # Check if the current sum is less than 0
        if current_sum < 0:
            # If the current sum is less than 0, reset it to 0
            current_sum = 0
            start_index = j + 1

        # Check if the current index is a multiple of k
        if j + 1!= k * (j + 1):
            continue

        # If the current index is a multiple of k, reset the current sum to 0
        current_sum = 0

    # Return the maximum sum
    return max_sum
