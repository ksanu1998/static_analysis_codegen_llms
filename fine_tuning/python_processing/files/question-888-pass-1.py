def countZeros(a, n):
    count = 0
    while n > 0:
        if a[n - 1] == 0:
            count += 1
        n -= 1
    return count
