def getNumber(s):
    n = len(s)
    ans = 0
    for i in range(1, n):
        if (s[i] == s[i - 1]):
            ans += 1
    if (ans == 0):
        print("-1")
    else:
        print(ans)


if __name__ == "__main__":
    getNumber("123456")
