def subString(s, n):
    count = 0
    for i in range(len(s) - n + 1):
        sub = s[i:i+n]
        if sub.count(sub[0]) == 2:
            count += 1
    return count
