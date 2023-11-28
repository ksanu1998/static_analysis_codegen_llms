from bisect import bisect_left


def smallestPermutation(arr, N):
    w = [False for i in range(2 * N + 1)]
    for i in range(N):
        w[arr[i]] = True
    S = set()
    for i in range(1, 2 * N + 1, 1):
        if (w[i] == False):
            S .add(i)
    found = True
    P = []
    S = list(S)
    for i in range(N):
        it = bisect_left(S, arr[i])
        if (it == -1):
            found = False
            break
        P .append(arr[i])
        P .append(S[it])
        S .remove(S[it])
    if (found == False):
        print("-1")
    else:
        for i in range(2 * N):
            print(P[i], end=" ")


if __name__ == '__main__':
    arr = [4, 1, 3]
    N = len(arr)
    smallestPermutation(arr, N)
