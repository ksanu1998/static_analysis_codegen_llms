def numberOfArithmeticSequences(L, N):
    count = 0
    for i in range(N-2):
        if L[i+1] - L[i] == L[i+2] - L[i+1]:
            count += 1
    return count
