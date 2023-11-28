def allCombinationsRec(arr, elem, n):
    if n == 0:
        print(arr)
        return
    for i in range(len(elem)):
        arr.append(elem[i])
        allCombinationsRec(arr, elem, n-1)
        arr.pop()
    return
