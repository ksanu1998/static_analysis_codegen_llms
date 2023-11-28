import math
import sys



def changeTheArray(arr, n):
    # Initialize a variable to keep track of the minimum number of operations
    min_operations = math.inf

    # Loop through all possible pairs of elements in the array
    for i in range(n):
        for j in range(i+1, n):
            # Calculate the absolute difference between the two elements
            diff = abs(arr[i] - arr[j])

            # If the difference is less than the minimum, update the minimum
            if diff < min_operations:
                min_operations = diff

    # Return the minimum number of operations
    return min_operations
