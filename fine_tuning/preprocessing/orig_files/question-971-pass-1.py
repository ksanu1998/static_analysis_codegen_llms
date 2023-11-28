def nonFibonacci(n):
    prevPrev = 1
    prev = 2
    curr = 3
    while n > 0:
        prevPrev = prev
        prev = curr
        curr = prevPrev + prev
        n = n - (curr - prev - 1)
    n = n + (curr - prev - 1)
    return prev + n


print(nonFibonacci(5))
