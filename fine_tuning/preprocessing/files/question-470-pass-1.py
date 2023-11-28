def findIfPossible(N, str_):
    while N > 0:
        if str_.startswith(N):
            str_ = str_[N:]
            N = N - 1
        else:
            return False
    return True
