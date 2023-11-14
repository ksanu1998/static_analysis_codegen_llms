from math import pow, ceil

def solve(n):
    for i in range(1, int(ceil(n ** 0.25))):
        j = n - i ** 4
        if j >= 0 and j % 1 == 0:
            return (i, j // 1)
    return None
