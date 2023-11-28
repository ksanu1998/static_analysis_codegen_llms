def countSol(coeff, start, end, rhs):
    n = len(coeff)
    d = {}
    for i in range(n):
        d[i] = (start[i], end[i])
    sol = 0
    def rec(i, val, coeff, d):
        if i == n:
            if val == rhs:
                sol += 1
            return
        for j in range(d[i][0], d[i][1] + 1):
            rec(i + 1, val + j * coeff[i], coeff, d)
    rec(0, 0, coeff, d)
    return sol
