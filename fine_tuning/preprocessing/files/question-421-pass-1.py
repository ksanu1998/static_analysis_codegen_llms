def countSubarray(arr, n, k):
    count = 0
    for i in range(n):
        max_val = -1
        for j in range(i, n):
            if arr[j] > k:
                max_val = arr[j]
                break
        if max_val!= -1:
            count += 1
    return count
