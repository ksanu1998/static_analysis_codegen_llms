def xorK(n, k):
    if (k == 0):
        return n
    if (k == 1):
        return n
    if (k == 2):
        return (n ^ n)
    if (k == 3):
        return (n ^ (n ^ n))
    if (k == 4):
        return (n ^ (n ^ (n ^ n)))
    if (k == 5):
        return (n ^ (n ^ (n ^ (n ^ n))))
    if (k == 6):
        return (n ^ (n ^ (n ^ (n ^ (n ^ n)))))
    if (k == 7):
        return (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ n))))))
    if (k == 8):
        return (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ n)))))))
    if (k == 9):
        return (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ n))))))))
    if (k == 10):
        return (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ n)))))))))
    if (k == 11):
        return (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ n))))))))))
    if (k == 12):
        return (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ n)))))))))))
    if (k == 13):
        return (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (n ^ (
