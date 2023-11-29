def xorK(n, k):
    result = n
    for i in range(k):
        result = result ^ n
    return result
