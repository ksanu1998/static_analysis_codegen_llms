def equation_plane(x1, y1, z1, x2, y2, z2, x3, y3, z3, x, y, z):
    a1 = x2 - x1
    b1 = y2 - y1
    c1 = z2 - z1
    a2 = x3 - x1
    b2 = y3 - y1
    c2 = z3 - z1
    a = b1 * c2 - b2 * c1
    b = a2 * c1 - a1 * c2
    c = a1 * b2 - b1 * a2
    d = (-a * x1 - b * y1 - c * z1)
    if (a * x + b * y + c * z + d == 0):
        print("Coplanar")
    else:
        print("Not Coplanar")


x1 = 3
y1 = 2
z1 = -5
x2 = -1
y2 = 4
z2 = -3
x3 = -3
y3 = 8
z3 = -5
x4 = -3
y4 = 2
z4 = 1
/*function calling * /
equation_plane(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4)
