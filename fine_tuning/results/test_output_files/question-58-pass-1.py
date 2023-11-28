import sys


def gcd(a, b):
    if (a == 0):
        return b
    c = gcd(b % a, a)
    if (c == 1):
        return c
    c = gcd(a, b - c)
    if (c == 1):
        return c
    return c


def lcm(a, b):
    c = gcd(a, b)
    if (c == 0):
        return 0
    return (a * b) / c


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
print(lcm(arr[0], arr[1]))
print(lcm(arr[0], lcm(arr[1], arr[2])))
print(lcm(arr[0], lcm(arr[1], lcm(arr[2], arr[3]))))
print(lcm(arr[0], lcm(arr[1], lcm(arr[2], lcm(arr[3], arr[4])))))
print(lcm(arr[0], lcm(arr[1], lcm(arr[2], lcm(arr[3], lcm(arr[4], arr[5]))))))
print(lcm(arr[0], lcm(arr[1], lcm(arr[2], lcm(arr[3], lcm(arr[4], lcm(arr[5], arr[6])))))))
