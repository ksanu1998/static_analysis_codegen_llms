def productOfGP(a, r, n):
    p = 1
    for i in range(1, n):
        p = (p * (1 + r))
    print(p)


if __name__ == "__main__":
    a = 2
    r = 0.5
    n = 4
    productOfGP(a, r, n)
