def build_tree(b, seg_tree, l, r, vertex):
    if (l == r):
        seg_tree[vertex] = b[l]
        return
    mid = int((l + r) / 2)
    build_tree(b, seg_tree, l, mid, 2 * vertex)
    build_tree(b, seg_tree, mid + 1, r, 2 * vertex + 1)
    seg_tree[vertex] = __gcd(seg_tree[2 * vertex], seg_tree[2 * vertex + 1])


def __gcd(a, b):
    if b == 0:
        return b
    else:
        return __gcd(b, a % b)


def range_gcd(seg_tree, v, tl, tr, l, r):
    if (l > r):
        return 0
    if (l == tl and r == tr):
        return seg_tree[v]
    tm = int((tl + tr) / 2)
    return __gcd(range_gcd(seg_tree, 2 * v, tl, tm, l, min(tm, r)),
                 range_gcd(seg_tree, 2 * v + 1, tm + 1, tr, max(tm + 1, l), r))


def maxSubarrayLen(arr, n):
    seg_tree = [0] * (4 * n + 1)
    build_tree(arr, seg_tree, 0, n - 1, 1)
    maxLen = 0
    l, r = 0, 0
    while (r < n and l < n):
        if (range_gcd(seg_tree, 1, 0, n - 1, l, r) == 1):
            l += 1
        maxLen = max(maxLen, r - l - 1)
        r += 1
    print(maxLen, end="")


arr = [410, 52, 51, 180, 222, 33, 33]
N = len(arr)
maxSubarrayLen(arr, N)
