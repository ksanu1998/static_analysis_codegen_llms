import sys


def smallestSumSubarr(arr, n):
    # Initialize result
    result = 0

    # Initialize minimum sum
    min_sum = sys.maxsize

    # Initialize sum
    sum = 0

    # Iterate through the array
    for i in range(n):
        sum += arr[i]

        # Check if sum is less than min_sum
        if sum < min_sum:
            # Update min_sum and result
            min_sum = sum
            result = i

        # Check if sum is greater than sum
        elif sum > min_sum:
            # Update sum
            sum = sum - arr[result] + arr[i]

    # Return result
    return result
