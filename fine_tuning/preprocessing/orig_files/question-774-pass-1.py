def minimumMEX(arr, N, K):
    s = set()
    for i in range(1, N + 2, 1):
        s .add(i)
    for i in range(K):
        s .remove(arr[i])
    mex = list(s)[0]
    for i in range(K, N, 1):
        s .remove(arr[i])
        s .add(arr[i - K])
        firstElem = list(s)[0]
        mex = min(mex, firstElem)
    print(mex)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    K = 3
    N = len(arr)
    minimumMEX(arr, N, K)
