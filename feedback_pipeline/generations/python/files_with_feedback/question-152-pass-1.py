def calculate(n, k, m, power):
    result = 0
    for i in range(n):
        for j in range(k):
            for l in range(m):
                if (i + j + l) % power == 0:
                    result += 1
    return result
