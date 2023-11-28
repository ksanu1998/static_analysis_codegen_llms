def findSplit(arr, N):
    for l in range(1, N - 3, 1):
        for r in range(l + 2, N - 1, 1):
            lsum = 0
            rsum = 0
            msum = 0
            for i in range(0, l, 1):
                lsum += arr[i]
            for i in range(l + 1, r, 1):
                msum += arr[i]
            for i in range(r + 1, N, 1):
                rsum += arr[i]
            if (lsum == rsum and rsum == msum):
                print(l, r)
                return
    print(-1)


if __name__ == '__main__':
    arr = [2, 5, 12, 7, 19, 4, 3]
    N = len(arr)
    findSplit(arr, N)
