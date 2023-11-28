from math import pow, ceil



def solve(n):
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if pow(j-i, 4) == n:
                return [i, j]
    return None
