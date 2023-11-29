def countPairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] - arr[j] == i - j:
                count += 1
    return count
