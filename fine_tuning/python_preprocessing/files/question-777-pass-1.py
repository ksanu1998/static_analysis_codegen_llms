import sys


def average(arr, N):
    # Initialize variables
    sum = 0
    count = 0

    # Iterate through the array
    for i in range(N):
        # Check if the element is not zero
        if arr[i]!= 0:
            # Increment the sum and count
            sum += arr[i]
            count += 1

    # Check if the count is not zero
    if count!= 0:
        # Return the average
        return sum / count
    else:
        # Return zero if the count is zero
        return 0
