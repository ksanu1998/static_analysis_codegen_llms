def PrintReverseOrder(N):
    if (N == 0):
        return
    PrintReverseOrder(N - 1)
    print(N, end=" ")


if __name__ == "__main__":
    N = 5
    PrintReverseOrder(N)
