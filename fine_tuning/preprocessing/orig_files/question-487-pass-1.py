def maximum_pallindromic(arr):
    res = 0
    c1 = 0
    c2 = 0
    for i in range(26):
        res += arr[i] // 3
        arr[i] = arr[i] % 3
        if (arr[i] == 1):
            c1 += 1
        elif (arr[i] == 2):
            c2 += 1
    res += min(c1, c2)
    t = min(c1, c2)
    c1 -= t
    c2 -= t
    res += 2 * (c2 // 3)
    c2 %= 3
    res += c2 // 2
    print(res)


if __name__ == "__main__":
    arr = [4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    maximum_pallindromic(arr)
