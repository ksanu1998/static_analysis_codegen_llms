def nthTerm(n):
    if n == 1:
        return 1
    else:
        return nthTerm(n-1) * 3 + 2
