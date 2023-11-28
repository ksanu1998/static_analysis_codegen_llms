def removeEveryKth(l, k):
    for i in range(0, len(l)):
        if i % k == 0:
            l[i] = 0
    arr = [0]
    for i in range(1, len(l)):
        if l[i] != 0:
            arr .append(l[i])
    return arr


def printArray(l):
    for i in range(1, len(l)):
        print(l[i], end=" ")
    print()


def printSequence(n, k):
    l = [int(i)for i in range(0, n + 1)]
    x = 1
    for i in range(0, k):
        p = l[x] + l[x + 1]
        l = removeEveryKth(l, p)
        x += 1
    printArray(l)


N = 8
K = 2
printSequence(N, K)
