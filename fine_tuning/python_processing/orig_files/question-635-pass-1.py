MAX_CHAR = 26


def countSubstringWithEqualEnds(s):
    result = 0
    n = len(s)
    count = [0] * MAX_CHAR
    for i in range(n):
        count[ord(s[i]) - ord('a')] += 1
    for i in range(MAX_CHAR):
        result += (count[i] * (count[i] + 1) / 2)
    return result


s = "abcab"
print(countSubstringWithEqualEnds(s))
