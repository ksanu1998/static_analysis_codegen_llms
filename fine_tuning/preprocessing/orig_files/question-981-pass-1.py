def pairAndSum(arr, n):
    for i in range(0, n):
        for j in range((i + 1), n):
            ans = ans + arr[i] & arr[j]
    return ans


arr = [5, 10, 15]
n = len(arr)
print(pairAndSum(arr, n))
