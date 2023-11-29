def count_setbit(N):

def count_setbit(N):
    count = 0
    while N > 0:
        count += N & 1
        N >>= 1
    return count
