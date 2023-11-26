def countSol(coeff, start, end, rhs):
    if (rhs == 0):
        return 1
    result = 0
    for i in range(start, end + 1):
        if (coeff[i] <= rhs):
            result += countSol(coeff, i, end, rhs - coeff[i])
    return result


coeff = [2, 2, 5]
rhs = 4
n = len(coeff)
print(countSol(coeff, 0, n - 1, rhs))
