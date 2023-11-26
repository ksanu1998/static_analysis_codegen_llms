def sumOfDigits(N):
    count = 0
    for i in range(1, N+1):
        if sum(map(int, str(i))) == K:
            count += 1
    return count
