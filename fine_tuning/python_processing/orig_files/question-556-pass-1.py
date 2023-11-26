def countSubstrings(s, c):
    n = len(s)
    cnt = 0
    Sum = 0
    for i in range(n):
        if (s[i] != c):
            cnt += 1
        else:
            Sum += (cnt * (cnt + 1)) // 2
            cnt = 0
    Sum += (cnt * (cnt + 1)) // 2
    return Sum


s = "baa"
c = 'b'
print(countSubstrings(s, c))
