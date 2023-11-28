def ExtendedEuclidAlgo(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = ExtendedEuclidAlgo(b % a, a)
        return (g, x - (b // a) * y, y)
