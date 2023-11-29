def maxLenSubArr(a, n):
    # Initialize the result
    max_len = 1
    curr_len = 1

    # Iterate over the array
    for i in range(1, n):
        # Check if the current element is equal to the previous element
        if a[i] == a[i-1]:
            curr_len += 1
        else:
            max_len = max(max_len, curr_len)
            curr_len = 1

    # Return the maximum length of the subarray
    return max(max_len, curr_len)