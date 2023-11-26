M = 18
a = 0
b = 0
dp = [[[[-1 for i in range(2)]for j in range(90)]
       for k in range(90)]for l in range(M)]
fib = set()


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
