def nthElement(a, b, n):
    return a[n] if n < len(a) else b[n - len(a)]
