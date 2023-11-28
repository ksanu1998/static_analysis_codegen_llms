def findSplit(arr, N):
    # Initialize variables
    min_diff = float('inf')
    min_index = -1

    # Iterate over all possible pairs of elements
    for i in range(N):
        for j in range(i+1, N):
            # Calculate the difference between the sums of the two subarrays
            diff = abs(arr[i] + arr[j] - (arr[0] + arr[1] + arr[2]))

            # Update the minimum difference and its index
            if diff < min_diff:
                min_diff = diff
                min_index = i

    # Return the index of the element to be removed
    return min_index
