import math


def complement(num):
    i = 0
    len = 0
    comp = 0
    temp = num
    while (1):
        len += 1
        num = int(num / 10)
        if (abs(num) == 0):
            break
    num = temp
    comp = math .pow(10, len) - num
    return int(comp)


print(complement(25))
print(complement(456))
