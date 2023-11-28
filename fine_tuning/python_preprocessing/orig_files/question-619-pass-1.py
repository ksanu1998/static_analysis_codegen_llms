def check(list, s):
    n = len(list)
    if (n == 0):
        return False
    for i in range(0, n, 1):
        if (len(list[i]) != len(s)):
            continue
        diff = False
        for j in range(0, len(list[i]), 1):
            if (list[i][j] != s[j]):
                if (diff == False):
                    diff = True
                else:
                    diff = False
                    break
        if (diff):
            return True
    return False


if __name__ == '__main__':
    s = []
    s .append("bana")
    s .append("apple")
    s .append("banacb")
    s .append("bonanza")
    s .append("banamf")
    print(int(check(s, "banana")))
