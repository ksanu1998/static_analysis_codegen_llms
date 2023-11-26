def solve(x):
    ans, temp = 0, x
    if (x < 10):
        return x
    last = x % 10
    while (x):
        first = x % 10
        x = x // 10
    if (first <= last):
        ans = 9 + temp // 10
    else:
        ans = 8 + temp // 10
    return ans


L, R = 2, 60
print(solve(R) - solve(L - 1))
L, R = 1, 1000
print(solve(R) - solve(L - 1))
