def fillString(s, k):
    mp = {}
    for i in range(len(s)):
        if (s[i] != '?'):
            mp[i % k] = s[i]
    s = list(s)
    for i in range(len(s)):
        if ((i % k)not in mp):
            print(-1)
            return
        s[i] = mp[i % k]
    s = ''.join(s)
    print(s)


if __name__ == '__main__':
    S = "????abcd"
    K = 4
    fillString(S, K)
