from math import sqrt, floor


def finalPosition(a, b, M):
    x = 0
    y = 0
    for i in range(M):
        if a[i] == 1:
            x += b[i]
        elif a[i] == 2:
            y += b[i]
        elif a[i] == 3:
            x -= b[i]
        elif a[i] == 4:
            y -= b[i]
    return (x, y)
