def cbrt(n):
    return (int)(n ** (1. / 3))


def printCubes(a, b):
    acrt = cbrt(a)
    bcrt = cbrt(b)
    for i in range(acrt, bcrt + 1):
        if (i * i * i >= a and i * i * i <= b):
            print(i * i * i, " ", end="")


a = 24
b = 576
print("Perfect cubes in given range:")
printCubes(a, b)
