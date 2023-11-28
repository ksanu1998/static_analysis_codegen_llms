def equation_plane(x1, y1, z1, x2, y2, z2, x3, y3, z3, x, y, z):
    a = (y2-y1)*(z3-z1) - (y3-y1)*(z2-z1)
    b = (x3-x1)*(z2-z1) - (x2-x1)*(z3-z1)
    c = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)
    return a*x + b*y + c*z + a*x1 + b*y1 + c*z1 == 0
