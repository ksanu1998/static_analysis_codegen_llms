def check(arr, n, m, d):
    count = 0
    for i in range(n - 1):
        if arr[i] == 1 and arr[i + 1] == 1:
            count += 1
    return count >= d
