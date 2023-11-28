def getmask(val):
    mask = 0
    for i in range(10):
        if i in val:
            mask |= 1 << i
    return mask
