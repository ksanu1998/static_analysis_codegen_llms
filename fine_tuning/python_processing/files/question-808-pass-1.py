def findMaxLen(s):
    max_len = 0
    start = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            continue
        else:
            max_len = max(max_len, i - start)
            start = i
    return max(max_len, len(s) - start)
