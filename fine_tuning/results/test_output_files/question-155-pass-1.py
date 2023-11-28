def negProdSubArr(arr, n):
    negProd = 0
    for (i, j) in product(range(n), range(n)):
        if (i > j):
            continue
        prod = 1
        for k in range(i, j + 1):
            prod *= arr[k]
        if (prod > 0):
            negProd += 1
    print(negProd)


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
negProdSubArr(arr, n)
