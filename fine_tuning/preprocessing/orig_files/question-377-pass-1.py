term = [0 for i in range(1000)]


def fib(n):
    if n <= 1:
        return n
    if term[n] != 0:
        return term[n]
    else:
        term[n] = fib(n - 1) + fib(n - 2)
        return term[n]


n = 6
print(fib(n))
