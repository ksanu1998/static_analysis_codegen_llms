def countWays(s):
    count = [0] * 26
    for x in s:
        count[ord(x) - ord('a')] = (count[ord(x) - ord('a')]) + 1
    count[ord(s[0]) - ord('a')] = 1
    ans = 1
    for i in range(26):
        if (count[i] != 0):
            ans *= count[i]
    return ans


if __name__ == '__main__':
    s = "acbbcc"
    print(countWays(s))
