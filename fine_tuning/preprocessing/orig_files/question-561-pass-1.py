def valid(cnt):
    for i in range(0, 26):
        if cnt[i] >= 2:
            return False
    return True


def getGoodString(s, n):
    if n < 26:
        return "-1"
    for i in range(25, n):
        cnt = [0] * 26
        for j in range(i, i - 26, -1):
            if s[j] != '?':
                cnt[ord(s[j]) - ord('a')] += 1
        if valid(cnt):
            cur = 0
            while cur < 26 and cnt[cur] > 0:
                cur += 1
            for j in range(i - 25, i + 1):
                if s[j] == '?':
                    s[j] = chr(cur + ord('a'))
                    cur += 1
                    while cur < 26 and cnt[cur] > 0:
                        cur += 1
            return ''.join(s)
    return "-1"


if __name__ == "__main__":
    s = "abcdefghijkl?nopqrstuvwxy?"
    n = len(s)
    print(getGoodString(list(s), n))
