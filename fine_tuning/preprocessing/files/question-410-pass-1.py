def getTotalNumberOfSequences(m, n):
    count = 0
    for i in range(m, n+1):
        count += i
    return count
