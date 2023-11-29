def countNumber(N, S):
    count = 0
    for i in range(1, N+1):
        curr_sum = 0
        for j in range(i, N+1):
            curr_sum += j
            if curr_sum > S:
                count += 1
                break
    return count