def smallestPrimeFactor(n):
    if (n == 1):
        return 2
    if (n % 2 == 0):
        return 2
    for (i = 3; i * i <= n; i += 2)
        if (n % i == 0):
            return i
    return n


n = 10
print(smallestPrimeFactor(n))
