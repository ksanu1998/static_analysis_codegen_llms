def fib(n):memo = {0: 0, 1: 1}

def fib(n):
    if n in memo:
        return memo[n]
    else:
        result = fib(n-1) + fib(n-2)
        memo[n] = result
        return result
