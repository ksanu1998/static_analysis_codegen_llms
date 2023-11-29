def negProdSubArr(arr, n):
    count = 0
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            if product > 0:
                count += 1
    return count
