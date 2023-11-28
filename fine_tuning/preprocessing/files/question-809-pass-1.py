def longest_substring(s, n):
    max_len = 0
    start = 0
    end = 0
    for i in range(n):
        if s[i] == '0':
            start = i + 1
        else:
            end = i + 1
        max_len = max(max_len, end - start)
    return max_len
