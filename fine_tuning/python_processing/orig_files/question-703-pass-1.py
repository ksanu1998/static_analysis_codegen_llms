def totalTriangles(h, v):
    if (h == 0 and v == 0):
        return 1
    if (h == 0):
        return ((v + 1) * (v + 2) / 2)
    if (v == 0):
        return (h + 1)
    total = (h + 1) * ((v + 1) * (v + 2) / 2)
    return total


h = 2
v = 2
print(int(totalTriangles(h, v)))
