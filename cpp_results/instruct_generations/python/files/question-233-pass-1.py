def sum_harmonic_series(n):
    sum = 0
    for i in range(1, n+1):
        sum += 1/i
    return sum