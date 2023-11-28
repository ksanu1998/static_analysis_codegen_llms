PHI = 1.6180339
f = [0, 1, 1, 2, 3, 5]


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b / PHI
    return a
