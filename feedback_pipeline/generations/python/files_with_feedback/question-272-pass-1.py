def countdig(m):
    count = 0
    while m > 0:
        count += 1
        m //= 10
    return count
