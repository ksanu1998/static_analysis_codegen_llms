def minimumX(n, k):
    x = 1
    while (x * x < n):
        x = x * 2
    if (x * x == n):
        if (x % k == 0):
            print(x / k)
        else:
            print(-1)
    else:
        print(-1)


if __name__ == "__main__":
    n = 12
    k = 3
    minimumX(n, k)
