class Pair:
    def __init__(self, a, b):
        self .a = a
        self .b = b

    def __lt__(self, other):
        return self .a < other .a


def maxChainLength(arr):
    arr .sort()
    L = [[]for x in range(len(arr))]
    L[0].append(arr[0])
    for i in range(1, len(arr)):
        for j in range(i):
            if (arr[j].b < arr[i].a and len(L[j]) > len(L[i])):
                L[i] = L[j]
        L[i].append(arr[i])
    maxChain = []
    for x in L:
        if len(x) > len(maxChain):
            maxChain = x
    for pair in maxChain:
        print("({a},{b})".format(a=pair .a, b=pair .b), end=" ")
    print()


if __name__ == "__main__":
    arr = [Pair(5, 29), Pair(39, 40), Pair(15, 28), Pair(27, 40), Pair(50, 90)]
    n = len(arr)
    maxChainLength(arr)
