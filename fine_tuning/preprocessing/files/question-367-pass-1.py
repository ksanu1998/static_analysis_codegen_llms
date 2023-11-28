N = 100
n = 3
m = 4


def maxPlus(arr):
    # Initialize variables
    max_sum = -float('inf')
    current_sum = 0

    # Iterate over the array
    for i in range(len(arr)):
        # Check if the current sum is greater than the maximum sum
        if current_sum > max_sum:
            max_sum = current_sum

        # Add the current element to the current sum
        current_sum += arr[i]

        # Check if the current sum is less than 0
        if current_sum < 0:
            # If the current sum is less than 0, reset it to 0
            current_sum = 0

    # Return the maximum sum
    return max_sum
