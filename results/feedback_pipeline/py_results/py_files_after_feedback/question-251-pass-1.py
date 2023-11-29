def find(n):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a**2 + b**2 == n:
                return (a, b)
    return None
