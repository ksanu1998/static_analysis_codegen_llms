from bisect import bisect_left


def smallestPermutation(arr, N):
    # Create a list of indices from 0 to N-1
    indices = list(range(N))

    # Sort the indices based on the value of arr at that index
    indices.sort(key=lambda i: arr[i])

    # Return the sorted indices
    return indices
