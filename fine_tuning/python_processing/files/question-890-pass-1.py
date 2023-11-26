import math
pwr = [0] * 10


def isMunchhausen(n):
    if n == 0:
        return False
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            pwr[i] += 1
            if pwr[i] > 1:
                return False
    return True
