import math


def Triplets(n):
    c = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(i, int(math.sqrt(n)) + 1):
            if (i * i + j * j == n * n):
                c += 1
    print(c)


if __name__ == "__main__":
    n = 10
    Triplets(n)
