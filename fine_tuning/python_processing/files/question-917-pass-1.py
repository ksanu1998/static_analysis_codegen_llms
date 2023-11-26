def recDigSum(n):
    if n == 0:
        return False
    if n % 10 == 0:
        return False
    return recDigSum(n // 10)
