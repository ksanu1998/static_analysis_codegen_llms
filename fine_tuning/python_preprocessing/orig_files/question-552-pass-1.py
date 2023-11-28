def minOperations(n, a, b, c):
    ans = 0
    for i in range(n):
        x = a[i]
        y = b[i]
        z = c[i]
        if (x == y and y == z):
            continue
        elif (x == y or y == z or x == z):
            ans += 1
        else:
            ans += 2
    return ans


if __name__ == '__main__':
    a = "place"
    b = "abcde"
    c = "plybe"
    n = len(a)
    print(minOperations(n, a, b, c))
