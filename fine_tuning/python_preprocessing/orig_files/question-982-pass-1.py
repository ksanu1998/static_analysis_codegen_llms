def pairAndSum(arr, n):
    for i in range(0, 32):
        k = 0
        for j in range(0, n):
            if ((arr[j] & (1 << i))):
                k = k + 1
        ans = ans + (1 << i) * (k * (k - 1) // 2)
    return ans


arr = [5, 10, 15]
n = len(arr)
print(pairAndSum(arr, n))
