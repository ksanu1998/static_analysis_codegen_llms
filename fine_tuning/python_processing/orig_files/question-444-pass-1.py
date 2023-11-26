def countPalindrome(S):
    N = len(S)
    Z = [0] * N
    l = 0
    r = 0
    for i in range(1, N):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - 1])
        while ((i + Z[i]) < N and (S[Z[i]] == S[i + Z[i]])):
            Z[i] += 1
        if ((i + Z[i] - 1) > r):
            l = ir = i + Z[i] - 1
    sum = 0
    for i in range(0, len(Z)):
        sum += Z[i] + 1
    return sum


S = "abab"
print(countPalindrome(S))
