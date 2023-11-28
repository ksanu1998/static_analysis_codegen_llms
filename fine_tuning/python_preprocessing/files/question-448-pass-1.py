def restore(arr, N):
    result = []
    for i in range(N):
        result.append(arr[i])
        if i % 2 == 0:
            result.append(arr[i // 2])
        else:
            result.append(arr[i // 2 + 1])
    return result
