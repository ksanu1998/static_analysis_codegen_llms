def numLen(K):
    count = 0
    while K > 0:
        K //= 10
        count += 1
    return count