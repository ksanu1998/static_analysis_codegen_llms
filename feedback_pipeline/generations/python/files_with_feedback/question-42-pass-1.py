def is_containdigit(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
