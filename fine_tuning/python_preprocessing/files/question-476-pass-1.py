def countSubstring(S, N):
    count = 0
    for i in range(len(S) - N + 1):
        if all(c.islower() == c.isupper() for c in S[i:i+N]):
            count += 1
    return count
