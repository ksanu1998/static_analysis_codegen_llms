import math
import sys


def changeTheArray(arr, n):
    # Initialize a variable to store the minimum number of operations
    min_operations = float("inf")

    # Loop through each element in the array
    for i in range(n):
        # Calculate the absolute difference between the current element and the target element
        diff = abs(arr[i] - n)

        # Check if the absolute difference is less than the minimum number of operations
        if diff < min_operations:
            # Update the minimum number of operations
            min_operations = diff

    # Return the minimum number of operations
    return min_operations
