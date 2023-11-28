def sumProductDifference(a, b, c, d, e):
    n = 4
    x = [0] * n
    x[0] = a
    x[1] = b
    x[2] = c
    x[3] = d
    x[4] = e
    x.sort()
    sum = 0
    for i in range(n):
        sum += x[i]
    product = 1
    for i in range(n):
        product *= x[i]
    print(abs(sum - product))


if __name__ == "__main__":
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    sumProductDifference(a, b, c, d, e)
