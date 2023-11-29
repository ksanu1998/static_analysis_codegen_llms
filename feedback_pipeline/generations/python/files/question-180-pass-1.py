import sys


def closetAND(arr, n, k):
    # Initialize result with the first element
    result = arr[0]

    # Iterate through the array
    for i in range(1, n):
        # Calculate the bitwise AND of the current element and the previous result
        result &= arr[i]

    # Return the result
    return result