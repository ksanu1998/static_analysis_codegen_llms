def lineFromPoints(P, Q):import math

def lineFromPoints(P, Q):
    A = (P[1] - Q[1]) / (P[0] - Q[0])
    B = P[1] - A * P[0]
    return A, B
