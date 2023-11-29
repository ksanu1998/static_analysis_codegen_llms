def cntCakes(n, m):
    if (n < m):
        print("-1")
        return
    cnt = 0
    for i in range(1, m + 1):
        cnt += (n // i)
    print(cnt)


if __name__ == "__main__":
    n = 10
    m = 3
    cntCakes(n, m)
