import math
N = 100001
adj = [[]for i in range(N)]
a = [0 for i in range(N)]
ans = [0 for i in range(N)]


def hasOddNumberOfDivisors(n):
    if (a[n] == 1)
        return 1
    if (n == 1)
        return 0
    if (a[n] == 0)
        a[n] = hasOddNumberOfDivisors(n / 2)
    if (a[n] == 1)
        return 1
    a[n] = hasOddNumberOfDivisors(n / 2)
    return a[n]


def countOddDivisors(n):
    ans[n] = hasOddNumberOfDivisors(n)


def main():
    n = 10
    for i in range(1, n + 1):
        adj[i].append(i * 2)
        adj[i].append(i * 2 + 1)
    for i in range(1, n + 1):
        countOddDivisors(i)
    for i in range(1, n + 1):
        print(ans[i])


if __name__ == "__main__":
    main()
