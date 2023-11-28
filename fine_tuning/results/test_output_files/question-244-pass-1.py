def find_probability(p, q, r, s):
    if (p == 0 or q == 0):
        return 0
    if (p == 1):
        return 1
    if (q == 1):
        return 0
    if (r == 1):
        return 1
    if (s == 1):
        return 0
    if (r == 0):
        return 1
    if (s == 0):
        return 0
    if (r == 1 and s == 1):
        return 1
    if (r == 1 and s == 0):
        return 1
    if (r == 0 and s == 1):
        return 1
    if (r == 0 and s == 0):
        return 0
    if (r == 1 and s == 1):
        return 1
    if (r == 1 and s == 0):
        return 1
    if (r == 0 and s == 1):
        return 1
    if (r == 0 and s == 0):
        return 0
    if (r == 1 and s == 1):
        return 1
    if (r == 1 and s == 0):
        return 1
    if (r == 0 and s == 1):
        return 1
    if (r == 0 and s == 0):
        return 0
    if (r == 1 and s == 1):
        return 1
    if (r == 1 and s == 0):
        return 1
    if (r == 0 and s == 1):
        return 1
    if (r == 0 and s == 0):
        return 0
    if (r == 1 and s == 1):
        return
