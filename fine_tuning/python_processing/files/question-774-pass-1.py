def minimumMEX(arr, N, K):
    # Initialize the result array
    min_mex = [0] * (N - K + 1)

    # Loop through each subarray of length K
    for i in range(N - K + 1):
        # Find the minimum element in the subarray
        min_val = min(arr[i:i+K])

        # Find the maximum element in the subarray
        max_val = max(arr[i:i+K])

        # Calculate the minimum MEX value for the subarray
        min_mex[i] = max_val - min_val

    return min_mex
