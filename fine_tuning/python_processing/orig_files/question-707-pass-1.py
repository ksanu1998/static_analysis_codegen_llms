from math import sqrt


def hexagonArea(d):
    return (3 * sqrt(3) * pow(d, 2)) / 8


if __name__ == "__main__":
    d = 10
    print("Area of hexagon:", round(hexagonArea(d), 3))
