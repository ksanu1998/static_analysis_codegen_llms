import math



def sumOfTwoCubes(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        j = math.cbrt(n - i**3)
        if j == int(j):
            return True
    return False
