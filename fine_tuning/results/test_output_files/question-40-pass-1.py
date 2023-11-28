def sumOfSumSeries(N):
    sum = 0
    for i in range(1, N + 1):
        sum += i
    for i in range(1, N + 1):
        sum -= i
    print(sum)


if __name__ == "__main__":
    N = 5
    sumOfSumSeries(N)
