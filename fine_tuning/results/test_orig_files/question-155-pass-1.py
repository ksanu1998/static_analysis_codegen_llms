def negProdSubArr(arr, n):

def negProdSubArr(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            prod = 1
            for k in range(i, j+1):
                prod *= arr[k]
            if prod > 0:
                count += 1
    return count
