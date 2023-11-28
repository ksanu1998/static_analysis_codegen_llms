def printPalindrome(left, mid, right):
    for x in left:
        print(x, end="")
    print(mid, end="")
    right = right[::-1]
    for x in right:
        print(x, end="")
    print('', end="")


def findPalindrome(S, N, M):
    d = set()
    for i in range(M):
        d .add(S[i])
    left = []
    right = []
    mid = ""
    for i in range(N):
        t = S[i]
        t = t[::-1]
        if (t == S[i]):
            mid = t
        elif (t in d):
            left .append(S[i])
            right .append(t)
            d .remove(S[i])
            d .remove(t)
    printPalindrome(left, mid, right)


if __name__ == '__main__':
    S = ["tab", "one", "bat"]
    M = 3
    N = len(S)
    findPalindrome(S, N, M)
