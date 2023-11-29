def factorial(n):
    if (n == 0):
        return 1
    res = 1
    for (i = 1; i <= n; i++)
        res *= i
    return res


def gcd(a, b):
    if (a > b):
        return gcd(b, a)
    if (b == 0):
        return a
    res = gcd(b, a % b)
    return res


arr = [1, 2, 3, 4, 5]
n = len(arr)
ans = 1
for (i = 0; i < n; i++)
    ans = gcd(ans, factorial(arr[i]))
print(ans)
