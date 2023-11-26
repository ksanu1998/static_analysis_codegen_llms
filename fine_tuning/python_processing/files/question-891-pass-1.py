def kthdigit(a, b, k):
    if k == 0:
        return a
    elif k == 1:
        return b
    else:
        return kthdigit(a, b, k-1)
