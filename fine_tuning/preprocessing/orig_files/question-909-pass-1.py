def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)


def findNumber(arr, n):
    ans = arr[0]
    for i in range(0, n):
        ans = gcd(ans, arr[i])
    for i in range(0, n):
        if (arr[i] == ans):
            return ans
    return -1


arr = [2, 2, 4]
n = len(arr)
print(findNumber(arr, n))
