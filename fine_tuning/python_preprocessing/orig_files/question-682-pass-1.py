def noOfTriangles(n):
    return n * (n + 2) * (2 * n + 1) // 8


n = 3
print(noOfTriangles(n))
