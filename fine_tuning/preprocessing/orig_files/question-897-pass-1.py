def func(x, y):
    return (x + y + x * y)


def euler(x0, y, h, x):
    temp = -0
    while x0 < x:
        temp = y
        y = y + h * func(x0, y)
        x0 = x0 + h
    print("Approximate solution at x = ", x, " is ", "%.6f" % y)


x0 = 0
y0 = 1
h = 0.025
x = 0.1
euler(x0, y0, h, x)
