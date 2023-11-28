def nthMagicNo(n):
    if n == 1:
        return 0
    else:
        return (nthMagicNo(n-1) + n) % 10
