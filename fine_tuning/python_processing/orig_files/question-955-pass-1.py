def checkRecursive(num, rem_num, next_int, n, ans=0):
    if (rem_num == 0):
        ans += 1
    r = int(num ** (1 / n))
    for i in range(next_int + 1, r + 1):
        a = rem_num - int(i ** n)
        if a >= 0:
            ans += checkRecursive(num, rem_num - int(i ** n), i, n, 0)
    return ans


def check(x, n):
    return checkRecursive(x, x, 0, n)


if __name__ == '__main__':
    print(check(10, 2))
