def calculateB(x, y, n):
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += x[i] * y[i]
        sum2 += x[i] ** 2
    return sum1 / sum2