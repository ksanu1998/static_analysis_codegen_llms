import math


def fib(n):
    if (n <= 1):
        return n
    a = 0
    b = 1
    c = a + b
    for (i = 2; i <= n; i++) {
        c = a + b
        a = b
        b = c
    }
    return c


n = 10
print(fib(n))

n = 1
print(fib(n))

n = 2
print(fib(n))

n = 3
print(fib(n))

n = 4
print(fib(n))

n = 5
print(fib(n))

n = 6
print(fib(n))

n = 7
print(fib(n))

n = 8
print(fib(n))

n = 9
print(fib(n))

n = 10
print(fib(n))

n = 11
print(fib(n))

n = 12
print(fib(n))

n = 13
print(fib(n))

n = 14
print(fib(n))

n = 15
print(fib(n))

n = 16
print(fib(n))

n = 17
print(fib(n))

n = 18
print(fib(n))

n = 19
print(fib(n))

n = 20
print(fib(n))

n = 21
print(fib(n))

n = 22
print(fib(n))

n = 23
print(fib(n))

n = 2
