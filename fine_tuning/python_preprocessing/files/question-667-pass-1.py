def count(arr, low, high, x):
    if low > high:
        return 0
    mid = (low + high) // 2
    count_left = count(arr, low, mid, x)
    count_right = count(arr, mid + 1, high, x)
    count_mid = 0
    for i in range(low, high + 1):
        if arr[i] == x:
            count_mid += 1
    return count_left + count_right + count_mid
