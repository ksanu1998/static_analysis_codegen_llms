def msbPos(n):
    pos = 0
    while n != 0:
        pos += 1
        n = n >> 1
    return pos


def josephify(n):
    position = msbPos(n)


'
j = 1 << (position - 1)
n = n ^ j
n = n << 1
n = n | 1
return n
n = 41
print(josephify(n))
