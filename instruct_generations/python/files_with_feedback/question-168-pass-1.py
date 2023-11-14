def smallestPrimeFactor(n):
    if n <= 1:
        return n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n
