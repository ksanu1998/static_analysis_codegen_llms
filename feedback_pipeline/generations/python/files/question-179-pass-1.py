def isEven(arr, n, r):
    # Initialize result
    result = 0

    # Iterate through the array
    for i in range(n):
        # Check if the current element is even
        if arr[i] % 2 == 0:
            # If it is even, add it to the result
            result += arr[i]

    # Return the result
    return result