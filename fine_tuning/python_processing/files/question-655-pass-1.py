def partition_subsets(arr, k):
    # Base case: if k is 1, there is only one way to partition the array
    if k == 1:
        return [arr]

    # Initialize the result list
    result = []

    # Loop over each possible partition point
    for i in range(len(arr)):
        # Get the elements on the left and right of the partition point
        left = arr[:i]
        right = arr[i:]

        # Recursively partition the left and right elements
        for l in partition_subsets(left, k - 1):
            for r in partition_subsets(right, k - 1):
                # Combine the left and right partitions
                result.append(l + [arr[i]] + r)

    return result
