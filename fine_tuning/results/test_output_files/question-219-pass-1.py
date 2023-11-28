def getPairs(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] < a[j]):
                count += 1
    print(count)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    getPairs(a)
