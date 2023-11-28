import math


def countDivisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 2
    if count == 2:
        count += 1
    return count
