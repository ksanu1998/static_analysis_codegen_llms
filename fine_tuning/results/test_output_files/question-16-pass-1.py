def alternatingSumOfFirst_N(N):
    if (N == 1):
        return 1
    else:
        sum = 0
        for i in range(1, N + 1):
            if (i % 2 == 0):
                sum = sum + i
            else:
                sum = sum - i
        print(sum)


if __name__ == "__main__":
    N = 5
    alternatingSumOfFirst_N(N)
