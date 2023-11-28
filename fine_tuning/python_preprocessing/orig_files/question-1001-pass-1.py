def check(arr, n, m, d):
    i = 0
    while (i < n and m > 0):
        m -= 1
        i += d
    if m == 0:
        return True
    return False


def maximumDistance(arr, n, m):
    low = 1
    high = n - 1
    ans = 0
    while (low <= high):
        mid = (low + high) // 2
        flag = check(arr, n, m, mid)
        if (flag):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


n = 5
m = 3
arr = [0] * n
print(maximumDistance(arr, n, m))
