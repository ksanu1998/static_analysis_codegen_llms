def product(x):
    prod = 1
    while (x):
        prod *= (x % 10)
        x //= 10
    return prod


def findNumber(l, r):
    a = str(l)
    b = str(r)
    ans = r
    for i in range(len(b)):
        if (b[i] == '0'):
            continue
        curr = list(b)
        curr[i] = str(((ord(curr[i]) - ord('0')) - 1) + ord('0'))
        for j in range(i + 1, len(curr)):
            curr[j] = str(ord('9'))
        num = 0
        for c in curr:
            num = num * 10 + (int(c) - ord('0'))
        if (num >= l and product(ans) < product(num)):
            ans = num
    return ans


if __name__ == "__main__":
    l, r = 1, 10
    print(findNumber(l, r))
    l, r = 51, 62
    print(findNumber(l, r))
