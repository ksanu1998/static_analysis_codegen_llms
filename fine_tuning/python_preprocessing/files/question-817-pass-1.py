def countNumber(n):
    count = 0
    for i in range(1, n+1):
        if i > int(str(i)[::-1]):
            count += 1
    return count
