def findAverage(N):
    sum = 0
    for i in range(1, N+1):
        sum += i**4
    return sum / N
