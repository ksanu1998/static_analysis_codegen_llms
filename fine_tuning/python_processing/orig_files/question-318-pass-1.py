M = 18
a = 0
b = 0
dp = [[[[-1 for i in range(2)]for j in range(90)]
       for k in range(90)]for l in range(M)]
fib = set()


def fibonacci():
    prev = 0
    curr = 1
    fib .add(prev)
    fib .add(curr)
    while (curr <= 100):
        temp = curr + prev
        fib .add(temp)
        prev = curr
        curr = temp


def count(pos, even, odd, tight, num):
    if (pos == len(num)):
        if ((len(num) & 1)):
            val = odd
            odd = even
            even = val
        d = even - odd
        if (d in fib):
            return 1
        return 0
    if (dp[pos][even][odd][tight] != -1):
        return dp[pos][even][odd][tight]
    ans = 0
    if (tight == 1):
        limit = 9
    else:
        limit = num[pos]
    for d in range(limit):
        currF = tight
        currEven = even
        currOdd = odd
        if (d < num[pos]):
            currF = 1
        if (pos & 1):
            currOdd += d
        else:
            currEven += d
        ans += count(pos + 1, currEven, currOdd, currF, num)
    return ans


def solve(x):
    num = []
    while (x > 0):
        num .append(x % 10)
        x //= 10
    num = num[::-1]
    return count(0, 0, 0, 0, num)


if __name__ == '__main__':
    fibonacci()
    L = 1
    R = 50
    print(solve(R) - solve(L - 1) + 1)
    L = 50
    R = 100
    print(solve(R) - solve(L - 1) + 2)
