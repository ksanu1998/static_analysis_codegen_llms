import sys


def findMax(n, a, b, k, m):
    # Initialize the maximum value
    max_val = a[0]

    # Loop through each element in the array
    for i in range(n):
        # Check if the element is in the range of the current operation
        if b[i] - k <= m <= b[i] + k:
            # Update the maximum value if the current element is greater than the previous maximum
            if a[i] > max_val:
                max_val = a[i]

    return max_val
