import math


def complement(num):
    return int(math.pow(2, num.bit_length()) - 1 - num)
