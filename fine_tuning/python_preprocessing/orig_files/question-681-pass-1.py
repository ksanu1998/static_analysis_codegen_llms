import time
import random
random .seed(time .time())


def generatePoints(L, W):
    hash = {}
    total = (L * W)
    for i in range(total):
        X = random .randint(0, L) % L
        Y = random .randint(0, W) % W
        while ((X, Y) in hash):
            X = random .randint(0, L) % L
            Y = random .randint(0, W) % W
        hash[(X, Y)] = 1
    for points in sorted(hash):
        print("(", points[0], ", ", points[1], ") ", end="")


if __name__ == '__main__':
    L, W = 3, 2
    generatePoints(L, W)
