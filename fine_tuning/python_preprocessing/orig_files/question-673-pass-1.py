import math


def findLine(distance, degree):
    x = degree * 3.14159 / 180
    if (degree > 90):
        print("Not Possible")
        return
    result_1 = math .sin(x)
    result_2 = math .cos(x)
    print(
        '%.2f' %
        result_2,
        "x +",
        '%.2f' %
        result_1,
        "y = ",
        distance,
        sep="")


D = 10
A = 30
findLine(D, A)
