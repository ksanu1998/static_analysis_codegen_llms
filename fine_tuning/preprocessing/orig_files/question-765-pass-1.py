def makeEqual(arr, n):
    fre0 = [0] * 33
    fre1 = [0] * 33
    for i in range(n):
        x = arr[i]
        for j in range(33):
            if (x & 1):
                fre1[j] += 1
            else:
                fre0[j] += 1
            x = x >> 1
    ans = 0
    for i in range(33):
        ans += min(fre0[i], fre1[i])
    return ans


if __name__ == '__main__':
    arr = [3, 5]
    N = len(arr)
    print(makeEqual(arr, N))
