def countOfGreaterElements(arr, n):
    count = [0] * n
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                count[i] += 1
    return count
