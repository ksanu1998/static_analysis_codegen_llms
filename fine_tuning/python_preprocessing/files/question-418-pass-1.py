def maximumDifferenceSum(arr, N):
    max_diff = 0
    for i in range(N-1):
        for j in range(i+1, N):
            diff = abs(arr[i] - arr[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff
