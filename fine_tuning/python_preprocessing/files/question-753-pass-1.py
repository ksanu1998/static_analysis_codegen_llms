def factorialWithoutMul(n):
    if n == 0:
        return 1
    else:
        return n * factorialWithoutMul(n-1)
