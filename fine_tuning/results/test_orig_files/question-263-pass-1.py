from math import floor



def solve(n, base):
    total = 0
    for i in range(n):
        total += floor(i / base)
    return total
