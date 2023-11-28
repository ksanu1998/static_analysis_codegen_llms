def calculateB(x, y, n):
    sumX = 0
    sumY = 0
    sumX2 = 0
    sumXY = 0
    for i in range(n):
        sumX += x[i]
        sumY += y[i]
        sumX2 += x[i] * x[i]
        sumXY += x[i] * y[i]
    b = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX)
    return b


def calculateA(x, y, n):
    sumX = 0
    sumY = 0
    sumX2 = 0
    sumXY = 0
    for i in range(n):
        sumX += x[i]
        sumY += y[i]
        sumX2 += x[i] * x[i]
        sumXY += x[i] * y[i]
    a = (sumY * sumX2 - sumX * sumXY) / (n * sumX2 - sumX * sumX)
    return a


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5]
    n = len(x)
    a = calculateA(x, y, n)
    b = calculateB(x, y, n)
    print("Slope = ", a)
    print("Intercept = ", b)
