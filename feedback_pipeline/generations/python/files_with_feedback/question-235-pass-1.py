def powerfulIntegers(x, y, bound):
    integers = []
    for i in range(x, bound+1):
        for j in range(y, bound+1):
            if i+j == bound:
                integers.append(i+j)
    return integers
