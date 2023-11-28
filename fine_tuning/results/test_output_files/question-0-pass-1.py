def maxPresum(a, b):
    n = len(a)
    m = len(b)
    if (n > m):
        a, b = b, a
        n = len(a)
        m = len(b)
    if (n == 0):
        return 0
    if (n == 1):
        return a[0]
    if (n == 2):
        return max(a[0], a[0] + b[0])
    if (n == 3):
        return max(a[0] + b[0], a[0] + b[1], a[1] + b[1])
    if (n == 4):
        return max(a[0] + b[0], a[0] + b[1], a[1] + b[1], a[2] + b[2])
    if (n == 5):
        return max(a[0] + b[0], a[0] + b[1], a[1] + b[1], a[2] + b[2],
                   a[3] + b[3])
    if (n == 6):
        return max(a[0] + b[0], a[0] + b[1], a[1] + b[1], a[2] + b[2],
                   a[3] + b[3], a[4] + b[4])
    if (n == 7):
        return max(a[0] + b[0], a[0] + b[1], a[1] + b[1], a[2] + b[2],
                   a[3] + b[3], a[4] + b[4], a[5] + b[5])
    if (n == 8):
        return max(
