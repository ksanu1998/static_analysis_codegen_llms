def totalways(arr, n):
    # Initialize result
    result = 0

    # Loop through all elements of the array
    for i in range(n):
        # Calculate the absolute difference between the current element and the element to its right
        diff = abs(arr[i] - arr[i+1])

        # Increment the result by the absolute difference
        result += diff

    # Return the result
    return result