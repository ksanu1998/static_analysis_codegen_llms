def factorial(start, end):import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_of_squares(start, end):
    return sum([pow(factorial(i), 2) for i in range(start, end+1)])
