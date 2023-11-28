def numberOfArithmeticSequences(L, N):
    if (N <= 2):
        return 0
    count = 0
    res = 0
    for i in range(2, N):
        if ((L[i] - L[i - 1]) == (L[i - 1] - L[i - 2])):
            count += 1
        else:
            count = 0
        res += count
    return res


L = [1, 3, 5, 6, 7, 8]
N = len(L)
print(numberOfArithmeticSequences(L, N))
