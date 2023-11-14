def minSum(arr, n, x):
    # Initialize result variable
    result = 0

    # Iterate through the array and calculate the sum
    for i in range(n):
        result += arr[i]

    # Return the result
    return result
