from math import sqrt


def countOrderedPairs(N):
    c = 0
    for i in range(1, int(sqrt(N)) + 1):
        c += (N // i)
    return c


if __name__ == "__main__":
    N = 10
    print(countOrderedPairs(N))
