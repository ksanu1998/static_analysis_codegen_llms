def findAllSequence(N):
    if (N % 2 == 0):
        return (pow(2, N / 2 + 1) + pow(2, N / 2) - 2)
    else:
        return (pow(2, (N + 1) / 2) + pow(2, (N + 1) / 2) - 2)


N = 2
print(int(findAllSequence(N)))
