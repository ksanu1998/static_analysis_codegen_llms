import math


def FirstDigit(arr, n):
    product = 1
    for i in range(n):
        product *= arr[i]
    return int(math.log10(product) + 1)
