import math
sub = [0 for i in range(100005)]


def minDivisorDifference(n):
    min_diff = float('inf')
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            min_diff = min(min_diff, abs(i - (n // i)))
    return min_diff