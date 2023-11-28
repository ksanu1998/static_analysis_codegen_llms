def getBinaryLength(n):
    length = 0
    while (n > 0):
        length += 1
        n //= 2
    return length


def concat(m, n):
    length = getBinaryLength(n)
    return (m << length) + n


m, n = 4, 5
print(concat(m, n))
