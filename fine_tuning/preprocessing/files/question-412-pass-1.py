def lis(arr, n):
    # Create a list to store the longest increasing subsequence
    lis = [0] * n

    # Initialize the first element of the LIS
    lis[0] = arr[0]

    # Loop through the rest of the elements
    for i in range(1, n):
        # Loop through the elements that have already been added to the LIS
        for j in range(i):
            # If the current element is greater than the last element of the LIS, replace it
            if arr[i] > lis[j]:
                lis[j] = arr[i]

    # Return the length of the LIS
    return len(lis)
