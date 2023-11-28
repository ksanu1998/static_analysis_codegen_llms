import math


def isPowerOfTwo(n):
    if (n == 1):
        return 1
    if (n == 0):
        return 0
    if (n & (n - 1)):
        return 0
    return 1


if (isPowerOfTwo(10)):
    print("Yes")
else:
    print("No")


if (isPowerOfTwo(16)):
    print("Yes")
else:
    print("No")


if (isPowerOfTwo(100)):
    print("Yes")
else:
    print("No")


if (isPowerOfTwo(1000)):
    print("Yes")
else:
    print("No")


if (isPowerOfTwo(1000000)):
    print("Yes")
else:
    print("No")


if (isPowerOfTwo(1000000000)):
    print("Yes")
else:
    print("No")


if (isPowerOfTwo(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
