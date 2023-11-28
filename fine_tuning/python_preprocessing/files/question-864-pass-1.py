def everMeet(x1, x2, v1, v2):
    while x1!= x2:
        x1 += v1
        x2 += v2
    return x1 == x2
