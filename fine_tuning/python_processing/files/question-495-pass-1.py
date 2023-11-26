def rearrange(s):
    result = ""
    for i in range(len(s)):
        if i == 0 or s[i]!= s[i - 1]:
            result += s[i]
    return result
