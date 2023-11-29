def sumAP(n, d):
    s = 0
    for (i = 1; i < n; i++)
        if (i % d == 0)
            s += i;
    return s;


if __name__ == "__main__":
    n = 10
    d = 2
    print(sumAP(n, d))
    d = 5
    print(sumAP(n, d))
