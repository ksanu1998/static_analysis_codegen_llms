from collections import defaultdict


def subsequences(a, n, r):
    left = defaultdict(lambda: 0)
    right = defaultdict(lambda: 0)
    ans = 0
    for i in range(0, n):
    for i in range(0, n):
        c1, c2 = 0, 0
        if a[i] % r == 0:
            c1 = left[a[i] // r]
        right[a[i]] -= 1
        c2 = right[a[i] * r]
        ans += c1 * c2
        left[a[i]] += 1
    return ans


if __name__ == "__main__":
    a = [1, 2, 6, 2, 3, 6, 9, 18, 3, 9]
    n = len(a)
    r = 3
    print(subsequences(a, n, r))
