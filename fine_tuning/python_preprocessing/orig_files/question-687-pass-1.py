import math


def calculateAngle(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    ABx = x1 - x2
    ABy = y1 - y2
    ABz = z1 - z2
    BCx = x3 - x2
    BCy = y3 - y2
    BCz = z3 - z2
    dotProduct = (ABx * BCx + ABy * BCy + ABz * BCz)
    magnitudeAB = (ABx * ABx + ABy * ABy + ABz * ABz)
    magnitudeBC = (BCx * BCx + BCy * BCy + BCz * BCz)
    angle = dotProduct
    angle /= math .sqrt(magnitudeAB * magnitudeBC)
    angle = (angle * 180) / 3.14
    print(round(abs(angle), 4))


if __name__ == '__main__':
    x1, y1, z1 = 1, 3, 3
    x2, y2, z2 = 3, 4, 5
    x3, y3, z3 = 5, 6, 9
    calculateAngle(x1, y1, z1, x2, y2, z2, x3, y3, z3)
