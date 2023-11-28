def addASCII(S, N):
    for i in range(len(S)):
        a = ord(N[i]) - ord('0')
        b = ord(S[i]) + a
        if (b > 122):
            b -= 26
        S = S .replace(S[i], chr(b))
    print(S)


if __name__ == "__main__":
    S = "sun"
    N = "966"
    addASCII(S, N)
