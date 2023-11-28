def printMaxOfMin(arr, n):
    # Initialize the result list
    result = []

    # Iterate over the window sizes
    for i in range(n, 0, -1):
        # Initialize the minimum value and its index
        min_val = float("inf")
        min_idx = 0

        # Iterate over the current window
        for j in range(i - 1, n):
            # Check if the current element is less than the minimum
            if arr[j] < min_val:
                # Update the minimum value and its index
                min_val = arr[j]
                min_idx = j

        # Append the maximum of the minimum to the result list
        result.append(min_val)

    # Return the result list
    return result[::-1]
