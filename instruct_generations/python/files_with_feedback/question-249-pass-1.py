def minimumX(n, k):
    x = 1
    while (x % k) * (x / k)!= n:
        x += 1
    return x
