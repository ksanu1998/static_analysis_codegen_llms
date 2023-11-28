def area(d1, a):
    d2 = (4 * (a ** 2) - d1 ** 2)**0.5
    area = 0.5 * d1 * d2
    return (area)


d = 7.07
a = 5
print(area(d, a))
