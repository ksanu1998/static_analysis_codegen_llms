def numbers(n):
    count = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if str(i*j)[-n:] == str(i*j)[:n]:
                count += 1
    return count