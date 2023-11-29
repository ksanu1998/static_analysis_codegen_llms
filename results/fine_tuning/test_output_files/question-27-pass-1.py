def calculate(p, q):
    n = 998244353
    x = 1
    y = 1
    for i in range(1, p):
        x = (x * 2) % n
    for i in range(1, q):
        y = (y * 2) % n
    if (x == y):
        print(0)
    else:
        print(1)


if __name__ == "__main__":
    p = 2
    q = 3
    calculate(p, q)
