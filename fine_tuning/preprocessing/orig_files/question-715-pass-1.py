def mirror_point(a, b, c, d, x1, y1, z1):
    k = (-a * x1 - b * y1 - c * z1 - d) / float((a * a + b * b + c * c))
    x2 = a * k + x1
    y2 = b * k + y1
    z2 = c * k + z1
    x3 = 2 * x2 - x1
    y3 = 2 * y2 - y1
    z3 = 2 * z2 - z1
    print "x3 =", x3,
    print "y3 =", y3,
    print "z3 =", z3,


a = 1
b = -2
c = 0
d = 0
x1 = -1
y1 = 3
z1 = 4
mirror_point(a, b, c, d, x1, y1, z1)
