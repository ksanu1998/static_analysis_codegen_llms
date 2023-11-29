def sum(x, n):import math

def sum(x, n):
    result = 0
    for i in range(1, n+1):
        result += x ** i / math.factorial(i)
    return result