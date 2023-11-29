def count_setbit(N):
    count = 0
    while N > 0:
        count += 1
        N &= N - 1
    return count
