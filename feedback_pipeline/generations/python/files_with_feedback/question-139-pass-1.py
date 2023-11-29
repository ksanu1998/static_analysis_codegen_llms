def cntSquares(n):
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                count += 1
    return count
