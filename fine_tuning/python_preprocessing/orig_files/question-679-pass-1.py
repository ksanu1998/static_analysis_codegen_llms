import math


def ConvertDegToRad(degree):
    pi = 3.14159
    return (degree * (pi / 180.0))


def ConvertToCartesian(polar):
    polar[1] = ConvertDegToRad(polar[1])
    cartesian = [
        polar[0] *
        math .cos(
            polar[1]),
        polar[0] *
        math .sin(
            polar[1])]
    print('%.3f' % cartesian[0], '%.3f' % cartesian[1])


if __name__ == "__main__":
    polar = [1.4142, 45]
    ConvertToCartesian(polar)
