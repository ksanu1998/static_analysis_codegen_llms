def nthTerm(N):
    if N == 1:
        return 12
    else:
        return nthTerm(N-1) * 3 + nthTerm(N-2) * 5
