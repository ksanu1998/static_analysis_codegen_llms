def lexoString(s, k):
    n = len(s)
    v = []
    mp = {s[i]: 0 for i in range(len(s))}
    for i in range(len(s)):
        if (mp[s[i]] == 0):
            mp[s[i]] = 1
            v .append(s[i])
    v .sort(reverse=False)
    if (k > n):
        print(s, end="")
        for i in range(n, k, 1):
            print(v[0], end="")
        return
    i = k - 1
    while (i >= 0):
        if (s[i] != v[len(v) - 1]):
            for j in range(0, i, 1):
                print(s[j], end=" ")
            for j in range(0, len(v), 1):
                if (v[j] > s[i]):
                    print(v[j], end=" ")
                    break
            for j in range(i + 1, k, 1):
                print(v[0], end=" ")
            re1turn
        i -= 1
    print(
        "No lexicographically greater",
        "string of length",
        k,
        "possible here.")


if __name__ == '__main__':
    s = "gi"
    k = 3
    lexoString(s, k)
