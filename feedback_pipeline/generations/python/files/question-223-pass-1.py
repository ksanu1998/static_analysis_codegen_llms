from math import floor, pow
import sys


def digitSum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum