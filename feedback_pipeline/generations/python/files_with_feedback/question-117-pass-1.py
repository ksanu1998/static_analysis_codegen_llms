def checkArray(a, b, n):
    result = 0
    for i in range(n):
        if a[i]!= b[i]:
            result += 1
    return result
