def find_digit(s, n):
    for i in range(len(s)):
        if s[i] == n:
            return i
    return -1
