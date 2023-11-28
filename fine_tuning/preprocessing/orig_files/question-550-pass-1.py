def printMatrix(n, m):
    if (n < 5 or m < 5):
        print(-1, end=" ")
        return
    s = "aeiou"
    s = list(s)
    for i in range(n):
        for j in range(m):
            print(s[j % 5], end=" ")
        print()
        c = s[0]
        for i in range(4):
            s[i] = s[i + 1]
        s[4] = c


if __name__ == "__main__":
    n = 5
    m = 5
    printMatrix(n, m)
