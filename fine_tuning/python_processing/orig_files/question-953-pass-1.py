def minToggle(arr, n):
    zero = [0 for i in range(n + 1 + 1)]
    zero[0] = 0
    for i in range(1, n + 1):
        if (arr[i - 1] == 0):
            zero[i] = zero[i - 1] + 1
        else:
            zero[i] = zero[i - 1]
    ans = n
    for i in range(1, n + 1):
        ans = min(ans, i - zero[i] + zero[n] - zero[i])
    return ans


arr = [1, 0, 1, 1, 0]
n = len(arr)
print(minToggle(arr, n))
