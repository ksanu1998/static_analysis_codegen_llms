def count_setbit(N):
    count = 0
    while (N > 0):
        if (N & 1):
            count += 1
        N >>= 1
    return count


if __name__ == "__main__":
    N = 10
    print(count_setbit(N))
