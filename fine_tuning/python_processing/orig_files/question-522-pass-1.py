def countSubstring(S, L, n):
    freq = [0 for i in range(26)]
    for i in range(n):
        freq[(ord(L[i]) - ord('a'))] = 1
    count, ans = 0, 0
    for x in S:
        if (freq[ord(x) - ord('a')]):
            ans += (count * count + count) // 2
            count = 0
        else:
            count += 1
    ans += (count * count + count) // 2
    return ans


S = "abcpxyz"
L = ['a', 'p', 'q']
n = len(L)
print(countSubstring(S, L, n))
