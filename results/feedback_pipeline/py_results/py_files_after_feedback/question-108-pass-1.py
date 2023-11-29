def get(x, y, z):
    if z <= x:
        return z
    else:
        return get(x, y, z - 1)
