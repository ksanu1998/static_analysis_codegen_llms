def findMinLength(arr, n):
    if n == 1:
        return arr[0]

    min_length = float('inf')
    for i in range(n):
        prefix = arr[i]
        for j in range(i+1, n):
            if arr[j].startswith(prefix):
                min_length = min(min_length, len(prefix))
                break

    return min_length
