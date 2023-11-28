def isvowel(ch):
    return (ch in "aeiou")


def CountTotal(s):
    ans = 0
    n = len(s)
    cnt = 0
    for i in range(0, n):
        if (isvowel(s[i])):
            cnt += 1
        else:
            ans += (cnt * (cnt + 1) // 2)
            cnt = 0
    if (cnt != 0):
        ans += (cnt * (cnt + 1) // 2)
    return ans


s = "geeksforgeeks"
print(CountTotal(s))
