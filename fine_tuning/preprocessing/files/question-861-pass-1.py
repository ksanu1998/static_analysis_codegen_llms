import math


def divSum(n):
    sum1 = sum2 = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum1 += i
            sum2 += n // i
    if sum1 == sum2:
        return True
    else:
        return False
