from math import sqrt


def dydx(x, y):
    return (x * (x - 1) * (x - 2) * (x - 3) * (x - 4) * (x - 5) * (x - 6) * (x - 7) * (x - 8) * (x - 9) * (x - 10))


if __name__ == "__main__":
    x = 1
    y = 1
    h = 0.01
    for i in range(1, 100):
        y = y + (h * dydx(x, y))
        x = x + h
    print("The value of y is: ", y)
