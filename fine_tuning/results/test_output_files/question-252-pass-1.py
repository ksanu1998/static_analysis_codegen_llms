from math import sqrt, floor


def isPerfect(N):
    if (N == 0):
        return 1
    if (N < 0):
        return 0
    if (floor(sqrt(N)) == sqrt(N)):
        return 1
    return 0


if __name__ == "__main__":
    N = 12
    if (isPerfect(N)):
        print("Yes")
    else:
        print("No")
