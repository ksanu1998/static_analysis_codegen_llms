import sys


def isPossible(arr, n):
    # Sort the array in ascending order
    arr.sort()
    # Initialize the minimum element
    min_element = arr[0]
    # Initialize the remainder
    remainder = 0
    # Iterate over the array
    for i in range(n):
        # Check if the current element can be reduced to the minimum element by replacing it with the remainder
        if arr[i] - min_element <= remainder:
            # Update the remainder
            remainder = arr[i] - min_element
        else:
            # Return False if the current element cannot be reduced to the minimum element by replacing it with the remainder
            return False
    # Return True if all elements can be reduced to the minimum element by replacing it with the remainder
    return True
