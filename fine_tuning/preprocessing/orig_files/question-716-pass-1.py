def countRectangles(radius):
    rectangles = 0
    diameter = 2 * radius
    diameterSquare = diameter * diameter
    for a in range(1, 2 * radius):
        for b in range(1, 2 * radius):
            diagonalLengthSquare = (a * a + b * b)
            if (diagonalLengthSquare <= diameterSquare):
                rectangles += 1
    return rectangles


radius = 2
totalRectangles = countRectangles(radius)
print(totalRectangles, "rectangles can be",
      "cut from a circle of Radius", radius)
