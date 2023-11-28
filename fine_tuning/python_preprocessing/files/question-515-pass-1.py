def rec(s, i):
    if i == len(s):
        return s
    elif s[i] == 'x':
        return rec(s[:i] + s[i+1:], i) + 'x'
    else:
        return rec(s, i+1)
