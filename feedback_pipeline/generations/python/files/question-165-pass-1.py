def proizvolov(a, b, n):
    result = 0
    for i in range(n):
        result += a * b
        a, b = b, a + b
    return result