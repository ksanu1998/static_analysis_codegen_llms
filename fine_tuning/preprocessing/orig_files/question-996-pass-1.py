def build_num(bit):
    ans = 0
    for i in range(32):
        if (bit[i] > 0):
            ans += (1 << i)
    return ans


def maximumOR(arr, n, k):
    bit = [0] * 32
    for i in range(k):
        for j in range(32):
            if ((arr[i] & (1 << j)) > 0):
                bit[j] += 1
    max_or = build_num(bit)
    for i in range(k, n):
        for j in range(32):
            if ((arr[i - k] & (1 << j)) > 0):
                bit[j] -= 1
        for j in range(32):
            if ((arr[i] & (1 << j)) > 0):
                bit[j] += 1
        max_or = max(build_num(bit), max_or)
    return max_or


if __name__ == '__main__':
    arr = [2, 5, 3, 6, 11, 13]
    k = 3
    n = len(arr)
    print(maximumOR(arr, n, k))
