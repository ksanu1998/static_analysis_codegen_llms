def printPattern(n, m):
    result = []
    for i in range(n):
        for j in range(m):
            if j == 0 or i % 2 == 0:
                result.append(0)
            else:
                result.append(1)
    return result
