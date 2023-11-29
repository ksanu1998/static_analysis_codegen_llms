import math


def sumOfTwoCubes(n):import math

def sumOfTwoCubes(n):
    for i in range(1, int(n ** 0.5) + 1):
        j = math.ceil((n - i ** 3) ** 0.5)
        if i ** 3 + j ** 3 == n:
            return True
    return False
