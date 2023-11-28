def tripletAndSum(arr, n):
    ans = 0
    for bit in range(32):
        cnt = 0
        for i in range(n):
            if (arr[i] & (1 << bit)):
                cnt += 1
        ans += (1 << bit) * cnt * (cnt - 1) * (cnt - 2) // 6
    return ans


arr = [3, 5, 4, 7]
N = len(arr)
print(tripletAndSum(arr, N))
