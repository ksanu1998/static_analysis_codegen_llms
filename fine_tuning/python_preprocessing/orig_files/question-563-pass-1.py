def largestPalinSub(s):
    res = ""
    mx = s[0]
    for i in range(1, len(s)):
        mx = max(mx, s[i])
    for i in range(0, len(s)):
        if s[i] == mx:
            res += s[i]
    return res


if __name__ == "__main__":
    s = "geeksforgeeks"
    print(largestPalinSub(s))
