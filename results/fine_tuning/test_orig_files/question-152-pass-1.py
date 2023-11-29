def calculate(n, k, m, power):

def calculate(n, k, m, power):
    result = 0
    for i in range(n):
        for j in range(m):
            if (i + j) % k == 0:
                result += power
    return result
