from math import sqrt


def findAandB(N):
    sq = int(sqrt(N))
    for (i) in range(1, sq + 1):
        j = N / i
        if (i == j):
            print(i, " ", i)
        elif (i < j):
            print(i, " ", j)


if __name__ == "__main__":
    N = 12
    findAandB(N)
