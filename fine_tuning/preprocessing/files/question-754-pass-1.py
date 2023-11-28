def tripletAndSum(arr, n):
    result = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                result += (arr[i] & arr[j] & arr[k])
    return result
