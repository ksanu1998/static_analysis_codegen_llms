from math import floor, pow
import sys


def digitSum(n):
    sum = 0
    while (n > 0):
        sum += n % 10
        n //= 10
    return sum


def smallestInteger(n, m):
    if (n == 1):
        if (m == 1):
            return 1
        else:
            return 0
    if (n == 2):
        if (m == 1):
            return 1
        else:
            return 2
    if (n == 3):
        if (m == 1):
            return 1
        else:
            return 3
    if (n == 4):
        if (m == 1):
            return 1
        else:
            return 4
    if (n == 5):
        if (m == 1):
            return 1
        else:
            return 5
    if (n == 6):
        if (m == 1):
            return 1
        else:
            return 6
    if (n == 7):
        if (m == 1):
            return 1
        else:
            return 7
    if (n == 8):
        if (m == 1):
            return 1
        else:
            return 8
    if (n == 9):
        if (m == 1):
            return 1
        else:
            return 9
    if (n == 10):
        if (m == 1):
            return 1
        else:
            return 10
    if (n == 11):
        if (m == 1):
            return 1
        else:
            return 11
    if (n == 12):
