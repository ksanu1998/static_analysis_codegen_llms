def candies(n, k):
    return [max(0, n - i) for i in range(k)]