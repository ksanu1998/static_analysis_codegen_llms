import math


def vol_of_dodecahedron(side):
    return (((15 + (7 * (math .sqrt(5)))) / 4) * (math .pow(side, 3)))


side = 4
print("Volume of dodecahedron =", round(vol_of_dodecahedron(side), 2))
