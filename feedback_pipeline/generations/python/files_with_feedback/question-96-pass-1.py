def findEquation(a, b, c):
    x = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    y = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return x, y
