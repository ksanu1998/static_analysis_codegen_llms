def findAverage(N):
    avg = ((6 * N * N * N * N) + (15 * N * N * N) + (10 * N * N) - 1) / 30
    return avg


N = 3
print(round(findAverage(N), 4))
