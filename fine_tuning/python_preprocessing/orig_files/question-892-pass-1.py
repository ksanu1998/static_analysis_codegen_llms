import math


def digSum(n):
    if (n == 0):
        return 0
    if n % 9 == 0:
        return 9
    else:
        return (n % 9)


def PowDigSum(n, x):
    sum = digSum(n)
    rem = x % 6
    if ((sum == 3 or sum == 6) and x > 1):
        return 9
    elif (x == 1):
        return sum
    elif (x == 0):
        return 1
    elif (rem == 0):
        return digSum(math .pow(sum, 6))
    else:
        return digSum(math .pow(sum, rem))


n = 33333
x = 332654
print(PowDigSum(n, x))
