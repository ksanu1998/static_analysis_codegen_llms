import math


def minAbsDiff(n):
    # Find the closest power of 2 to n
    power = int(math.log(n, 2))

    # Calculate the absolute difference between n and the power of 2
    diff = abs(n - 2**power)

    # Return the minimum absolute difference
    return diff
