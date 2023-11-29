from math import sqrt


def isoctagonal(N):
    n = int(sqrt(N))
    if (n * (n + 1) / 2 == N):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    N = 12
    isoctagonal(N)
