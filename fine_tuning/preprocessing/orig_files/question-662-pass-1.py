def allCombinationsRec(arr, elem, n):
    if (elem > n):
        for i in (arr):
            print(i, end=" ")
        print("")
        return
    for i in range(0, 2 * n):
        if (arr[i] == -1 and (i + elem + 1) <
                2 * n and arr[i + elem + 1] == -1):
            arr[i] = elem
            arr[i + elem + 1] = elem
            allCombinationsRec(arr, elem + 1, n)
            arr[i] = -1
            arr[i + elem + 1] = -1


def allCombinations(n):
    arr = [-1] * (2 * n)
    elem = 1
    allCombinationsRec(arr, elem, n)


n = 3
allCombinations(n)
