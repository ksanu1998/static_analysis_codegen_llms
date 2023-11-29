def findMinSum(arr, n):
    # Initialize result
    result = 0

    # Loop through all subarrays of size i
    for i in range(1, n+1):
        # Find the minimum element of the subarray
        min_element = min(arr[0:i])

        # Add the minimum element to the result
        result += min_element

    # Return the result
    return result