import math


def calculate(a, b, n, m):
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[i] / b[j])
        result.append(row)
    return result
