def isPowerOfTwo(n):
    return (n and (not (n & (n - 1))))


def previousPowerOfTwo(n):
    while (n & n - 1):
        n = n & n - 1
    return n


def checkSum(n):
    if (n == 0 or n == 1):
        return False
    elif (isPowerOfTwo(n)):
        print(n // 2, n // 2)
        return True
    else:
        x = previousPowerOfTwo(n)
        y = n - x
        if (isPowerOfTwo(y)):
            print(x, y)
            return True
        else:
            return False


n1 = 20
if (checkSum(n1)):
    print("No")
n2 = 11
if (checkSum(n2)):
    print("No")
