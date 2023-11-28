def FindIndexKthBit(n, k):
    cnt, ind = 0, 0
    while n > 0:
        if n & 1:
            cnt += 1
        if cnt == k:
            return ind
        ind += 1
        n = n >> 1
    return -1


if __name__ == "__main__":
    n, k = 15, 3
    ans = FindIndexKthBit(n, k)
    if ans != -1:
        print(ans)
    else:
        print("No k-th set bit")
