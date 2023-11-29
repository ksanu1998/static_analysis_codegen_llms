def prefixProduct(a, n):
    result = [1] * n
    for i in range(1, n):
        result[i] = result[i - 1] * a[i - 1]
    return result