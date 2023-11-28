def prefixProduct(a, n):

def prefixProduct(a, n):
    result = [0] * n
    result[0] = 1
    for i in range(1, n):
        result[i] = result[i-1] * a[i-1]
    return result
