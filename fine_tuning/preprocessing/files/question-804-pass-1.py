INT_MIN = -1000000


def printMaxOfMin(arr, n):
    # Initialize result
    result = []

    # Iterate through each window size
    for i in range(n+1):
        # Initialize minimum and maximum values
        min_val = INT_MIN
        max_val = INT_MIN

        # Iterate through the array
        for j in range(i, n+1):
            # Update minimum and maximum values
            min_val = min(min_val, arr[j])
            max_val = max(max_val, arr[j])

        # Append the maximum of minimum value to the result
        result.append(max_val - min_val)

    # Return the result
    return result[::-1]
