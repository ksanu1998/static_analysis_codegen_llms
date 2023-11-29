def findAandB(n, k):
    for i in range(1, n):
        if i % 10!= k:
            if n - i % 10!= k:
                return i, n - i
    return None