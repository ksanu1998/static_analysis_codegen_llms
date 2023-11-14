from math import floor, pow
import sys


def smallest_multiple_of_n_with_digit_sum_m(n, m):
    # Find the smallest integer greater than or equal to n that is a multiple of n
    n = n * math.ceil(n / n)

    # Keep dividing n by 10 and adding the digits until the digit sum is greater than or equal to m
    while True:
        if sum(int(i) for i in str(n)) >= m:
            return n
        n = n // 10
