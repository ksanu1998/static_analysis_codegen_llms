from math import floor


def solve(n, base):
    sum = 0
    for i in range(2, base):
        sum += floor(n / i) % 10
    return sum
