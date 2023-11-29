from math import sqrt


def isPentadecagon(N):
    if (N < 15):
        return 0
    a = (sqrt(1 + 24 * N) + 1) / 6
    if (a - int(a) == 0):
        return 1
    return 0


if __name__ == "__main__":
    N = 22
    if (isPentadecagon(N)):
        print("Yes")
    else:
        print("No")
