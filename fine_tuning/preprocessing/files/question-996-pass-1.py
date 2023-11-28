def build_num(bit):
    num = 0
    for i in range(len(bit)):
        num += bit[i] * (2 ** i)
    return num
