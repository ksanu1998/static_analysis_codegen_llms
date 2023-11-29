def print_h_index(arr, N):
    # Sort the array in descending order
    arr.sort(reverse=True)
    # Initialize variables
    h_index = 0
    count = 0
    # Iterate through the array
    for i in range(N):
        # If the current element is greater than or equal to the count, increment the h-index
        if arr[i] >= count:
            h_index += 1
            count += 1
        # If the current element is less than the count, increment the count
        else:
            count += 1
    # Return the h-index
    return h_index