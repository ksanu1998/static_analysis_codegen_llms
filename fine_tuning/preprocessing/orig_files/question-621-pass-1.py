def xorZero(str):
    one_count = 0
    zero_count = 0
    n = len(str)
    for i in range(0, n, 1):
        if (str[i] == '1'):
            one_count += 1
        else:
            zero_count += 1
    if (one_count % 2 == 0):
        return zero_count
    return one_count


if __name__ == '__main__':
    str = "11111"
    print(xorZero(str))
