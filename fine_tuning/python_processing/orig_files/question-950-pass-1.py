def closestMultiple(n, x):
    if x > n:
        return x
    z = (int)(x / 2)
    n = n + z
    n = n - (n % x)
    return n


n = 56287
x = 27
print(closestMultiple(n, x))
