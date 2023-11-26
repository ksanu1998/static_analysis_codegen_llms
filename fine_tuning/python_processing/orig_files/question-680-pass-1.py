import math


def distance(p1, p2):
    x1, x2 = p1[0], p2[0]
    y1, y2 = p1[1], p2[1]
    return int(math .sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)))


def find_orthocenter(A, B, C):
    AB = distance(A, B)
    BC = distance(B, C)
    CA = distance(C, A)
    if (AB > BC and AB > CA):
        return C
    if (BC > AB and BC > CA):
        return A
    return B


def find_circumcenter(A, B, C):
    AB = distance(A, B)
    BC = distance(B, C)
    CA = distance(C, A)
    if (AB > BC and AB > CA):
        return ((A[0] + B[0]) // 2, (A[1] + B[1]) // 2)
    if (BC > AB and BC > CA):
        return ((B[0] + C[0]) // 2, (B[1] + C[1]) // 2)
    return ((C[0] + A[0]) // 2, (C[1] + A[1]) // 2)


def findDistance(A, B, C):
    circumcenter = find_circumcenter(A, B, C)
    orthocenter = find_orthocenter(A, B, C)
    distance_between = distance(circumcenter, orthocenter)
    print(distance_between)


A = [0, 0]
B = [6, 0]
C = [0, 8]
findDistance(A, B, C)
