def CreateArray(N, even, odd):
    if (N == 1):
        if (even == 1):
            print(1)
        else:
            print(0)
        return
    if (even == 1):
        CreateArray(N - 1, 0, odd)
        CreateArray(N - 1, 1, 1)
    else:
        CreateArray(N - 1, 1, odd)
        CreateArray(N - 1, 0, 1)


if __name__ == "__main__":
    N = 4
    even = 1
    odd = 1
    CreateArray(N, even, odd)
