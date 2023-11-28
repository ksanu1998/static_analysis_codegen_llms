from math import log


def isPower(m, y):
    res1 = log(y) // log(m)
    res2 = log(y) // log(m)
    return (res1 == res2)


def numSub(arr, n, m):
    ans = 0
    cnt = 0
    for i in range(n):
        if (isPower(m, arr[i])):
            cnt += 1
            ans += (cnt * (cnt - 1)) // 2
        else:
            cnt = 0
    return ans


if __name__ == '__main__':
    arr = [1, 1, 1, 3]
    m = 3
    n = len(arr)
    print(numSub(arr, n, m))
