def sumOfDigits(N):
    sum = 0
    while N > 0:
        sum += N % 10
        N //= 10
    return sum
