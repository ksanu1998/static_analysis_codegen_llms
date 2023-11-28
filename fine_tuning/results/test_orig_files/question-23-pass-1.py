def calculateB(x, y, n):

def calculateB(x, y, n):
    sum_x = 0
    sum_y = 0
    sum_x_squared = 0
    sum_x_y = 0
    for i in range(n):
        sum_x += x[i]
        sum_y += y[i]
        sum_x_squared += x[i] ** 2
        sum_x_y += x[i] * y[i]
    b = (n * sum_x_y - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    return b
