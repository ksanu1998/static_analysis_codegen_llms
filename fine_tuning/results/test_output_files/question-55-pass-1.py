def isCenteredcube(N):
    if (N < 10):
        return (N == 1)
    if (N % 3 == 0):
        return (isCenteredcube(N // 3))
    if (N % 3 == 1):
        return (N == 125)
    if (N % 3 == 2):
        return (N == 125)
    return (0)


if __name__ == "__main__":
    N = 125
    if (isCenteredcube(N)):
        print("Yes")
    else:
        print("No")
