def countNumber(N, S):

def countNumber(N, S):
    count = 0
    for i in range(1, N+1):
        if i > S:
            count += 1
    return count
