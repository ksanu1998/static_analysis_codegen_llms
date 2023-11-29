def MaxSubarrayLength(arr, n, k):
    window_start, window_end = 0, 0
    max_length = 0
    sum = 0
    for window_end in range(0, n):
        sum += arr[window_end]
        while sum >= k:
            sum -= arr[window_start]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length
