def PythagoreanTriplet(n):

def PythagoreanTriplet(n):
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return (a, b, c)
    return None
