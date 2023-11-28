def maxRepeating(s):
    count = 0
    c = ""
    for i in range(len(s)):
        if s[i] == c or c == "":
            count += 1
            c = s[i]
        else:
            count = 1
            c = s[i]
    return count
