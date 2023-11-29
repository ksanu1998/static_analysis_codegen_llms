from math import sqrt, pow



def isPerfectPower(n):
    if n == 1:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if pow(i, 2) == n:
            return True
    return False
