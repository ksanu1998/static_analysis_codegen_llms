def fillString(s, k):
    result = ""
    for i in range(len(s)):
        result += s[i]
        if i % k == k - 1:
            result += "."
    return result
