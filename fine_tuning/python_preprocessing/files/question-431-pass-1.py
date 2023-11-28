list, size: int):def print_longest_bitonic_subsequence(arr, size):
    # Initialize result with the first element
    result = [arr[0]]

    # Loop through the rest of the elements
    for i in range(1, size):
        # If the current element is greater than the last element of the result
        if arr[i] > result[-1]:
            # Add the current element to the result
            result.append(arr[i])
        # If the current element is less than the last element of the result
        elif arr[i] < result[-1]:
            # Replace the last element of the result with the current element
            result[-1] = arr[i]

    # Return the result
    return result
