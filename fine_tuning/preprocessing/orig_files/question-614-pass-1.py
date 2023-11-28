def getBinaryRep(N, num_of_bits):
    r = ""
    num_of_bits -= 1
    while (num_of_bits >= 0):
        if (N & (1 << num_of_bits)):
            r += ("1")
        else:
            r += ("0")
        num_of_bits -= 1
    return r


def NBitBinary(N):
    r = []
    first = 1 << (N - 1)
    last = first * 2
    for i in range(last - 1, first - 1, -1):
        zero_cnt = 0
        one_cnt = 0
        t = i
        num_of_bits = 0
        while (t):
            if (t & 1):
                one_cnt += 1
            else:
                zero_cnt += 1
            num_of_bits += 1
            t = t >> 1
        if (one_cnt >= zero_cnt):
            all_prefix_match = True
            msk = (1 << num_of_bits) - 2
            prefix_shift = 1
            while (msk):
                prefix = ((msk & i) >> prefix_shift)
                prefix_one_cnt = 0
                prefix_zero_cnt = 0
                while (prefix):
                    if (prefix & 1):
                        prefix_one_cnt += 1
                    else:
                        prefix_zero_cnt += 1
                    prefix = prefix >> 1
                if (prefix_zero_cnt > prefix_one_cnt):
                    all_prefix_match = False
                    break
                prefix_shift += 1
                msk = msk & (msk << 1)
            if (all_prefix_match):
                r .append(getBinaryRep(i, num_of_bits))
    return r


if __name__ == "__main__":
    n = 4
    results = NBitBinary(n)
    for i in range(len(results)):
        print(results[i], end=" ")
    print()
