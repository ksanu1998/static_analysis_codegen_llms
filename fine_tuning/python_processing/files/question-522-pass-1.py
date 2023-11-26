def countSubstring(S, L, n):
    count = 0
    for i in range(n):
        if S[i] not in L:
            count += 1
    return count
