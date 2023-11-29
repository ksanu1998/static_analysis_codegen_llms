def candies(n, k):
    if n < k:
        return 0
    if n == k:
        return n
    if n > k:
        return n // k
