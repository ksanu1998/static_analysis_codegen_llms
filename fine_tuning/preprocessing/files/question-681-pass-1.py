import time
import random
random .seed(time .time())


def generatePoints(L, W):import random

def generatePoints(L, W):
    points = []
    for i in range(L):
        for j in range(W):
            points.append((i, j))
    return points
